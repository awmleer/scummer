from .languages import en

class Validator:
    schema = None
    language = en
    default_required = True
    default_allow_none = True
    def __init__(self, schema):
        self.schema = schema

    def validate(self,data):
        return self._check_schema(schema=self.schema,data=data)

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
                # TODO raise error
                pass
        if data[key] is None:
            if allow_none:
                return
            else:
                # TODO raise error
                pass
        if isinstance(definition['type'], str):  # TypeStr
            pass
        if isinstance(definition['type'], dict):  # Schema
            self._check_definition(definition={'type': definition['type']})
            self._check_schema(schema=definition['type'], data=data[key])
        if isinstance(definition['type'], Validator):  # Validator
            definition['type'].validate(data[key])


    def _is_any(self):
        pass

