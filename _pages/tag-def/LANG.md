---
title: LANG
permalink: /terms/v7/LANG.html
layout: none
redirect-from:
  - /terms/v7/LANG
...

```

%YAML 1.2
---
type: structure

tag: LANG

superstructures: [COMM, HEAD, NOTE, PLAC, SNOTE, SUBM, TEXT, TRAN]

substructures:

payload: Special

descriptions:
  - Tag abbreviated from "Language"
  - |
    The human language of the superstructure. In the header, this provides
    the default language for the entire document. In a SUBMITTER_RECORD, it
    provides a language the subject of that record understands. Elsewhere it
    provides the language in which the Text-typed payloads of superstructure
    and its substructures appears.
    
    The payload of LANG structure is a language tag, as defined by IETF BCP
    47. A registry of component subtags is maintained publicly by the IANA.
...

```