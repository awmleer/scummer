if __name__ == '__main__':
    from scummer.validator import Validator

    t = {
        'a': 'xxx',
        'b': {
            'b1': 123
        }
    }

    v = Validator(schema={
        'a': 'str',
        'b': {
            'b1': 'any',
            'b2': 'int'
        },
        'c': ('any',{
            'verbose_name': 'CCC',
            'required': False
        })
    })

    v.validate(t)
