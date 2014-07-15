===================================================================================
JCR 2.0: 23 Orderable Child Nodes (Content Repository for Java Technology API v2.0)
===================================================================================

23 Orderable Child Nodes
========================

A repository may support *orderable child nodes*, which enables
persistent, client-controlled ordering of a node's child nodes.

Whether a particular implementation supports orderable child nodes can
be determined by querying the repository descriptor table with

Repository.NODE\_TYPE\_MANAGEMENT\_ORDERABLE\_CHILD\_NODES\_SUPPORTED.

A return value of true indicates support for transactions (see
*Repository Descriptors*).

23.1 Scope of Orderable Child Nodes
-----------------------------------

The orderable child nodes setting is defined *per node type*. Whether
the child nodes of a node *N* are orderable depends on the node type of
*N*.

A repository supports orderable child nodes by permitting the
registration of node types with an orderable child node setting of true.
Disallowing orderable child nodes consists in preventing the
availability of such node types.

For a given NodeType T:

-  If T.hasOrderableChildNodes() returns true then *all* nodes with
   primary type *T* *must* have orderable child nodes.

-  If T.hasOrderableChildNodes() returns false then *some* nodes with
   primary type T *may* have orderable child nodes.

Only the primary node type of a node is relevant to the orderable status
of its child nodes. This setting on a mixin node type of a node has no
meaning.

If a node has orderable child nodes then at any time its child node set
has a *current order*, reflected in the iterator returned by
Node.getNodes()(see §5.2.2 *Iterating Over Child Items*). If a node does
not have orderable child nodes then the order of nodes returned by
Node.getNodes is not guaranteed and may change at any time.

23.2 Ordering Child Nodes
-------------------------

If a node has orderable child nodes then their *current order* can be
changed using

| void Node.orderBefore(String srcChildRelPath,
|  String destChildRelPath).

This method moves the child node at srcChildRelPath and inserts it
immediately before its sibling at destChildRelPath in the child node
list. To place the node srcChildRelPath at the end of the list, a
destChildRelPath of null is used.

Apart from the case where destChildRelPath is null, both of these
arguments must be relative paths of depth 1, in other words, they must
be the names of child nodes, possibly suffixed with an index. (see §3.2
*Names* and §3.4 *Paths*).

If srcChildRelPath and destChildRelPath are the identical, then no
change is made.

Changes to the current order are visible immediately through the current
Session and are persisted to the workspace on Session.save.

23.3 Adding a New Child Node
----------------------------

When a child node is added to a node that has orderable child nodes it
is added to the end of the list.

23.4 Orderable Same-Name Siblings
---------------------------------

If a node supports orderable child nodes *and* same-name siblings then
the order of the nodes within a set of same-name siblings must be
persisted and be re-orderable by the client. For example, given the
following initial ordering of child nodes,

[A, B, C, A, D]

a call to

orderBefore(“A[2]”,”A[1]”)

will cause the child node currently called A[2] to be moved to the
position before the child node currently called A[1], the resulting
order will be:

[A, A, B, C, D]

where the first A is the one that was formerly after C and the second A
is the one that was formerly at the head of the list.

Note, however, that after the completion of this operation *the indices
of the two nodes have now switched*, due to their new positions relative
to each other. What was formerly A[2] is now A[1] and what was formerly
A[1] is now A[2].

23.5 Non-orderable Child Nodes
------------------------------

When a node does not support orderable child nodes this means that it is
left up to the implementation to maintain the order of child nodes.
Applications should not, in this case, depend on the order of child
nodes returned by Node.getNodes(), as it may change at any time.

23.6 Properties are Never Orderable
-----------------------------------

Properties are never client orderable, the order in which properties are
returned by Node.getProperties() is always maintained by the
implementation and can change at any time.

|
