========================================================================
JCR 2.0: 15 Versioning (Content Repository for Java Technology API v2.0)
========================================================================

15 Versioning
=============

A repository may support *simple versioning* or *full versioning*. This
section describes the syntax and behavior of the Java API for both types
of versioning. Details on the underlying concepts, data structures and
node types can be found in §3.13 *Versioning Model*.

Whether an implementation supports simple versioning can be determined
by querying the repository descriptor table with

Repository.OPTION\_SIMPLE\_VERSIONING\_SUPPORTED.

Whether it supports full versioning can be determined by querying

Repository.OPTION\_VERSIONING\_SUPPORTED.

A return value of true indicates support (see §24.2 *Repository
Descriptors*).

15.1 Creating a Versionable Node
--------------------------------

A new versionable node is created by assigning it the appropriate mixin
type: mix:simpleVersionable under simple versioning or mix:versionable
under full versioning. This may be done either to an existing node,
through a Node.addMixin or at node creation, through assignment of a
primary type that inherits from the mixin. Some repositories may also
automatically assign a versionable mixin on creation of certain nodes
(see §3.7.6 *Node Type Inheritance* and §10.10 *Node Type Assignment*).

Under both simple and full versioning, on persist of a new versionable
node N that neither corresponds nor shares with an existing node:

-  The jcr:isCheckedOut property of N is set to true and

-  A new VersionHistory (H) is created for N. H contains one Version,
   the root version (V:sub:`0`) (see §3.13.5.2 *Root Version*).

Additionally, under full versioning:

-  A new nt:versionHistory node is created and bound to the
   VersionHistory object H .

   -  The jcr:versionableUuid property of H is set to the identifier of
      N.

   -  If N is the result of a copy operation then the jcr:copiedFrom
      property of H is set as described in §15.1.4 *Copying Versionable
      Nodes and Version Lineage*. Otherwise this property is not added.

   -  A new nt:versionLabels node (L) is created as the
      jcr:versionLabels child node of H.

   -  A new nt:version node is created and bound to V\ :sub:`0`. This
      node becomes the jcr:rootVersion child node of H.

      -  A new nt:frozenNode node (F) is created as the jcr:frozenNode
         child node of V\ :sub:`0`. F does not hold any state
         information about N except the node type and identifier
         information found in jcr:frozenPrimaryType,
         jcr:frozenMixinTypes, and jcr:frozenUuid properties (see
         §3.13.4 *Frozen Nodes*).

-  The REFERENCE property jcr:versionHistory of N is initialized to the
   identifier of H. This constitutes a reference from N to its version
   history.

-  The REFERENCE property jcr:baseVersion of N is initialized to the
   identifier of V\ :sub:`0`. This constitutes a reference from N to its
   current base version.

-  The multi-value REFERENCE property jcr:predecessors of N is
   initialized to contain a single identifier, that of V\ :sub:`0` (the
   same as jcr:baseVersion).

15.1.1 VersionHistory Object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The version history of a versionable node is represented by a
VersionHistory object acquired through

VersionHistory Node.getVersionHistory()

or

| VersionHistory
|  VersionManager.getVersionHistory(String absPath)

where absPath is the absolute path to the node.

Conversely, given a VersionHistory, the versionable node to which it
belongs can be found through

String VersionHistory.getVersionableIdentifier()

which returns the identifier of the versionable node, which can then be
used to get the node itself (see §5.1.4 *Getting a Node by Identifier*).

15.1.1.1 Root Version
^^^^^^^^^^^^^^^^^^^^^

The root version of a version history is accessed through

Version VersionHistory.getRootVersion().

Under full versioning the root version can also be accessed through a
Node.getNode or an equivalent standard content access method, since it
also exists as an nt:version child node of the nt:versionHistory node,
called jcr:rootVersion.

15.1.1.2 Versions
^^^^^^^^^^^^^^^^^

The full set of versions within a version history can be retrieved
through

VersionIterator VersionHistory.getAllVersions().

If the version graph of this history is linear then the versions are
returned in order of creation date, from oldest to newest. Otherwise the
order of the returned versions is implementation-dependent.

Alternatively, the method

VersionIterator VersionHistory.getAllLinearVersions()

returns an iterator over all the versions in the *line of descent* from
the root version to the base version that is bound to the workspace
through which this VersionHistory was acquired.

Within a version history H, B is the base version bound to workspace W
if and only if there exists a versionable node N in W whose version
history is H and B is the base version of N.

The line of descent from version V\ :sub:`1` to V\ :sub:`2`, where
V\ :sub:`2` is an eventual successor of V\ :sub:`1`, is the ordered list
of versions starting with V\ :sub:`1` and proceeding through each direct
successor to V\ :sub:`2`.

The versions are returned in order of creation date, from oldest to
newest.

Note that in a simple versioning repository the behavior of this method
is equivalent to returning all versions in the version history in order
from oldest to newest.

Versions can also be retrieved directly by name, using

Version VersionHistory.getVersion(String versionName),

or by label, using,

Version VersionHistory.getVersionByLabel(String label)

(see §15.4 *Version Labels*).

15.1.1.3 Frozen Nodes
^^^^^^^^^^^^^^^^^^^^^

The frozen nodes within each of the versions within the history can be
accessed directly from the VersionHistory through

NodeIterator VersionHistory.getAllFrozenNodes() and

NodeIterator VersionHistory.getAllLinearFrozenNodes().

These methods return the frozen nodes within the version history
corresponding to, and in the same order as, the Version objects returned
by VersionHistory.getAllVersions and
VersionHistory.getAllLinearVersions, respectively.

15.1.1.4 VersionHistory Extends Node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The VersionHistory interface extends Node. Under simple versioning
version histories are not represented by nodes in content, so the
methods inherited from Node are not required to function and may instead
throw a RepositoryException. Under full versioning the VersionHistory
object represents the corresponding nt:versionHistory node and its Node
methods must function accordingly.

15.1.2 Getting the Base Version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The method

Version VersionManager.getBaseVersion(String absPath)

returns the current base version of the versionable node at absPath.

15.1.3 Moving Versionable Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When an existing versionable node is moved to a new location with
Workspace.move or Session.move, it maintains the same version history
and no changes are made to that history.

15.1.4 Copying Versionable Nodes and Version Lineage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under both simple and full versioning, when an existing versionable node
N is copied to a new location either in the same workspace or another,
and the repository preserves the versionable mixin (see §10.7.4
*Dropping Mixins on Copy*):

-  A copy of N, call it M, is created, as usual.

-  A new, empty, version history for M, call it H\ :sub:`M`, is also
   created.

Under full versioning:

-  The properties jcr:versionHistory, jcr:baseVersion and
   jcr:predecessors of M are not copied from N but are initialized as
   usual.

-  The jcr:copiedFrom property of H\ :sub:`M` is set to point to the
   base version of N.

15.1.4.1 Version Lineage
^^^^^^^^^^^^^^^^^^^^^^^^

The jcr:copiedFrom property allows an application to determine the
*lineage* of a version across version histories that were produced by
copying a versionable node to a new location.

15.1.5 Cloning Versionable Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under both simple and full versioning, when a versionable node N is
cloned to another workspace:

-  A clone of N, call it N’, is created, as usual.

-  N’ is initialized to have the same version history and base version
   as N.

Under full versioning:

-  The jcr:versionHistory, jcr:baseVersion and jcr:predecessors
   properties of N are copied to N’ unchanged.

15.1.6 Sharing Versionable Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under both simple and full versioning, when a new node N’ is added to
the shared set of a shareable, versionable node N:

-  The shared node N’ is created, as usual.

-  N’ is initialized to have the same version history and base version
   as N. Unlike in the case of cloning (see §15.1.5 *Cloning Versionable
   Nodes*) the base versions of N and N’ will always remain identical.

Under full versioning:

-  Because nodes in the same shared set have identical properties,
   mix:versionable nodes in the same shared set will necessarily have
   identical jcr:versionHistory, jcr:baseVersion and jcr:predecessors
   properties.

15.2 Check-In: Creating a Version
---------------------------------

A new *version* of a versionable node is created using

Version VersionManager.checkin(String absPath)

where absPath is the absolute path of the node.

On check-in of a versionable node N with version history H:

-  If N is not mix:simpleVersionable or mix:versionable, an
   UnsupportedRepositoryOperationException is thrown, otherwise,

-  if N has unsaved changes pending, an InvalidItemStateException is
   thrown, otherwise,

-  if N is already *checked-in*, this method has no effect and returns
   the *base version* (see §3.13.6.2 *Base Version*) of N, otherwise,

-  if N has a jcr:mergeFailed property present, a VersionException is
   thrown (notice that this is enforced in any case due to the ABORT
   setting of the jcr:mergeFailed property's OnParentVersion attribute).

Otherwise:

-  The subgraph rooted at N is made *read-only* (see §15.2.2 *Read-Only
   on Check-In*).

-  A new Version, V, is created with a system-determined *version name*
   (see §15.2.1.1 *Version Name*) and a *created date* (see §15.2.1.2
   *Created Date*) as part of its state. Under full versioning, a new
   nt:version node is bound to V and added as a child node of H, with
   the version name as its node name and the created date as the value
   of its jcr:created property.

-  The *versionable state* of N is recorded in the *frozen node* F of V
   as described in §3.13.9 *Versionable State*. Under full versioning, F
   is added as the jcr:frozenNode child node of V.

-  V is added to the version history of N as the direct successor of the
   *base version* of N. Under full versioning:

   -  The jcr:predecessors property of N is copied to the
      jcr:predecessors property of V.

   -  The jcr:predecessors property of N is set to the empty array.

   -  A reference to V is added to the jcr:successors property of each
      of the nt:version nodes referred to by the jcr:predecessors
      property of V.

-  The base version of N is changed to V. Under full versioning, the
   jcr:baseVersion property of N is changed to refer to V.

-  The jcr:isCheckedOut property of N is set to false. This change is a
   workspace-write and therefore does not require a save.

-  N is now *checked-in*.

-  V is returned.

15.2.1 Version Object
~~~~~~~~~~~~~~~~~~~~~

A version is represented by a Version object.

15.2.1.1 Version Name
^^^^^^^^^^^^^^^^^^^^^

The name given to a version is automatically generated and must be
unique within its version history. How the name is generated is up to
the implementation. The name of a version is retrieved with the method

String Item.getName(),

inherited by Version. Under simple versioning this is the only inherited
method that is required to function (see §15.2.1.7 *Version Extends
Node*).

15.2.1.2 Created Date
^^^^^^^^^^^^^^^^^^^^^

Calendar Version.getCreated()

returns a timestamp indicating the date and time that the version was
created. The precision of the timestamp is implementation-dependent.

15.2.1.3 Containing History
^^^^^^^^^^^^^^^^^^^^^^^^^^^

VersionHistory Version.getContainingHistory()

returns the VersionHistory that contains this Version.

15.2.1.4 Predecessors
^^^^^^^^^^^^^^^^^^^^^

Version[] Version.getPredecessors()

returns the direct predecessors of this Version. Under simple versioning
this set will be at most of size 1. Under full versioning, this set
maybe of size greater than 1, indicating a merge within the version
graph.

The method

Version Version.getLinearPredecessor()

returns the direct predecessor of this Version along the same line of
descent returned by VersionHistory.getAllLinearVersions in the current
workspace (see §3.1.8.2 *Current Session and Workspace*), or null if no
such direct predecessor exists. Note that under simple versioning the
behavior of this method is equivalent to getting the unique direct
predecessor (if any) of this version.

15.2.1.5 Successors
^^^^^^^^^^^^^^^^^^^

Version[] Version.getSuccessors()

returns the direct successors of this Version. Under simple versioning
this set will be at most of size 1. Under full versioning, this set
maybe of size greater than 1, indicating a branch within the version
graph.

The method

Version Version.getLinearSuccessor()

returns the direct successor of this Version along the same line of
descent returned by VersionHistory.getAllLinearVersions in the current
workspace (see §3.1.8.2 *Current Session and Workspace*), or null if no
such direct successor exists. Note that under simple versioning the
behavior of this method is equivalent to getting the unique direct
successor (if any) of this version.

15.2.1.6 Frozen Node
^^^^^^^^^^^^^^^^^^^^

The frozen node of a version is access with

Node Version.getFrozenNode().

Under simple versioning without in-content version store the frozen node
has no parent and therefore methods that depend on a node being within
the workspace tree (Item.getPath(), Item.getParent(), etc.) throw
RepositoryException. Under full versioning a frozen node is the child of
an nt:version within the in-content version store and so has all the
characteristics of a normal node.

15.2.1.7 Version Extends Node
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Version interface extends Node. Under simple versioning, however,
versions are not represented by nodes in content, consequently the
inherited methods, other than Item.getName() (see §15.2.1.1 *Version
Name*), are not required to function. These methods may throw a
RepositoryException. Under full versioning the methods of Version
inherited from Node function on the actual node in content that backs
that version (see §3.13.3.1 *nt:version*).

15.2.2 Read-Only on Check-In
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a versionable node is checked in, it and its subgraph become
*read-only.* The effect of read-only status on a node depends on the
on-parent-version (OPV) status of each of its child items.

When a node N becomes read-only:

-  No property of N can be added, removed or have its value changed
   *unless* it has an *on-parent-version* setting of IGNORE.

-  No child node of N can be added or removed *unless* it has an
   *on-parent-version* setting of IGNORE.

-  Every existing child node of N becomes read-only unless it has an
   *on-parent-version* setting of IGNORE or has an *on-parent-version*
   setting of VERSION and is itself versionable.

These restrictions apply to all methods with the exception of
VersionManager.restore, VersionManager.restoreByLabel (see §15.7
*Restoring a Version*), VersionManager.merge (see §15.9 *Merge*) and
Node.update (see §10.8.3 *Updating Nodes Across Workspaces*). These
operations do not respect checked-in status.

Note that remove of a read-only node is possible, as long as its parent
is not read-only, since removal is an alteration of the parent node.

15.3 Check-Out
--------------

A checked-in node is checked-out using

void VersionManager.checkout(String absPath),

where absPath is the absolute path of the node.

The checked-out state indicates to the repository and other clients that
the latest version of N is “being worked on” and will typically be
checked-in again at some point in the future, thus creating a new
version.

On checkout of a node N:

-  If N is already checked-out, this method has no effect.

-  If N is not versionable, an UnsupportedRepositoryOperationException
   is thrown.

Otherwise,

-  The jcr:isCheckedOut property of N is set to true.

-  N and all nodes and properties in the subgraph of N lose their
   read-only status.

-  Under full versioning, the current value of the jcr:baseVersion
   property of N is copied to the jcr:predecessors property of N.

This method is a workspace-write. There is no need to call save.

15.3.1.1 Testing for Checked-Out Status
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Only the actual versionable node has a jcr:isCheckedOut property,
however, the checked-in read-only effect extends into the subgraph of
the versionable node (see §15.2.2 *Read-Only on Check-In*). The method

**boolean VersionManager.isCheckedOut(String absPath)**

returns false if the node at absPath is read-only due to a check-in
operation. The method returns false otherwise.

Alternatively, the method

boolean Node.isCheckedOut()

can also be used directly on the node in question.

15.3.2 Checkpoint
~~~~~~~~~~~~~~~~~

The method

Version VersionManager.checkpoint(String absPath)

is a shortcut for checkin followed immediately by checkout.

15.4 Version Labels
-------------------

A version label is a JCR name (see §3.2 *Names*) associated with a
version. A version may have zero or more labels. Within a given version
history, a particular label may appear a maximum of once. Labels are
typically used to add application-level information to a stored version.

Under simple versioning labels are added, accessed and removed only
through the version-label-specific API.

Under full versioning version labels are also exposed in content. Each
nt:versionHistory node has a subnode called jcr:versionLabels of type
nt:versionLabels:

15.4.1.1 nt:versionLabels
^^^^^^^^^^^^^^^^^^^^^^^^^

[nt:versionLabels]

- \* (REFERENCE) protected ABORT

< 'nt:version'

Each version label is stored as a REFERENCE property whose name is the
label name and whose target is the nt:version node within the
nt:versionHistory to which the label applies. Dereferencing a label
property is equivalent to calling VersionHistory.getVersionByLabel.

15.4.1.2 Adding a Version Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method

| void VersionHistory.
|  addVersionLabel(String versionName,
|  String label,
|  boolean moveLabel).

adds the specified label to the version with the specified versionName.
The label must be a JCR name in either qualified or expanded form and
therefore must conform to the syntax restrictions that apply to such
names. In particular a colon (“:”) should not be used unless it is
intended as a prefix delimiter in a qualified name (see §3.2.5 *Lexical
Form of JCR Names*).

In a full versioning system, VersionHistory.addVersionLabel adds the
appropriate REFERENCE to the nt:versionLabels node. The addition of a
label is a workspace-write and therefore does not require a save.

If the specified label is already assigned to a version in this history
and moveLabel is true then the label is removed from its current
location and added to the version with the specified versionName. If
moveLabel is false, then an attempt to add a label that already exists
in this version history will throw a LabelExistsVersionException.

15.4.1.3 Testing for a Version Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method

boolean VersionHistory.hasVersionLabel(String label)

returns true if any version in the version history has the given label.
The method

| boolean VersionHistory.hasVersionLabel(Version version,
|  String label)

returns true if the specified version has the specified label.

15.4.1.4 Getting Version Labels
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method

String[] VersionHistory.getVersionLabels()

returns all the version labels on all the versions in the version
history. The method

String[] VersionHistory.getVersionLabels(Version version)

returns all version labels on the specified version.

15.4.1.5 Removing a Version Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method

void VersionHistory.removeVersionLabel(String label)

removes the specified label from this version history.

In a full versioning system, VersionHistory.removeVersionLabel removes
the appropriate REFERENCE from the nt:versionLabels. The change is a
workspace-write and therefore does not require a save.

15.5 Searching Version Histories
--------------------------------

In simple versioning, version histories are not searchable from within
the JCR API. In order to make version histories searchable under JCR,
version storage must be exposed in content. Since simple versioning
repositories *may* expose version storage (it is simply not *required*),
searchable versions are effectively an optional extension of simple
versioning (see §3.13.7 *Version Storage* and §6 *Query*).

Under full versioning, the exposure of version storage as content in the
workspace allows the stored versions and their associated version
meta-data to be searched or traversed just like any other part of the
workspace.

15.6 Retrieving Version Storage Nodes
-------------------------------------

When an nt:versionHistory or nt:version node is acquired through a query
or directly through a getNode, the actual Java type of the returned
object must be VersionHistory (in the case nt:versionHistory nodes) or
Version (in the case of nt:version nodes). This allows the application
to cast the returned object to either Version or VersionHistory and use
it in methods that take those types.

15.7 Restoring a Version
------------------------

Restoring a versionable node to the state recorded in an earlier version
can be done with

| void VersionManager.restore (Version version,
|  boolean removeExisting).

Given a version V and a boolean flag B, and letting N be the versionable
node in this workspace of which V is a version and F be the frozen node
of V, on restore(V, B), if N has unsaved changes pending, an
InvalidItemStateException is thrown, otherwise:

15.7.1 Simple vs. Full Versioning Before Restore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under simple versioning, if N is checked-in then it is automatically
checked-out before the restore is performed.

Under full versioning the restore methods work regardless of whether the
node in question is checked-out or checked-in.

Under both simple and full versioning, the changes are made through
workspace-write and therefore do not require save.

15.7.2 Restoring Type and Identifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The primary type, mixin types and identifier of N are set as follows:

-  The jcr:primaryType property of N (and, semantically, the actual
   primary node type of N) is set to the value recorded in the
   jcr:frozenPrimaryType of F.

-  The jcr:mixinTypes property of N (and, semantically, the actual mixin
   node types of N) is set to the value(s) recorded in the
   jcr:frozenMixinTypes of F.

-  The jcr:uuid property of N (and, semantically, the actual identifier
   of N) is set to the value recorded in the jcr:frozenUuid of F.

15.7.3 Restoring Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each property P present on F (other than jcr:frozenPrimaryType,
jcr:frozenMixinTypes and jcr:frozenUuid):

-  If P has an OPV of COPY or VERSION then F/P is copied to N/P,
   replacing any existing N/P.

-  F will never have a property with an OPV of IGNORE, INITIALIZE,
   COMPUTE or ABORT (see §15.2 *Check-In: Creating a Version*).

For each property P present on N but not on F:

-  If P has an OPV of COPY, VERSION or ABORT then N/P is removed. Note
   that while a node with a child item of OPV ABORT cannot be versioned,
   it is legal for a previously versioned node to have such a child item
   added to it and then for it to be restored to the state that it had
   before that item was added, as this step indicates.

-  If P has an OPV of IGNORE then no change is made to N/P.

-  If P has an OPV of INITIALIZE then, if N/P has a default value
   (either defined in the node type of N or implementation-defined) its
   value is changed to that default value. If N/P has no default value
   then it is left unchanged.

-  If P has an OPV of COMPUTE then the value of N/P may be changed
   according to an implementation-specific mechanism.

15.7.4 Identifier collision
~~~~~~~~~~~~~~~~~~~~~~~~~~~

An identifier collision occurs when a node exists outside the subgraph
rooted at A with the same identifier as a node that would be introduced
by the restore operation. The result in such a case is governed by the
removeExisting flag. If removeExisting is true, then the incoming node
takes precedence, and the existing node (and its subgraph) is removed
(if possible; otherwise a RepositoryException is thrown). If
removeExisting is false, then an ItemExistsException is thrown and no
changes are made.

15.7.5 Chained Versions on Restore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each child node C of N where C has an OPV of VERSION and C is
mix:versionable, is represented in F not as a copy of N/C but as special
node containing a reference to the version history of C. On restore, the
following occurs.

-  If the workspace currently has an already existing node corresponding
   to C’s version history and the removeExisting flag of the restore is
   set to true, then that instance of C becomes the child of the
   restored N.

-  If the workspace currently has an already existing node corresponding
   to C’s version history and the removeExisting flag of the restore is
   set to false then an ItemExistsException is thrown.

-  If the workspace does not have an instance of C then one is restored
   from C’s version history:

   -  If the restore was initiated through a restoreByLabel where L is
      the specified label and there is a version of C with the label L
      then that version is restored.

   -  If the version history of C does not contain a version with the
      label L or the restore was initiated by a method call that does
      not specify a label then the workspace in which the restore is
      being performed will determine which particular version of C will
      be restored. This determination depends on the configuration of
      the workspace and is outside the scope of this specification.

15.7.6 Restoring Child Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For each child node C present on F:

-  If C has an OPV of COPY or VERSION:

   -  B is true, then F/C and its subgraph is copied to N/C, replacing
      any existing N/C and its subgraph *and* any node in the workspace
      with the same identifier as C or a node in the subgraph of C is
      removed.

   -  B is false, then F/C and its subgraph is copied to N/C, replacing
      any existing N/C and its subgraph *unless* there exists a node in
      the workspace with the same identifier as C, or a node in the
      subgraph of C, in which case an ItemExistsException is thrown ,
      all changes made by the restore are rolled back leaving N
      unchanged.

Under full versioning each child node C of N where C has an OPV of
VERSION and C is versionable, is represented in F not as a copy of N/C
but as special node of type nt:versionedChild containing a reference to
the version history of C. On restore, N/C in the workspace is replaced
by a version of C. The determination of which version of C to use is
implementation-dependent (see §15.7.5 *Chained Versions on Restore*).

In a repository that supports orderable child nodes, the relative
ordering of the set of child nodes C that are copied from F is
preserved.

-  F will never have a child node with an OPV of IGNORE, INITIALIZE,
   COMPUTE or ABORT (see §15.2 *Check-In: Creating a Version*).

For each child node C present on N but not on F:

-  If C has an OPV of COPY, VERSION or ABORT then N/C is removed. Note
   that while a node with a child item of OPV ABORT cannot be versioned,
   it is legal for a previously versioned node to have such a child item
   added to it and then for it to be restored to the state that it had
   before that item was added, as this step indicates.

-  If C has an OPV of IGNORE then no change is made to N/C.

-  If C has an OPV of INITIALIZE then N/C is re-initialized as if it
   were newly created, as defined in its node type.

-  If C has an OPV of COMPUTE then N/C may be re-initialized according
   to an implementation-specific mechanism.

15.7.7 Simple vs. Full Versioning after Restore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under simple versioning N is automatically checked-in.

Under full versioning the jcr:isCheckedOut property of N is set to false
(though the other elements of a check-in are not performed).
Additionally, the jcr:baseVersion property of N is set to V. Note that
after the next check-out (see §15.3 *Check-Out*) and subsequent check-in
of N the version V will acquire an additional direct successor, forming
a branch.

15.7.8 Restore Variants
~~~~~~~~~~~~~~~~~~~~~~~

The method

| void VersionManager.restore(String absPath,
|  Version version,
|  boolean removeExisting)

takes the Version object and a target path. This method only works in
cases where no node exists at absPath. It is used to restore nodes that
have been removed or to introduce new subgraphs into a workspace based
on state stored in a version.

15.7.8.1 Restore by Version Name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method

| void VersionManager.restore(String absPath,
|  String versionName,
|  boolean removeExisting)

takes a version name instead of the actual Version object. The version
to be restored is identified by name from within the version history of
the node at absPath. This method requires that the node at absPath exist
and be a versionable node.

15.7.8.2 Restore by Version Label
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method

| void VersionManager.restoreByLabel(String absPath,
|  String versionLabel,
|  boolean removeExisting)

takes a version label instead of a Version object (see §15.2.1 *Version
Object*). The version to be restored is identified by label from within
the version history of the node at absPath. This method requires that
the node at absPath exist and be a versionable node.

15.7.8.3 Restoring a Group of Versions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method

| void VersionManager.
|  restore(Version[] versions, boolean removeExisting)

is used to simultaneously restore multiple versions. This may be
necessary in cases where sequential restoration is impossible due to a
cycle of REFERENCE properties in the nodes to be restored.

15.8 Removing a Version
-----------------------

In some implementations it may be possible to remove versions from
within a version history using VersionHistory.removeVersion. In such
cases the version graph must be automatically repaired so that the
direct successor of the removed version becomes the direct successor of
the direct predecessor of the removed version.

The method

void VersionHistory.removeVersion(String versionName)

removes the named version from this version history and automatically
repairs the version graph. If the version to be removed is V, V's direct
predecessor set is P and V's direct successor set is S, then the version
graph is repaired s follows:

-  For each member of P, remove the reference to V from its direct
   successor list and add references to each member of S.

-  For each member of S, remove the reference to V from its direct
   predecessor list and add references to each member of P.

This change is a workspace-write; there is no need to call save.

15.9 Merge
----------

The method

| NodeIterator VersionManager.
|  merge(String absPath, String srcWorkspace,
|  boolean bestEffort, boolean isShallow)

performs the first step in a *merge* of two corresponding nodes:

The merge method can be called on a versionable or non-versionable node.

Like update, merge does not respect the checked-in status of nodes. A
merge may change a node even if it is currently checked-in.

If this node (the one on which merge is called) does not have a
corresponding node in the indicated workspace, then the merge method
returns quietly and no changes are made.

If isShallow is true and this node, despite having a corresponding node,
is nevertheless non-versionable then the merge method also returns
quietly and no changes are made.

Otherwise, the following happens:

If isShallow is true then a merge test is performed on this node, call
it N. If isShallow is false then a merge test is performed recursively
on each versionable node, N within the subgraph rooted at this node.

The merge test is performed by comparing N with its corresponding node
in srcWorkspace, call it N'.

The merge test is done by comparing *the base version of* N (call it V)
and *the base version of* N' (call it V').

For any versionable node N there are three possible outcomes of the
merge test: *update*, *leave* or *failed*.

If N does not have a corresponding node then the merge result for N is
*leave*.

If N is currently checked-in then:

-  If V' is an eventual successor of V, then the merge result for N is
   *update*.

-  If V' is an eventual predecessor of V or if V and V' are identical
   (i.e., are actually the same version), then the merge result for N is
   *leave*.

-  If V is neither an eventual successor of, eventual predecessor of,
   nor identical with V', then the merge result for N is *failed*. This
   is the case where N and N' represent divergent branches of the
   version graph.

If N is currently checked-out then:

-  If V' is an eventual predecessor of V or if V and V' are identical
   (i.e., are actually the same version), then the merge result for N is
   *leave*.

-  If any other relationship holds between V and V', then the merge
   result for N is *fail*.

If bestEffort is false then the first time a merge result of *fail*
occurs, the entire merge operation on this subgraph is aborted, no
changes are made to the subgraph and a MergeException is thrown. If no
merge result of *fail* occurs then:

-  Each versionable node N with result *update* is updated to reflect
   the state of N'. The state of a node in this context refers to its
   set of properties and child node links.

-  Each versionable node N with result *leave* is left unchanged,
   *unless* *N* *is the child of a node with status* update *and* *N*
   *does not have a corresponding node in* *srcWorkspace, in which case
   it is removed.*

If bestEffort is true then:

-  Each versionable node N with result *update* is updated to reflect
   the state of N'. The state of a node in this context refers to its
   set of properties and child node links.

-  Each versionable node N with result *leave* is left unchanged, unless
   N is the child of a node with status *update* and N does not have a
   corresponding node in srcWorkspace. I such a case, N is removed.

-  Each versionable node N with result *failed* is left unchanged except
   that the identifier of V' (which is, in some sense, the “offending”
   version; the one that caused the merge to fail on that N) is added to
   the multi-value REFERENCE property jcr:mergeFailed of N. If the
   identifier of V' is already in jcr:mergeFailed, it is not added
   again. The jcr:mergeFailed property never contains repeated
   references to the same version. If the jcr:mergeFailed property does
   not yet exist then it is created. If present, the jcr:mergeFailed
   property will always contain at least one value. If not present on a
   node, this indicates that no merge failure has occurred on that node.
   Note that the presence of this property on a node will in any case
   prevent it from being checked-in because the OnParentVersion setting
   of jcr:mergeFailed is ABORT.

-  This property can later be used by the application to find those
   nodes in the subgraph that have failed to merge and thus require
   special attention (see §15.9.2 *Merging Branches*). This property is
   multi-valued so that a record of successive failed merges can be
   kept.

In either case, (regardless of whether bestEffort is true or false) for
each non-versionable node (including both referenceable and
non-referenceable), if the merge result of its *nearest versionable
ancestor* is *update,* or if it has *no versionable ancestor*, then it
is updated to reflect the state of its corresponding node. Otherwise, it
is left unchanged. The definition of corresponding node in this context
is the same as usual: the match is done by identifier.

Note that a deep merge performed on a subgraph with no versionable nodes
at all (or indeed in a repository that does not support versioning in
the first place) will be equivalent to an update.

The merge method returns a NodeIterator over all versionable nodes in
the subgraph that received a merge result of fail.

Note that if bestEffort is false, then merge will either return an empty
iterator (since no merge failure occurred) or throw a MergeException (on
the first merge failure that was encountered).

If bestEffort is true, then the iterator will contain all nodes that
received a fail during the course of this merge operation.

All changes made by merge are workspace-write, and therefore this method
does not require a save.

15.9.1 Merge Algorithm
~~~~~~~~~~~~~~~~~~~~~~

The above declarative description can also be expressed in pseudo-code
as follows:

| let ws' be the workspace against which the merge is done.
| let bestEffort be the flag passed to merge.
| let isShallow be the flag passed to merge.
| let failedset be a set of identifiers, initially empty.
| let startnode be the node on which merge was called.
| domerge(startnode).
| return the nodes with the identifiers in failedset.

| domerge(n)
|  let n' be the corresponding node of n in ws'.
|  if no such n' doleave(n).
|  else if n is not versionable doupdate(n, n').
|  else if n' is not versionable doleave(n).
|  let v be base version of n.
|  let v' be base version of n'.
|  if v' is an eventual successor of v and
| n is not checked-in doupdate(n, n').
|  else if v is equal to or an eventual predecessor of v' doleave(n).
|  else dofail(n, v').

| dofail(n, v')
|  if bestEffort = false throw MergeException.
|  else add identifier of v' (if not already present) to the
| jcr:mergeFailed property of n,
|  add identifier of n to failedset,
|  if isShallow = false
|  for each versionable child node c of n domerge(c).

| doleave(n)
|  if isShallow = false
|  for each child node c of n domerge(c).

| doupdate(n, n')
|  replace set of properties of n with those of n'.
|  let S be the set of child nodes of n.
|  let S' be the set of child nodes of n'.
|  judging by the name of the child node:
|  let C be the set of nodes in S and in S'
|  let D be the set of nodes in S but not in S'.
|  let D' be the set of nodes in S' but not in S.
|  remove from n all child nodes in D.
|  for each child node of n' in D' copy it (and its subgraph) to n
|  as a new child node (if an incoming node has the same
|  identifier as a node already existing in this workspace,
|  the already existing node is removed).
|  for each child node m of n in C domerge(m).

15.9.2 Merging Branches
~~~~~~~~~~~~~~~~~~~~~~~

When a merge test on a node N fails, this indicates that the two base
versions V and V' are on separate branches of the version graph.
Consequently, determining the result of the merge is not simply a matter
of determining which version is the eventual successor of the other in
terms of version history. Instead, the subgraph of N' must be merged
into the subgraph of N according to some domain specific criteria which
must be performed at the application level, for example, through a merge
tool provided to the user.

The jcr:mergeFailed property is used to tag nodes that fail the merge
test so that an application can find them and deal appropriately with
them. The jcr:mergeFailed property is multi-valued so that information
about merge failures is not lost if more than one successive merge is
attempted before being dealt with by the application.

After the subgraph of N' is merged into N, the application must also
merge the two branches of the version graph. This is done by calling
N.doneMerge(V') where V' is retrieved by following the reference stored
in the jcr:mergeFailed property of N. This has the effect of moving the
reference-to-V' from the jcr:mergeFailed property of N to its
jcr:predecessors property.

If, on the other hand, the application chooses not to join the two
branches, then cancelMerge(V') is performed. This has the effect of
removing the reference to V' from the jcr:mergeFailed property of N
without adding it to jcr:predecessors.

Once the last reference in jcr:mergeFailed has been either moved to
jcr:predecessors (with doneMerge) or just removed from jcr:mergeFailed
(with cancelMerge) the jcr:mergeFailed property is automatically
removed, thus enabling this node to be checked-in, creating a new
version (note that before the jcr:mergeFailed is removed, its
OnParentVersion setting of ABORT prevents check-in). This new version
will have a direct predecessor connection to each version for which
doneMerge was called, thus joining those branches of the version graph.

All changes made by doneMerge and cancelMerge are workspace-write and
therefore do not require save.

15.9.3 Merging Activities
~~~~~~~~~~~~~~~~~~~~~~~~~

In repositories that support activities (see §15.12 *Activities*)
merging an activity into another workspace is done with the method

VersionManager.merge(Node activityNode).

(see §15.12.7 *Merging an Activity into Another Workspace*).

15.10 Serialization of Version Storage
--------------------------------------

Serialization of version information can be done in the same way as
normal serialization by serializing the subgraph below
/jcr:system/jcr:versionStorage. The special status of these nodes with
respect to versioning is transparent to the serialization mechanism.

The serialized content of the source version storage can be imported as
“normal” content on the target repository, but it will not actually be
interpreted and integrated into the repository as version storage data
unless it is integrated into or used to replace the target repository's
own version storage.

Methods for doing this kind of “behind the scenes” alteration to an
existing version storage (whether based on the serialized version
storage of another repository, or otherwise) are beyond the scope of
this specification.

15.11 Versioning within a Transaction
-------------------------------------

In a repository that supports both versioning and transactions, all
versioning operations must be fully transactional, meaning that they can
be bracketed within a transaction and rolled-back just like any other
set of operations.

15.12 Activities
----------------

Activities provide a way of grouping together a set of logically related
changes performed in a workspace and then later merging this set of
changes into another workspace.

Before starting to make a particular set of changes, the user sets the
*current activity*. Each subsequent checkout made within the scope of
that activity will associate that activity with that checked-out
versionable, and will create a version that is tagged with the specified
activity when that versionable is subsequently checked-in.

Abstractly, therefore, an activity is a set of changes that produce new
versions. However, if that set includes changes that produce more than
one version within a particular version history, then those versions
must all be on the same line of descent, that is, there must be a
non-branching sequence of direct successor relationships beginning at
the root version of the version history that reaches every version in
the set. This ensures that there is always at most one “latest” version
that contains all changes in a given version history for a given
activity.

15.12.1 Support for Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for activities is an optional addition to the full versioning
feature. An implementation that supports versioning *may* support
activities.

Whether a particular implementation supports activities can be
determined by querying the repository descriptor table with

Repository.OPTION\_ACTIVITIES\_SUPPORTED.

A return value of true indicates support for activities (see §24.2
*Repository Descriptors*).

15.12.2 Related Node Types
~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities are represented by nodes of node type nt:activity:

[nt:activity] > mix:referenceable

- jcr:activityTitle (STRING) **** mandatory autocreated protected

The relationship between version and activity is modeled by the property
jcr:activity, in the mix:versionable and nt:version node types:

| [mix:versionable] > mix:simpleVersionable, mix:referenceable
|  mixin

- jcr:versionHistory (REFERENCE) mandatory protected IGNORE

< 'nt:versionHistory'

- jcr:baseVersion (REFERENCE) mandatory protected IGNORE

< 'nt:version'

- jcr:predecessors (REFERENCE) mandatory protected multiple

IGNORE < 'nt:version'

- jcr:mergeFailed (REFERENCE) protected multiple ABORT

< 'nt:version'

**- jcr:activity (REFERENCE) protected IGNORE < 'nt:activity'**

| - jcr:configuration (REFERENCE) protected IGNORE
|  < 'nt:configuration'

| 

[nt:version] > mix:referenceable

| - jcr:created (DATE) mandatory autocreated protected
|  ABORT

- jcr:predecessors (REFERENCE) protected multiple ABORT

< 'nt:version'

- jcr:successors (REFERENCE) protected multiple ABORT

< 'nt:version'

**- jcr:activity (REFERENCE) protected ABORT < 'nt:activity'**

+ jcr:frozenNode (nt:frozenNode) protected ABORT

15.12.3 Activity Storage
~~~~~~~~~~~~~~~~~~~~~~~~

Activities are persisted as nodes of type nt:activity under
system-generated node names in activity storage below
/jcr:system/jcr:activities.

The organization of this subgraph is left up to the implementation (for
example, there may be intervening nodes structuring the activity
storage).

Similar to the /jcr:system/jcr:versionStorage subgraph, the activity
storage is a single repository wide store, but is reflected into each
workspace. However access control may be employed so that different
sessions see different parts of the tree.

15.12.3.1 Activity Storage is Read-Only
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The activity storage subgraph is not writable through the core write
methods (see §10.2 *Core Write Methods*). It can only be altered through
the activity-specific write methods described in this section.

15.12.4 Creating an Activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Activities are created using:

Node VersionManager.createActivity(String title)

creates a new nt:activity node at an implementation-determined location
in the /jcr:system/jcr:activities subgraph and returns it.

The name of the nt:activity node is automatically generated by the
repository. The repository *may* use the title parameter as a hint to
give a value to the jcr:activityTitle property of the new node. The new
node addition is dispatched immediately and therefore does not require a
save.

15.12.5 Setting the Current Activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Node VersionManager.setActivity(Node activity)

is called by the user to set the current activity on the session by
specifying a previously created nt:activity node. Changing the current
activity is done by calling setActivity again. Cancelling the current
activity is done by calling setActivity(null) and results in the session
having no current activity. The method returns the *previously set*
nt:activity node or null if no such node exists.

Assuming,

-  the current activity of session S is represented by node A and

-  node N is a versionable node with version history H,

then each checkout of node N made through S while A is in effect causes
the following:

-  If there exists another workspace with node N' where N' also has
   version history H, N' is checked out and the jcr:activity property of
   N' references A, then the check-out fails with an
   ActivityViolationException indicating which workspace currently has
   the check-out.

-  If there is a version in H that is not an eventual predecessor of N
   but whose jcr:activity references A, then the check-out fails with an
   ActivityViolationException.

-  Otherwise, the jcr:activity property of N is set to reference A and
   when N is subsequently checked in, the jcr:activity property of the
   new version is set to reference A, and the jcr:activity property of N
   is removed.

15.12.6 Getting the Current Activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The method

Node VersionManager.getActivity()

returns the node representing the current activity or null if there is
no current activity.

15.12.7 Merging an Activity into Another Workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Once an activity has been completed, the changes that it records can be
imported into another workspace. This is done with a variant of the
merge method:

NodeIterator VersionManager.merge(Node activityNode)

This method merges the changes that were made under the specified
activity into this workspace.

An activity A will be associated with a set of versions through the
jcr:activity reference of each version node in the set. We call each
such associated version a member of A.

For each version history H that contains one or more members of A, one
such member will be the latest member of A in H. The latest member of A
in H is the version in H that is a member of A and that has no eventual
successor versions that are also members of A.

The set of versions that are the latest members of A in their respective
version histories is called the change set of A. It fully describes the
changes made under the activity A.

This method performs a shallow merge, with bestEffort equal to true,
into this workspace (see §15.9 *Merge*) of each version in the change
set of the activity specified by activityNode. If there is no
corresponding node in this workspace for a given member of the change
set, that member is ignored.

This method returns a NodeIterator over all versionable nodes in the
subgraph that received a merge result of *fail* (see §15.9.1 *Merge
Algorithm*).

All changes made through this method are workspace-write and therefore
do not require save.

15.12.8 Removing an Activity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some repositories may support

void VersionManager.removeActivity(Node activityNode)

which removes the specified activity node from the activity storage and
automatically removes all REFERENCE properties referring to that node in
all workspaces, with the exception of REFERENCE properties in version
storage. The existence of a REFERENCE to the activity node from within
version storage will cause an exception to be thrown. Changes made
through this method are workspace-write and therefore do not require
save.

15.13 Configurations and Baselines
----------------------------------

A *configuration* is the subgraph of a specifically designated
versionable node (called the *configuration root node*) in a workspace,
minus any parts of that subgraph that are themselves designated as
configurations. A *baseline* is the state of a configuration at some
point in time, recorded in version storage as a version object.

15.13.1 Support for Configurations and Baselines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for configurations and baselines is an optional addition to the
full versioning feature. An implementation that supports full versioning
*may* support configurations and baselines. Whether a particular
implementation supports configurations and baselines can be determined
by querying the repository descriptor table with

Repository.OPTION\_BASELINES\_SUPPORTED.

A return value of true indicates support for configurations and
baselines (see §24.2 *Repository Descriptors*).

15.13.2 Configuration Proxy Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each configuration in a given workspace is represented by a distinct
*proxy node* of type nt:configuration located in *configuration storage*
within the same workspace under /jcr:system/jcr:configurations/. The
configuration storage in a particular workspace is specific to that
workspace. It is not a common repository-wide store mirrored into each
workspace, as is the case with version storage.

The proxy node of a configuration is used to perform certain operations
on that configuration. In particular, version operations performed on
the proxy node act not only on that node itself but also on the
configuration it represents, as a whole. Creating a baseline, for
example, is done by performing a checkin on a configuration’s proxy
node.

15.13.2.1 nt:configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^

Every configuration proxy node is of type nt:configuration:

[nt:configuration] > mix:versionable

- jcr:root (REFERENCE) mandatory autocreated protected

This node type is a subtype of mix:versionable and adds a single
property, the REFERENCE property jcr:root, which points to the root node
of the configuration that this proxy represents.

Since every configuration proxy node is versionable, each has a version
history. The versions within this history store state information about
configuration represented by the proxy node, in addition to information
about the proxy node itself.

15.13.2.2 Structure of Configuration Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The organization of configuration storage is left up to the
implementation (for example, there may be intervening nodes structuring
the storage). It is expected that access control will also be employed
to ensure that only sessions with appropriate authorization may create
or have access to particular configurations.

15.13.3 Creating a Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A configuration is created by designating a mix:versionable node N in
the workspace as a configuration root node. This is done by calling

| Node VersionManager.
|  createConfiguration(String absPath)

where absPath is the path of N.

On creation of a new configuration with root N, a new proxy node C, of
type nt:configuration, is created under /jcr:system/jcr:configurations/
and a new version history H\ :sub:`C` is created for C with a root
version B\ :sub:`0`. Note that H\ :sub:`C` is also called a *baseline
history* and its contained versions, including B\ :sub:`0`, are called
*baselines*. The baselines within H\ :sub:`C` store not only the state
of C but also the state of the configuration represented by C (see
15.13.4.1 *Creating a Baseline*).

The properties of C and N are initialized as follows:

-  N/jcr:configuration points to C.

-  C/jcr:root points to N.

-  C/jcr:versionHistory points to H\ :sub:`C`.

-  C/jcr:baseVersion points to B\ :sub:`0`.

The createConfiguration call will fail if

-  the node at absPath is not mix:versionable.

-  the node at absPath is already a configuration root (i.e., if it
   already has a jcr:configuration property).

-  There exists in the subgraph at N a versionable node that has never
   been checked-in (i.e., one whose base version is still its root
   version).

The createConfiguration method is workspace-write. Therefore the changes
it makes are dispatched immediately and a save is not required.

15.13.4 Baselines
~~~~~~~~~~~~~~~~~

A baseline records the state of a configuration at some particular time
and is represented by a version (i.e., an nt:version node) of the
nt:configuration node in question.

15.13.4.1 Creating a Baseline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A baseline is created by performing a checkin on a configuration proxy
node (i.e., a node of type nt:configuration found in configuration
storage). Note that since nt:configuration is subtype of
mix:versionable, a configuration node will have its own version history,
*distinct from the version history of its configuration root node*.

On checkin of the configuration proxy node C:

-  The state of the C is recorded in a new baseline B just as it would
   be in a normal version.

-  In addition, the current base version of every versionable node in
   the configuration is also recorded.

How the configuration state information is stored is up to the
repository. It need not be stored as content in the substructure of the
nt:version node. For example, some repositories are likely to have some
efficient internal mechanisms involving lists of identifiers, possibly
stated as a delta against the direct predecessor baseline. The only
requirement is that baselines be “restoreable”.

15.13.4.2 Restoring a Baseline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Using the method

VersionManager.restore(Version version, boolean removeExisting)

where version is a baseline Version object, C is the nt:configuration
node whose version history contains version and N is the configuration
root node pointed to by C/jcr:root:

-  The state of C is restored to the state recorded in version and
   C/jcr:baseVersion is set to point to version (as in the restore of
   any normal version).

-  Each versionable node M in the subgraph below and including N is
   restored to the state recorded in V where V is the version of M in
   M’s version history that was recorded in B (i.e., the base version of
   M at the time B was created).

The removeExisting parameter behaves just as in a normal restore expect
that that it applies to all nodes restored below N. The same behavior
applies for the multi-version signature of restore,

| VersionManager.restore(Version[] versions,
|  boolean removeExisting)

except that multiple baselines may be restored simultaneously.

15.13.4.3 Creating a Configuration from an Existing Baseline
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The method

| VersionManager.restore(String absPath,
|  Version version,
|  boolean removeExisting),

where version is a baseline Version object and absPath is a path to a
location where no node exists but which has a suitable parent node,
creates a new configuration at absPath by restoring the baseline
version. A configuration proxy node C with C/jcr:root pointing to the
root node of the new configuration at absPath is automatically created
in configuration storage. If a node already exists at absPath, the
method fails. The variant signatures

| VersionManager.restore(String absPath,
|  String versionName,
|  boolean removeExisting),

and

| VersionManager.restoreByLabel(String absPath,
|  String label,
|  boolean removeExisting),

work identically except that the baseline to be restored is identified
either by name or by label instead of being passed in as a Version
object.
