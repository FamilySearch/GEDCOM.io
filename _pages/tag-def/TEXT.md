---
title: TEXT
permalink: /terms/v7/TEXT.html
layout: none
redirect-from:
  - /terms/v7/TEXT
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/TEXT

standard tag: 'TEXT'

specification:
  - Text from Source
  - A verbatim copy of any description contained within the source. This indicates
    notes or text that are actually contained in the source document, not the
    submitter's opinion about the source. This should be, from the evidence point
    of view, "what the original record keeper said" as opposed to the researcher's
    interpretation.

label: 'Text from Source'

payload: http://www.w3.org/2001/XMLSchema#string

substructures:
  "https://gedcom.io/terms/v7/LANG": "{0:1}"
  "https://gedcom.io/terms/v7/MIME": "{0:1}"

superstructures:
  "https://gedcom.io/terms/v7/SOUR-DATA": "{0:M}"
  "https://gedcom.io/terms/v7/record-SOUR": "{0:1}"

contact: "https://gedcom.io/community/"
...

```
