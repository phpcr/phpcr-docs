====================================================================
JCR 2.0: 5 Reading (Content Repository for Java Technology API v2.0)
====================================================================

5 Reading
=========

There are three types of read access which a session may have with
respect to a particular item, depending on that session's permissions:
direct access, traversal access and query access.

5.1 Direct Access
-----------------

*Direct access* to an item means being able to retrieve it by absolute
and relative path and, in the case of nodes, by identifier.

Let p(x) return the normalized absolute path of item x, p(x, y) return
the normalized relative path from item x to item y and, id(x) return the
identifier of node x.

For any session S and node N, the statements below must be either all
true or all false. If they are all true then S has direct access to N,
if they are all false then S does not have direct access to N:

-  S.getItem(p(N)) returns N.

-  S.itemExists(p(N)) returns true.

-  S.getNode(p(N)) returns N.

-  S.nodeExists(p(N)) returns true.

-  S.getNodeByIdentifier(id(N)) returns N.

-  If N is the primary item of a node M then M.getPrimaryItem() returns
   N.

-  If N is the root node of the workspace then S.getRootNode() returns
   N.

-  For all nodes M to which S has direct access, M.getNode(p(M,N))
   returns N.

-  For all nodes M to which S has direct access, M.hasNode(p(M,N))
   returns true.

For any session S and property P, the statements below must be either
all true or all false. If they are all true then S has direct access to
P, if they are all false then S does not have direct access to P:

-  If there is no node at the path p(P) to which S has read access then

   -  S.getItem(p(P)) returns P and

   -  S.itemExists(p(P)) returns true.

-  S.getProperty(p(P)) returns P.

-  S.propertyExists(p(P)) returns true.

-  S has read access to the value of P (see §9.1 *Permissions*).

-  If P is the primary item of a node N then N.getPrimaryItem() returns
   P.

-  For all nodes M to which S has direct access, M.getProperty(p(M,P))
   returns P.

-  For all nodes M to which S has direct access, M.hasProperty(p(M,P))
   returns true.

5.1.1 Getting the Root Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The root node of the workspace can be acquired with

Node Session.getRootNode().

5.1.2 Testing for Existence by Absolute Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The existence of a node or property at a particular absolute path can be
tested for with

boolean Session.itemExists(String absPath),

boolean Session.nodeExists(String absPath) and

boolean Session.propertyExists(String absPath).

5.1.3 Access by Absolute Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nodes and properties can be acquired by absolute path with

Item Session.getItem(String absPath),

Node Session.getNode(String absPath) and

Property Session.getProperty(String absPath).

5.1.4 Getting a Node by Identifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A node can be retrieved by its identifier with

Node Session.getNodeByIdentifier(String identifier).

Using an identifier-based absolute path a node can also be retrieved by
identifier with a path-base get method. For example,

S.getNode(“[“ + id + “]”)

where S is the session and id is the identifier.

5.1.5 Testing for Existence by Relative Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Existence of nodes and properties can be tested by path relative to a
given node with

boolean Node.hasNode(String relPath) and

boolean Node.hasProperty(String relPath).

5.1.6 Access by Relative Path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nodes and properties can be acquired via relative path with

Node Node.getNode(String relPath) and

Property Node.getProperty(String relPath)

5.1.7 Primary Item Access
~~~~~~~~~~~~~~~~~~~~~~~~~

If a primary child item is specified by the node type of a node, this
item can be retrieved directly from the node with

Item Node.getPrimaryItem().

See §3.7.1.7 *Primary Item*.

5.1.8 Node and Property with Same Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In some repositories a node and property with the same parent may have
the same name. The methods Node.getNode, Session.getNode,
Node.getProperty and Session.getProperty specify whether the desired
item is a node or a property. The method Session.getItem will return the
item at the specified path if there is only one such item, if there is
both a node and a property at the specified path, getItem will return
the node.

Whether an implementation supports this feature can be determined by
querying the repository descriptor table with

Repository.OPTION\_NODE\_AND\_PROPERTY\_WITH\_SAME\_NAME\_SUPPORTED.

A return value of true indicates support (see §24.2 *Repository
Descriptors*).

5.2 Traversal Access
--------------------

Traversal access to an item I means that it is returned when iterating
over the children of a node.

For any given session S and item I, the statements below must be either
both true or both false. If they are both true then S has traversal
access to I, if they are both false then S does not have traversal
access to I:

-  S has access to N where N is the parent of I and I appears among the
   items in the iterator returned by either N.getNodes or
   N.getProperties.

-  S has access to N, I is a descendant of N and I appears in the
   serialized output of an export of the subgraph rooted at N.

5.2.1 Testing Existence
~~~~~~~~~~~~~~~~~~~~~~~

A client can test whether a retrieved iterator will be empty using the
following:

boolean Node.hasNodes()

boolean Node.hasProperties()

5.2.2 Iterating Over Child Items
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Iterators over child nodes and properties can be acquired using the
following methods:

NodeIterator Node.getNodes()

PropertyIterator Node.getProperties()

These methods return all the child nodes or properties (as the case may
be) of the node that are visible to the current session.

NodeIterator Node.getNodes(String namePattern)

NodeIterator Node.getNodes(String[] nameGlobs)

PropertyIterator Node.getProperties(String namePattern)

PropertyIterator Node.getProperties(String[] nameGlobs)

These methods return all the child nodes or properties (as the case may
be) of the node that are both visible to the current session and that
match the passed namePattern or nameGlobs array.

5.2.2.1 Name Patterns
^^^^^^^^^^^^^^^^^^^^^

The namePattern passed in Node.getNodes and Node.getProperties is a
string matched against the qualified names (not the paths) of the
immediate child items of this node. We call the namePattern parameter
the *pattern* and the qualified names against which it is tested the
*target strings*.

-  A *pattern* consists of one or more *globs*. In cases of two or more
   globs, they are delimited by the pipe character (\|, U+0076).

-  A pattern matches a target string if and only if at least one of its
   globs matches that target string.

-  A *glob* matches a target string if and only if it matches character
   for character, except for any asterisk characters (\*, U+002A) in the
   glob, which match any substring (including the empty string) in the
   target string.

The characters “\|” and “\*” are excluded from qualified JCR names (see
§3.2.5.2 *Qualified Form*), so their use as metacharacters in the
pattern will not lead to a conflict.

For backwards compatibility with JCR 1.0, leading and trailing
whitespace around a glob is ignored but whitespace within a glob forms
part of the pattern to be matched.

5.2.2.2 Name Globs
^^^^^^^^^^^^^^^^^^

The alternate signatures

NodeIterator Node.getNodes(String[] nameGlobs)

PropertyIterator Node.getProperties(String[] nameGlobs)

Behave identically to those that take namePattern except that the
parameter passed is an array of globs, as defined above, which are
“ORed” together, removing the need for the “\|” metacharacter to
indicate disjunction. The items returned, therefore, are those that
match *at least one* of the globs in the array. Unlike the namePattern
case, leading and trailing whitespace in globs *is not* ignored by these
methods.

5.2.2.3 Child Node Order Preservation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Depending on the implementation, the order of child nodes within the
returned iterator may be more or less stable across different
retrievals. A repository that supports *preservation of child node
ordering* will maintain a constant total order across separate
retrievals. A repository that supports orderable child nodes necessarily
also supports order preservation (§23 *Orderable Child Nodes*).

5.2.3 Export
~~~~~~~~~~~~

Exporting a subgraph within a workspace can be done with

Session.exportSystemView or

Session.exportDocumentView.

See §7 *Export*.

5.3 Query Access
----------------

A session S has query access to I if and only if for at least one Query
object Q, where Q is created through the QueryManager of the Workspace
object bound to S, I is returned in the QueryResult for Q (see §6
*Query*).

5.4 Relationship among Access Modes
-----------------------------------

For any given session S and item I:

-  If S has traversal access to I then S must have direct access to I.

If S has query access I then S has direct access to I.

However, note that,

-  If S has direct access to I then S may or may not have traversal
   access to I.

-  If S has direct access to I then S may or may not have query access
   to I.

-  If S has direct access to I then S may or may not have direct access
   to any parent of I.

5.5 Effect of Access Denial on Read
-----------------------------------

If a repository restricts the read access of a session, then the nodes
and properties to which that session does not have read access must
appear not to exist. For example, the iterator returned on N.getNodes
will not include subnodes of N to which the session in question does not
have read access. In other words, lack of read access to an item blocks
access to both information about the content of that item and
information about the existence of that item.

In repositories that support *same-name siblings*, denial of access to a
subset of nodes within a same-name sibling series *may* result in gaps
in the index numbering of that series, thus revealing information about
the existence of the inaccessible nodes.

5.6 Item Information
--------------------

The Item interface includes a number of methods that provide information
about an item.

5.6.1 Item to Session
~~~~~~~~~~~~~~~~~~~~~

This method provides access to the current Session.

Session Item.getSession()

5.6.2 Item in Hierarchy
~~~~~~~~~~~~~~~~~~~~~~~

These methods provide information about the location of an Item within
the workspace hierarchy:

String Item.getName()

returns the name of the Item.

String Item.getPath()

returns the absolute path of the Item.

Node Item.getAncestor(int depth)

returns the ancestor of the Item that is at the specified depth below
the root node.

Node Item.getParent()

returns the parent of the Item.

int Item.getDepth()

returns the depth below the root node of the Item.

5.6.3 Item Subclass
~~~~~~~~~~~~~~~~~~~

boolean Item.isNode()

returns true if the Item is a Node and false if it is a Property.

5.6.4 Item Comparison
~~~~~~~~~~~~~~~~~~~~~

This method is used to determine the repository-level semantic identity
of two Item objects.

boolean Item.isSame(Item otherItem)

returns true if this Item object represents the same actual repository
item as the object otherItem. This method does not compare the states of
the two items. For example, if two Item objects representing the same
actual repository item have been retrieved through two different
sessions and one has been modified, then this method will still return
true for these two objects. Note that if two Item objects representing
the same repository item are retrieved through the same Session they
will always reflect the same state so comparing state is not an issue
(see section §10.11.7 *Reflecting Item State*).

5.6.5 Item Visitor
~~~~~~~~~~~~~~~~~~

This method implements the *visitor design pattern*.

void Item.accept(ItemVisitor visitor)

The ItemVisitor interface defines the methods

void ItemVisitor.visit(Node node) and

void ItemVisitor.visit(Property property)

which the user can implement.

5.7 Node Identifier
-------------------

The method

String Node.getIdentifier()

returns the identifier of a node.

5.8 Node Index
--------------

The method

int Node.getIndex()

returns the index of a node among its same-name siblings (see §22
*Same-Name Siblings*). Same-name sibling indexes begin with [1], so this
method will return 1 for a node without any same-name siblings.

5.9 Iterators
-------------

Methods that return a set of Node or Property objects do so using a
NodeIterator or PropertyIterator, subclasses of RangeIterator.

JCR also specifies the following subclasses of RangeIterator:
RowIterator, NodeTypeIterator, VersionIterator, EventListenerIterator,
AccessControlPolicyIterator, EventIterator and EventJournal.

5.9.1 Iterator Lifespan
~~~~~~~~~~~~~~~~~~~~~~~

The lifespan of an instance of RangeIterator or any of its subclasses is
implementation-specific. For example, in some implementations a
Session.refresh (see §10.11.1 *Refresh*) might invalidate a previously
acquired NodeIterator while in others it might not.

5.10 Reading Properties
-----------------------

If a session has read access to a single–value property then it can read
the value of that property. If a session has read access to a
multi-value property then it can read *all* the values of that property.

5.10.1 Getting a Value
~~~~~~~~~~~~~~~~~~~~~~

The generic value getter for single value properties is

Value Property.getValue().

For multi-value properties it is

Value[] Property.getValues().

Single and multi-value properties can be distinguished by calling

boolean Property.isMultiple().

5.10.2 Value Type
~~~~~~~~~~~~~~~~~

int Value.getType()

returns one of the constants of PropertyType (see §3.6.1 *Property
Types*) indicating the property type of the Value.

5.10.3 Value Length
~~~~~~~~~~~~~~~~~~~

The length of a value in a single-value property, as defined in §3.6.7
*Length of a Value*, is returned by

long Property.getLength()

Similarly, the method

long[] Property.getLengths()

is used to get an array of the lengths of all the values of a
multi-value property.

5.10.4 Standard Value Read Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each property type has a standard Value read method. This is the method
that returns the Java object or primitive type that corresponds
naturally to the JCR property type. A Value may also be readable by a
non-standard read method, depending on whether it is convertible to that
method's return type according to the rules described in §3.6.4
*Property Type Conversion*. The following sections set out the standard
read method for each type.

5.10.4.1 STRING
^^^^^^^^^^^^^^^

String Value.getString()

returns a JCR STRING as a java.lang.String.

5.10.4.2 BINARY
^^^^^^^^^^^^^^^

Binary Value.getBinary()

returns a JCR BINARY as a javax.jcr.Binary (see §5.10.5 *Binary
Object*).

5.10.4.3 LONG
^^^^^^^^^^^^^

long Value.getLong()

returns a JCR LONG as a Java long.

5.10.4.4 DOUBLE
^^^^^^^^^^^^^^^

double Value.getDouble()

returns a JCR DOUBLE as a Java double.

5.10.4.5 DECIMAL
^^^^^^^^^^^^^^^^

BigDecimal Value.getDecimal()

returns a JCR DECIMAL as a java.math.BigDecimal.

5.10.4.6 DATE
^^^^^^^^^^^^^

Calendar Value.getDate()

returns a JCR DATE as a java.util.Calendar.

5.10.4.7 BOOLEAN
^^^^^^^^^^^^^^^^

boolean Value.getBoolean()

returns a JCR BOOLEAN as a Java boolean.

5.10.4.8 NAME
^^^^^^^^^^^^^

String Value.getString()

returns a JCR NAME as a String. The String returned must be the JCR name
in *qualified form* (see §3.2.5.2 *Qualified Form*).

5.10.4.9 PATH
^^^^^^^^^^^^^

String Value.getString()

returns a JCR PATH as a String. The String returned must be the JCR path
in *standard form* (see §3.4.3.1 *Standard Form*). However, if the
original value was *non-normalized* it must be returned non-normalized,
preserving the path structure as it was originally set, including any
redundant path segments that may exist (see §3.4.5 *Normalized Paths*).

5.10.4.10 REFERENCE and WEAKREFERENCE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

String Value.getString()

returns a JCR REFERENCE or WEAKREFERENCE as a String. The value of a
REFERENCE or WEAKREFERENCE is a node referenceable identifier (see
§3.8.3 *Referenceable Identifiers*). Since an identifier is simply a
String, the returned value can be used directly to find the referenced
node (see §5.1.4 *Getting a Node by Identifier*).

5.10.5 Binary Object
~~~~~~~~~~~~~~~~~~~~

The Binary object returned by Value.getBinary() provides the following
methods:

InputStream Binary.getStream(),

which returns an InputStream representation of the value. Each call to
this method returns a new stream and the API consumer is responsible for
calling close() on the returned stream.

int Binary.read(byte[] b, long position),

which reads successive bytes starting from the specified position in the
value into the passed byte array until either the byte array is full or
the end of the value is encountered.

long Binary.getSize(),

which returns the size of the value in bytes.

5.10.5.1 Disposing of a Binary Object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When an application is finished with a Binary object it should call

void Binary.dispose()

on that object. This will releases all resources associated with the
object and inform the repository that these resources may now be
reclaimed.

5.10.5.2 Deprecated Binary Behavior
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Binary interface and its related methods in Property, Value and
ValueFactory replace the deprecated Value.getStream() and
Property.getStream() methods from JCR 1.0. Though these methods have
been deprecated, for reasons of backward compatibility their behavior
must conform to the following rules:

-  Once a Value object has been read once using getStream(), all
   subsequent calls to getStream() will return the same stream object.
   This may mean, for example, that the stream returned is fully or
   partially consumed. In order to get a fresh stream the Value object
   must be reacquired via Property.getValue() or Property.getValues().

-  Unlike in JCR 1.0, calling a get method other than getStream before
   calling getStream on the same Value object will never cause an
   IllegalStateException.

5.10.6 Dereferencing
~~~~~~~~~~~~~~~~~~~~

PATH, WEAKREFERENCE and REFERENCE properties function as pointers to
other items in the workspace. A PATH can point to a node or a property
while a WEAKREFERENCE or REFERENCE can point only to a referenceable
node. REFERENCE properties enforce referential integrity while
WEAKREFERENCE properties and PATH properties do not. These properties
can be dereferenced either manually or though convenience methods.

5.10.6.1 Manual Dereference
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To manually dereference a pointer property it is first read as a string,
for example with

Value.getString().

In the case of WEAKREFERENCE and REFERENCE properties the resulting
string is passed to

Session.getNodeByIdentifier(String id).

In the case of PATH properties the string is passed to

Session.getNode(String absPath) or

Session.getProperty(String absPath)

as appropriate to the target item. Whether the Item is a Node or
Property can be determined with Session.nodeExists or
Session.propertyExists (see §5.1.2 *Testing for Existence by Absolute
Path*).

5.10.6.2 Dereferencing Convenience Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Property interface provides convenience methods for dereferencing
pointer properties:

Node Property.getNode()

returns the node pointed to by a single-value property. This method
works with WEAKREFERENCE and REFERENCE properties and with PATH
properties that point to nodes.

Property Property.getProperty()

returns the property pointed to by a single-value PATH property.

For multi-value pointer properties the array of values must be retrieved
with Property.getValues and each individually manually dereferenced.

5.10.7 Backtracking References
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a referenceable node,

Node.getReferences()

returns all accessible REFERENCE properties in the workspace that point
to the node.

Node.getWeakReferences()

returns all accessible WEAKREFERENCE properties in the workspace that
point to the node.

Note that access control and other implementation-specific limitations
my mean that some references within the workspace are not accessible.

PATH properties are not automatically backtrackable.

5.10.8 Single-Value Property Read Methods
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The property interface provides convenience methods for reading
single-value properties which function identically to their Value
counterparts.

5.10.9 Reading Multi-Value Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A multi-value property can be accessed with

Value[] Property.getValues().

5.10.10 PropertyType Class
~~~~~~~~~~~~~~~~~~~~~~~~~~

The class PropertyType defines integer constants for the property types
as well as string constants for their standardized type names (which are
used in serialization) and two methods for converting back and forth
between name and integer value (see Javadoc).

5.11 Namespace Mapping
----------------------

The method

| void Session.setNamespacePrefix(String prefix,
|  String uri)

is used to change the local namespace mappings of the current Session.
When called, all local mappings that include either the specified prefix
or the specified uri are removed and the new mapping is added. However,
the method will throw an exception if

-  the specified prefix begins with the characters “xml” (in any
   combination of case) or,

-  the specified prefix is the empty string or,

-  the specified namespace URI is the empty string.

The following methods are also related to the local namespace mapping:

String[] Session.getNamespacePrefixes()

String Session.getNamespaceURI(String prefix)

String Session.getNamespacePrefix(String uri)
