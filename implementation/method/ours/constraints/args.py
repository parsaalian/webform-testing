class ConstantArg:
    def __init__(self, value):
        self.value = value.strip("\'")
    
    
    def __str__(self):
        return str(self.value)


class FieldArg:
    def __init__(self, field_name):
        self.value = field_name
    
    
    def __str__(self):
        return f'field({self.value})'