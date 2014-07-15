=============================================================================
JCR 2.0: 14 Shareable Nodes (Content Repository for Java Technology API v2.0)
=============================================================================

14 Shareable Nodes
==================

A repository may support *shareable nodes*. This section describes the
syntax and behavior of the Java API for shareable nodes. For details on
the shareable nodes model see §3.9 *Shareable Nodes Model*.

Whether an implementation supports shareable nodes can be determined by
querying the repository descriptor table with

Repository.OPTION\_SHAREABLE\_NODES\_SUPPORTED.

A return value of true indicates support (see §24.2 *Repository
Descriptors*).

14.1 Creation of Shared Nodes
-----------------------------

Cloning a mix:shareable node into the same workspace is the standard way
of creating a shared node.

Given workspace W, and an existing mix:shareable node at /A/B/C, the
call

W.clone(“W”, “/A/B/C”, “/X/Y/Z”, false)

will create a new node at /X/Y/Z that shares with /A/B/C.

Note that if the removeExisting flag is set to true, the Workspace.clone
does not create a shared node, but instead behaves identically to a
Workspace.move.

14.1.1 Shared Node Creation on Restore
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If VersionManager.restore, restoreByLabel, merge or update is called and
this call would create a node with the same identifier as that of an
existing mix:shareable node in the same workspace without at the same
time removing that existing node (that is, removeExisting is set to
false), then the new node is created and is added to the shared set of
the existing mix:shareable node.

14.1.2 Shared Node Creation on Import
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During import the behavior of the IMPORT\_UUID\_COLLISION\_THROW
indicates that if an incoming referenceable node has the same identifier
as an existing mix:shareable node in the workspace, the incoming node is
created and added to the shared set of the existing mix:shareable node
(see §3.9.1 *mix:shareable*). Note that if the import in question is a
Session import (see §11.6.2 *Session Event-Based Import* and §11.7.2
*Session Stream-Based Import*) new shared transient nodes will be
created. These nodes are not considered to be *new*, in the sense that
Node.isNew will return false.

14.2 Shared Set
---------------

The *shared set* of a node consists of all nodes (including itself) with
which it shares. This set is retrieved with

NodeIterator Node.getSharedSet().

14.3 Removing Shared Nodes
--------------------------

The method

void Node.removeShare()

removes the node from its shared set without affecting the other nodes
in the set. The method

void Node.removeSharedSet()

removes the node and all the members of its shared set.

In the first case, assuming more than one member in the shared set, the
children of the removed node are unaffected since they still have at
least one other node as parent. In the second case, however, the
children of the shared set are removed.

In cases where the shared set consists of a single node, or when these
methods are called on a non-shareable node, their behavior is identical
to Node.remove().

When applied to a shared node with at least one other member in its
shared set, the method

void Item.remove or

void Session.removeItem

may behave as Node.removeShare() or as Node.removeSharedSet(). Which
behavior is adopted is an implementation issue.

The behavior of Node.remove() is permitted to vary across repositories
because the details of the underlying implementation will make one or
the other of the behaviors more natural for that repository. In
particular if a repository implements a shared set by one “primary”
parent (that controls the lifetime of the child) and zero or more
“secondary” parents (that reference that child), then Item.remove is
most naturally interpreted differently on the primary parent and one of
the secondary parents. To force that repository to do a Node.removeShare
on the primary parent would require that implementation to pick one of
the secondary parents as the new primary parent, and change all of the
other secondary parents to refer to that new primary parent.

For all three methods, the removal is dispatched on Session.save().

14.4 Transient Layer
--------------------

When a change is made to a shared node in the transient layer,
Node.isModified becomes true and that change is visible in all nodes in
the shared set of that node. After a transient shared node is
dispatched, Node.isModified becomes false for all nodes in the shared
set of that node.

14.5 Copy
---------

The new nodes created by a copy are never in the shared set of any node
that existed before the copy, but if two nodes A and B in the source of
a copy are in the same shared set S, then the two resulting nodes A' and
B' in the destination of the copy must both be in the same shared set
S', where S and S' are disjoint.

14.6 Share Cycles
-----------------

In an implementation that forbids share cycles, any session-write method
that can create a shared node will cause a ShareCycleException to be
thrown either immediately or on save, if persisting the change would
result in a share cycle.

Similarly, any workspace-write method that can create a shared node will
throw a ShareCycleException if completion of the operation would result
in a share cycle.

In an implementation that does not prevent share cycles, checking for
cycles is left to the repository user.

14.7 Export
-----------

When more than one shared node in a given shared set is exported to an
XML document, the first node in that shared set is exported in the
normal fashion (with all of its properties and children), but any
subsequent shared node in that shared set is exported as a special node
of type nt:share, which contains only the jcr:uuid property of the
shared node and the jcr:primaryType property indicating the type
nt:share. Note that nt:share only appears in a serialization document,
and never appears as a node type of a node in a repository.

14.8 Import
-----------

When an XML element with node type nt:share is imported into a
repository that does not support shared nodes, the import must fail
(getImportContentHandler will throw a SAXException, while importXML will
throw an UnsupportedRepositoryOperationException).

14.9 Observation
----------------

When a property of a shared node is modified, or when a child item is
added to or deleted from a shared node, although that property or child
node modification is performed on every node in the shared set of that
node, only one event is fired for the shared set. Which node in the
shared set is identified in the event is implementation-defined.

14.10 Locking
-------------

When a lock is added or removed from a shared node, it is automatically
added or removed from every node in the shared set of that node.

If at least one share-ancestor of a node N holds a deep locked then that
lock applies to N, resulting in N being locked.

14.11 Node Type Constraints
---------------------------

All the nodes in a shared set always have the same declared primary node
type and the same set of assigned mixin node types. Since different
nodes in the shared set may have different parents, those parents must
be of an appropriate node type to have a child of with these types.

If the members of a shared set correspond to child node definitions (in
their respective parents) with conflicting *protected* settings, the
effective protected value of all the members of the shared set will be
the logical OR of the protected settings of the set of child node
definitions.

14.12 Versioning
----------------

If a node is versionable then all nodes within its shared set share the
same version history. Under full versioning this follows logically from
the fact that the nodes all share the same jcr:versionHistory reference
(see §3.13.2.2 *mix:versionable*), pointing to a single common
nt:versionHistory node (see §3.13.5.1 *nt:versionHistory*).

On check-in of a node *N* within the shared set, its versionable state
is determined just as in the non-shared case, but because the node is
shared, the resulting version will also reflect the versionable state of
any node *N'* in the shared set of *N*.

On check-in of a parent *M* of a shared node *N* the contribution of *N*
to the versionable state of *M* is determined according to the OPV of
*N*. Note that the OPV of two nodes *N* and *N*' in the same shared set
(with parent node *M* and *M'*, respectively) may *differ* because the
OPV of *N* is determined by the node type of *M*, while that of *N'* is
determined by the node type of *M'*.

14.13 Restore
-------------

The effect of shared nodes on restore falls into three cases:

-  A restore that causes the creation of a new shared node (see §14.1.1
   *Shared Node Creation on Restore*).

-  A restore that causes the removal of a shared node: In this case the
   particular shared node is removed but its descendants continue to
   exist below the remaining members of the shared set.

-  A restore causes a change to the state of a shared node: Any change
   is reflected in all nodes in its shared set.

-  A restore that causes a change below a shared node: The subgraph is
   changed as usual and the change is visible through many paths.

14.14 IsSame
------------

If node /a/b shares with node /a/c then these two nodes are considered
“the same” according to the Item.isSame() method. Additionally, if the
shared nodes have a property p, then /a/b/p and /a/c/p are also
considered “the same”. If they have a child node x then, similarly,
/a/b/x and /a/c/x are also the “the same”.

14.15 RemoveMixin
-----------------

If an attempt is made to remove the mix:shareable mixin node type from a
node in a shared set the implementation may either throw a
ConstraintViolationException or allow the removal and change the
subgraph in some implementation-specific manner. One possibility is to
replace the node with a copy that has no children (if this does not
violate the node type restrictions of that node). Another possibility is
to give the node a copy of all of its descendants (unless the resulting
copy operation would be unfeasible, as would be the case if a share
cycle were involved).

14.16 Query
-----------

If a query matches two or more nodes in a shared set, whether all of
these nodes or just one is returned in the query result is an
implementation issue.

This variability is allowed since different implementations might have
different “natural” behaviors, and it would be expensive for an
implementation to compute the answer that is “unnatural” for that
implementation.

If a query matches a descendant node of a shared set, it appears in
query results only once.
