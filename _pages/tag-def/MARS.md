---
title: MARS
permalink: /terms/v7/MARS.html
layout: none
redirect-from:
  - /terms/v7/MARS
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/MARS

standard tag: 'MARS'

specification:
  - Marriage settlement
  - A [Family Event]. See also `FAMILY_EVENT_STRUCTURE`.
  - marriage settlement
  - Creating an agreement between 2 people contemplating marriage, at which time
    they agree to release or modify property rights that would otherwise arise from
    the marriage.

label: 'Marriage settlement'

payload: Y|<NULL>

substructures:
  "https://gedcom.io/terms/v7/ADDR": "{0:1}"
  "https://gedcom.io/terms/v7/AGNC": "{0:1}"
  "https://gedcom.io/terms/v7/ASSO": "{0:M}"
  "https://gedcom.io/terms/v7/CAUS": "{0:1}"
  "https://gedcom.io/terms/v7/DATE": "{0:1}"
  "https://gedcom.io/terms/v7/EMAIL": "{0:M}"
  "https://gedcom.io/terms/v7/FAX": "{0:M}"
  "https://gedcom.io/terms/v7/HUSB": "{0:1}"
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
  "https://gedcom.io/terms/v7/WIFE": "{0:1}"
  "https://gedcom.io/terms/v7/WWW": "{0:M}"

superstructures:
  "https://gedcom.io/terms/v7/record-FAM": "{0:M}"

value of:
  - "https://gedcom.io/terms/v7/enumset-EVEN"
  - "https://gedcom.io/terms/v7/enumset-EVENATTR"

contact: "https://gedcom.io/community/"
...

```
