---
title: MEDI
permalink: /terms/v7/MEDI.html
layout: none
redirect-from:
  - /terms/v7/MEDI
...

```

%YAML 1.2
---
type: structure

tag: MEDI

superstructures: [CALN, FORM]

substructures:
  PHRASE: "{0:1}"

payload: Enum

enumeraton values: [AUDIO, BOOK, CARD, ELECTRONIC, FICHE, FILM, MAGAZINE, 
  MANUSCRIPT, MAP, NEWSPAPER, OTHER, PHOTO, TOMBSTONE, VIDEO]

descriptions:
  - Tag abbreviated from "Medium"
  - An enumerated value providing information about the media or the medium
    in which information is stored.
...

```