---
title: PLAC-TRAN
permalink: /terms/v7/PLAC-TRAN.html
layout: none
redirect-from:
  - /terms/v7/PLAC-TRAN
...

```

%YAML 1.2
---
lang: en-US

type: structure

uri: https://gedcom.io/terms/v7/PLAC-TRAN

standard tag: 'TRAN'

specification:
  - Translation
  - |
    A type of `TRAN` substructure specific to places. Each `PLAC`.`TRAN` must have
    a `LANG` substructure. See also `PLAC`.
    
    <div class="example">
    
    The following presents a place in Japanese with a romaji transliteration and
    English translation
    
    ```gedcom
    2 PLAC 千代田, 東京, 日本
    3 FORM 区, 都, 国
    3 LANG ja
    3 TRAN Chiyoda, Tokyo, Nihon
    4 LANG ja-Latn
    3 TRAN Chiyoda, Tokyo, Japan
    4 LANG en
    ```
    
    </div>
  - |
    A representation of the superstructure's data in a different format.
    
    In some situations it is desirable to provide the same semantic content in
    multiple formats. Where this is desirable, a `TRAN` substructure is used, where
    the specific format is given in its language tag substructure, media type
    substructure, or both.
    
    Different `TRAN` structures are used in different contexts to fully capture the
    structure of the information being presented in multiple formats. In all cases,
    a `TRAN` structure's payload and substructures should provide only information
    also contained in the `TRAN` structures' superstructure, but provide it in a
    new language, script, or media type.
    
    Each `TRAN` substructure must have either a language tag or a media type or
    both. Each `TRAN` structure must differ from its superstructure and from every
    other `TRAN` substructure of its superstructure in either its language tag or
    its media type or both.

label: 'Translation'

payload: https://gedcom.io/terms/v7/type-List#Text

substructures:
  "https://gedcom.io/terms/v7/LANG": "{1:1}"

superstructures:
  "https://gedcom.io/terms/v7/PLAC": "{0:M}"

contact: "https://gedcom.io/community/"
...

```
