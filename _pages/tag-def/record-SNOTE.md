---
title: record-SNOTE
permalink: /terms/v7/record-SNOTE.html
layout: none
redirect-from:
  - /terms/v7/record-SNOTE
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/record-SNOTE

standard tag: 'SNOTE'

specification:
  - Shared note
  - A note that is shared by multiple structures. See `SHARED_NOTE_RECORD` for more
    details.
  - |
    A catch-all location for information that does not fully fit within other
    structures. It may include research notes, additional context, alternative
    interpretations, reasoning, and so forth.
    
    A shared note record may be pointed to by multiple other structures. Shared
    notes should only be used if editing the note in one place should edit it in
    all other places or if the note itself requires an `IDENTIFIER_STRUCTURE`. If
    each instance of the note may be edited separately and no identifier is needed,
    a `NOTE` should be used instead.
    
    Each [`SNOTE`.`TRAN`] must have either a `MIME` or `LANG` substructure or
    both.
    
    <div class="example">
    
    The origin of a name might be a reasonable shared note, while the reason a
    particular person was given that name may make more sense as a non-shared note.
    
    ```gedcom
    0 @GORDON@ SNOTE "Gordon" is a traditional Scottish surname.
    1 CONT It became a given name in honor of Charles George Gordon.
    0 @I1@ INDI
    1 NAME Gordon /Jones/
    2 NOTE Named after the astronaut Gordon Cooper
    2 SNOTE @GORDON@
    ```
    
    </div>
    
    <div class="note">
    
    The ability to have multiple structures share a single note using pointers was
    introduced in version 5.0 in 1991. However, as of 2021 relatively few
    applications have a user interface that presents shared notes as such to users.
    It is recommended that `SNOTE` be avoided when `NOTE` will suffice.
    
    </div>
    
    A `SHARED_NOTE_RECORD` may contain a pointer to a `SOURCE_RECORD` and vice
    versa. Applications must not create datasets where these mutual pointers form a
    cycle. Applications should also ensure they can handle invalid files with such
    cycles in a safe manner.

label: 'Shared note'

payload: http://www.w3.org/2001/XMLSchema#string

substructures:
  "https://gedcom.io/terms/v7/CHAN": "{0:1}"
  "https://gedcom.io/terms/v7/CREA": "{0:1}"
  "https://gedcom.io/terms/v7/EXID": "{0:M}"
  "https://gedcom.io/terms/v7/LANG": "{0:1}"
  "https://gedcom.io/terms/v7/MIME": "{0:1}"
  "https://gedcom.io/terms/v7/NOTE-TRAN": "{0:M}"
  "https://gedcom.io/terms/v7/REFN": "{0:M}"
  "https://gedcom.io/terms/v7/SOUR": "{0:M}"
  "https://gedcom.io/terms/v7/UID": "{0:M}"

superstructures: {}

contact: "https://gedcom.io/community/"
...

```
