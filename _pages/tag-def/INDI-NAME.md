---
title: INDI-NAME
permalink: /terms/v7/INDI-NAME.html
layout: none
redirect-from:
  - /terms/v7/INDI-NAME
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/INDI-NAME

standard tag: 'NAME'

specification:
  - Name
  - A `PERSONAL_NAME_STRUCTURE` with parts, translations, sources, and so forth.
  - |
    Names of individuals are represented in the manner the name is normally spoken,
    with the family name, surname, or nearest cultural parallel thereunto separated
    by slashes (U+002F `/`). Based on the dynamic nature or unknown compositions of
    naming conventions, it is difficult to provide a more detailed name piece
    structure to handle every case. The `PERSONAL_NAME_PIECES` are provided
    optionally for systems that cannot operate effectively with less structured
    information. The Personal Name payload shall be seen as the primary name
    representation, with name pieces as optional auxiliary information; in
    particular it is recommended that all name parts in `PERSONAL_NAME_PIECES`
    appear within the `PersonalName` payload in some form, possibly adjusted for
    gender-specific suffixes or the like. It is permitted for the payload to
    contain information not present in any name piece substructure.
    
    The name may be translated or transliterated into different languages or
    scripts using the `TRAN` substructure. It is recommended, but not required,
    that if the name pieces are used, the same pieces are used in each translation
    and transliteration.
    
    A `TYPE` is used to specify the particular variation that this name is. For
    example; it could indicate that this name is a name taken at immigration or
    that it could be an ‘also known as’ name. See
    `https://gedcom.io/terms/v7/enumset-NAME-TYPE` for more details.
    
    <div class="note">
    
    Alternative approaches to representing names are being considered for future
    versions of this specification.
    
    </div>

label: 'Name'

payload: https://gedcom.io/terms/v7/type-Name

substructures:
  "https://gedcom.io/terms/v7/GIVN": "{0:M}"
  "https://gedcom.io/terms/v7/NAME-TRAN": "{0:M}"
  "https://gedcom.io/terms/v7/NAME-TYPE": "{0:1}"
  "https://gedcom.io/terms/v7/NICK": "{0:M}"
  "https://gedcom.io/terms/v7/NOTE": "{0:M}"
  "https://gedcom.io/terms/v7/NPFX": "{0:M}"
  "https://gedcom.io/terms/v7/NSFX": "{0:M}"
  "https://gedcom.io/terms/v7/SNOTE": "{0:M}"
  "https://gedcom.io/terms/v7/SOUR": "{0:M}"
  "https://gedcom.io/terms/v7/SPFX": "{0:M}"
  "https://gedcom.io/terms/v7/SURN": "{0:M}"

superstructures:
  "https://gedcom.io/terms/v7/record-INDI": "{0:M}"

contact: "https://gedcom.io/community/"
...

```
