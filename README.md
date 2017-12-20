# scummer
Python dict validator.

## Basic Formats

### Schema

```
{
  "key1": <Definition>,
  "key2": <Definition>,
  ...
}
```

### Definition

A definition is one of these three forms:

```
<Meta>
```

```
(<Meta>, <Param>)
```

```
[<Meta>,(<Meta>, <Param>),...]
```

### Meta

A meta is an instance of one of these classes:

```
<TypeStr> | <Validator> | <Schema>
```

### Param

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

**definition**: a definition (see above)

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