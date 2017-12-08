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
                self._check_definition(definition=item[0],data=data,key=key)
            else:
                self._check_definition(definition={'type': item}, data=data, key=key)

    def _check_definition(self,definition,data,key):
        required = definition['required'] if 'required' in definition else self.default_required
        allow_none = definition['allow_none'] if 'allow_none' in definition else self.default_allow_none
        if required:
            if not key in data:
                raise ValidationMissingRequiredKeyError(language=self.language, key=definition['verbose_name'] if 'verbose_name' in definition else key)
                pass
        if data[key] is None:
            if allow_none:
                return
            else:
                raise ValidationNoneValueError(language=self.language, key=definition['verbose_name'] if 'verbose_name' in definition else key)
                pass
        if isinstance(definition['type'], str):  # TypeStr
            # TODO
            pass
        if isinstance(definition['type'], dict):  # Schema
            self._check_schema(schema=definition['type'], data=data[key])
        if isinstance(definition['type'], Validator):  # Validator
            definition['type'].validate(data[key])


    def _is_any(self):
        pass

