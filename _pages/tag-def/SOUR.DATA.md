---
title: SOUR.DATA
permalink: /terms/v7/SOUR.DATA.html
layout: none
redirect-from:
  - /terms/v7/SOUR.DATA
...

```

%YAML 1.2
---
type: structure

tag: DATA

superstructures: [SOUR]

substructures:
  DATE: "{0:1}"
  TEXT: "{0:M}"

payload: None

descriptions:
  - A structure with no payload used to distinguish a description of
    something from metadata about it. For example, SOUR and its other
    substructures describe a source itself, while SOUR.DATA describes the
    content of the source.
...

```