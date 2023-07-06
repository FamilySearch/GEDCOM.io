---
title: YAML description format
permalink: /terms/format
sidebar:
  nav: "tools"
...


This page documents the organization of YAML documents delivered at the URIs of the standard tags in the FamilySearch GEDCOM 7 specification and the extension tag registry. The YAML documents are not part of the standard itself, and while the intent is that they remain stable and usable in the long term, if a valid reason arises they may be changed independently of the versioning process.

YAML documents in this form are used to define

- Structure types
- Enumeration values and sets
- Calendars and months
- Payload datatypes
- Known payloads for URI-valued structures

For ease of presentation, we call whatever a YAML document is describing a "concept".

# Readable YAML

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

To ease machine identification of YAML blocks, [document markers](https://yaml.org/spec/1.2.2/#912-document-markers) are recommended. In particular, documents should begin with both the YAML directive "`%YAML 1.2`" and the directives end marker "`---`", and should end with the document end marker "`...`".

# YAML document schema

Each YAML document is a `map` with `str` keys.

The following shorthand types are used in this document:

| Name | YAML type | Other constraints |
|------|-----------|-------------------|
| Cardinality Marker | `str` | A cardinality marker as defined in the FamilySearch GEDCOM 7 specification |
| `extTag` | `str`| Matching `extTag` from the FamilySearch GEDCOM 7 specification |
| Language Tag | `str` | A valid language tag, as defined in BCP 47 |
| `stdTag` | `str`| Matching `stdTag` from the FamilySearch GEDCOM 7 specification |
| `Tag` | `str`| Matching `Tag` from the FamilySearch GEDCOM 7 specification |
| URI | `str` | A valid URI, as defined by RFC 3986 |


## Required keys

Three keys are always present:

-   <table><tbody>
    <tr><th>Key</th><td><code>lang</code></td></tr>
    <tr><th>Type</th><td>Language Tag</td></tr>
    <tr><th>Required by</th><td>all</td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    A language tag, as specified in BCP 47.
    The entire YAML document is presented in this language.
    
-   <table><tbody>
    <tr><th>Key</th><td><code>type</code></td></tr>
    <tr><th>Type</th><td><code>str</code> from a limited set (see below)</td></tr>
    <tr><th>Required by</th><td>all</td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    One of the following string values:

    - `structure`
    - `enumeration`
    - `enumeration set`
    - `calendar`
    - `month`
    - `data type`
    - `uri`
    
    Which other keys are present depends on the `type`.

    It is anticipated that additional types will be added in the future.
    Types for assisting in knowing which extensions a given application supports
    and for finding a translation of the YAML document into other languages are expected.

-   <table><tbody>
    <tr><th>Key</th><td><code>uri</code></td></tr>
    <tr><th>Type</th><td>URI</td></tr>
    <tr><th>Required by</th><td>all</td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    The URI that identifies the concept documented in this YAML file.

## Other keys

The following keys may appear in a YAML file.
Their names may be changed a YAML file with a `lang` other than `en`.

-   <table><tbody>
    <tr><th>Key</th><td><code>enumeration set</code></td></tr>
    <tr><th>Type</th><td>URI</td></tr>
    <tr><th>Required by</th><td><code>type: structure</code> with <code>payload</code> either <code>g7:type-Enum</code> or <code>g7:type-List#Enum</code></td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>
    
    The URI of the set of enumeration values permitted in the payload of this structure.

-   <table><tbody>
    <tr><th>Key</th><td><code>calendars</code></td></tr>
    <tr><th>Type</th><td><code>seq</code> of URI</td></tr>
    <tr><th>Required by</th><td><code>type: month</code></td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>
    
    A list (in no particular order) of the URIs of calendars that use this month.
    
    The list may be incomplete, as a new calendar might be defined that uses an existing month.

-   <table><tbody>
    <tr><th>Key</th><td><code>specification</code></td></tr>
    <tr><th>Type</th><td><code>seq</code> of <code>str</code></td></tr>
    <tr><th>Required by</th><td>all except <code>type: enumeration set</code></td></tr>
    <tr><th>Allowed by</th><td>all</td></tr>
    </tbody></table>
    
    A list (in no particular order) of descriptions of the concept the YAML document is defining.
    
    The specification are generally programmer-centric; for user-centric text, see `label` and `help text`

-   <table><tbody>
    <tr><th>Key</th><td><code>documentation</code></td></tr>
    <tr><th>Type</th><td><code>seq</code> of URI</td></tr>
    <tr><th>Required by</th><td>—</td></tr>
    <tr><th>Allowed by</th><td>all</td></tr>
    </tbody></table>

    One or more external URLs where additional documentation can be found. If there is no such URL, this entry should be omitted.

-   <table><tbody>
    <tr><th>Key</th><td><code>enumeration values</code></td></tr>
    <tr><th>Type</th><td><code>seq</code> of URI</td></tr>
    <tr><th>Required by</th><td><code>type: enumeration set</code></td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    A list (in no particular order) of URIs of enumeration values supported by the structure.

    The listed URIs needn't identify only enumeration values:
    some structures explicitly enumerate other concepts,
    such as <https://gedcom.io/terms/v7/SOUR-EVEN> enumerating even types.

    The list may be incomplete, as a new enumeration values might be defined that may be included in existing structures.
    
-   <table><tbody>
    <tr><th>Key</th><td><code>extension tags</code></td></tr>
    <tr><th>Type</th><td><code>seq</code> of <code>extTag</code></td></tr>
    <tr><th>Required by</th><td>*</td></tr>
    <tr><th>Allowed by</th><td><code>type</code>s <code>calendar</code>, <code>enumeration</code>, <code>month</code>, <code>structure</code></td></tr>
    </tbody></table>
    
    \* Required instead of allowed if no `standard tag` is provided

    A list, with the most-preferred tag first, of extension tags known to be used by applications for this concept.

    Standard structures may have an `extension tags` entry to list *fully compatible* extensions that predated the standard and can be converted to the `standard tag` without any other modification.
    For example, 7.0's `UID` structure is fully compatible with the common 5.5.1 extension identified by tag `_UID`.

-   <table><tbody>
    <tr><th>Key</th><td><code>help text</code></td></tr>
    <tr><th>Type</th><td><code>str</code></td></tr>
    <tr><th>Required by</th><td>—</td></tr>
    <tr><th>Allowed by</th><td>all</td></tr>
    </tbody></table>

    A recommended detailed description to show to users. For programmer-centric explanations of the concept, see `specification`.
    
    Help text may be lengthy; for brief text to use in UI elements, see `label`.

-   <table><tbody>
    <tr><th>Key</th><td><code>label</code></td></tr>
    <tr><th>Type</th><td><code>str</code></td></tr>
    <tr><th>Required by</th><td>—</td></tr>
    <tr><th>Allowed by</th><td>all</td></tr>
    </tbody></table>

    A recommended brief name or label to show to users.
    Labels are user-centric; for programmer-centric explanations of the concept, see `specification`.
    
    Labels are short to fit in forms and other constrained-space UI elements; for more detailed text see `help text`.

-   <table><tbody>
    <tr><th>Key</th><td><code>months</code></td></tr>
    <tr><th>Type</th><td><code>seq</code> of URI</td></tr>
    <tr><th>Required by</th><td><code>type: calendar</code></td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    A list of all of the months used in the given calendar. Months are listed in the order they appear in a year to facilitate chronological sorting.
    Some calendars include leap months, so it may be that not all months appear every year in the given calendar.
    
    The list should be taken as exhaustive. Extensions may not add new months to existing calendars.

-   <table><tbody>
    <tr><th>Key</th><td><code>payload</code></td></tr>
    <tr><th>Type</th><td><code>null</code> or <code>str</code>; see below fore more</td></tr>
    <tr><th>Required by</th><td><code>type: structure</code></td></tr>
    <tr><th>Allowed by</th><td>—</td></tr>
    </tbody></table>

    Indicates the payload type of the given structure.
    This will be one of
    
    - `null`, meaning no payload is permitted
    - The special string "`Y|<NULL>`", meaning the payload is either "`Y`" or omitted
    - The URI of a datatype, meaning a payload of this type is required
    - A string of the form `@<`URI`>@`, meaning the payload is a pointer to a structure whose type is given by the URI.
    
-   <table><tbody>
    <tr><th>Key</th><td><code>standard tag</code></td></tr>
    <tr><th>Type</th><td><code>stdTag</code></td></tr>
    <tr><th>Required by</th><td>*</td></tr>
    <tr><th>Allowed by</th><td><code>type</code>s <code>calendar</code>, <code>enumeration</code>, <code>month</code>, <code>structure</code></td></tr>
    </tbody></table>
    
    \* Required instead of allowed if no `extension tag` is provided


    The standard tag of this concept, as given in an official GEDCOM standard document.

-   <table><tbody>
    <tr><th>Key</th><td><code>substructure</code> and <code>superstucture</code></td></tr>
    <tr><th>Type</th><td><code>map</code> with URI keys and Cardinality Marker values</td></tr>
    <tr><th>Required by</th><td><code>type: structure</code></td></tr>
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
    <tr><th>Key</th><td><code>value of</code></td></tr>
    <tr><th>Type</th><td><code>seq</code> of URI</td></tr>
    <tr><th>Required by</th><td><code>type: enumeration</code></td></tr>
    <tr><th>Allowed by</th><td><code>type: structure</code>*</td></tr>
    </tbody></table>
    
    \* Note that potentially any concept could be referred to in an enumeration set, and hence any YAML file could include the `value of` key. So far, all known examples are either `type: enumeration` or `type: structure`.

    A list (in no particular order) of enumeration sets that are known to contain this concepts as an enumeration value.
    
    The list may be incomplete, as a new enumeration set might be defined that re-uses an existing enumeration value.
    
