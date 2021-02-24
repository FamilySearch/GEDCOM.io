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
type: structure

tag: DATA

superstructures: [SOUR]

substructures:
  AGNC: "{0:1}"
  DATA.EVEN: "{0:M}"
  NOTE: "{0:M}"
  SNOTE: "{0:M}"

payload: None

descriptions:
  - A structure with no payload used to distinguish a description of
    something from metadata about it. For example, SOUR and its other
    substructures describe a source itself, while SOUR.DATA describes the
    content of the source.
...

```