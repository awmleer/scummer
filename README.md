# scummer
Python dict validator.

### Schema

```
{
  "key1": <Meta> | (<Meta>, <Definition>),
  "key2": ...
  ...
}
```

### Meta

A meta is an instance of one of these classes:

```
<TypeStr> | <Validator> | <Schema>
```

### Definition

```
{
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



