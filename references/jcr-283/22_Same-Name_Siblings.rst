================================================================================
JCR 2.0: 22 Same-Name Siblings (Content Repository for Java Technology API v2.0)
================================================================================

22 Same-Name Siblings
=====================

A repository may support *same-name siblings (SNS)*, which enables a
node to have more than one child node with the same name.

Whether a particular implementation supports same-name siblings can be
determined by querying the repository descriptor table with

Repository.NODE\_TYPE\_MANAGEMENT\_SAME\_NAME\_SIBLINGS\_SUPPORTED.

A return value of true indicates support for transactions (see
*Repository Descriptors*).

22.1 Scope of Same-Name Siblings
--------------------------------

Same-name sibling capability is defined *per child node* in the node
type definition of the parent node using the same-name sibling attribute
of the child node definition. Therefore, whether a particular child node
can have sibling node with the same name depends on that child node's
*scoping* *child node definition* (see §3.7.2.1 *Item Definition Name*).

A repository supports same-name siblings by permitting the registration
of node types (or by providing built-in node types) with child node
definitions that have a same-name sibling attribute of true. Disallowing
same-name siblings consists in preventing the availability of such node
types.

22.2 Addressing Same-Name Siblings by Path
------------------------------------------

A particular node within a same-name sibling group can be addressed by
embedding an array-like notation within the path. For example the path
/a/b[2]/c[3] specifies the third child node called c of the second child
node called b of the node a below the root.

The indexing of same-name siblings begins at 1, not 0. This is done for
backwards compatibility with JCR 1.0 and in particular the support in
that specification for XPath, which uses a base-1 index.

A name in a content repository path that does not explicitly specify an
index implies an index of 1. For example, /a/b/c is equivalent to
/a[1]/b[1]/c[1].

The indexing is based on the order in which child nodes are returned in
the iterator acquired through Node.getNodes().

Same-name siblings are indexed by their position relative to each other
in this larger ordered set. For example, the order of child nodes
returned by a getNodes on some parent might be:

[A, B, C, A, D]

In this case, A[1] refers the first node in the list and A[2] refers to
the fourth node in the list.

If a node with same-name siblings is removed, this decrements by one the
indices of all the siblings with indices greater than that of the
removed node. In other words, a removal compacts the array of same-name
siblings and causes the minimal re-numbering required to maintain the
original order but leave no gaps in the numbering.

The relative ordering of a set of same-name sibling nodes is not
guaranteed to be persistent unless the nodes are specified to also be
orderable (see §23 *Orderable Child Nodes*). Non-orderable same-name
siblings can only be relied upon to act as an anonymous, unordered
collection of nodes, though an implementation is free to make the
ordering more stable.

22.3 Reading and Writing Same-Name Siblings
-------------------------------------------

22.3.1 Getting a Same-Name Sibling Set
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

NodeIterator Node.getNodes(String namePattern)

can be used to retrieve a same-name sibling set. This method returns an
iterator over all the child nodes of the calling node that have the
specified pattern. Making namePattern just a name, without wildcards,
retrieves all the child nodes with that name, see §5.2.2 *Iterating Over
Child Items*.

22.3.2 Getting a Particular Same-Name Sibling Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the method

Node Node.getNode(String relPath),

if relPath contains a path element that refers to a node with same-name
sibling nodes without explicitly including an index using the
array-style notation ([x]), then the index [1] is assumed.

22.3.3 Getting a Node's Index
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

int Node.getIndex()

returns the index of this node within the ordered set of its same-name
sibling nodes. This index is the one used to address same-name siblings
using the square-bracket notation, e.g., /a[3]/b[4]. For nodes that do
not have same-name-siblings, this method will always return 1.

22.3.4 When a Same-Name Sibling is a Primary Item
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In cases where the primary child item of a node specifies the name of a
set of same-name sibling child nodes, the node returned by

Item Node.getPrimaryItem()

will be the one among the same-name siblings with index [1].

22.3.5 Removing a Same-Name Sibling Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a node with same-name siblings is removed using

void Node.remove()

this decrements by one the indices of all the siblings with indices
greater than that of the removed node. In other words, a removal
compacts the array of same-name siblings and causes the minimal
re-numbering required to maintain the original order but leave no gaps
in the numbering.

22.4 Properties Cannot Have Same-Name Siblings
----------------------------------------------

Properties cannot have sibling properties of the same name. However,
they may have multiple values (see §3.6.3 *Single and Multi-Value
Properties*).

22.5 Effect of Access Denial on Read of Same-Name Siblings
----------------------------------------------------------

In most cases, the nodes and properties to which a user does not have
read access will simply appear not to exist on a read attempt (see §5.5
*Effect of Access Denial on Read*).

However, a repository that supports same-name siblings *may* violate
this general rule in the case where a user is denied access to a subset
of same-name sibling nodes. In such a case, a repository may choose not
to compact the indices of the same-name-sibling set (thus “hiding” the
any inaccessible nodes), but instead allow “holes” to appear in the
index count.

For example, consider the nodes M/N, M/N[2] and M/N[3] with identifiers
x, y and z, respectively:

| M/N (x)
| M/N[2] (y)
| M/N[3] (z)

On M.getNodes(), a user with no read access to the node with identifier
y will observe one of two behaviors, depending on the implementation. A
repository that compacts indices on read denial will return

| M/N (x)
| M/N[2] (z)

while a repository that does not compact indices will return

| M/N (x)
| M/N[3] (z)

Which behavior is followed is implementation-determined. Note however,
that in the case where a subset of same-name siblings is actually
removed (as opposed to hidden from certain users), index compaction is
required (see §22.2.5 *Removing a Same-Name Sibling Node*).
