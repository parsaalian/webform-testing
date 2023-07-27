
system_message = """
Your task is to generate a set of constraints for web form fields. Your decisions must be made independently without seeking user assistance or additional information. If there are multiple ways to express constraints, use the least number of constraints to describe them. Only generate the constraints and refrain from explaining your answers. Only generate constraints for the input field in question, not those in the relevant information section. You must choose your constraints in the format of our modified version of the Jest library in JavaScript. The list of functions in this modified format are:
1. toBeEqual(value) # the input field value is exactly equal to the given value
2. toHaveLengthCondition(condition, value) # the length of the input field value matches the given condition
3. toBeTruthy() # the input field value is truthy and not empty (not false, 0, ‘’, null, undefined, or NaN)
4. toHaveCompareCondition(condition, numberOrDateValue) # the input field value has the given condition to the given value
5. toContainSubString(stringValue)
6. toContainChar(charValue)
7. toBeAlphabetical()
8. toBeNumerical()
9. toBeAlphaNumerical()
10. toContainUpperCaseChars()
11. toContainSpecialChars()
12. toContainWhiteSpace()
13. toStartWithString(stringValue)
14. toEndWithString(stringValue)
15. freeTextConstraint(constraintStringValue) # for constraints that cannot be expressed as a deterministic function from the above functions
16. dummy(relevantField) # add if value of some field could help with filling of this field
You must choose only from this list of functions, and avoid using any other functions. Use the notation “field(‘elementId’)” to refer to input fields in the form. When generating constraints for date-related fields, also take current date into your considerations.
Example of generated constraints for a password input field:
expect(field(‘password’))
.toHaveLengthCondition(‘>’, 8)
.toHaveLengthCondition(‘<’, 50)
.toBeAlphaNumeric()
.toHaveUpperCase()
.toHaveSpecialChars()
.not.toBeTruthy()
.freeTextConstraint(’your password must be a dog\‘s name’)
.dummy(field(‘email’))
.toBeEqual(field(‘confirm-password’))
"""

prompt = """
Today’s date: 2023-07-25 11:13:46. When generating constraints for date fields, also generate constraints to compare them with the current date, past, and future if applicable.
The following are all the labels in the form, which provide context for the functionality of the form:
First Name, Last Name, Email address, First Name, Last Name, Company, Phone, Address line 1, Address line 2, City, ZIP / Postal code, Country, Note
We are generating constraints for the following input field:
input: <input name=\“postalCode\” type=\“text\” value=\“\”/>
with label: ZIP / Postal code
The relevant input fields available in the form are (in order of relevance):
1.
input: <input name=\“city\” type=\“text\” value=\“\”/>
with label: City
2.
input: <input name=\“streetAddress1\” type=\“text\” value=\“\”/>
with label: Address line 1
"""