class ValidationError(Exception):
    message = ''
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message


class ValidationKeyError(ValidationError):
    key_name = None
    def __init__(self, key_name, message):
        self.key_name=key_name
        super(ValidationKeyError, self).__init__(message=message)


class ValidationKeyGeneralError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationKeyGeneralError, self).__init__(
            key_name=key_name,
            message=language['key_general_error'].replace("$KEY$", key_name)
        )


class ValidationNoTypeMatchError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationNoTypeMatchError, self).__init__(
            key_name=key_name,
            message=language['no_type_match'].replace("$KEY$", key_name)
        )


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


class ValidationNotNumberError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationNotNumberError, self).__init__(
            key_name=key_name,
            message=language['not_number'].replace("$KEY$", key_name)
        )


class ValidationNotBoolError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationNotBoolError, self).__init__(
            key_name=key_name,
            message=language['not_bool'].replace("$KEY$", key_name)
        )


class ValidationNotArrayError(ValidationKeyError):
    def __init__(self, language, key_name):
        super(ValidationNotArrayError, self).__init__(
            key_name=key_name,
            message=language['not_array'].replace("$KEY$", key_name)
        )


class ValidationMaxLengthError(ValidationKeyError):
    def __init__(self, language, key_name, length):
        super(ValidationMaxLengthError, self).__init__(
            key_name=key_name,
            message=language['max_length'].replace("$KEY$", key_name).replace("$LENGTH$", str(length))
        )


class ValidationMaxLimitError(ValidationKeyError):
    def __init__(self, language, key_name, max):
        super(ValidationMaxLimitError, self).__init__(
            key_name=key_name,
            message=language['max_limit'].replace("$KEY$", key_name).replace("$MAX$", str(max))
        )


class ValidationMinLimitError(ValidationKeyError):
    def __init__(self, language, key_name, min):
        super(ValidationMinLimitError, self).__init__(
            key_name=key_name,
            message=language['min_limit'].replace("$KEY$", key_name).replace("$MIN$", str(min))
        )



class SchemaError(Exception):
    message = ''
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message
