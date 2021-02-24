---
title: RECORD.SOUR
permalink: /terms/v7/RECORD.SOUR.html
layout: none
redirect-from:
  - /terms/v7/RECORD.SOUR
...

```

%YAML 1.2
---
type: structure

tag: SOUR

superstructures: [RECORD]

substructures:
  ABBR: "{0:1}"
  AUTH: "{0:1}"
  CHAN: "{0:1}"
  CREA: "{0:1}"
  EXID: "{0:M}"
  NOTE: "{0:M}"
  OBJE: "{0:M}"
  PUBL: "{0:1}"
  REFN: "{0:M}"
  SNOTE: "{0:M}"
  SOUR.DATA: "{0:1}"
  SOUR.REPO: "{0:M}"
  TEXT: "{0:1}"
  TITL: "{0:1}"
  UID: "{0:M}"

payload: None

descriptions:
  - also called SOURCE_RECORD
  - |
    A source record describes an entire source. A source may also point to
    REPOs to describe repositories or archives where the source document may
    be found. The part of a source relevant to a specific fact, such as a
    specific page or entry, is indicated in a SOURCE_CITATION that points to
    the source record.
    
    This sourcing model is known to be insufficient for some use cases and
    may be refined in a future version of GEDCOM.
    
    A SOURCE_RECORD may contain a pointers to a SHARED_NOTE_RECORD and vice
    versa. Applications must not create GEDCOM document where these mutual
    pointers form a cycle. Applications should also ensure they can handle
    invalid files with such cycles in a safe manner.
...

```