---
title: INDI-NCHI
permalink: /terms/v7/INDI-NCHI.html
layout: none
redirect-from:
  - /terms/v7/INDI-NCHI
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/INDI-NCHI

standard tag: 'NCHI'

specification:
  - Number of children
  - An [Individual Attribute]. See also `INDIVIDUAL_ATTRIBUTE_STRUCTURE`.
  - number of children
  - The number of children that this person is known to be the parent of (all
    marriages).

label: 'Number of children'

payload: http://www.w3.org/2001/XMLSchema#nonNegativeInteger

substructures:
  "https://gedcom.io/terms/v7/ADDR": "{0:1}"
  "https://gedcom.io/terms/v7/AGE": "{0:1}"
  "https://gedcom.io/terms/v7/AGNC": "{0:1}"
  "https://gedcom.io/terms/v7/ASSO": "{0:M}"
  "https://gedcom.io/terms/v7/CAUS": "{0:1}"
  "https://gedcom.io/terms/v7/DATE": "{0:1}"
  "https://gedcom.io/terms/v7/EMAIL": "{0:M}"
  "https://gedcom.io/terms/v7/FAX": "{0:M}"
  "https://gedcom.io/terms/v7/NOTE": "{0:M}"
  "https://gedcom.io/terms/v7/OBJE": "{0:M}"
  "https://gedcom.io/terms/v7/PHON": "{0:M}"
  "https://gedcom.io/terms/v7/PLAC": "{0:1}"
  "https://gedcom.io/terms/v7/RELI": "{0:1}"
  "https://gedcom.io/terms/v7/RESN": "{0:1}"
  "https://gedcom.io/terms/v7/SDATE": "{0:1}"
  "https://gedcom.io/terms/v7/SNOTE": "{0:M}"
  "https://gedcom.io/terms/v7/SOUR": "{0:M}"
  "https://gedcom.io/terms/v7/TYPE": "{0:1}"
  "https://gedcom.io/terms/v7/UID": "{0:M}"
  "https://gedcom.io/terms/v7/WWW": "{0:M}"

superstructures:
  "https://gedcom.io/terms/v7/record-INDI": "{0:M}"

contact: "https://gedcom.io/community/"
...

```
