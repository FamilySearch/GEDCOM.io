---
title: PAGE
permalink: /terms/v7/PAGE.html
layout: none
redirect-from:
  - /terms/v7/PAGE
...

```

%YAML 1.2
---
type: structure

tag: PAGE

superstructures: [SOUR]

substructures:

payload: Text

descriptions:
  - Tag abbreviated from "Page"
  - |
    A specific location within the information referenced. For a published
    work, this could include the volume of a multi-volume work and the page
    number or numbers. For a periodical, it could include volume, issue, and
    page numbers. For a newspaper, it could include a date, page number, and
    column number. For an unpublished source or microfilmed works, this
    could be a film or sheet number, page number, or frame number. A census
    record might have an enumerating district, page number, line number,
    dwelling number, and family number.
    
    It is recommended that the data in this field be formatted
    comma-separated with label: value pairs
    
        2 SOUR @S1@
        3 PAGE Film: 1234567, Frame: 344, Line: 28
...

```