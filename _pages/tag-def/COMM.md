---
title: COMM
permalink: /terms/v7/COMM.html
layout: none
redirect-from:
  - /terms/v7/COMM
...

```

%YAML 1.2
---
type: structure

tag: COMM

superstructures: [CHAN, SOUR]

substructures:
  LANG: "{0:1}"
  MIME: "{0:1}"

payload: Text

descriptions:
  - Tag abbreviated from "Comment"
  - also called COMMENT_STRUCTURE
  - Like a NOTE_STRUCTURE, but without a source citation substructure.
  - A COMMENT_STRUCTURE, which has the same semantic meaning as a
    NOTE_STRUCTURE but may not have SOUR substructures.
...

```