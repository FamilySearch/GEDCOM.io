---
title: YAML description format
permalink: /terms/format
sidebar:
  nav: "tools"
...


# YAML descriptions

This page documents the organization of YAML documents delivered at the URIs of the standard tags in the FamilySearch GEDCOM 7 specification and the gedcom.io extension tag registry. The YAML documents are not part of the standard itself, and while the intent is that they remain stable and usable in the long term, if a valid reason arises they may be changed independently of the versioning process.

YAML documents in this form are used to define

- Structure types
- Enumeration values
- Calendars
- Months
- Known payloads for URI-valued structures

For ease of presentation, we call whatever a YAML document is describing a "concept".

## Readable YAML

The files are provided in [YAML 1.2](https://yaml.org).
YAML was chosen because it is readily parseable in many programming languages
and it can be formatted in a human-readable way.
Because YAML provides many formatting options, using a readable style is an option, not a guarantee, and should be considered when preparing the YAML documents.

The YAML should use only [untagged nodes](https://yaml.org/spec/1.2.2/#resolved-tags) with types `seq`, `map`, and `str` from the [fail safe schema](https://yaml.org/spec/1.2.2/#failsafe-schema)
and `null` from the [JSON schema](https://yaml.org/spec/1.2.2/#json-schema).

Long strings should be wrapped on whitespace to keep the YAML under 80 columns if feasible.
Strings containing newlines should be presented using the [literal block style](https://yaml.org/spec/1.2.2/#literal-style).
Strings without newlines may presented in any [flow style](https://yaml.org/spec/1.2.2/#73-flow-scalar-styles)
(though note the restrictions on [plain style strings](https://yaml.org/spec/1.2.2/#plain-style)).

[Sequences](https://yaml.org/spec/1.2.2/#821-block-sequences) and [mappings](https://yaml.org/spec/1.2.2/#822-block-mappings) should be in the block style unless they are empty, in which case a [flow style](https://yaml.org/spec/1.2.2/#74-flow-collection-styles) should be used instead.
The top-level mapping should have a blank line between each mapping entry.

To ease machine identification of YAML blocks, [document markers](https://yaml.org/spec/1.2.2/#912-document-markers) are recommended. In particular, documents should begin with a YAML directive "`%YAML 1.2`" a and directives end marker "`---`" and should end with a document end marker "`...`".

## YAML document schema

Each YAML document is a `map` with `str` keys.

### Required keys

Three keys are always present:

- `lang`<br/>
    A language tag, as specified in BCP 47.
    The entire YAML document is presented in this language.
    
- `type`<br/>
    One of the following string values:

    - `structure`
    - `enumeration`
    - `enumeration set`
    - `calendar`
    - `month`
    - `datatype`
    - `uri`
    
    Which other keys are present depends on the `type`.

    It is anticipated that additional types will be added in the future.
    Types for assisting in knowing which extensions a given application supports
    and for finding a translation of the YAML document into other languages are expected.

- `uri`<br/>
    The URI that identifies the concept documented in this YAML file.

### Other keys

The following keys may appear in a YAML file.
Their names may be changed a YAML file with a `lang` other than `en`.

-   <table><tbody>
    <tr><th>Tag</th><td>`enumeration set`</td></tr>
    <tr><th>Type</th><td>URI</td></tr>
    <tr><th>Required by</th><td>`type: structure` with `payload` either `g7:type-Enum` or `g7:type-List#Enum`</td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>
    
    The URI of the set of enumeration values permitted in the paylaod of this structure.

-   <table><tbody>
    <tr><th>Tag</th><td>`calendars`</td></tr>
    <tr><th>Type</th><td>`seq` of URI</td></tr>
    <tr><th>Required by</th><td>`type: month`</td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>
    
    A list (in no particular order) of the URIs of calendars that use this month.
    
    The list may be incomplete, as a new calendar might be defined that uses an existing month.

-   <table><tbody>
    <tr><th>Tag</th><td>`specification`</td></tr>
    <tr><th>Type</th><td>`seq` of `str`</td></tr>
    <tr><th>Required by</th><td>all except `type: enumeration set`</td></tr>
    <tr><th>Allowed by</th><td>all</td></tr>
    </tbody></table>
    
    A list (in no particular order) of descriptions of the concept the YAML document is defining.
    
    The specification are generally programmer-centric; for user-centric text, see `label` and `help text`

-   <table><tbody>
    <tr><th>Tag</th><td>`documentation`</td></tr>
    <tr><th>Type</th><td>`seq` of URI</td></tr>
    <tr><th>Required by</th><td>—</td></tr>
    <tr><th>Allowed by</th><td>all</td></tr>
    </tbody></table>

    One or more external URLs where additional documentation can be found. If there is no such URL, this entry should be omitted.

-   <table><tbody>
    <tr><th>Tag</th><td>`enumeration values`</td></tr>
    <tr><th>Type</th><td>`seq` of URI</td></tr>
    <tr><th>Required by</th><td>`type: enumeration set`</td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    A list (in no particular order) of URIs of enumeration values supported by the structure.

    The listed URIs needn't identify only enumeration values:
    some structures explicitly enumerate other concepts,
    such as <https://gedcom.io/terms/v7/SOUR-EVEN> enumerating even types.

    The list may be incomplete, as a new enumeration values might be defined that may be included in existing structures.
    
-   <table><tbody>
    <tr><th>Tag</th><td>`extension tags`</td></tr>
    <tr><th>Type</th><td>`seq` of `extTag`</td></tr>
    <tr><th>Required by</th><td>—</td></tr>
    <tr><th>Allowed by</th><td>`type`s `calendar`, `enumeration`, `month`, `structure`, and `uri`</td></tr>
    </tbody></table>

    A list, with the most-preferred tag first, of extension tags known to be used by applications for this concept.

    Standard structures may have an `extension tags` entry to list *fully compatible* extensions that predated the standard and can be converted to the `standard tag` without any other modification.
    For example, 7.0's `UID` structure is fully compatible with the common 5.5.1 extension identified by tag `_UID`.

-   <table><tbody>
    <tr><th>Tag</th><td>`help text`</td></tr>
    <tr><th>Type</th><td>`str`</td></tr>
    <tr><th>Required by</th><td>—</td></tr>
    <tr><th>Allowed by</th><td>all</td></tr>
    </tbody></table>

    A recommended detailed description to show to users. For programmer-centric explanations of the concept, see `specification`.
    
    Help text may be lengthy; for brief text to use in UI elements, see `label`.

-   <table><tbody>
    <tr><th>Tag</th><td>`label`</td></tr>
    <tr><th>Type</th><td>`str`</td></tr>
    <tr><th>Required by</th><td>—</td></tr>
    <tr><th>Allowed by</th><td>all</td></tr>
    </tbody></table>

    A recommended brief name or label to show to users.
    Labels are user-centric; for programmer-centric explanations of the concept, see `specification`.
    
    Labels are short to fit in forms and other constrained-space UI elements; for more detailed text see `help text`.

-   <table><tbody>
    <tr><th>Tag</th><td>`months`</td></tr>
    <tr><th>Type</th><td>`str`</td></tr>
    <tr><th>Required by</th><td>`type: calendar`</td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    A list of all of the months used in the given calendar. Months are listed in the order they appear in a year to facilitate chronological sorting.
    Some calendars include leap months, so it may be that not all months appear every year in the given calendar.
    
    The list should be taken as exhaustive. Extensions may not add new months to existing calendars.

-   <table><tbody>
    <tr><th>Tag</th><td>`payload`</td></tr>
    <tr><th>Type</th><td>a payload type</td></tr>
    <tr><th>Required by</th><td>`type: structure`</td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    Indicates the payload type of the given structure.
    This will be one of
    
    - `null`, meaning no payload is permitted
    - The special string "`Y|<NULL>`", meaning the payload is either "`Y`" or omitted
    - The URI of a datatype, meaning a payload of this type is required
    - A string of the form `@<`URI`>@`, meaning the payload is a pointer to a structure whose type is given by the URI.
    
-   <table><tbody>
    <tr><th>Tag</th><td>`standard tag`</td></tr>
    <tr><th>Type</th><td>`stdTag`</td></tr>
    <tr><th>Required by</th><td>—</td></tr>
    <tr><th>Allowed by</th><td>`type`s `calendar`, `enumeration`, `month`, `structure`, and `uri`</td></tr>
    </tbody></table>

    The standard tag of this concept, as given in an official GEDCOM standard document.

-   <table><tbody>
    <tr><th>Tag</th><td>`substructure` and `superstucture`</td></tr>
    <tr><th>Type</th><td>`map` with URI keys and cardinality marker values</td></tr>
    <tr><th>Required by</th><td>`type: structure`</td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    These express how structures may be nested, and with what cardinality.
    Structure types are given by URI; cardinalities are expressed using the same strings as the standard (i.e. "`{0:1}`", "`{1:1}`", "`{0:M}`", and "`{1:M}`")
    
    Because new structures may be added over time in any order,
    *x* may be a substructure of *y* if
    either *x*'s `superstructures` includes *y* 
    or *y*'s `substructures` includes *x*.
    
    If the relationship is listed in both a `substructures` entry and a `superstructures` entry, the two must have the same cardinality.
    
    If `superstructures` is an empty `map`, then the structure is a record and must not appear in any other structure's `substructures`.

-   <table><tbody>
    <tr><th>Tag</th><td>`value of`</td></tr>
    <tr><th>Type</th><td>`seq` of URI</td></tr>
    <tr><th>Required by</th><td>`type: enumeration`</td></tr>
    <tr><th>Allowed by</th><td>all</td></tr>
    </tbody></table>

    A list (in no particular order) of enumeration sets that are known to contain this concepts as an enumeration value.
    
    The list may be incomplete, as a new enumeration set might be defined that re-uses an existing enumeration value.
