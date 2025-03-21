---
title: DATA
permalink: /terms/v7/DATA.html
layout: none
redirect-from:
  - /terms/v7/DATA
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/DATA

standard tag: 'DATA'

specification:
  - Data
  - A structure with no payload used to distinguish a description of something from
    metadata about it. For example, `SOUR` and its other substructures describe a
    source itself, while `SOUR`.`DATA` describes the content of the source.

label: 'Data'

payload: null

substructures:
  "https://gedcom.io/terms/v7/AGNC": "{0:1}"
  "https://gedcom.io/terms/v7/DATA-EVEN": "{0:M}"
  "https://gedcom.io/terms/v7/NOTE": "{0:M}"
  "https://gedcom.io/terms/v7/SNOTE": "{0:M}"

superstructures:
  "https://gedcom.io/terms/v7/record-SOUR": "{0:1}"

contact: "https://gedcom.io/community/"
...

```
