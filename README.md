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
  "required"?: <boolean>, //default is True
  "allow_none"?: <boolean>, //default is False
  "verbose_name"?: <string>,
  ...
  (some meta specific params)
  ...
}
```

### TypeStr

A `TypeStr` can be a **basic type string**:

```
'any' | 'str' | 'int' | 'float' | 'bool' | 'number' | 'enum'
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

### map

**basic_type**: a basic type string

### array

**basic_type**: a basic type string

**max_length**: an integer

### str

**basic_type**: a basic type string

**max_length**: an integer

### int

**max**: the upper limit (<=)

**min**: the lower limit (>=)

### float

**max**: the upper limit (<=)

**min**: the lower limit (>=)

### enum

**items**: a list contain the possible values, default as []