# EXID TYPE Base URIs

The FamilySearch GEDCOM 7 specification defines `EXID`.`TYPE` as holding
the URI of the authority for the identifier in the `EXID` payload.
The following table lists a number of well-known base URIs defined for this
purpose. These base URIs can be used together with the `EXID` value to form
the full URI. For a few examples, see [Migrating v5.5.1 to v7.0](../migrate/#afn-rfn-rin).

Applications can use base URIs beyond those listed in this table,
but additional URIs may not be recognized by other applications.

Type of Identifier                 | Base URI
---------------------------------- | ------------
Ancestral File Number              | <https://gedcom.io/terms/v7/AFN>
FamilySearch Memory ID             | <https://gedcom.io/exid-type/FamilySearch-MemoryId>
FamilySearch Person ID             | <https://gedcom.io/exid-type/FamilySearch-PersonId>
FamilySearch Place ID              | <https://gedcom.io/exid-type/FamilySearch-PlaceId>
FamilySearch Source Description ID | <https://gedcom.io/exid-type/FamilySearch-SourceDescriptionId>
FamilySearch User ID               | <https://gedcom.io/exid-type/FamilySearch-UserId>
Record ID Number                   | <https://gedcom.io/terms/v7/RIN>
Record File Number                 | <https://gedcom.io/terms/v7/RFN>
