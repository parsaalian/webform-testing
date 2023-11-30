LLM_value_generation_prompt = '''
Your task is to generate testing values for a web form. When given a web form, you need to generate value combinations that can pass and fail when tried on the form. Your response should be in the following format:
{
passing: <a base passing combination for the form>,
failing: <a list of failing combination for the form>
}
Your response must be parsable by Python's json.loads function. Use "id" attribute to refer to the fields.
'''

'''
Your task is to generate testing values for a web form. When given a web form, you need to generate values that can pass and fail when tried on the form. Your response should be in the following format:
{
[field_identifier]: {
passing: <a base passing value for the field>,
failing: <a list of failing values for the field>
}
}
Your response must be parsable by Python's json.loads function. Use "id" attribute to refer to the fields.
'''


LLM_test_generation_prompt = '''
Your task is to generate test cases for a web form. When given a form, generate a test suit in Selenium which has the following format:
class FormTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("{url}")
    def tearDown(self):
        self.driver.close()
{test_cases}
Only respond with the python code. Try to test different cases for the inputs.
'''