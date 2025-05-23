---
title: CROP
permalink: /terms/v7/CROP.html
layout: none
redirect-from:
  - /terms/v7/CROP
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/CROP

standard tag: 'CROP'

specification:
  - Crop
  - |
    A subregion of an image to display. It is only valid when the superstructure
    links to a `MULTIMEDIA_RECORD` with at least 1 `FILE` substructure that refers
    to an external file with a defined pixel unit.
    
    `LEFT` and `TOP` indicate the top-left corner of the region to display. `WIDTH`
    and `HEIGHT` indicate how many pixels wide and tall the region to display is.
    If omitted, `LEFT` and `TOP` each default to 0; `WIDTH` defaults to the image
    width minus `LEFT`; and `HEIGHT` defaults to the image height minus `TOP`.
    
    If the superstructure links to a `MULTIMEDIA_RECORD` that includes multiple
    `FILE` substructures, the `CROP` applies to the first `FILE` to which it can
    apply, namely the first external file with a defined pixel unit.
    
    It is recommended that `CROP` be used only with a single-FILE
    `MULTIMEDIA_RECORD`.
    
    The following are errors:
    
    - `LEFT` or `LEFT` + `WIDTH` exceed the image width.
    - `TOP` or `TOP` + `HEIGHT` exceed the image height.
    - `CROP` applied to a non-image or image without a defined pixel unit.

label: 'Crop'

payload: null

substructures:
  "https://gedcom.io/terms/v7/HEIGHT": "{0:1}"
  "https://gedcom.io/terms/v7/LEFT": "{0:1}"
  "https://gedcom.io/terms/v7/TOP": "{0:1}"
  "https://gedcom.io/terms/v7/WIDTH": "{0:1}"

superstructures:
  "https://gedcom.io/terms/v7/OBJE": "{0:1}"

contact: "https://gedcom.io/community/"
...

```
