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
type: structure

tag: FILE

superstructures: [OBJE]

substructures:
  FORM: "{1:1}"
  TITL: "{0:1}"

payload: Special

descriptions:
  - |
    A reference to an external file. Syntactically, the payload is a URL, as
    defined by IETF RFC 1808 and https://url.spec.whatwg.org/. However, only
    some URLs may be used:
    
    -   A URL with scheme ftp, http, or https refers to a web-accessible
        file.
    
    -   A URL with scheme file refers to a machine-local file. Machine-local
        files must not be used in GEDZIP nor when sharing GEDCOM documents
        on the web or with unknown parties, but may be used for close
        collaboration between parties with known similar file structures.
    
    -   A URL with all of the following:
    
        -   no scheme
        -   not beginning with / (U+002F)
        -   not containing any path segments equal to .. (U+002E U+002E)
        -   not containing a reverse solidus character (U+005C \) or banned
            character, either directly or in escaped form
        -   no query or fragment
    
        refers to a local file. If the GEDCOM document is part of a GEDZIP,
        the URL of the local file is a zip archive filename; otherwise, the
        URL of a local file is resolved with base equal to the directory
        containing the GEDCOM file.
    
    The meaning of a FILE payload with any URL format not listed above is
    undefined in GEDCOM 7.0, but may be defined in subsequent versions of
    GEDCOM.
...

```