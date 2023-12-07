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