import openai

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from minijax.config import Config
from minijax.crawler.driver import get_driver_container
from minijax.crawler.utils import get_element_xpath


# example prompt
'''
You are an agent filling forms on a website. You can issue these commands:
    - FILL////X////"Y": Fill the <input> or <textarea> element that has a relative xpath X with value Y
    - SELECT////X////"Y": Select the option Y in the <select> element that has a relative xpath X
Each command must be issued in a new line, with no preceding or trailing text values.
You are given a form to fill. The form's html is as follows:
<form _ngcontent-jwh-c36="" novalidate="" method="get" id="search-owner-form" class="form-horizontal ng-untouched ng-pristine ng-valid ng-submitted"><div _ngcontent-jwh-c36="" class="form-group"><div _ngcontent-jwh-c36="" id="lastNameGroup" class="control-group"><label _ngcontent-jwh-c36="" class="col-sm-2 control-label">Last name </label><div _ngcontent-jwh-c36="" class="col-sm-10"><input _ngcontent-jwh-c36="" size="30" maxlength="80" id="lastName" name="lastName" value="" class="form-control ng-untouched ng-pristine ng-valid"><span _ngcontent-jwh-c36="" class="help-inline"></span></div></div></div><div _ngcontent-jwh-c36="" class="form-group"><div _ngcontent-jwh-c36="" class="col-sm-offset-2 col-sm-10"><button _ngcontent-jwh-c36="" type="submit" class="btn btn-default">Find Owner</button></div></div></form>
The xpath in this format must be relative to the form element. Just give me the commands and nothing else.
YOUR COMMANDS:
'''


cfg = Config()
driver = get_driver_container().get_driver()


gpt3_completion_prompt = """You are an agent filling forms on a website. You can issue these commands:
    - FILL////X////"Y": Fill the <input> or <textarea> element that has a relative xpath X with value Y
    - SELECT////X////"Y": Select the option Y in the <select> element that has a relative xpath X
Each command must be issued in a new line, with no preceding or trailing text values.
You are given a form to fill. The form's html is as follows:
{form_html}
The xpath in this format must be relative to the form element. Just give me the commands and nothing else.
YOUR COMMANDS:"""


def fill_form_gpt3(form, zero_shot=True):
    form_html = form.get_attribute('outerHTML')
    prompt = gpt3_completion_prompt.format(form_html=form_html)
    res = openai.Completion.create(
        model=cfg.llm_config['parameters']['model'],
        prompt=prompt,
        temperature=cfg.llm_config['parameters']['temperature'],
        max_tokens=512,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    values = {}
    commands = res.choices[0].text.split('\n')[1:]
    print(commands)
    for command in commands:
        try:
            print(command)
            cmd, xpath, value = command.split('////')
            complete_xpath = f'//{xpath}'
            value = value.strip('"')
            values[complete_xpath] = value
            if cmd == 'FILL':
                form.find_element(By.XPATH, complete_xpath).send_keys(value)
            elif cmd == 'SELECT':
                select = Select(form.find_element(By.XPATH, complete_xpath))
                select.select_by_visible_text(value)
        except:
            continue
    return values