def get_or_else(obj, key, default):
    try:
        key_breakdown = key.split('.')
        for key in key_breakdown:
            obj = obj[key]
        return obj
    except:
        return default