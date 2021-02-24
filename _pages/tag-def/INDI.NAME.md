---
title: INDI.NAME
permalink: /terms/v7/INDI.NAME.html
layout: none
redirect-from:
  - /terms/v7/INDI.NAME
...

```

%YAML 1.2
---
type: structure

tag: NAME

superstructures: [INDI]

substructures:
  GIVN: "{0:M}"
  NAME.TRAN: "{0:M}"
  NAME.TYPE: "{0:1}"
  NICK: "{0:M}"
  NOTE: "{0:M}"
  NPFX: "{0:M}"
  NSFX: "{0:M}"
  SNOTE: "{0:M}"
  SOUR: "{0:M}"
  SPFX: "{0:M}"
  SURN: "{0:M}"

payload: Personal Name

descriptions:
  - also called PERSONAL_NAME_STRUCTURE
  - A PERSONAL_NAME_STRUCTURE with parts, translations, sources, and so
    forth.
  - |
    Names of individuals are represented in the manner the name is normally
    spoken, with the family name, surname, or nearest cultural parallel
    thereunto separated by slashes (U+002F /). Based on the dynamic nature
    or unknown compositions of naming conventions, it is difficult to
    provide more detailed name piece structure to handle every case. The
    PERSONAL_NAME_PIECES are provided optionally for systems that cannot
    operate effectively with less structured information. The Personal Name
    payload shall be seen as the primary name representation, with name
    pieces as optional auxiliary information.
    
    The name may be translated or transliterated into different languages or
    scripts using the TRAN substructure. It is recommended, but not
    required, that if the name pieces are used, the same pieces are used in
    each translation and transliteration.
    
    A TYPE is used to specify the particular variation that this name is.
    For example; it could indicate that this name is a name taken at
    immigration or that it could be an ‘also known as’ name. See the
    NAME.TYPE enumeration for more.
    
    Alternative approaches to representing names are being considered for
    future GEDCOM releases.
...

```