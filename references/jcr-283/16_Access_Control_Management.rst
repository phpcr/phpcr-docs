=======================================================================================
JCR 2.0: 16 Access Control Management (Content Repository for Java Technology API v2.0)
=======================================================================================

16 Access Control Management
============================

A repository may support *access control management*, enabling the
following:

-  Privilege discovery: Determining the privileges that a user has in
   relation to a node.

-  Assigning access control policies: Setting the privileges that a user
   has in relation to a node using access control policies specific to
   the implementation.

Whether a particular implementation supports access control can be
determined by querying the repository descriptor table with

Repository.OPTION\_ACCESS\_CONTROL\_SUPPORTED.

A return value of true indicates support (see §24.2 *Repository
Descriptors*).

16.1 Access Control Manager
---------------------------

Access control is exposed through a

javax.jcr.security.AccessControlManager

acquired from the Session using

AccessControlManager Session.getAccessControlManager().

16.2 Privilege Discovery
------------------------

A privilege represents the ability to perform a particular set of
operations on a node. Each privilege is identified by a JCR name.

JCR defines a set of standard privileges within the Privilege interface.
An implementation may add additional privileges, using an appropriate
implementation-specific namespace for their names.

16.2.1 Aggregate Privileges
~~~~~~~~~~~~~~~~~~~~~~~~~~~

A privilege may be an *aggregate privilege*. Aggregate privileges are
sets of other privileges. Granting, denying, or testing an aggregate
privilege is equivalent to individually granting, denying, or testing
each privilege it contains. The privileges contained by an aggregate
privilege may themselves be aggregate privileges if the resulting
privilege graph is acyclic.

16.2.2 Abstract Privileges
~~~~~~~~~~~~~~~~~~~~~~~~~~

A privilege may be an *abstract privilege*. Abstract privileges cannot
themselves be granted or denied, but can be individually tested and can
be composed into aggregate privileges which are granted or denied.

Abstract privileges facilitate application interoperability against
repositories supporting different privilege granularities. For example,
consider aggregate privilege *p* containing privileges *p1* and *p2*. In
repository A, *p1* and *p2* are not abstract and can therefore be
individually granted, whereas in repository B both *p1* and *p2* are
abstract and cannot be individually granted. For both repositories,
however, an application can test whether a user has privilege *p1*, even
though in repository B, *p1* can only be acquired through non-abstract
privilege *p*.

A privilege can be both aggregate and abstract.

16.2.3 Standard Privileges
~~~~~~~~~~~~~~~~~~~~~~~~~~

A repository must support the following standard privileges identified
by the string constants of javax.jcr.security.Privilege:

-  jcr:read: The privilege to retrieve a node and get its properties and
   their values.

-  jcr:modifyProperties: The privilege to create, remove and modify the
   values of the properties of a node.

-  jcr:addChildNodes: The privilege to create child nodes of a node.

-  jcr:removeNode: The privilege to remove a node.

-  jcr:removeChildNodes: The privilege to remove child nodes of a node.

In order to actually remove a node requires jcr:removeNode on that node
and jcr:removeChildNodes on the parent node. The distinction is provided
in order to distinguish implementations that internally model a “remove”
as a “delete” from those that model it as an “unlink”. A repository that
uses the “delete” model can have jcr:removeChildNodes in every access
control policy, so that removal is effectively controlled by
jcr:removeNode. Conversely, a repository that uses the “unlink” model
can have jcr:removeNode in every access control policy.

-  jcr:write: An aggregate privilege that contains:

   -  jcr:modifyProperties

   -  jcr:addChildNodes

   -  jcr:removeNode

   -  jcr:removeChildNodes

-  jcr:readAccessControl: The privilege to read the access control
   settings of a node.

-  jcr:modifyAccessControl: The privilege to modify the access control
   settings of a node.

-  jcr:lockManagement: The privilege to lock and unlock a node (see §17
   *Locking*).

-  jcr:versionManagement: The privilege to perform versioning operations
   on a node (see §15 *Versioning*).

-  jcr:nodeTypeManagement: The privilege to add and remove mixin node
   types and change the primary node type of a node (see §10.10 *Node
   Type Assignment*).

-  jcr:retentionManagement: The privilege to perform retention
   management operations on a node (see §20 *Retention and Hold*).

-  jcr:lifecycleManagement: The privilege to perform lifecycle
   operations on a node (see §18 *Lifecycle Management*).

-  jcr:all: An aggregate privilege that contains:

   -  jcr:read

   -  jcr:write

   -  jcr:readAccessControl

   -  jcr:modifyAccessControl

   -  jcr:lockManagement

   -  jcr:versionManagement

   -  jcr:nodeTypeManagement

   -  jcr:retentionManagement

   -  jcr:lifecycleManagement

Whether a privilege is abstract is an implementation variant, with the
exception that jcr:all is never an abstract privilege. For example, a
repository unable to separately control the abilities to add child
nodes, remove child nodes, and set properties could make
jcr:modifyProperties, jcr:addChildNodes, and jcr:removeChildNodes
abstract privileges within the aggregate privilege jcr:write.

Similarly, whether any one of these privileges is aggregate is an
implementation variant, with the exception that jcr:write and jcr:all
are always aggregate privileges.

A repository should also add all implementation-defined privileges to
jcr:all.

The standard privilege names are defined as expanded form JCR names in
string constants of javax.jcr.security.Privilege.

16.2.4 Supported Privileges
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The privileges available for a particular node can be determined through

| Privilege[]
|  AccessControlManager.
|  getSupportedPrivileges(String absPath)

where absPath is the location of the node. Note that this method does
not return the privileges *held* by a Session with respect to the
specified node, but rather the privileges *supported* by the repository
with respect to that node (see §16.3.7 *Testing Privileges*).

16.2.5 Retrieving Privileges by Name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Privilege object can be obtained from the AccessControlManager through

| Privilege
|  AccessControlManager.
|  privilegeFromName(String privilegeName)

where privilegeName identifies an existing Privilege (see §16.3.6
*Privilege Object*). Since the privilege name is a JCR name it may be
passed in either qualified or expanded form (see §3.2.6 *Use of
Qualified and Expanded Names*).

16.2.6 Privilege Object
~~~~~~~~~~~~~~~~~~~~~~~

The characteristics of a Privilege object are exposed through the
following methods:

String Privilege.getName()

returns the name of this privilege. Since the privilege name is a JCR
name it must be returned in qualified form (see §3.2.6 *Use of Qualified
and Expanded Names*).

boolean Privilege.isAbstract()

returns whether the privilege is abstract.

boolean Privilege.isAggregate()

returns whether the privilege is aggregate.

Privilege[] Privilege.getDeclaredAggregatePrivileges().

If this privilege is aggregate, this method returns the privileges
directly contained within it. Otherwise, it returns an empty array.

Privilege[] Privilege.getAggregatePrivileges().

If this privilege is aggregate, this method returns the privileges it
contains, the privileges contained by any aggregate privileges among
those, and so on (i.e., the transitive closure of privileges contained
by the initial privilege). Otherwise, it returns an empty array.

16.2.7 Testing Privileges
~~~~~~~~~~~~~~~~~~~~~~~~~

The method

| boolean AccessControlManager.
|  hasPrivileges(String absPath, Privilege[] privileges)

returns whether the Session has the specified privileges for the node at
absPath. Testing an aggregate privilege is equivalent to testing each
non-aggregate privilege among the set returned by calling
Privilege.getAggregatePrivileges().

The method

Privilege[] AccessControlManager.getPrivileges(String absPath)

returns the privileges the session has for absolute path absPath. The
returned privileges are those for which hasPrivileges would return true.

The set of *privileges* held by a session with respect to a particular
node are the result of

-  access control policies applied using JCR (see §16.4 *Access Control
   Policies*),

-  privilege affecting mechanisms external to JCR, if any.

The set of privileges reported by the privilege test methods reflects
the current net *effect* of these mechanisms. It does not reflect
unsaved access control policies.

16.3 Access Control Policies
----------------------------

The privileges granted to a user can be controlled by assigning *access
control policies* to nodes. The content and semantics of these policies
are implementation specific and may be based on any mechanism, including
access control lists or role-responsibility assignments. JCR does not
expose the internals of policies, nor does it provide a mechanism for
defining them. However, it does provide a marker interface
AccessControlPolicy and two derived interfaces NamedAccessControlPolicy
and AccessControlList (see §16.6 *Access Control Lists*). Furthermore,
JCR provides means to:

-  Find which polices are available to be bound to a node.

-  Bind a policy to a node.

-  Get the policies bound to a given node (including transient
   modifications).

-  Get the policies that affect access to a given node.

-  Unbind a policy from a node.

In addition to these methods, any *effect* that a policy has on a node
is always reflected in the information returned by the privilege
discovery methods (see §16.2.7 *Testing Privileges*). Note that the
*scope* of the effect of an access control policy may not be identical
to the node to which that policy is bound (see §16.4.2 *Binding a Policy
to a Node*).

16.3.1 Applicable Policies
~~~~~~~~~~~~~~~~~~~~~~~~~~

| AccessControlPolicyIterator
|  AccessControlManager.getApplicablePolicies(String absPath)

returns a list of access control policies that are capable of being
applied to the node at absPath. The mechanism for defining the set of
policies applicable to a particular node is implementation-dependent.
For a given node, the set of applicable policies available at a specific
time may depend on the set of policies bound to the node at that time.
Therefore, the set returned by this method may vary between calls as
policies are bound and unbound.

16.3.2 Binding a Policy to a Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The method

| void AccessControlManager.
|  setPolicy(String absPath, AccessControlPolicy policy)

binds a policy to the node at absPath. The behavior of the call

acm.setPolicy(absPath, policy)

differs depending on how the policy object was originally acquired. If
policy was acquired through

acm.getApplicablePolicies(absPath)

then policy is added to the node at absPath. On the other hand, if
policy was acquired through

acm.getPolicies(absPath)

then that policy object (after, presumably, being altered) replaces its
older version on the node at absPath (see §16.3.4 *Getting the Bound
Policies*)

16.3.3 Binding vs. Effect
~~~~~~~~~~~~~~~~~~~~~~~~~

A policy is *bound* to a node upon completion of the setPolicy call but
only *takes* *effect* upon Session.save.

16.3.4 Getting the Bound Policies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The method

| AccessControlPolicy[]
|  AccessControlManager.getPolicies(String absPath)

returns the policies bound to the node at absPath. If this method is
called from the AccessControlManager of a Session which holds pending,
unsaved policy bindings, then the policies returned will reflect the
transient state instead of the persisted state. If there are no policies
bound to the node at absPath through the JCR API this method returns an
empty array.

16.3.5 Scope of a Policy
~~~~~~~~~~~~~~~~~~~~~~~~

When an access control policy takes effect, it may affect the
accessibility characteristics not only of the node to which it is bound
but also of nodes elsewhere in the
workspace.\ :sup:``:sup:`20` <#sdfootnote20sym>`__` The method

| AccessControlPolicy[]
|  AccessControlManager.getEffectivePolicies(String absPath)

performs a best-effort search to determine the policies in effect on the
node at absPath.

16.3.6 Default Access Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a node has no effective policy assigned through the JCR API, then an
implementation-specific default policy must be in effect and this policy
must be returned by AccessControlManager.getEffectivePolicies. The
default privileges for the node are determined by the implementation in
accordance with this default policy.

16.3.7 Removing a Policy
~~~~~~~~~~~~~~~~~~~~~~~~

The method

| void AccessControlManager.
|  removePolicy(String absPath, AccessControlPolicy policy)

removes the specified AccessControlPolicy from the node at absPath. An
AccessControlPolicy can only be removed if it was previously bound to
the specified node through this API. The effect of the removal only
takes place upon Session.save().

16.3.8 Interaction with the Transient Layer and Transactions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Changes to access control are session-write operations (see §10.1.1
*Session-Write*) and interact with the transient layer and persistent
store no differently than other such operations:

-  A node which has had a policy set or removed is marked as modified
   until the changes are saved.

-  The access control modifications can be reverted by calling
   Session.refresh(false).

-  The changes are visible to sessions other than the session making the
   change *no earlier than* its being dispatched (i.e., saved if outside
   a transaction, committed if within a transaction).

-  Depending on the repository implementation, the changes may not be
   reflected in another session until that session reacquires the
   modified node (for example, by calling Session.refresh).

16.3.9 Access to Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access to a property is controlled by the effective access control
policies of its parent node.

16.3.10 Access Control Restrictions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A repository may restrict which nodes may be access controlled. For
example a document-centric repository might allow only nt:hierarchyNode
nodes to be access controlled. A repository may automatically add access
control policies to a newly created node based upon an
implementation-determined default.

16.3.11 Exposing Policies in Content
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A repository may expose a node's access control policies as child nodes
or properties. If it does so, then the add, remove and save semantics of
the item must match those of the policy it represents.

16.3.12 Interaction with Protected Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many features of JCR expose repository metadata as protected properties
defined by mixin node types. For example, locking status is exposed by
the properties jcr:lockOwner and jcr:lockIsDeep defined by mix:lockable.
Changes to protected properties can only be made indirectly through a
feature-specific API (for example, Node.lock), not through a generic
write method like Node.setProperty. Such changes *are not* governed by
the jcr:modifyProperties privilege, but rather by the particular
feature-specific privilege, for example, jcr:lockManagement (see §16.2.3
*Standard Privileges*).

16.3.13 Interaction with Versioning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JCR does not mandate a specific approach to access control of versioning
nodes. Whatever approach is taken, any restrictions placed on operations
as a consequence of access control are *in addition* to the restrictions
imposed by the versioning feature itself (for example, checked-in nodes
being immutable).

16.4 Named Access Control Policies
----------------------------------

The NamedAccessControlPolicy extends the AccessControlPolicy marker
interface. A NamedAccessControlPolicy represents an opaque, immutable
policy with a name, which must be a JCR name. The name is accessed
through

String NamedAccessControlPolicy.getName().

16.5 Access Control Lists
-------------------------

AccessControlList extends the AccessControlPolicy marker interface. An
AccessControlList represents a list of AccessControlEntry objects.
Before being bound to a node, the AccessControlList is mutable.

16.5.1 Access Control Entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An AccessControlEntry represents the association of one or more
javax.jcr.security.Privilege objects with a specific
java.security.Principal. These are accessed through

Privilege[] AccessControlEntry.getPrivileges()

and

java.security.Principal AccessControlEntry.getPrincipal().

16.5.2 Getting the Access Control Entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AccessControlEntry[] AccessControlList.getAccessControlEntries()

returns all access control entries present on the AccessControlList
policy. It reflects the current state of the policy including
modifications that have not yet been persisted.

16.5.3 Adding an Access Control Entry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| boolean AccessControlList.addAccessControlEntry(
|  java.security.Principal prinicipal,
|  Privilege[] privileges)

adds an access control entry consisting of the specified principal and
the specified privileges to the AccessControlList policy and returns
true if the AccessControlList was thereby modified.

How the entries are grouped within the list is implementation-specific.
An implementation may, for example, combine the specified privileges
with those added by a previous call to addAccessControlEntry for the
same Principal. However, a call to addAccessControlEntry for a given
Principal can never remove a Privilege added by a previous call.

16.5.4 Removing an Access Control Entry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| void AccessControlList.
|  removeAccessControlEntry(AccessControlEntry ace)

removes the specified AccessControlEntry from the AccessControlList
policy. This method is guaranteed to affect only the privileges of the
principal defined within the specified AccessControlEntry. Only exactly
those entries obtained from AccessControlList.getAccessControlEntries
can be removed through this API.

16.5.5 Modification vs. Effect
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An access control entry is added to or removed from an AccessControlList
upon completion of the addAccessControlEntry or removeAccessControlEntry
call, respectively. However, those modifications only *take* *effect*
once the policy has been bound to a node through
AccessControlManager.setPolicy and saved.

16.5.6 Privileges to Manage Entries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The user must have the jcr:modifyAccessControl **** privilege to add or
remove access control entries and the jcr:readAccessControl privilege to
read access control entries from an AccessControlList.

16.5.7 Principal Discovery
~~~~~~~~~~~~~~~~~~~~~~~~~~

The discovery of java.security.Principals is outside the scope of this
specification.

16.6 Privileges Permissions and Capabilities
--------------------------------------------

In JCR, the terms *privilege*, *permission* and *capability* have
precise and distinct meanings.

16.6.1 Privileges
~~~~~~~~~~~~~~~~~

The set of *privileges* held by a session with respect to a particular
node are the result of access control policies applied using JCR and any
other privilege affecting mechanisms external to JCR that may exist, if
any.

16.6.2 Permissions
~~~~~~~~~~~~~~~~~~

Testing for *permissions* is a feature that all repositories must
support regardless of whether they support access control management.

In repositories that do support access control management, the
permissions encompass the restrictions imposed by privileges, but also
include any additional policy-internal refinements with effects too
fine-grained to be exposed through privilege discovery. A common case
may be to provide finer-grained access restrictions to individual
properties or child nodes of the node to which the policy applies.

In the case of a policy that does not define any refinements, testing
privileges is equivalent to using these methods with the following
mapping:

+-------------------------+------------------------------------------+----------------------------------------------+------------------------------------------------------------------------+----------------------------------------------+--------------------+----------------------------------+
| **The action**          | add\_node                                | set\_property                                | remove                                                                 | remove                                       | read               | read                             |
|                         |                                          |                                              |                                                                        |                                              |                    |                                  |
| **on** ***I,*** **a**   | node                                     | property                                     | node                                                                   | property                                     | node               | property                         |
|                         |                                          |                                              |                                                                        |                                              |                    |                                  |
| **is equivalent to**    | jcr:addChildNode on the parent of *I*.   | jcr:modifyProperties on the parent of *I*.   | jcr:removeChildNodes on the parent of *I* and jcr:removeNode on *I*.   | jcr:modifyProperties on the parent of *I*.   | jcr:read on *I*.   | jcr:read on the parent of *I.*   |
+-------------------------+------------------------------------------+----------------------------------------------+------------------------------------------------------------------------+----------------------------------------------+--------------------+----------------------------------+

16.6.3 Capabilities
~~~~~~~~~~~~~~~~~~~

*Capabilities* encompass the restrictions imposed by permissions, but
also include any further restrictions unrelated to access control. These
include constraints enforced by node types, versioning or any other JCR
or implementation-specific mechanism. Capabilities are reported by
Session.hasCapability (see §9.2 *Capabilities*). The reporting of
capabilities is always subject to practical limitations, but should be
as accurate as possible, given the design of the implementation.
