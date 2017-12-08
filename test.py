if __name__ == '__main__':
    from scummer.validator import Validator

    t = {
        'a': 'xxx',
        'b': 123
    }

    v = Validator(schema={
        'a': 'str',
        'b': 'any',
        'c': ('any',{
            'verbose_name': 'CCC',
            'required': False
        })
    })

    v.validate(t)
