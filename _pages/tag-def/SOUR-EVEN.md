---
title: SOUR-EVEN
permalink: /terms/v7/SOUR-EVEN.html
layout: none
redirect-from:
  - /terms/v7/SOUR-EVEN
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/SOUR-EVEN

standard tag: 'EVEN'

specification:
  - Event
  - An enumerated value from set `https://gedcom.io/terms/v7/enumset-EVENATTR`
    indicating the type of event or attribute which was responsible for the source
    entry being recorded. For example, if the entry was created to record a birth
    of a child, then the type would be `BIRT` regardless of the assertions made
    from that record, such as the mother's name or mother's birth date.

label: 'Event'

payload: https://gedcom.io/terms/v7/type-Enum

enumeration set: "https://gedcom.io/terms/v7/enumset-EVENATTR"

substructures:
  "https://gedcom.io/terms/v7/PHRASE": "{0:1}"
  "https://gedcom.io/terms/v7/ROLE": "{0:1}"

superstructures:
  "https://gedcom.io/terms/v7/SOUR": "{0:1}"

contact: "https://gedcom.io/community/"
...

```
