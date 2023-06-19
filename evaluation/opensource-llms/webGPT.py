#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from constants import CHROMA_SETTINGS
from langchain.chains import RetrievalQA
from langchain import PromptTemplate, LLMChain
from langchain.vectorstores import Chroma
from langchain.llms import GPT4All, LlamaCpp
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

load_dotenv()

embeddings_model_name = os.environ.get("EMBEDDINGS_MODEL_NAME")
persist_directory = os.environ.get('PERSIST_DIRECTORY')

model_type = os.environ.get('MODEL_TYPE')
model_path = os.environ.get('MODEL_PATH')
model_n_ctx = os.environ.get('MODEL_N_CTX')
target_source_chunks = int(os.environ.get('TARGET_SOURCE_CHUNKS', 4))

def main():
    # Parse the command line arguments
    embeddings = HuggingFaceEmbeddings(model_name=embeddings_model_name)
    db = Chroma(persist_directory=persist_directory, embedding_function=embeddings, client_settings=CHROMA_SETTINGS)
    retriever = db.as_retriever(search_kwargs={"k": target_source_chunks})

    # Prepare the LLM
    match model_type:
        case "LlamaCpp":
            llm = LlamaCpp(model_path=model_path, n_ctx=model_n_ctx, verbose=False)
        case "GPT4All":
            llm = GPT4All(model=model_path, n_ctx=model_n_ctx, backend='gptj', verbose=False)
        case "chatgpt-3.5":
            llm = OpenAI(temperature=0, openai_api_key=os.environ.get("OPENAI_API_KEY"))
        case _default:
            print(f"Model {model_type} not supported!")
            exit

    template = """
            Question: {question}
            Answer: Let's think step by step.
            """

    prompt = PromptTemplate(template=template, input_variables=["question"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

    # Get the answer from the chain
    answer = llm_chain.run(question)
    print("question: ", question)
    print("answer: ", answer)

if __name__ == "__main__":
    main()