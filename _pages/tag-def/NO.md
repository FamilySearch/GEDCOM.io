---
title: NO
permalink: /terms/v7/NO.html
layout: none
redirect-from:
  - /terms/v7/NO
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/NO

standard tag: 'NO'

specification:
  - Did not happen
  - |
    An enumerated value from set `https://gedcom.io/terms/v7/enumset-EVEN`
    identifying an event type which did not occur to the superstructure's subject.
    A specific payload `NO XYZ` should only appear where `XYZ` would be legal.
    
    See `NON_EVENT_STRUCTURE` for more details.
  - |
    Indicates that a specific type of event, given in the payload, did not happen
    within a given date period (or never happened if there is no `DATE`
    substructure).
    
    Substructures may provide discussion about the non-occurrence of the event but
    must not limit the meaning of what did not occur. No substructure other than
    `DATE` may restrict the breadth of that negative assertion.
    
    <div class="example">
    
    `1 NO MARR` means "no marriage occurred"
    
    </div>
    
    <div class="example">
    
    ```gedcom
    1 NO MARR
    2 DATE TO 24 MAR 1880
    ```
    
    means "no marriage had occurred as of March 24^th^, 1880"
    
    </div>

label: 'Did not happen'

payload: https://gedcom.io/terms/v7/type-Enum

enumeration set: "https://gedcom.io/terms/v7/enumset-EVEN"

substructures:
  "https://gedcom.io/terms/v7/NO-DATE": "{0:1}"
  "https://gedcom.io/terms/v7/NOTE": "{0:M}"
  "https://gedcom.io/terms/v7/SNOTE": "{0:M}"
  "https://gedcom.io/terms/v7/SOUR": "{0:M}"

superstructures:
  "https://gedcom.io/terms/v7/record-FAM": "{0:M}"
  "https://gedcom.io/terms/v7/record-INDI": "{0:M}"

contact: "https://gedcom.io/community/"
...

```
