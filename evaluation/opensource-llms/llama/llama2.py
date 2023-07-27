from transformers import AutoTokenizer, pipeline, logging
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig
import constants


def load_model_llama(model_type, use_triton=False):
    if model_type == '70B':
        model_name_or_path = "TheBloke/Llama-2-70B-chat-GPTQ"
        model_basename = "gptq_model-4bit--1g"
    elif model_type == '13B':
        model_name_or_path = "TheBloke/Llama-2-13B-chat-GPTQ"
        model_basename = "gptq_model-4bit-128g"
    else:
        raise ValueError('Invalid model_type. Choose either "70B" or "13B".')

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


if __name__ == "__main__":
    # Load the model - load_model_llama2_70b
    tokenizer, model = load_model_llama("70B")
    # tokenizer, model = load_model_llama("13B")

    # Run inference
    system_message = constants.system_message
    prompt = constants.prompt

    response = run_inference(tokenizer, model, system_message, prompt)
    print("\n\n*** output LLAMA (70B).....:")
    print(response)
