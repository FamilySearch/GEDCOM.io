---
title: RECORD.SNOTE
permalink: /terms/v7/RECORD.SNOTE.html
layout: none
redirect-from:
  - /terms/v7/RECORD.SNOTE
...

```

%YAML 1.2
---
type: structure

tag: SNOTE

superstructures: [RECORD]

substructures:
  CHAN: "{0:1}"
  CREA: "{0:1}"
  EXID: "{0:M}"
  LANG: "{0:1}"
  MIME: "{0:1}"
  REFN: "{0:M}"
  SOUR: "{0:M}"
  UID: "{0:M}"

payload: Text

descriptions:
  - also called SHARED_NOTE_RECORD
  - |
    A catch-all location for information that does not fully fit within
    other structures. It may include research notes, additional context,
    alternative interpretations, reasoning, and so forth.
    
    A shared note record may be pointed to by multiple other structures, and
    should only be used when the intended semantics is that editing the note
    in one place edits it in all places. If each instance of the note may be
    edited separately, a NOTE should be used instead.
    
    The origin of a name might be a reasonable shared note, while the reason
    a particular person was given that name may make more sense as a
    non-shared note.
    
        0 @GORDON@ SNOTE "Gordon" is a traditional Scottish surname.
        1 CONT It became a given name in honor of Charles George Gordon.
        1 SOUR @VOID@
        2 COMM https://en.wikipedia.org/wiki/Gordon_(given_name)
        0 @I1@ INDI
        1 NAME Gordon /Jones/
        2 NOTE Named after the astronaut Gordon Cooper
        2 SNOTE @GORDON@
    
    Although sharable notes have been part of GEDCOM since version 5.0 was
    released in 1991, as of 2021 relatively few applications have a user
    interface that presents shared notes as such to users. It is recommended
    that SNOTE be avoided when NOTE will suffice.
    
    A SHARED_NOTE_RECORD may contain a pointer to a SOURCE_RECORD and vice
    versa. Applications must not create GEDCOM document where these mutual
    pointers form a cycle. Applications should also ensure they can handle
    invalid files with such cycles in a safe manner.
...

```