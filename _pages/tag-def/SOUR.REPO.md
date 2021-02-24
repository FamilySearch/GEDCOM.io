---
title: SOUR.REPO
permalink: /terms/v7/SOUR.REPO.html
layout: none
redirect-from:
  - /terms/v7/SOUR.REPO
...

```

%YAML 1.2
---
type: structure

tag: REPO

superstructures: [SOUR]

substructures:
  CALN: "{0:M}"
  NOTE: "{0:M}"
  SNOTE: "{0:M}"

payload: xref:REPO

descriptions:
  - Tag abbreviated from "Repository"
  - also called SOURCE_REPOSITORY_CITATION
  - For a record, see REPOSITORY_RECORD. For a substructure, see
    SOURCE_REPOSITORY_CITATION.
  - This structure is used within a source record to point to a name and
    address record of the holder of the source document. Formal and informal
    repository name and addresses are stored in the REPOSITORY_RECORD. More
    formal repositories, such as the Family History Library, should show a
    call number of the source at that repository. The call number of that
    source should be recorded using a CALN substructure.
...

```