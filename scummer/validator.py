from .languages import en
from .errors import *

class Validator:
    schema = None
    language = en
    default_required = True
    default_allow_none = True

    def __init__(self, schema=None):
        self.schema = schema

    def validate(self,data):
        return self._check_schema(schema=self.schema,data=data)

    def is_valid(self,data):
        try:
            self.validate(data)
            return True
        except ValidationError:
            return False

    def _check_schema(self,schema,data):
        if schema is None:
            return
        for key in schema:
            self._check_key(data=data, key=key, item=schema[key])


    def _check_key(self, data, key, item):
        if isinstance(item, tuple):  # Definition
            self._check_definition(meta=item[0], definition=item[1], data=data, key=key)
        elif isinstance(item, list):
            flag = True
            key_name = key
            for i in item:
                try:
                    self._check_key(data=data, key=key, item=i)
                    flag = False
                except ValidationKeyError as e:
                    key_name=e.key_name
                except ValidationError:
                    pass
            if flag:
                raise ValidationNoTypeMatchError(language=self.language, key_name=key_name)
        else:
            self._check_definition(meta=item, data=data, key=key)

    def _check_definition(self,data, key, meta, definition={}):
        required = definition['required'] if 'required' in definition else self.default_required
        allow_none = definition['allow_none'] if 'allow_none' in definition else self.default_allow_none
        key_name = definition['verbose_name'] if 'verbose_name' in definition else key
        # print(data)
        # print(key)
        # print(meta)
        # print(definition)
        # print('-----')
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
        if isinstance(meta, str):  # TypeStr
            if meta == 'array':
                basic_type = definition['basic_type'] if 'basic_type' in definition else 'any'
                self._check_array(value=data[key], key_name=key_name, basic_type=basic_type)
            elif meta.endswith('[]'):
                self._check_array(value=data[key], key_name=key_name, basic_type=meta.replace('[]',''))
            else:
                self._check_type(type_str=meta, value=data[key], key_name=key_name)
        if isinstance(meta, dict):  # Schema
            self._check_schema(schema=meta, data=data[key])
        if isinstance(meta, Validator):  # Validator
            meta.validate(data[key])

    def _check_array(self, value, key_name, basic_type='any'):
        if not isinstance(value, list):
            raise ValidationNotArrayError(language=self.language, key_name=key_name)
        for v in value:
            try:
                self._check_type(type_str=basic_type, value=v, key_name=key_name)
            except ValidationKeyError:
                raise ValidationKeyError(
                    key_name=key_name,
                    message=self.language['key_general_error'].replace("$KEY$",key_name)
                )

    def _check_type(self, type_str, value, key_name):
        if type_str == 'any':
            return
        elif type_str == 'int':
            if type(value) != int:
                raise ValidationNotIntError(language=self.language, key_name=key_name)
        elif type_str == 'str':
            if type(value) != str:
                raise ValidationNotStrError(language=self.language, key_name=key_name)
        elif type_str == 'float':
            if type(value) != float:
                raise ValidationNotFloatError(language=self.language, key_name=key_name)
        elif type_str == 'bool':
            if type(value) != bool:
                raise ValidationNotBoolError(language=self.language, key_name=key_name)
        else:
            raise SchemaError(message='Type '+type_str+'is invalid')

