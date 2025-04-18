---
title: HEAD-SOUR-DATA
permalink: /terms/v7/HEAD-SOUR-DATA.html
layout: none
redirect-from:
  - /terms/v7/HEAD-SOUR-DATA
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/HEAD-SOUR-DATA

standard tag: 'DATA'

specification:
  - Data
  - The database, electronic data source, or digital repository from which this
    dataset was exported. The payload is the name of the database, electronic data
    source, or digital repository, with substructures providing additional details
    about it (not about the export).

label: 'Data'

payload: http://www.w3.org/2001/XMLSchema#string

substructures:
  "https://gedcom.io/terms/v7/COPR": "{0:1}"
  "https://gedcom.io/terms/v7/DATE-exact": "{0:1}"

superstructures:
  "https://gedcom.io/terms/v7/HEAD-SOUR": "{0:1}"

contact: "https://gedcom.io/community/"
...

```
