---
title: GEDCOM Specifications
permalink: /specs/
sidebar:
  nav: "specs"
---
***Access to recent specifications and current repository***

*The section provides access to past and present specifications, and a public repository for future versions of FamilySearch GEDCOM. Specifications for versions 5.5 and 5.5.1 are provided since they are both currently in use in the marketplace.  The released version 7.0 is available in both PDF and HTML. Contributors are invited to work on future versions of FamilySearch GEDCOM through the public GitHub repository. A link to GEDCOM X, the backend data structure behind FamilySearch Family Tree, is available for learning and joining that repository.*

## Version 5

- [Version 5.5](/specifications/ged55.pdf)

- [Version 5.5.1](/specifications/ged551.pdf)

## Version 7

- [FamilySearch GEDCOM Version 7.0 PDF](/specifications/FamilySearchGEDCOMv7.pdf) 
- [FamilySearch GEDCOM Version 7.0 HTML](/specifications/FamilySearchGEDCOMv7.html)
- [FamilySearch GEDCOM Changelog](/changelog/)


## GEDCOM X

- [GEDCOM X](http://gedcomx.org)

<script> 
let url = '//assets.adobedtm.com/05064fe6cab0/c247cd0acad1/launch-7e623b6eec86.min.js'

// import _satellite library
const script = document.createElement('script')
script.src = url
script.async = true
script.onload = sendPageView// you won't be able to use `window._satellite` until this has loaded
const child = document.querySelector('script')
const parentNode = child.parentNode
parentNode.insertBefore(script, child)

// Now that the library is loaded, call a page view event
function sendPageView() {
  // build the payload with any data you need
  const payload = {
    // example; consult Kurt for what you should be sending
    site_id: 'FamilySearch',
    site_language: 'en',
    page_channel: 'GEDCOM.io',
    page_detail: 'specs',
  }
  window._satellite.track('page_view', payload)
}
</script>
