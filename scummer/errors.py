class ValidationError(Exception):
    message = ''
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message


class ValidationKeyError(ValidationError):
    key_name = None
    def __init__(self, key_name, message):
        super(ValidationKeyError, self).__init__(message=message)


class ValidationMissingRequiredKeyError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationMissingRequiredKeyError, self).__init__(
            key_name=key_name,
            message=language['missing_required_key'].replace("$KEY$", key_name)
        )


class ValidationNoneValueError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationNoneValueError, self).__init__(
            key_name=key_name,
            message=language['none_value'].replace("$KEY$", key_name)
        )


class ValidationNotIntError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationNotIntError, self).__init__(
            key_name=key_name,
            message=language['not_int'].replace("$KEY$", key_name)
        )


class ValidationNotStrError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationNotStrError, self).__init__(
            key_name=key_name,
            message=language['not_str'].replace("$KEY$", key_name)
        )


class ValidationNotFloatError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationNotFloatError, self).__init__(
            key_name=key_name,
            message=language['not_float'].replace("$KEY$", key_name)
        )


class ValidationNotBoolError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationNotBoolError, self).__init__(
            key_name=key_name,
            message=language['not_bool'].replace("$KEY$", key_name)
        )



class SchemaError(Exception):
    message = ''
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
