# scummer
Python dict validator.

## Basic Formats

### Schema

```
{
  "key1": <Meta> | (<Meta>, <Definition>) | [<Meta>,(<Meta>, <Definition>),...] ,
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
  (some type specific params)
  ...
}
```

### TypeStr

A `TypeStr` can be:

```
'any' | 'str' | 'int' | 'float' | 'bool' | 'array'
```

## Type Specific Params

