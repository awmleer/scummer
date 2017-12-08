class ValidationError(Exception):
    message = ''
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message


class ValidationMissingRequiredKeyError(ValidationError):
    key_name = None
    def __init__(self, language, key_name):
        self.key_name = key_name
        super(ValidationMissingRequiredKeyError, self).__init__(language['missing_required_key'].replace("$KEY$", key_name))


class ValidationNoneValueError(ValidationError):
    key_name = None
    def __init__(self, language, key_name):
        self.key_name = key_name
        super(ValidationNoneValueError, self).__init__(language['none_value'].replace("$KEY$", key_name))