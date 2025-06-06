---
title: type-Enum
permalink: /terms/v7/type-Enum.html
layout: none
redirect-from:
  - /terms/v7/type-Enum
...

```

%YAML 1.2
---
lang: en-US

type: data type

uri: https://gedcom.io/terms/v7/type-Enum

specification:
  - |
    An enumeration is a selection from a set of options. They are represented as a
    string matching the same production as a tag, with the additional permission
    that standard enumerations may be integers.
    
    ```abnf
    stdEnum = stdTag / Integer
    Enum    = stdEnum / extTag
    ```
    
    Each structure type with an enumeration payload also defines specific payload
    values it permits. These permitted payloads match production `stdEnum` and
    should each have a defined URI. Payload values that match production `extTag`
    are always permitted in structures with an enumeration payload and have their
    URI defined by the schema.
    
    Each enumeration value has a distinct meaning as identified by its
    corresponding URI.
    
    The URI of a given tag in an enumeration payload is determined by the tag
    itself and by the structure type of the structure it is in the payload of.
    
    <div class="example">
    
    The tag `HUSB` is used in this document to represent two enumeration values.
    Which one is meant can be identified by the structure type it appears in as
    follows:
    
    | Containing structure type              | Enumeration value identified by tag `HUSB`  |
    | -------------------------------------- | ------------------------------------------- |
    | `https://gedcom.io/terms/v7/FAMC-ADOP` | `https://gedcom.io/terms/v7/enum-ADOP-HUSB` |
    | `https://gedcom.io/terms/v7/ROLE`      | `https://gedcom.io/terms/v7/enum-HUSB`      |
    
    An [extension] could also place either of these enumeration values in an
    extension structure type; the extension authors should document which one they
    permit.
    
    The `HUSB` tag is also used to identify two different structure types,
    `https://gedcom.io/terms/v7/FAM-HUSB` and `https://gedcom.io/terms/v7/HUSB`.
    
    </div>
    
    The URI for the `Enum` data type is `https://gedcom.io/terms/v7/type-Enum`.

contact: "https://gedcom.io/community/"
...

```
