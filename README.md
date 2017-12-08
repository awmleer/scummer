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
  (some meta specific params)
  ...
}
```

### TypeStr

A `TypeStr` can be a **basic type string**:

```
'any' | 'str' | 'int' | 'float' | 'bool'
```

or:

```
'array'
```

or a **basic type string** with a `[]`, such as:

```
'any[]' | 'str[]' | 'int[]'
```

## Meta Specific Params

### array

```
"basic_type": a basic type string
```

