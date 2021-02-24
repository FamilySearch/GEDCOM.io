---
title: CROP
permalink: /terms/v7/CROP.html
layout: none
redirect-from:
  - /terms/v7/CROP
...

```

%YAML 1.2
---
type: structure

tag: CROP

superstructures: [OBJE]

substructures:
  HEIGHT: "{0:1}"
  LEFT: "{0:1}"
  TOP: "{0:1}"
  WIDTH: "{0:1}"

payload: None

descriptions:
  - |
    A subregion of an image to display. It is only valid when the
    superstructure links to an image with a defined pixel unit.
    
    LEFT and TOP indicate the top-left corner of the region to display.
    WIDTH and HEIGHT indicate how many pixels wide and tall the region to
    display is. If omitted, LEFT and TOP each default to 0; WIDTH defaults
    to the image width minus LEFT; and HEIGHT defaults to the image height
    minus TOP.
    
    The following are errors:
    
    -   LEFT or LEFT + WIDTH exceed the image width.
    -   TOP or TOP + HEIGHT exceed the image height.
    -   CROP applied to a non-image or image without a defined pixel unit.
...

```