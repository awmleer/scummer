# scummer
Python dict validator.

### Schema

```
{
  "key1": <TypeStr> | <Validator> | <Schema> | (<Definition>),
  "key2": ...
  ...
}
```

### Definition

```
{
  "type": <TypeStr> | <Validator> | <Schema>,
  "required"?: <boolean>,
  "allow_none"?: <boolean>,
  "verbose_name"?: <string>,
  ...
  (some type specific fields)
  ...
}
```

### TypeStr

A `TypeStr` is:

```
'any' | 'str' | 'int' | 'float' | 'bool' | 'array'
```



