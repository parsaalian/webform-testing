# Lllama 2 

## Setup

```
git clone --branch gptq-4bit-32g-actorder_True https://huggingface.co/TheBloke/Llama-2-70B-chat-GPTQ
```

## Conda environment

```
conda create -n llama2-vanilla python=3.8
pip3 install git+https://github.com/huggingface/transformers
```

```
conda create -n textgen python=3.10.9
conda activate textgen
pip3 install torch torchvision torchaudio
```

```
https://github.com/oobabooga/text-generation-webui
pip install -r requirements.txt
```




# Created also a testing environment for ad-hoc work

```
conda create -n testing python=3.10.9
conda activate testing
pip3 install torch torchvision torchaudio
```




## Conda environment - Llama 2 (vanilla)
```
conda create -n llama2-vanilla python=3.10.9
conda activate llama2-vanilla
pip3 install torch torchvision torchaudio
```

```
pip install transformers
huggingface-cli login
```


# Llama 2 - 13B

```
git clone --branch gptq-4bit-32g-actorder_True https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ
```


