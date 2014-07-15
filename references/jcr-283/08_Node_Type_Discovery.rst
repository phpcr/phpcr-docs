================================================================================
JCR 2.0: 8 Node Type Discovery (Content Repository for Java Technology API v2.0)
================================================================================

8 Node Type Discovery
=====================

All repositories are required to support methods for the discovery of
the following node type-related information:

-  Which node types are supported in the repository.

-  The definition of a supported node type.

-  The node type of a node.

-  The definition of an item in the node type of its parent.

8.1 NodeTypeManager Object
--------------------------

A repository has a single, global node type registry that holds all node
types available in the repository. The registry is represented by a
NodeTypeManager object acquired through

NodeTypeManager Workspace.getNodeTypeManager().

The method

NodeType NodeTypeManager.getNodeType(String nodeTypeName)

returns the NodeType object representing the specified registered node
type. NodeTypeManager also provides the following related methods for
accessing registered node types:

boolean NodeTypeManager.hasNodeType(String nodeTypeName)

NodeTypeIterator NodeTypeManager.getPrimaryNodeTypes()

NodeTypeIterator NodeTypeManager.getMixinNodeTypes()

NodeTypeIterator NodeTypeManager.getAllNodeTypes()

8.2 NodeType Object
-------------------

The NodeType interface is a subclass of NodeTypeDefinition, which
provides access methods to the static definitional characteristics of a
node type.

NodeType adds methods relevant to a “live” node type that is registered
in a repository.

Repositories that support *node type management* must implement
NodeTypeTemplate, which is another subclass of NodeTypeDefinition (see
§19 *Node Type Management*).

The NodeType interface provides methods to access the attributes of a
node type:

8.2.1 Name
~~~~~~~~~~

String NodeTypeDefinition.getName()

returns the name of the node type (see §3.7.1.1 *Node Type Name*).

8.2.2 Supertypes and Subtypes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

String[] NodeTypeDefinition.getDeclaredSupertypeNames()

returns the list of the names of declared supertypes in this definition
(see §3.7.1.2 *Supertypes*).

In a repository that supports *node type management* NodeTypeDefinition
objects not bound to a live node type may be encountered (for example,
in the form of a NodeTypeTemplate). In such cases this method may return
null.

NodeType additionally provides the following methods for accessing
supertype and subtype information

NodeType[] NodeType.getDeclaredSupertypes()

NodeType[] NodeType.getSuperTypes()

boolean NodeType.isNodeType(String nodeTypeName)

NodeTypeIterator NodeType.getDeclaredSubtypes()

NodeTypeIterator NodeType.getSubtypes()

8.2.3 Abstract
~~~~~~~~~~~~~~

boolean NodeTypeDefinition.isAbstract()

returns true if the node type is abstract and false otherwise (see
§3.7.1.3 *Abstract*).

8.2.4 Mixin
~~~~~~~~~~~

boolean NodeTypeDefinition.isMixin()

returns true if the node type is a mixin and false if it is a primary
type (see §3.7.1.4 *Mixin*).

8.2.5 Queryable Node Type
~~~~~~~~~~~~~~~~~~~~~~~~~

boolean NodeTypeDefinition.isQueryable()

returns true if the node type is queryable and false otherwise (see
§3.7.1.5 *Queryable Node Type*).

8.2.6 Orderable Child Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~

boolean NodeTypeDefinition.hasOrderableChildNodes()

returns true if the node type supports orderable child nodes and false
otherwise (see §3.7.1.6 *Orderable Child Nodes*). Support for *orderable
child nodes* is optional (see §23 *Orderable Child Nodes*).

8.2.7 Primary Item
~~~~~~~~~~~~~~~~~~

String NodeTypeDefinition.getPrimaryItemName()

returns the primary item of the node type, if any (see §3.7.1.7 *Primary
Item*).

8.2.8 Property Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~

The set of property definitions is represented by an array of
PropertyDefinition objects, accessed through the following methods:

| PropertyDefinition[]
|  NodeTypeDefinition.getDeclaredPropertyDefinitions()

PropertyDefinition[] NodeType.getPropertyDefinitions()

(see §3.7.1.8 *Property Definitions*)

8.2.9 Child Node Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The set of child node definitions is represented by an array of
NodeDefinition objects, accessed through the following methods:

| NodeDefinition[]
|  NodeTypeDefinition.getDeclaredChildNodeDefinitions()

NodeDefinition[] NodeType.getChildNodeDefinitions()

(see §3.7.1.8 *Property Definitions*)

8.3 ItemDefinition Object
-------------------------

The attributes common to both property and child node definitions are
accessed through the ItemDefinition interface. Attributes specific to
property definitions or child node definitions are accessed through the
PropertyDefinition and NodeDefinition interfaces, respectively. These
interfaces are both subclasses of ItemDefinition. The ItemDefinition
interface provides methods to access the following attributes:

8.3.1 Name
~~~~~~~~~~

String ItemDefinition.getName()

returns the JCR Name (in qualified form) of the item to which the
definition applies or “\*”, indicating that the definition is residual
(see §3.7.2.1 *Item Definition Name*).

8.3.2 Protected
~~~~~~~~~~~~~~~

boolean ItemDefinition.isProtected()

returns true if the item is protected and false otherwise (see §3.7.2.2
*Protected*).

8.3.3 Auto-Created
~~~~~~~~~~~~~~~~~~

boolean ItemDefinition.isAutoCreated()

returns true if the item is auto-created and false otherwise (see
§3.7.2.3 *Auto-Created*).

8.3.4 Mandatory
~~~~~~~~~~~~~~~

boolean ItemDefinition.isMandatory()

returns true if the item is mandatory and false otherwise (see §3.7.2.4
*Mandatory*).

8.3.5 On-Parent-Version
~~~~~~~~~~~~~~~~~~~~~~~

int ItemDefinition.getOnParentVersion()

returns the on-parent-version setting of the definition; one of the
constants of OnParentVersionAction (see §3.7.2.5 *On-Parent-Version*).

8.3.6 Declaring Node Type
~~~~~~~~~~~~~~~~~~~~~~~~~

NodeType ItemDefinition.getDeclaringNodeType()

returns the NodeType object that contains this definition (see §8.2
*NodeType Object*).

8.4 PropertyDefinition Object
-----------------------------

The attributes specific to property definitions are accessed through the
PropertyDefinition interface, which is a subclass of ItemDefinition:

8.4.1 Required Type
~~~~~~~~~~~~~~~~~~~

int PropertyDefinition.getRequiredType()

returns the property type setting of the definition, which must be one
of the constants of the PropertyType interface (see §3.7.3.1 *Property
Type*).

8.4.2 Default Values
~~~~~~~~~~~~~~~~~~~~

Value[] PropertyDefinition.getDefaultValues()

returns the default values of the definition (see §3.7.3.2 *Default
Values*).

8.4.3 Available Query Operators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

String[] PropertyDefinition.getAvailableQueryOperators()

returns an array of String constants indicating which query operators
are supported for this property (see §3.7.3.3 *Available Query
Operators*). The constants are defined in the class
QueryObjectModelConstants and represent the operators defined in §6.7.16
*Comparison*.

8.4.4 Full-Text Searchable
~~~~~~~~~~~~~~~~~~~~~~~~~~

boolean NodeTypeDefinition.isFullTextSearchable()

returns true if the property is full-text searchable and false otherwise
(see §3.7.3.4 *Full-Text Searchable*).

8.4.5 Query-Orderable
~~~~~~~~~~~~~~~~~~~~~

boolean NodeTypeDefinition.isQueryOrderable()

returns true if the property is query-orderable and false otherwise (see
§3.7.3.5 *Query-Orderable*).

8.4.6 Value Constraints
~~~~~~~~~~~~~~~~~~~~~~~

String[] PropertyDefinition.getValueConstraints()

returns the value constraints of the definition (see §3.7.3.6 *Value
Constraints*),

8.4.7 Multi-value
~~~~~~~~~~~~~~~~~

boolean PropertyDefinition.isMultiple()

returns true if the definition defines a multi-value property and false
if it defines a single value property (see §3.7.3.7 *Multi-Value*).

8.5 NodeDefinition Object
-------------------------

The attributes specific to child node definitions are accessed through
the NodeDefinition interface, which is a subclass of ItemDefinition:

8.5.1 Required Primary Node Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods

NodeType[] NodeDefinition.getRequiredPrimaryTypes() and

String[] NodeDefinition.getRequiredPrimaryTypeNames()

return information about the required primary node types of the
definition (§3.7.4.1 *Required Primary Node Types*). The latter method
returns the names of the node types while the former method returns the
live NodeType objects representing the types. The former only functions
if the NodeDefinition is part of a live registered NodeType.

8.5.2 Default Primary Node Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods

NodeType NodeDefinition.getDefaultPrimaryType() and

String NodeDefinition.getDefaultPrimaryTypeName()

return information about the default primary node type of the definition
(§3.7.4.2 *Default Primary Node Type*). The latter method returns the
name of the node type while the former method returns the live NodeType
object representing the type. The former only functions if the
NodeDefinition is part of a live registered NodeType.

8.5.3 Same-Name Siblings
~~~~~~~~~~~~~~~~~~~~~~~~

boolean NodeDefinition.allowsSameNameSiblings()

returns true if the definition allows same-name sibling nodes and false
otherwise (see §3.7.4.3 *Same-Name Siblings*).

8.6 Node Type Information for Existing Nodes
--------------------------------------------

Given an existing Node, the methods

NodeType Node.getPrimaryNodeType() and

NodeType[] Node.getMixinNodeTypes()

return, respectively, the primary and mixin node types of the node. The
method

boolean Node.isNodeType(String nodeTypeName)

returns true if the Node is of the specified node type, according to the
*is-of-type* relation (see §3.7.6.3 *Is-of-Type Relation*), and false
otherwise.

8.6.1.1 Discovery of Item Definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Node and Property interfaces offer methods that allow direct access
to the NodeDefinition or PropertyDefinition within the node type of a
parent node that is applicable to a particular child item:

NodeDefinition Node.getDefinition()

PropertyDefinition Property.getDefinition()

The definition that applies to an item is determined upon creation of
that item (see §3.7.7 *Applicable Item Definition*).

8.6.1.2 Root Node Definition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method getDefinition called on the root node must return a valid,
non-null, NodeDefinition object. The values returned by the methods of
this object must be as follows:

-  getName(): ““, the empty string.

-  getDeclaringNodeType(): A valid NodeType object (see §8.6.1.3 *Root
   Declaring Node Type*).

-  isMandatory(): true

-  isAutoCreated(): true

-  isProtected(): false

-  allowsSameNameSiblings(): false

-  getOnParentVersion(): VERSION, if versioning is supported and the
   root node is capable of being made versionable, IGNORE otherwise.

-  getDefaultPrimaryType(): A valid non-null NodeType object (see §3.7.8
   *Root Node Type*).

-  getRequiredPrimaryTypes(): An array containing a single NodeType
   object identical with that returned by getDefaultPrimaryType.

8.6.1.3 Root Declaring Node Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Calling getDeclaringNodeType() on the NodeDefinition of the root node
must return a valid NodeType object. The values returned by the methods
of this object must be as follows:

-  getName() returns the name of a node type N, where N is
   implementation-determined.

-  `isNodeType <http://www.day.com/maven/jsr170/javadocs/jcr-1.0/javax/jcr/nodetype/NodeType.html#isNodeType%28java.lang.String%29>`__\ (String nodeTypeName)
   returns true if an only if nodeTypeName is N or a supertype of N.

-  `getChildNodeDefinitions <http://www.day.com/maven/jsr170/javadocs/jcr-1.0/javax/jcr/nodetype/NodeType.html#getChildNodeDefinitions%28%29>`__\ ()
   and getDeclaredChildNodeDefinitions() both return an array containing
   the child node definition of the root node.

All other methods either return false (if they return a boolean) or an
empty array (if they return an array).
