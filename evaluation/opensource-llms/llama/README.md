# OpenLLMs - Llama 2 

### Environment setup - from scratch

```
conda create -n llama2 python=3.10.9
conda activate llama2
pip3 install torch torchvision torchaudio
```

Need the dependencies from [text-generation-webui](https://github.com/oobabooga/text-generation-webui)
```
git clone https://github.com/oobabooga/text-generation-webui
cd text-generation-webui
pip install -r requirements.txt
```

## Llama 2 70B
```
git clone --branch gptq-4bit-32g-actorder_True https://huggingface.co/TheBloke/Llama-2-70B-chat-GPTQ
```

## Llama 2 13B
```
git clone --branch gptq-4bit-32g-actorder_True https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ
```
