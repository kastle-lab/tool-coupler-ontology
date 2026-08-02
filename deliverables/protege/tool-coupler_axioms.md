# Server hasMetadata Metadata
disjoint: `Server DisjointWith Metadata`

existential: `Server SubClassOf hasMetadata some Metadata`

global range: `owl:Thing SubClassOf hasMetadata only Metadata`

inverse scoped functionality: `Metadata SubClassOf inverse hasMetadata max 1 owl:Thing`

qualified scoped functionality: `Server SubClassOf hasMetadata max 1 Metadata`

# Metadata hasFormat Format
disjoint: `Metadata DisjointWith Format`

existential: `Metadata SubClassOf hasFormat some Format`

global domain: `hasFormat some owl:Thing SubClassOf Metadata`

global range: `owl:Thing SubClassOf hasFormat only Format`

qualified scoped functionality: `Metadata SubClassOf hasFormat max 1 Format`

# Metadata hasLocation Location
disjoint: `Metadata DisjointWith Location`

global domain: `hasLocation some owl:Thing SubClassOf Metadata`

global range: `owl:Thing SubClassOf hasLocation only Location`

inverse existential: `Location SubClassOf inverse hasLocation some Metadata`

qualified scoped functionality: `Metadata SubClassOf hasLocation max 1 Location`

# Server hasTool Tool
disjoint: `Server DisjointWith Tool`

existential: `Server SubClassOf hasTool some Tool`

global domain: `hasTool some owl:Thing SubClassOf Server`

global range: `owl:Thing SubClassOf hasTool only Tool`

inverse existential: `Tool SubClassOf inverse hasTool some Server`

inverse qualified scoped functionality: `Tool SubClassOf inverse hasTool max 1 Server`

# Tool hasParameter Parameter
disjoint: `Tool DisjointWith Parameter`

global domain: `hasParameter some owl:Thing SubClassOf Tool`

global range: `owl:Thing SubClassOf hasParameter only Parameter`

inverse existential: `Parameter SubClassOf inverse hasParameter some Tool`

inverse qualified scoped functionality: `Parameter SubClassOf inverse hasParameter max 1 Tool`

# Parameter isOfDataType DataType
disjoint: `Parameter DisjointWith DataType`

existential: `Parameter SubClassOf isOfDataType some DataType`

global range: `owl:Thing SubClassOf isOfDataType only DataType`

qualified scoped functionality: `Parameter SubClassOf isOfDataType max 1 DataType`

# Parameter containsElement Element
disjoint: `Parameter DisjointWith Element`

global range: `owl:Thing SubClassOf containsElement only Element`

# Element isOfDataType DataType
disjoint: `Element DisjointWith DataType`

existential: `Element SubClassOf isOfDataType some DataType`

global range: `owl:Thing SubClassOf isOfDataType only DataType`

qualified scoped functionality: `Element SubClassOf isOfDataType max 1 DataType`

# Parameter hasMetadata Metadata
disjoint: `Parameter DisjointWith Metadata`

existential: `Parameter SubClassOf hasMetadata some Metadata`

global range: `owl:Thing SubClassOf hasMetadata only Metadata`

inverse scoped functionality: `Metadata SubClassOf inverse hasMetadata max 1 owl:Thing`

qualified scoped functionality: `Parameter SubClassOf hasMetadata max 1 Metadata`

# Tool hasMetadata Metadata
disjoint: `Tool DisjointWith Metadata`

existential: `Tool SubClassOf hasMetadata some Metadata`

global range: `owl:Thing SubClassOf hasMetadata only Metadata`

inverse scoped functionality: `Metadata SubClassOf inverse hasMetadata max 1 owl:Thing`

qualified scoped functionality: `Tool SubClassOf hasMetadata max 1 Metadata`

# Metadata hasName xsd:string
existential: `Metadata SubClassOf hasName some xsd:string`

global domain: `hasName some owl:Thing SubClassOf Metadata`

global range: `owl:Thing SubClassOf hasName only xsd:string`

qualified scoped functionality: `Metadata SubClassOf hasName max 1 xsd:string`

# Metadata hasDescription xsd:string
global domain: `hasDescription some owl:Thing SubClassOf Metadata`

global range: `owl:Thing SubClassOf hasDescription only xsd:string`

qualified scoped functionality: `Metadata SubClassOf hasDescription max 1 xsd:string`

# Metadata hasTag xsd:string
global domain: `hasTag some owl:Thing SubClassOf Metadata`

global range: `owl:Thing SubClassOf hasTag only xsd:string`

# Location asString xsd:string
global range: `owl:Thing SubClassOf asString only xsd:string`

qualified scoped functionality: `Location SubClassOf asString max 1 xsd:string`

# Location hasURI xsd:anyURI
global range: `owl:Thing SubClassOf hasURI only xsd:anyURI`

qualified scoped functionality: `Location SubClassOf hasURI max 1 xsd:anyURI`

# Location hasIP xsd:anyURI
global range: `owl:Thing SubClassOf hasIP only xsd:anyURI`

qualified scoped functionality: `Location SubClassOf hasIP max 1 xsd:anyURI`

# Location hasFilePath xsd:string
global range: `owl:Thing SubClassOf hasFilePath only xsd:string`

qualified scoped functionality: `Location SubClassOf hasFilePath max 1 xsd:string`

# Element containsElement Element
global range: `owl:Thing SubClassOf containsElement only Element`

# Input SubClassOf Parameter
subclass: `Input SubClassOf Parameter`

# Output SubClassOf Parameter
subclass: `Output SubClassOf Parameter`

# Inout SubClassOf Parameter
subclass: `Inout SubClassOf Parameter`

# Required SubClassOf Parameter
subclass: `Required SubClassOf Parameter`

