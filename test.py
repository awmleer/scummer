if __name__ == '__main__':
    from scummer.validator import Validator

    t = {
        'a': 'x',
        'b': {
            'b1': 123
        },
        'c': [1,2],
        'd': {
            'x': 1,
            'y': 'aaaa'
        }
    }

    v = Validator(schema={
        'a': ('enum',{
            'items': ['x','y']
        }),
        'b': {
            'b1': ['str','int'],
            'b2': ('int',{'required':False})
        },
        'c': 'int[]',
        'd': ('map',{
            'definition': 'int'
        })
    })

    v.validate(t)
