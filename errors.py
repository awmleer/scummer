class ValidationError(Exception):
    message = ''
    def __init__(self, message):
        self.message = message
    def __str__(self):
        return self.message


class ValidationMissingRequiredKeyError(ValidationError):
    key = ''
    def __init__(self, language, key):
        self.key = key
        super(language['missing_required_key'].replace("$KEY$", key))


class ValidationNoneValueError(ValidationError):
    def __init__(self, language, key):
        self.key = key
        super(language['none_value'].replace("$KEY$", key))