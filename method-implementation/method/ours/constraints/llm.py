from method.llm.openai import ApiManager


# number of tokens: 498
constraint_generation_prompt = """
Your task is to generate a set of constraints for form fields. Your decisions must be made independently without seeking user assistance or additional information.

The list of the constraints and their signatures is as follows:

1. toBe(value) # the input field value exactly matches the given value
2. toHaveLengthCondition(condition, value) # the length of the input field value matches the given condition
3. toBeTruthy() # the input field value is truthy and not empty (not false, 0, '', null, undefined, or NaN)
4. toHaveCompareCondition(condition, value) # the input field value has the given condition to the given value
5. toContainSubstr(value) # the input field value contains a specific string
6. toContainChar(value) # the input field value contains a specific character
7. toBeAlpha() # the input field value is alphabetic
8. toBeNumeric() # the input field value is numeric
9. toBeAlphaNumeric() # the input value contains both alphabetical and numeric characters
10. toHaveUpperCase() # the input value field contains upper case characters
11. toHaveSpecialChars() # the input value field contains special characters
12. toHaveWhiteSpace() # the input value field contains whitespace
13. toStartWith(value) # the input value field must start with a certain value
14. toEndWith(value) # the input value field must end with a certain value
15. toMatch(regex) # the input value field must match a certain regex pattern

generate conditions in the as the sample:

# sample
expect(field('password'))
.toHaveLengthCondition('>', 8)
.toHaveLengthCondition('<', 50)
.toBeAlphaNumeric()
.toHaveUpperCase()
.toHaveSpecialChars()
.not.toBeTruthy()
.toBeExactlyEqual(field('confirm password'))
# end of sample

If there are multiple ways to express constraints, use the one with the least number of constraints to describe it.
Only generate the constraints and don't explain your answers.
Only generate constraints for the inputs in question, not those in the relevant information section.
""".strip()


def generate_constraints_with_llm(
    user_constraint_prompt,
    openai_api_key,
    model='gpt-4',
    temperature=0,
    max_tokens=None,
):
    api_manager = ApiManager()
    
    messages = [
        {
            "role": "system",
            "content": constraint_generation_prompt,
        },
        {
            "role": "user",
            "content": f"""
            We are generating constraints for the following input field:
            {user_constraint_prompt}
            """.strip()
        }
    ]
    
    response = api_manager.create_chat_completion(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        openai_api_key=openai_api_key
    )
    
    response_text = response.choices[0].message.content
    
    return response_text
