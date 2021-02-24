---
title: NAME.TRAN
permalink: /terms/v7/NAME.TRAN.html
layout: none
redirect-from:
  - /terms/v7/NAME.TRAN
...

```

%YAML 1.2
---
type: structure

tag: TRAN

superstructures: [NAME]

substructures:
  GIVN: "{0:M}"
  LANG: "{1:1}"
  NICK: "{0:M}"
  NPFX: "{0:M}"
  NSFX: "{0:M}"
  SPFX: "{0:M}"
  SURN: "{0:M}"

payload: Personal Name

descriptions:
  - Tag abbreviated from "Translation or transliteration"
  - A translation or transliteration of the superstructure. It presents
    information in the same format as the superstructure, but with a
    different language tag. See PLACE_STRUCTURE, PERSONAL_NAME_STRUCTURE,
    and LANG for more.
...

```