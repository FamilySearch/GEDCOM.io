---
title: FILE
permalink: /terms/v7/FILE.html
layout: none
redirect-from:
  - /terms/v7/FILE
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/FILE

standard tag: 'FILE'

specification:
  - File reference
  - A reference to an external file. See the [File Path datatype] for more details.

label: 'File reference'

payload: https://gedcom.io/terms/v7/type-FilePath

substructures:
  "https://gedcom.io/terms/v7/FILE-TRAN": "{0:M}"
  "https://gedcom.io/terms/v7/FORM": "{1:1}"
  "https://gedcom.io/terms/v7/TITL": "{0:1}"

superstructures:
  "https://gedcom.io/terms/v7/record-OBJE": "{1:M}"

contact: "https://gedcom.io/community/"
...

```
