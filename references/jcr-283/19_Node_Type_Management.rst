==================================================================================
JCR 2.0: 19 Node Type Management (Content Repository for Java Technology API v2.0)
==================================================================================

19 Node Type Management
=======================

A repository may support *node type management*. Depending on
implementation-specific limitations (see §19.3 *Node Type Registration
Restrictions*), this feature may include some or all of the following:

-  Adding a node type to the registry.

-  Removing a node type from the registry.

-  Updating the definition of a registered node type that *is* *not*
   currently in use as the node type of any node in the repository.

-  Updating the definition of a registered node type that *is* currently
   in use as the node type of a node in the repository.

-  Import of node type definitions to the repository.

-  Export of node types from the repository.

Whether a particular implementation supports node type management and
the restrictions in place with regard to this feature can be determined
by querying the repository descriptor table with the constants listed in
§24.2.4 *Node Type Management*.

19.1 NodeTypeDefinition
-----------------------

The NodeTypeDefinition interface provides methods for discovering the
static definition of a node type. These are accessible both before and
after the node type is registered. Its subclass NodeType adds methods
that are relevant only when the node type is “live”; that is, after it
has been registered.

In implementations that support node type registrations,
NodeTypeDefinition serves as the superclass of both NodeType and
NodeTypeTemplate. In implementations that do not support node type
registration, only objects implementing the subclass NodeType will be
encountered.

19.2 NodeTypeManager
--------------------

The NodeTypeManager interface provides the following methods related to
registering node types. For methods of this interface that are related
to node type discovery, see §8 *Node Type Discovery*. In implementations
that do not support node type management, the methods of NodeTypeManager
will throw an UnsupportedRepositoryOperationException.

19.2.1 Creating a NodeTypeTemplate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NodeTypeTemplate NodeTypeManager.createNodeTypeTemplate()

returns an empty NodeTypeTemplate which can then be used to define a
node type and passed to registerNodeType.

| NodeTypeTemplate NodeTypeManager.
|  createNodeTypeTemplate(NodeTypeDefinition ntd)

returns a NodeTypeTemplate holding the specified NodeTypeDefinition.
This template may then be altered and passed to registerNodeType.

19.2.2 Creating a NodeDefinitionTemplate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| NodeDefinitionTemplate NodeTypeManager.
|  createNodeDefinitionTemplate()

returns an empty NodeDefinitionTemplate which can then be used to create
a child node definition and attached to a NodeTypeTemplate.

19.2.3 Creating a PropertyDefinitionTemplate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| PropertyDefinitionTemplate NodeTypeManager.
|  createPropertyDefinitionTemplate()

returns an empty PropertyDefinitionTemplate which can then be used to
create a property definition and attached to a NodeTypeTemplate.

19.2.4 Registering a Node Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| NodeType NodeTypeManager.
|  registerNodeType(NodeTypeDefinition ntd, boolean allowUpdate)

registers a new node type or updates an existing node type using the
specified definition and returns the resulting NodeType object.
Typically, the object passed to this method will be a NodeTypeTemplate
(a subclass of NodeTypeDefinition) acquired from
NodeTypeManager.createNodeTypeTemplate and then filled-in with
definition information. If allowUpdate is true then an attempt to change
the definition of an already registered node type will be made (see
§19.2.4.1 *Updating Node Types*), otherwise an attempt to register a
node type with the same name as an already registered one will fail
immediately.

| NodeTypeIterator NodeTypeManager.
|  registerNodeTypes(NodeTypeDefinition[] ntds,
|  boolean allowUpdate)

registers or updates the specified array of NodeTypeDefinition objects.
This method is used to register or update a set of node types with
mutual dependencies. It returns an iterator over the resulting NodeType
objects. The effect of the method is “all or nothing”; if an error
occurs, no changes are made.

19.2.4.1 Updating Node Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A repository that supports node type management may support updates to a
node type already in use as the type of an existing node. The extent of
any such capability is implementation dependent. For example, some
implementations may permit only changes which do not invalidate existing
content, while others may allow larger changes. How any resulting
incompatibilities are resolved is also implementation dependent. Any
changes to the type of an exiting node must take effect in accordance
with the *node type assignment behavior* of the repository (see §10.10.1
*Node Type Assignment Behavior*).

19.2.5 Unregistering a Node Type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

void NodeTypeManager.unregisterNodeType(String nodeTypeName)

unregisters the specified node type.

| void NodeTypeManager.
|  unregisterNodeTypes(String[] nodeTypeNames)

unregisters the specified set of node types. This method is used to
unregister a set of node types with mutual dependencies.

19.2.6 Testing for Node Types
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

boolean NodeTypeManager.hasNodeType(String nodeTypeName)

returns true if a node type with the specified name is registered and
returns false otherwise.

19.3 Node Type Registration Restrictions
----------------------------------------

A repository *must* prevent the registration of any node type that uses
a reserved namespace either in its name or in the name of any of its
item definitions (see 3.4 *Namespace Mapping*).

A repository *may* restrict the range of node types that can be
registered according to implementation-specific criteria. This is most
relevant in cases where a JCR repository is built on top of an existing
content store which has intrinsic limitations that restrict the space of
supported node types.

19.4 Templates
--------------

Node types are defined programmatically by setting the attributes of
template objects and passing these to the NodeTypeManager.

The NodeTypeTemplate is a container holding the node type's attributes
and its property and child node definitions, which are themselves
represented by NodeDefinitionTemplate and PropertyDefinitionTemplate
objects, respectively.

The user registers a node type by first acquiring a NodeTypeTemplate and
the necessary PropertyDefinitionTemplate or NodeDefinitionTemplate
objects through the NodeTypeManager (see §19.2 *NodeTypeManager*). The
attributes of these objects are then set, with the appropriate
PropertyDefinitionTemplate and NodeDefinitionTemplate objects added to
the NodeTypeTemplate object. The resulting NodeTypeTemplate object is
then passed to a registration method of the NodeTypeManager.

19.4.1 NodeTypeTemplate
~~~~~~~~~~~~~~~~~~~~~~~

NodeTypeTemplate, like NodeType, is a subclass of NodeTypeDefinition, so
it shares with NodeType those methods that are relevant to a static
definition. In addition to the methods inherited from
NodeTypeDefinition, NodeTypeTemplate provides methods for setting the
attributes of the definition. The setter methods are named appropriately
according to the attribute that they set (see 3.6.1 *Node Type
Definition Attributes*). Consult the Javadoc for details on the method
signatures.

19.4.1.1 Setting Property and Child Node Definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setting the property definitions within a node type template is done by
adding PropertyDefinitionTemplate objects to the mutable List object
retrieved from

List NodeTypeTemplate.getPropertyDefinitionTemplates().

Similarly, setting the child node definitions is done by adding
NodeDefinitionTemplate objects to the mutable List object retrieved from

List NodeTypeTemplate.getNodeDefinitionTemplates().

19.4.1.2 Default Values of Node Type Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See the corresponding get methods for each attribute in
NodeTypeDefinition (see §19.1 *NodeTypeDefinition*) for the default
values assumed when a new empty NodeTypeTemplate is created.

19.4.2 PropertyDefinitionTemplate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The PropertyDefinitionTemplate interface extends PropertyDefinition (see
§8.4 *PropertyDefinition Object*) with the addition of write methods,
enabling the characteristics of a child property definition to be set,
after which the PropertyDefinitionTemplate is added to a
NodeTypeTemplate. The setter methods are named appropriately according
to the attribute that they set (see §3.7.2 *Item Definition Attributes*
and §3.7.3 *Property Definition Attributes*). Consult the Javadoc for
details on the method signatures.

19.4.2.1 Default Values of Property Definition Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See the corresponding get methods for each attribute in
PropertyDefinition (see §8.4 *PropertyDefinition Object*) for the
default values assumed when a new empty PropertyDefinitionTemplate is
created.

19.4.3 NodeDefinitionTemplate
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The NodeDefinitionTemplate interface extends NodeDefinition (see §8.5
*NodeDefinition Object*) with the addition of write methods, enabling
the characteristics of a child node definition to be set, after which
the NodeDefinitionTemplate is added to a NodeTypeTemplate. The setter
methods are named appropriately according to the attribute that they set
(see §3.7.2 *Item Definition Attributes* and §3.7.4 *Child Node
Definition Attributes*). Consult the Javadoc for details on the method
signatures.

19.4.3.1 Default Values of Child Node Definition Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

See the corresponding get methods for each attribute in NodeDefinition
(see §8.5 *NodeDefinition Object*) for the default values assumed when a
new empty NodeDefinitionTemplate is created.
