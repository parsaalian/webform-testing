import logging

import click
import torch
from auto_gptq import AutoGPTQForCausalLM
from langchain import PromptTemplate, LLMChain
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFacePipeline

# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.vectorstores import Chroma
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    GenerationConfig,
    LlamaForCausalLM,
    LlamaTokenizer,
    pipeline,
)

from constants import CHROMA_SETTINGS, PERSIST_DIRECTORY


def load_model(device_type, model_id, model_basename=None):
    """
    Select a model for text generation using the HuggingFace library.
    If you are running this for the first time, it will download a model for you.
    subsequent runs will use the model from the disk.

    Args:
        device_type (str): Type of device to use, e.g., "cuda" for GPU or "cpu" for CPU.
        model_id (str): Identifier of the model to load from HuggingFace's model hub.
        model_basename (str, optional): Basename of the model if using quantized models.
            Defaults to None.

    Returns:
        HuggingFacePipeline: A pipeline object for text generation using the loaded model.

    Raises:
        ValueError: If an unsupported model or device type is provided.
    """

    logging.info(f"Loading Model: {model_id}, on: {device_type}")
    logging.info("This action can take a few minutes!")

    if model_basename is not None:
        # The code supports all huggingface models that ends with GPTQ and have some variation
        # of .no-act.order or .safetensors in their HF repo.
        logging.info("Using AutoGPTQForCausalLM for quantized models")

        if ".safetensors" in model_basename:
            # Remove the ".safetensors" ending if present
            model_basename = model_basename.replace(".safetensors", "")

        tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=True)
        logging.info("Tokenizer loaded")

        model = AutoGPTQForCausalLM.from_quantized(
            model_id,
            model_basename=model_basename,
            use_safetensors=True,
            trust_remote_code=True,
            device="cuda:0",
            use_triton=False,
            quantize_config=None,
        )
    elif (
            device_type.lower() == "cuda"
    ):  # The code supports all huggingface models that ends with -HF or which have a .bin
        # file in their HF repo.
        logging.info("Using AutoModelForCausalLM for full models")
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        logging.info("Tokenizer loaded")

        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            device_map="auto",
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
            trust_remote_code=True,
            # max_memory={0: "15GB"} # Uncomment this line with you encounter CUDA out of memory errors
        )
        model.tie_weights()
    else:
        logging.info("Using LlamaTokenizer")
        tokenizer = LlamaTokenizer.from_pretrained(model_id)
        model = LlamaForCausalLM.from_pretrained(model_id)

    # Load configuration from the model to avoid warnings
    generation_config = GenerationConfig.from_pretrained(model_id)
    # see here for details:
    # https://huggingface.co/docs/transformers/
    # main_classes/text_generation#transformers.GenerationConfig.from_pretrained.returns

    # Create a pipeline for text generation
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_length=2048,
        temperature=0,
        top_p=0.95,
        repetition_penalty=1.15,
        generation_config=generation_config,
    )

    local_llm = HuggingFacePipeline(pipeline=pipe)
    logging.info("Local LLM Loaded")

    return local_llm


# chose device typ to run on as well as to show source documents.
@click.command()
@click.option(
    "--device_type",
    default="cuda",
    type=click.Choice(
        [
            "cpu",
            "cuda",
            "ipu",
            "xpu",
            "mkldnn",
            "opengl",
            "opencl",
            "ideep",
            "hip",
            "ve",
            "fpga",
            "ort",
            "xla",
            "lazy",
            "vulkan",
            "mps",
            "meta",
            "hpu",
            "mtia",
        ],
    ),
    help="Device to run on. (Default is cuda)",
)
def main(device_type, show_sources):
    logging.info(f"Running on: {device_type}")
    logging.info(f"Display Source Documents set to: {show_sources}")


    # load the LLM for generating responses

    # for HF models
    # model_id = "TheBloke/vicuna-7B-1.1-HF"
    # model_id = "TheBloke/Wizard-Vicuna-7B-Uncensored-HF"
    # model_id = "TheBloke/guanaco-7B-HF"
    # model_id = 'NousResearch/Nous-Hermes-13b' # Requires ~ 23GB VRAM. Using STransformers
    # alongside will 100% create OOM on 24GB cards.
    # llm = load_model(device_type, model_id=model_id)

    # for GPTQ (quantized) models
    # model_id = "TheBloke/Nous-Hermes-13B-GPTQ"
    # model_basename = "nous-hermes-13b-GPTQ-4bit-128g.no-act.order"
    # model_id = "TheBloke/WizardLM-30B-Uncensored-GPTQ"
    # model_basename = "WizardLM-30B-Uncensored-GPTQ-4bit.act-order.safetensors" # Requires
    # ~21GB VRAM. Using STransformers alongside can potentially create OOM on 24GB cards.
    # model_id = "TheBloke/wizardLM-7B-GPTQ"
    # model_basename = "wizardLM-7B-GPTQ-4bit.compat.no-act-order.safetensors"
    model_id = "TheBloke/WizardLM-7B-uncensored-GPTQ"
    model_basename = "WizardLM-7B-uncensored-GPTQ-4bit-128g.compat.no-act-order.safetensors"
    llm = load_model(device_type, model_id=model_id, model_basename=model_basename)

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
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)s - %(message)s", level=logging.INFO
    )
    main(device_type="cuda")
