# Faceted Search

Redis has no native support for Compound or Secondary Indexes.

## UseCase: Attribute Search

*   Object Inspection
    *   findall matching domain objects using scan
    *   Limitation: All keys need to be matched and inspected
*   Faceted Search aka. the Inverted Index
    *   Using Set Intersection
    *   Data Distribution of the attribute values being matched
    *   Number of attributes need to be matched
*   Hashed Index
    *   Hashed keys
        *   Create a consistent Hash
        *   Search Hash
        *   Limitation: Data distribution of the attribute values being matched



