# Open source LLMs

# Libraries used:
- [Chroma](https://www.trychroma.com/)
- [SentenceTransformers](https://www.sbert.net/)
- [GPT4All](https://github.com/nomic-ai/gpt4all)
- [LlamaCpp](https://github.com/ggerganov/llama.cpp)
- [LangChain](https://github.com/hwchase17/langchain)

# Environment Setup
In order to set your environment up to run the code here, first install all requirements:

```shell
conda create --name opensource-llms python=3.10
conda activate opensource-llms
pip3 install -r requirements.txt
```

Then, download the desired LLM models and place them in the `models` folder.:

- Now downloaded the [ggml-gpt4all-j-v1.3-groovy.bin](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin) model.
- If you prefer a different GPT4All-J compatible model, just download it and reference it in your `.env` file.

Update the `.env` file and edit the following variables appropriately.
```
MODEL_TYPE: supports LlamaCpp or GPT4All
PERSIST_DIRECTORY: is the folder you want your vectorstore in
MODEL_PATH: Path to your GPT4All or LlamaCpp supported LLM
MODEL_N_CTX: Maximum token limit for the LLM model
EMBEDDINGS_MODEL_NAME: SentenceTransformers embeddings model name (see https://www.sbert.net/docs/pretrained_models.html)
TARGET_SOURCE_CHUNKS: The amount of chunks (sources) that will be used to answer a question
```

## Running models
In order to run a model:

```shell
python WebGPT.py
```
