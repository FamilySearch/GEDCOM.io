---
title: MIME
permalink: /terms/v7/MIME.html
layout: none
redirect-from:
  - /terms/v7/MIME
...

```

%YAML 1.2
---
type: structure

tag: MIME

superstructures: [COMM, NOTE, SNOTE, TEXT]

substructures:

payload: Special

descriptions:
  - Tag abbreviated from "Media type"
  - |
    Indicates the media type of the payload of the superstructure, as
    defined by IETC BCP 13.
    
    Only 2 media types are supported by this structure in this version of
    GEDCOM:
    
    -   text/plain shall be presented to the user as-is, preserving all
        spacing, line breaks, and so forth.
    
    -   text/html uses HTML tags to provide presentation information.
        Applications should support at least the following:
    
        -   p and br elements for paragraphing and line breaks.
        -   b, i, and u elements for bold, italic, and underlined text (or
            corresponding display in other locales; see HTML §4.5 for more).
        -   sup and sub elements for super- and sub-script.
        -   The 3 XML entities that appear in text: &amp;, &lt; &gt;. Note
            that &quote; and &apos; are only needed in attributes. Other
            entities should be represented as their respective Unicode
            characters instead.
    
        Supporting more of HTML is encouraged. Unsupported elements should
        be ignored during display.
    
    Media types are also used by external files, as described under FORM.
    External file media types are not limited to text/plain and text/html.
...

```