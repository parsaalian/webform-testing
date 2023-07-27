from transformers import AutoTokenizer, pipeline, logging
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
import constants

def load_model_llama2_70b(model_name_or_path="TheBloke/Llama-2-70B-chat-GPTQ",
                          model_basename="gptq_model-4bit--1g", use_triton=False):
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True, device_map="auto")

    model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
                                               model_basename=model_basename,
                                               inject_fused_attention=False,
                                               use_safetensors=True,
                                               trust_remote_code=False,
                                               use_triton=use_triton,
                                               quantize_config=None)
    return tokenizer, model


def load_model_llama2_13b(model_name_or_path="TheBloke/Llama-2-13B-chat-GPTQ",
                          model_basename="gptq_model-4bit-128g", use_triton=False):
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True, device_map="auto")

    model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
                                               model_basename=model_basename,
                                               inject_fused_attention=False,
                                               use_safetensors=True,
                                               trust_remote_code=False,
                                               use_triton=use_triton,
                                               quantize_config=None)
    return tokenizer, model


def run_inference(tokenizer, model, system_message, prompt):
    prompt_template = f'''[INST] <<SYS>>
    {system_message}
    <</SYS>>

    {prompt} [/INST]
    '''

    input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
    output = model.generate(inputs=input_ids, temperature=0.0, max_new_tokens=512)
    return tokenizer.decode(output[0])


def run_inference_70b():
    # Load the model - load_model_llama2_70b
    tokenizer, model = load_model_llama2_70b()

    # Run inference
    system_message = constants.system_message
    prompt = constants.prompt

    response = run_inference(tokenizer, model, system_message, prompt)
    print("\n\n*** output LLAMA (70B).....:")
    print(response)

def run_inference_13b():
    # Load the model - load_model_llama2_13b
    tokenizer, model = load_model_llama2_13b()

    # Run inference
    system_message = constants.system_message
    prompt = constants.prompt

    response = run_inference(tokenizer, model, system_message, prompt)
    print("\n\n*** output LLAMA (13B).....:")
    print(response)

if __name__ == "__main__":
    run_inference_70b()
    run_inference_13b()
