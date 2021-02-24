---
title: RECORD.SUBM
permalink: /terms/v7/RECORD.SUBM.html
layout: none
redirect-from:
  - /terms/v7/RECORD.SUBM
...

```

%YAML 1.2
---
type: structure

tag: SUBM

superstructures: [RECORD]

substructures:
  ADDR: "{0:1}"
  CHAN: "{0:1}"
  CREA: "{0:1}"
  EMAIL: "{0:M}"
  EXID: "{0:M}"
  FAX: "{0:M}"
  LANG: "{0:M}"
  NAME: "{1:1}"
  NOTE: "{0:M}"
  OBJE: "{0:M}"
  PHON: "{0:M}"
  REFN: "{0:M}"
  SNOTE: "{0:M}"
  UID: "{0:M}"
  WWW: "{0:M}"

payload: None

descriptions:
  - also called SUBMITTER_RECORD
  - The submitter record identifies an individual or organization that
    contributed information contained in the GEDCOM document. All records in
    the document are assumed to be contributed by the submitter referenced
    in the HEAD, unless a SUBM structure inside a specific record points at
    a different submitter record.
...

```