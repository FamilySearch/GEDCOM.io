---
title: type-Age
permalink: /terms/v7/type-Age.html
layout: none
redirect-from:
  - /terms/v7/type-Age
...

```

%YAML 1.2
---
lang: en-US

type: data type

uri: https://gedcom.io/terms/v7/type-Age

specification:
  - |
    Ages are represented by counts of years, months, weeks, and days.
    
    ```abnf
    Age         = [[ageBound D] ageDuration]
    
    ageBound    = "<" / ">"
    ageDuration = years [D months] [D weeks] [D days]
                / months [D weeks] [D days]
                / weeks [D days]
                / days
    
    years   = Integer %x79    ; 35y
    months  = Integer %x6D    ; 11m
    weeks   = Integer %x77    ; 8w
    days    = Integer %x64    ; 21d
    ```
    
    Where
    
    | Production | Meaning                                        |
    | :--------- | :--------------------------------------------- |
    | `<`        | The real age was less than the provided age    |
    | `>`        | The real age was greater than the provided age |
    | `years`    | a number of years                              |
    | `months`   | a number of months                             |
    | `weeks`    | a number of weeks                              |
    | `days`     | a number of days                               |
    
    Non-integer numbers should be rounded down to an integer. Thus, if someone has
    lived for 363.5 days, their age might be written as `363d`, `51w 6d`, `51w`,
    `0y`, etc.
    
    Because numbers are rounded down, `>` effectively includes its endpoint; that
    is, the age `> 8d` includes people who have lived 8 days + a few seconds.
    
    Different cultures count ages differently. Some increment years on the
    anniversary of birth and others at particular seasons. Some round to the
    nearest year, others round years down, others round years up. Because users may
    be unaware of these traditions or may fail to convert them to the round-down
    convention, errors in age of up to a year are common.
    
    <div class="note">
    
    Because age payloads are intended to allow recording the age as it was recorded
    in records that could contain errors, odd ages such as `8w 30d`, `1y 400d`,
    `1y 30m`, etc. are permitted. Some applications might convert these to more
    standard forms; if so, it is recommended that they use a `PHRASE` substructure
    to hold the original form.
    
    </div>
    
    Age payloads may also be omitted entirely if no suitable form is known but a
    substructure (such as a `PHRASE`) is desired.
    
    <div class="note">
    
    Versions 5.5 and 5.5.1 allowed a few specific phrases inside `Age` payloads.
    Age phrases were moved to the `PHRASE` substructure in 7.0.
    
    </div>
    
    The URI for the `Age` data type is `https://gedcom.io/terms/v7/type-Age`.

contact: "https://gedcom.io/community/"
...

```
