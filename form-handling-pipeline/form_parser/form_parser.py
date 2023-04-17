def simplest_form_parser(form):
    form_inputs = form.find_all('input')
    form_labels = form.find_all('label')
    
    print(form_inputs, form_labels)
    
    return {
        'action': form.attrs['action'] if 'action' in form.attrs else None,
        'method': form.attrs['method'] if 'method' in form.attrs else None,
        'inputs': [{
            'label': form_labels[i].text,
            'type': form_inputs[i].attrs['type'] if 'type' in form_inputs[i].attrs else 'text',
            'value': form_inputs[i].attrs['value'] if 'value' in form_inputs[i].attrs else None,
        } for i in range(len(form_inputs))]
    }
