def unity(*x):
    return x


def get_or_else(obj, key, default):
    try:
        key_breakdown = key.split('.')
        for key in key_breakdown:
            obj = obj[key]
        return obj
    except:
        return default


# compose a list of functions
def compose(*function_list):
    def __execute_one(function, args):
        if type(args) == tuple:
            return function(*args)
        else:
            return function(args)
    
    def __wrapped(*args):
        if len(function_list) == 0:
            return None
        f_args = __execute_one(function_list[0], args)
        for f in function_list[1:]:
            f_args = __execute_one(f, f_args)
        return f_args

    return __wrapped


# for feedback loop execution, execute a chain of functions until a condition is met
def compose_conditional_loop(condition):
    def _conditional_loop(*function_list):
        def __wrapped(*args):
            while condition(args):
                args = compose(*function_list)(args)
            return args
        return __wrapped
    return _conditional_loop