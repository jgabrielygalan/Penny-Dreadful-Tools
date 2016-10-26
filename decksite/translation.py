TAPPED_OUT = {
    'user': 'person'
}

def translate(mappings, data):
    result = data.copy()
    for k, v in data.items():
        our_key = mappings.get(k)
        if our_key:
            result[our_key] = v
    return result
