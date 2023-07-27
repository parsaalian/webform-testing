from transformers import AutoTokenizer, pipeline, logging
from auto_gptq import AutoGPTQForCausalLM, BaseQuantizeConfig

model_name_or_path = "TheBloke/Llama-2-70B-chat-GPTQ"
model_basename = "gptq_model-4bit--1g"

use_triton = False

tokenizer = AutoTokenizer.from_pretrained(model_name_or_path, use_fast=True, device_map="auto")

model = AutoGPTQForCausalLM.from_quantized(model_name_or_path,
                                           model_basename=model_basename,
                                           inject_fused_attention=False, # Required for Llama 2 70B model at this time.
                                           use_safetensors=True,
                                           trust_remote_code=False,
                                           #device="cuda:0",
                                           use_triton=use_triton,
                                           quantize_config=None)




prompt = "Tell me about AI"
system_message = "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."
prompt_template=f'''[INST] <<SYS>>
{system_message}
<</SYS>>

{prompt} [/INST]
'''

print("\n\n*** Generate:")

input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
output = model.generate(inputs=input_ids, temperature=0.7, max_new_tokens=512)
print(tokenizer.decode(output[0]))
