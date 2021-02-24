---
title: RECORD.OBJE
permalink: /terms/v7/RECORD.OBJE.html
layout: none
redirect-from:
  - /terms/v7/RECORD.OBJE
...

```

%YAML 1.2
---
type: structure

tag: OBJE

superstructures: [RECORD]

substructures:
  CHAN: "{0:1}"
  CREA: "{0:1}"
  EXID: "{0:M}"
  FILE: "{1:M}"
  NOTE: "{0:M}"
  REFN: "{0:M}"
  RESN: "{0:1}"
  SNOTE: "{0:M}"
  SOUR: "{0:M}"
  UID: "{0:M}"

payload: None

descriptions:
  - also called MULTIMEDIA_RECORD
  - |
    The multimedia record refers to one ore more external digital files, and
    may provide some additional information about the files and the media
    they encode.
    
    The file reference can occur more than once to group multiple files
    together. Grouped files should each pertain to the same context. For
    example, a sound clip and a photo both of the same event might be
    grouped in a single OBJE.
    
    The change and creation dates should be for the OBJE record itself, not
    the underlying files.
...

```