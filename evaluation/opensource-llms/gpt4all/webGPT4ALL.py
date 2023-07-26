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

    web_form = """
<form id=\"basic\" style=\"max-width:600px\" autocomplete=\"off\" class=\"ant-form ant-form-horizontal css-dfjnss\"><div class=\"ant-form-item css-dfjnss\"><div class=\"ant-row ant-form-item-row css-dfjnss\"><div class=\"ant-col ant-col-8 ant-form-item-label css-dfjnss\"><label for=\"basic_username\" class=\"ant-form-item-required\" title=\"Username\">Username</label></div><div class=\"ant-col ant-col-16 ant-form-item-control css-dfjnss\"><div class=\"ant-form-item-control-input\"><div class=\"ant-form-item-control-input-content\"><input id=\"basic_username\" aria-required=\"true\" class=\"ant-input css-dfjnss\" type=\"text\" value=\"\"></div></div></div></div></div><div class=\"ant-form-item css-dfjnss\"><div class=\"ant-row ant-form-item-row css-dfjnss\"><div class=\"ant-col ant-col-8 ant-form-item-label css-dfjnss\"><label for=\"basic_password\" class=\"ant-form-item-required\" title=\"Password\">Password</label></div><div class=\"ant-col ant-col-16 ant-form-item-control css-dfjnss\"><div class=\"ant-form-item-control-input\"><div class=\"ant-form-item-control-input-content\"><span class=\"ant-input-affix-wrapper ant-input-password css-dfjnss\"><input id=\"basic_password\" aria-required=\"true\" type=\"password\" class=\"ant-input css-dfjnss\"><span class=\"ant-input-suffix\"><span role=\"img\" aria-label=\"eye-invisible\" tabindex=\"-1\" class=\"anticon anticon-eye-invisible ant-input-password-icon\"><svg viewBox=\"64 64 896 896\" focusable=\"false\" data-icon=\"eye-invisible\" width=\"1em\" height=\"1em\" fill=\"currentColor\" aria-hidden=\"true\"><path d=\"M942.2 486.2Q889.47 375.11 816.7 305l-50.88 50.88C807.31 395.53 843.45 447.4 874.7 512 791.5 684.2 673.4 766 512 766q-72.67 0-133.87-22.38L323 798.75Q408 838 512 838q288.3 0 430.2-300.3a60.29 60.29 0 000-51.5zm-63.57-320.64L836 122.88a8 8 0 00-11.32 0L715.31 232.2Q624.86 186 512 186q-288.3 0-430.2 300.3a60.3 60.3 0 000 51.5q56.69 119.4 136.5 191.41L112.48 835a8 8 0 000 11.31L155.17 889a8 8 0 0011.31 0l712.15-712.12a8 8 0 000-11.32zM149.3 512C232.6 339.8 350.7 258 512 258c54.54 0 104.13 9.36 149.12 28.39l-70.3 70.3a176 176 0 00-238.13 238.13l-83.42 83.42C223.1 637.49 183.3 582.28 149.3 512zm246.7 0a112.11 112.11 0 01146.2-106.69L401.31 546.2A112 112 0 01396 512z\"></path><path d=\"M508 624c-3.46 0-6.87-.16-10.25-.47l-52.82 52.82a176.09 176.09 0 00227.42-227.42l-52.82 52.82c.31 3.38.47 6.79.47 10.25a111.94 111.94 0 01-112 112z\"></path></svg></span></span></span></div></div></div></div></div><div class=\"ant-form-item css-dfjnss\"><div class=\"ant-row ant-form-item-row css-dfjnss\"><div class=\"ant-col ant-col-16 ant-col-offset-8 ant-form-item-control css-dfjnss\"><div class=\"ant-form-item-control-input\"><div class=\"ant-form-item-control-input-content\"><label class=\"ant-checkbox-wrapper ant-checkbox-wrapper-checked ant-checkbox-wrapper-in-form-item css-dfjnss\"><span class=\"ant-checkbox css-dfjnss ant-checkbox-checked\"><input id=\"basic_remember\" class=\"ant-checkbox-input\" type=\"checkbox\" checked=\"\"><span class=\"ant-checkbox-inner\"></span></span><span>Remember me</span></label></div></div></div></div></div><div class=\"ant-form-item css-dfjnss\"><div class=\"ant-row ant-form-item-row css-dfjnss\"><div class=\"ant-col ant-col-16 ant-col-offset-8 ant-form-item-control css-dfjnss\"><div class=\"ant-form-item-control-input\"><div class=\"ant-form-item-control-input-content\"><button type=\"submit\" class=\"ant-btn css-dfjnss ant-btn-primary\"><span>Submit</span></button></div></div></div></div></div></form>\n    
    """

    template = """
    The form HTML is:\n            
    {web_form}            
    Parse this form in the specified format. Don't explain your process, just give the JSON output. Make sure your output can be parsed by json.loads.\n            "
    """

    #prompt = PromptTemplate(template=template, input_variables=["question"])
    prompt = PromptTemplate(template=template, input_variables=["web_form"])

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    question = "What NFL team won the Super Bowl in the year Justin Bieber was born?"

    # Get the answer from the chain
    answer = llm_chain.run(web_form)
    print("question: ", web_form)
    print("answer: ", answer)

if __name__ == "__main__":
    main()