if __name__ == '__main__':
    from scummer.validator import Validator

    t = {
        'a': 'xxx',
        'b': {
            'b1': 123.123
        }
    }

    v = Validator(schema={
        'a': ['str','int'],
        'b': {
            'b1': ['str','int'],
            'b2': ('int',{'required':False})
        },
        'c': ('any',{
            'verbose_name': 'CCC',
            'required': False
        })
    })

    v.validate(t)
