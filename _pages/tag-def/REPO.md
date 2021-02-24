---
title: REPO
permalink: /terms/v7/REPO.html
layout: none
redirect-from:
  - /terms/v7/REPO
...

```

%YAML 1.2
---
type: structure

tag: REPO

superstructures: [RECORD]

substructures:
  ADDR: "{0:1}"
  CHAN: "{0:1}"
  CREA: "{0:1}"
  EMAIL: "{0:M}"
  EXID: "{0:M}"
  FAX: "{0:M}"
  NAME: "{1:1}"
  NOTE: "{0:M}"
  PHON: "{0:M}"
  REFN: "{0:M}"
  SNOTE: "{0:M}"
  UID: "{0:M}"
  WWW: "{0:M}"

payload: None

descriptions:
  - also called REPOSITORY_RECORD
  - |
    The repository record provides information about an institution or
    person that has a collection of sources. Informal repositories include
    the owner of an unpublished work or of a rare published source, or a
    keeper of personal collections. An example would be the owner of a
    family Bible containing unpublished family genealogical entries.
    
    Layered repositories, such as an archive containing copies of a subset
    of records from another archive or archives that have moved or been
    bought by other archives, are not modeled in this version of GEDCOM. It
    is expected they will be added in a later version. Until such time, it
    is recommended that the repository record store current contact
    information, if known.
...

```