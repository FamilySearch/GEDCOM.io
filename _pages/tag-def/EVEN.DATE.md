---
title: EVEN.DATE
permalink: /terms/v7/EVEN.DATE.html
layout: none
redirect-from:
  - /terms/v7/EVEN.DATE
...

```

%YAML 1.2
---
type: structure

tag: DATE

superstructures: [EVEN]

substructures:
  PHRASE: "{0:1}"
  TIME: "{0:1}"

payload: DateValue

descriptions:
  - The principle date of the subject of the superstructure. The payload is
    a DateValue, and the DATE structure may have a PHRASE substructure.
...

```