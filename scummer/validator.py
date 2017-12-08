from .languages import en
from .errors import *

class Validator:
    schema = None
    language = en
    default_required = True
    default_allow_none = True
    def __init__(self, schema):
        self.schema = schema

    def validate(self,data):
        return self._check_schema(schema=self.schema,data=data)

    def is_validate(self,data):
        try:
            self.validate(data)
            return True
        except ValidationError:
            return False

    def _check_schema(self,schema,data):
        if schema is None:
            return
        for key in self.schema:
            item = self.schema[key]
            if isinstance(item,tuple): # Definition
                self._check_definition(type_name=item[0], definition=item[1], data=data, key=key)
            else:
                self._check_definition(type_name=item, data=data, key=key)

    def _check_definition(self,data, key, type_name, definition={}):
        required = definition['required'] if 'required' in definition else self.default_required
        allow_none = definition['allow_none'] if 'allow_none' in definition else self.default_allow_none
        print(definition)
        key_name = definition['verbose_name'] if 'verbose_name' in definition else key
        if not key in data:
            if required:
                raise ValidationMissingRequiredKeyError(language=self.language, key_name=key_name)
            else:
                return
        if data[key] is None:
            if allow_none:
                return
            else:
                raise ValidationNoneValueError(language=self.language, key_name=key_name)
        if isinstance(type_name, str):  # TypeStr
            # TODO
            pass
        if isinstance(type_name, dict):  # Schema
            self._check_schema(schema=type_name, data=data[key])
        if isinstance(type_name, Validator):  # Validator
            type_name.validate(data[key])


    def _is_any(self):
        pass

