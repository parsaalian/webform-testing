import openai
import random
import string


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


class FormFiller:
    def __init__(self, form_data):
        self.form_data = form_data


    def generate_values(self):
        pass
    
    
    def fill_form(self):
        generated_values = self.generate_values()
        for inp in generated_values['inputs']:
            inp['element'].send_keys(inp['value'])


class SimplestFormFiller(FormFiller):
    def generate_values(self):
        return {
            'action': self.form_data['action'],
            'method': self.form_data['method'],
            'inputs': self._fill_inputs()
        }


    def _fill_inputs(self):
        return [self._fill_input(inp) for inp in self.form_data['inputs']]


    def _fill_input(self, inp):
        if inp['type'] == 'text':
            return {
                'element': inp['element'],
                'label': inp['label'],
                'type': inp['type'],
                'value': random_string_generator(10, string.ascii_letters)
            }
        if inp['type'] == 'number':
            return {
                'element': inp['element'],
                'label': inp['label'],
                'type': inp['type'],
                'value': random.randint(0, 100)
            }
        else:
            return inp


class GPT3SimpleFormFiller(FormFiller):
    def __init__(self, form_data, model):
        super().__init__(form_data)
        self.model = model
    
    
    def generate_values(self):
        return {
            'action': self.form_data['action'],
            'method': self.form_data['method'],
            'inputs': self._fill_inputs()
        }
    
    
    def _fill_inputs(self):
        return [self._fill_input(inp) for inp in self.form_data['inputs']]
    
    
    def _fill_input(self, inp):
        prompt = '''We have a form with the following data:
        label: {}
        type: {}
        generate a value for this input:'''.format(inp['label'], inp['type'])
        
        print(prompt)
        
        fill_res = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            temperature=0,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            max_tokens=256
        )
        value = fill_res['choices'][0]['text']
        
        print(value)
        
        return {
            **inp,
            'value': value
        }