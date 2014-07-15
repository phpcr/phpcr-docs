===================================================================================
JCR 2.0: 24 Repository Compliance (Content Repository for Java Technology API v2.0)
===================================================================================

24 Repository Compliance
========================

A JCR implementation must support the *basic repository features*:

-  Repository acquisition and user authentication and authorization (see
   §4 *Connecting*)

-  Reading through path, identifier and browse access (see §5 *Reading*)

-  Query (see §6 *Query*)

-  Export (see §7 *Export*)

-  Node Type Discovery (see §8 *Node Type Discovery*)

-  Permission and capability checking (see §9 *Permissions and
   Capabilities*)

These features must be supported by all JCR repositories.

In addition, a repository *may* support any subset of the *additional
features* defined in sections §10 to §23.

The presence of each additional feature is individually testable either
through querying the value of a repository descriptor (see §24.2
*Repository Descriptors*) or testing for the availability of a specific
node type (see §24.3 *Node Type-Related Features*), thus allowing an
application to programmatically determine the capabilities of a specific
JCR implementation.

An implementation that supports all the additional features defined in
this specification is a *fully-compliant repository*.

24.1 Definition of Support
--------------------------

By indicating support for testable feature, a repository asserts that it
fully conforms to the semantics of that feature as defined in this
specification, with two possible exceptions:

-  aspects of the feature clearly indicated as being optional (i.e.,
   *should*, *may*, *should not*), and

-  aspects of the feature testable by their own repository descriptors
   (for example, whether a repository supports joins is separately
   testable from whether it supports searches in general).

However, to indicate that it supports a testable feature, a repository
is only required to support that feature in some, not all, contexts. For
example, a repository may restrict its support for a feature based on
access control, path, or other criteria.

24.2 Repository Descriptors
---------------------------

Repository descriptors are used to test support for repository features
that have a behavioral (as opposed to a data-model) aspect.

Each descriptor is identified by a unique *key*, which is a string. An
implementation must recognize all the standard keys defined in this
specification and may recognize additional implementation-specific keys.
The full set of valid keys (both standard and implementation-specific)
for an implementation is returned by

String[] Repository.getDescriptorKeys().

The method

boolean Repository.isStandardDescriptor(String key)

returns true if key is the name of a standard descriptor defined within
this specification and false if it is either a valid
implementation-specific key or not a valid key.

The method

boolean Repository.isSingleValueDescriptor(String key)

returns true if key is the name of a single value descriptor and false
otherwise.

The value of a particular descriptor is found by passing that
descriptor's key to either

Value Repository.getDescriptorValue(String key)

or

Value[] Repository.getDescriptorValues(String key).

depending on whether that key is defined to return a single or a
multiple value.

The JCR 1.0 method

String Repository.getDescriptor()

is still supported as a convenience method. The call

String s = repository.getDescriptor(key);

is equivalent to

| Value v = repository.getDescriptorValue(key);
| String s = (v == null) ? null : v.getString();

24.2.1 Repository Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------+--------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+---------------------------------------------+-------------------------------------------------------+----------------------------------------------------------+
| **Key**          | SPEC\_VERSION\_DESC                                                                                                            | SPEC\_NAME\_DESC                                                                                                                                                   | REP\_VENDOR\_DESC                            | REP\_VENDOR\_URL\_DESC                      | REP\_NAME\_DESC                                       | REP\_VERSION\_DESC                                       |
|                  |                                                                                                                                |                                                                                                                                                                    |                                              |                                             |                                                       |                                                          |
| **Descriptor**   | STRING: The version of the specification that this repository implements. For JCR 2.0 the value of this descriptor is “2.0”.   | STRING: The name of the specification that this repository implements. For JCR 2.0 the value of this descriptor is “Content Repository for Java Technology API”.   | STRING: The name of the repository vendor.   | STRING: The URL of the repository vendor.   | STRING: The name of this repository implementation.   | STRING: The version of this repository implementation.   |
+------------------+--------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+---------------------------------------------+-------------------------------------------------------+----------------------------------------------------------+

24.2.2 General
~~~~~~~~~~~~~~

**Key**

**Descriptor**

WRITE\_SUPPORTED

BOOLEAN: Returns true if and only if repository content can be *updated*
through the JCR API , as opposed to having read-only access (see §10
*Writing*).

IDENTIFIER\_STABILITY

STRING: Returns one of the following javax.jcr.Repository constants
indicating the *stability of non-referenceable identifiers*:

-  IDENTIFIER\_STABILITY\_METHOD\_DURATION: Identifiers may change
   between method calls

-  IDENTIFIER\_STABILITY\_SAVE\_DURATION: Identifiers are guaranteed
   stable within a single save/refresh cycle.

-  IDENTIFIER\_STABILITY\_SESSION\_DURATION: Identifiers are guaranteed
   stable within a single session.

-  IDENTIFIER\_STABILITY\_INDEFINITE\_DURATION: Identifiers are
   guaranteed to be stable forever. Note that *referenceable*
   identifiers always have this level of stability.

See 3.7 *Identifiers* and §3.8 *Referenceable Nodes*.

OPTION\_XML\_IMPORT\_SUPPORTED

BOOLEAN: Returns true if and only if *XML import* is supported (see §11
*Import*).

OPTION\_UNFILED\_CONTENT\_SUPPORTED

BOOLEAN: Returns true if and only if *unfiled content* is supported (see
§3.12 *Unfiled Content*).

| OPTION\_SIMPLE\_VERSIONING\_
| SUPPORTED

BOOLEAN: Returns true if and only if *simple versioning* is supported
(see §3.13 *Versioning Model* and §15 *Versioning*).

OPTION\_ACTIVITIES\_SUPPORTED

BOOLEAN: Returns true if and only if *activities* are supported (see
§15.12 *Activities*).

OPTION\_BASELINES\_SUPPORTED

BOOLEAN: Returns true if and only if *configurations and baselines* are
supported (see §3.13 *Versioning Model* and §15.13 *Configurations and
Baselines*).

OPTION\_ACCESS\_CONTROL\_SUPPORTED

BOOLEAN: Returns true if and only if *access control* is supported (see
§16 *Access Control Management*).

OPTION\_LOCKING\_SUPPORTED

BOOLEAN: Returns true if and only if *locking* is supported (see §17
*Locking*).

OPTION\_OBSERVATION\_SUPPORTED

BOOLEAN: Returns true if and only if *asynchronous observation* is
supported (see §12 *Observation*).

| OPTION\_JOURNALED\_OBSERVATION\_
| SUPPORTED

BOOLEAN: Returns true if and only if *journaled observation* is
supported (see §12 *Observation*).

OPTION\_RETENTION\_SUPPORTED

BOOLEAN: Returns true if and only if *retention and hold* are supported
(see §20 *Retention and Hold*).

OPTION\_LIFECYCLE\_SUPPORTED

BOOLEAN: Returns true if and only if *lifecycle management* is supported
(see §18 *Lifecycle Management*).

OPTION\_TRANSACTIONS\_SUPPORTED

BOOLEAN: Returns true if and only if *transactions* are supported (see
§21 *Transactions*).

| OPTION\_WORKSPACE\_MANAGEMENT\_
| SUPPORTED

BOOLEAN: Returns true if and only if *workspace management* is supported
(see §13 *Workspace Management*).

OPTION\_NODE\_AND\_PROPERTY\_WITH\_SAME\_NAME\_SUPPORTED

BOOLEAN: Returns true if and only if *node and property with same name*
is supported (see §5.1.8 *Node and Property with Same Name*).

24.2.3 Node Operations
~~~~~~~~~~~~~~~~~~~~~~

+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **Key**          | | OPTION\_UPDATE\_PRIMARY\_NODE\_TYPE\_                                                                                                            | | OPTION\_UPDATE\_MIXIN\_NODE\_TYPES\_                                                                                                                  | OPTION\_SHAREABLE\_NODES\_SUPPORTED                                                                                                                 |
|                  | | SUPPORTED                                                                                                                                        | | SUPPORTED                                                                                                                                             |                                                                                                                                                     |
| **Descriptor**   |                                                                                                                                                    |                                                                                                                                                         | BOOLEAN: Returns true if and only if *the creation of shareable nodes* is supported (see §3.9 *Shareable Nodes Model* and §14 *Shareable Nodes*).   |
|                  | BOOLEAN: Returns true if and only if *the primary node type of an existing node can be updated* (see §10.10.2 *Updating a Node's Primary Type*).   | BOOLEAN: Returns true if and only if *the mixin node types of an existing node can be added and removed* (see §10.10.3 *Assigning Mixin Node Types*).   |                                                                                                                                                     |
+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

24.2.4 Node Type Management
~~~~~~~~~~~~~~~~~~~~~~~~~~~

These repository descriptors characterize the types of nodes an API
consumer may register (see §19 *Node Type Management*). They do not
constrain a repository's built-in node types (see §3.7 *Node Types*).

**Key**

**Descriptor**

| OPTION\_NODE\_TYPE\_MANAGEMENT\_
| SUPPORTED

BOOLEAN: Returns true if and only if *node type management* is
supported.

NODE\_TYPE\_MANAGEMENT\_INHERITANCE

STRING: Returns one of the following javax.jcr.Repository constants
indicating *the level of support for node type inheritance*:

-  NODE\_TYPE\_MANAGEMENT\_INHERITANCE\_MINIMAL: Registration of primary
   node types is limited to those which have only nt:base as supertype.
   Registration of mixin node types is limited to those without any
   supertypes.

-  NODE\_TYPE\_MANAGEMENT\_INHERITANCE\_SINGLE: Registration of primary
   node types is limited to those with exactly one supertype.
   Registration of mixin node types is limited to those with at most one
   supertype.

-  NODE\_TYPE\_MANAGEMENT\_INHERITANCE\_MULTIPLE: Primary node types can
   be registered with one or more supertypes. Mixin node types can be
   registered with zero or more supertypes.

| NODE\_TYPE\_MANAGEMENT\_OVERRIDES\_
| SUPPORTED

BOOLEAN: Returns true if and only if *override of inherited property or
child node definitions* is supported (see §3.7.6 *Node Type
Inheritance*).

| NODE\_TYPE\_MANAGEMENT\_PRIMARY\_ITEM\_
| NAME\_SUPPORTED

BOOLEAN: Returns true if and only if *primary items* are supported (see
§3.7.1.7 *Primary Item*).

| NODE\_TYPE\_MANAGEMENT\_ORDERABLE\_
| CHILD\_NODES\_SUPPORTED

BOOLEAN: Returns true if and only if *preservation of child node
ordering* is supported (see §5.2.2.1 *Child Node Order Preservation*).

| NODE\_TYPE\_MANAGEMENT\_RESIDUAL\_
| DEFINITIONS\_SUPPORTED

BOOLEAN: Returns true if and only if *residual property and child node
definitions* are supported (see §3.7.2.1.2 *Item Definition Name and
Residual Definitions*).

| NODE\_TYPE\_MANAGEMENT\_AUTOCREATED\_
| DEFINITIONS\_SUPPORTED

BOOLEAN: Returns true if and only if *autocreated properties and child
nodes* are supported (see §3.7.2.3 *Auto-Created*).

| NODE\_TYPE\_MANAGEMENT\_SAME\_NAME\_
| SIBLINGS\_SUPPORTED

BOOLEAN: Returns true if and only if *same-name sibling child nodes* are
supported (see §3.7.4.3 *Same-Name Siblings*).

NODE\_TYPE\_MANAGEMENT\_PROPERTY\_TYPES

LONG[]: Returns an array holding the javax.jcr.PropertyType constants
for the property types (including UNDEFINED, if supported) that a
registered node type can specify, or a zero-length array if registered
node types cannot specify property definitions (see §3.6.1 *Property
Types*).

| NODE\_TYPE\_MANAGEMENT\_MULTIVALUED\_
| PROPERTIES\_SUPPORTED

boolean: Returns true if and only if *multi-value properties* are
supported (see §3.6.3 *Single and Multi-Value Properties*).

| NODE\_TYPE\_MANAGEMENT\_MULTIPLE\_
| BINARY\_PROPERTIES\_SUPPORTED

BOOLEAN: Returns true if and only if *registration of a node types with
more than one* *BINARY* *property* is permitted (see §3.6.1.7 *BINARY*).

| NODE\_TYPE\_MANAGEMENT\_VALUE\_
| CONSTRAINTS\_SUPPORTED

BOOLEAN: Returns true if and only *value-constraints* are supported (see
§3.7.3.6 *Value Constraints*).

NODE\_TYPE\_MANAGEMENT\_UPDATE\_IN\_USE\_SUPORTED

BOOLEAN: Returns true if and only the update of node types is supported
for node types currently in use as the type of an existing node in the
repository.

24.2.5 Query
~~~~~~~~~~~~

**Key**

**Descriptor**

QUERY\_LANGUAGES

STRING[]: Returns an array holding the constants representing the
supported query languages, or a zero-sized array if query is not
supported (see §6 *Query*).

QUERY\_STORED\_QUERIES\_SUPPORTED

BOOLEAN: Returns true if and only if *stored queries* are supported (see
§6.9.7 *Stored Query*).

QUERY\_FULL\_TEXT\_SEARCH\_SUPPORTED

BOOLEAN: Returns true if and only if *full-text search* is supported
(see §6.7.19 *FullTextSearch*).

QUERY\_JOINS

STRING: Returns one of the following javax.jcr.Repository constants
indicating *the level of support for joins in queries*:

-  QUERY\_JOINS\_NONE: Joins are not supported. Queries are limited to a
   single selector.

-  QUERY\_JOINS\_INNER: Inner joins are supported.

-  QUERY\_JOINS\_INNER\_OUTER: Inner and outer joins are supported.

See §6.7.5 *Join*.

24.2.6 Deprecated Descriptors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Key**

**Descriptor**

LEVEL\_1\_SUPPORTED

BOOLEAN: Returns true if and only if

-  OPTION\_XML\_EXPORT\_SUPPORTED = true and

-  QUERY\_LANGUAGES is of non-zero length.

These semantics are identical to those in JCR 1.0. This constant is
**deprecated**.

LEVEL\_2\_SUPPORTED

BOOLEAN: Returns true if and only if

-  LEVEL\_1\_SUPPORTED = true,

-  WRITE\_SUPPORTED = true and

-  OPTION\_XML\_IMPORT\_SUPPORTED = true.

These semantics are identical to those in JCR 1.0. This constant is
**deprecated**.

OPTION\_QUERY\_SQL\_SUPPORTED

BOOLEAN: Returns true if and only if the (deprecated) JCR 1.0 SQL query
language is supported . This constant is **deprecated**.

QUERY\_XPATH\_POS\_INDEX

BOOLEAN: Returns false unless the (deprecated) JCR 1.0 XPath query
language is supported. If JCR 1.0 XPath is supported then this
descriptor has the same semantics as in JCR 1.0. This constant is
**deprecated**.

QUERY\_XPATH\_DOC\_ORDER

BOOLEAN: Returns false unless the (deprecated) JCR 1.0 XPath query
language is supported. If JCR 1.0 XPath is supported then this
descriptor has the same semantics as in JCR 1.0. This constant is
**deprecated**.

24.2.7 Implementation-Specific Descriptors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementers are free to introduce their own descriptors. The descriptor
keys should use Java package-style names in namespaces controlled by the
implementer. The Repository.isStandardDescriptor method must return
false for these keys.

24.3 Node Type-Related Features
-------------------------------

The node type registry is used to test support for features which
correspond to a JCR-defined node type. For example, support for
*referenceable nodes* as a feature is equivalent to support for the node
type mix:referenceable. Such features are more data model-oriented than
the behavioral features reported by descriptors.

Testing for the availability of a particular node type is done using

boolean NodeTypeManager.hasNodeType(String nodeTypeName)

Any node types associated with a particular feature are described in the
section describing that feature.

The presence of the indicated node types in the node type registry
(tested with NodeTypeManager.hasNodeType, see §8.1 *NodeTypeManager
Object*) indicates support for the corresponding feature.

+-----------------+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| **Node Type**   | mix:referenceable                                       | | mix:created                                                                                                         | mix:etag                                   | nt:unstructured                                              | | nt:nodeType                                                                           |
|                 |                                                         | | mix:mimeType                                                                                                        |                                            |                                                              | | nt:propertyDefinition                                                                 |
| **Feature**     | Referenceable nodes (see §3.8 *Referenceable Nodes*).   | | mix:lastModified                                                                                                    | Entity tags (see §3.7.12 *Entity Tags*).   | Unstructured content (see §3.7.13 *Unstructured Content*).   | | nt:childNodeDefinition                                                                |
|                 |                                                         | | mix:title                                                                                                           |                                            |                                                              |                                                                                         |
|                 |                                                         | | mix:language                                                                                                        |                                            |                                                              | Node type definition storage in content (see §3.7.14 *Node Type Definition Storage*).   |
|                 |                                                         | | nt:hierarchyNode                                                                                                    |                                            |                                                              |                                                                                         |
|                 |                                                         | | nt:file                                                                                                             |                                            |                                                              |                                                                                         |
|                 |                                                         | | nt:linkedFile                                                                                                       |                                            |                                                              |                                                                                         |
|                 |                                                         | | nt:folder                                                                                                           |                                            |                                                              |                                                                                         |
|                 |                                                         | | nt:resource                                                                                                         |                                            |                                                              |                                                                                         |
|                 |                                                         | | nt:address                                                                                                          |                                            |                                                              |                                                                                         |
|                 |                                                         |                                                                                                                       |                                            |                                                              |                                                                                         |
|                 |                                                         | Standard application node types, a repository can support a subset (see §3.7.11 *Standard Application Node Types*).   |                                            |                                                              |                                                                                         |
+-----------------+---------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------+--------------------------------------------------------------+-----------------------------------------------------------------------------------------+

24.4 Implementation Issues
--------------------------

JCR adapters built against some existing repositories may require a
connection to the back-end repository to determine whether a feature is
supported. Using methods on Repository (as opposed, for example, to
methods on Session) to test support for a feature is therefore
potentially problematic. However, several approaches are open to such
adapters:

-  Establish a transient connection to the back-end (for example, using
   service-to-service authentication or as “guest”) to determine support
   for a feature.

-  Determine the features supported by the back-end upon application
   deployment, and store this in configuration file locally available to
   the JCR adapter at runtime.

-  Report the feature set supported by the type of back end, which may
   be a superset of the feature set supported by the specific instance
   of that back-end type.
