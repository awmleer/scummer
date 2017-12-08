if __name__ == '__main__':
    from scummer.validator import Validator

    t = {
        'a': 'xxx',
        'b': {
            'b1': 123
        },
        'c': [1,2]
    }

    v = Validator(schema={
        'a': ['str','int'],
        'b': {
            'b1': ['str','int'],
            'b2': ('int',{'required':False})
        },
        'c': ('array',{
            'basic_type': 'str'
        })
    })

    v.validate(t)
