from minijax.config import Config
from minijax.utils.functional import unity, compose

from minijax.models.form_parser import basic_parse_form_inputs
from minijax.models.value_generator import (
    rule_based_value_generator,
    gpt3_value_generator,
    chatgpt_value_generator,
)


cfg = Config()


# remove the combination of configs that cannot be executed together
def eliminate_invalid_workflows():
    INVALID_CASES = [
        {
            'parser': 'NONE',
            'filler': 'FIXED',
        },
        {
            'parser': 'NONE',
            'filler': 'RANDOM',
        }
    ]
    
    for invalid_case in INVALID_CASES:
        if cfg.model_config['parser']['mode'] == invalid_case['parser'] and \
            cfg.model_config['filler']['mode'] == invalid_case['filler']:
            raise Exception('Invalid combination of parser and filler')


# parser function should use the following signature:
# def parser_function(form):
#    return something
def evaluate_parser_function():
    parser_function = unity
    
    if cfg.model_config['parser']['mode'] == 'BASIC':
        parser_function = basic_parse_form_inputs
    
    return parser_function


# value generator function should use the following signature:
# def value_generator_function(parsed_form (or unparsed_form)):
#    return commands to execute
def evaluate_value_generator_function():
    value_generator_function = unity
    
    # Basic config
    if cfg.model_config['workflow']['filler'] == 'FIXED':
        value_generator_function = rule_based_value_generator(random=False)
    if cfg.model_config['workflow']['filler'] == 'RANDOM':
        value_generator_function = rule_based_value_generator(random=True)
    
    # GPT3 config
    if cfg.model_config['workflow']['filler'] == 'GPT3' and cfg.model_config['parameters']['zero_shot'] == True:
        value_generator_function = gpt3_value_generator(zero_shot=True)
    if cfg.model_config['workflow']['filler'] == 'GPT3' and cfg.model_config['parameters']['zero_shot'] == False:
        value_generator_function = gpt3_value_generator(zero_shot=False)
    
    # Chat model config (GPT3.5 - GPT4)
    if (
        cfg.model_config['workflow']['filler'] == 'GPT3.5' or cfg.model_config['workflow']['filler']
    ) and cfg.model_config['parameters']['zero_shot'] == True:
        value_generator_function = chatgpt_value_generator(zero_shot=True)
    if (
        cfg.model_config['workflow']['filler'] == 'GPT3.5' or cfg.model_config['workflow']['filler']
    ) and cfg.model_config['parameters']['zero_shot'] == False:
        value_generator_function = chatgpt_value_generator(zero_shot=False)
    
    return value_generator_function


def generate_workflow():
    eliminate_invalid_workflows()
    
    workflow = compose(
        evaluate_parser_function(),
        evaluate_value_generator_function(),
    )
    
    return workflow