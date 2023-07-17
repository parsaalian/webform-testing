import re

def parse_function(function_string):
    # matches function name and its arguments
    regex = r"(\w+)\((.*)\)"
    
    match = re.match(regex, function_string.strip())

    if match:
        function_name = match.group(1)
        arg_string = match.group(2)
        args = split_args(arg_string)
        return function_name, args
    else:
        return None

def split_args(arg_string):
    args = []
    bracket_count = 0
    current_arg = []
    for char in arg_string:
        print(char, bracket_count)
        if char == '\'' or char == '\"':
            bracket_count += 1
        if char == ',' and bracket_count % 2 == 0:
            args.append(''.join(current_arg).strip())
            current_arg = []
        else:
            current_arg.append(char)
    args.append(''.join(current_arg).strip())  # add the last argument
    return args

# Test the function
result = parse_function("totoHaveLengthCondition('=', field('hello-world'))")
print(f"Function name: {result[0]}")
for arg in result[1]:
    print(f"Argument: {arg}")