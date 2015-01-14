Performance considerations
==========================

While PHPCR can perform reasonably well, you should be careful. You are
working with an object model mapping interlinked data. Implementations are
supposed to lazy load data only when necessary. But you should take care to
only request what you actually need.

The implementations will also use some sort of storage backend (Jackrabbit,
(no)SQL database, ...). There might be a huge performance impact in
configuring that storage backend optimally. Look into your implementation
documentation if there are recommendations how to optimize storage.

One thing *not* to worry about is requesting the same node with
Session::getNode or Node::getNode/s several times. You always get the same
object instance back without overhead.

Only request what you need
--------------------------

Remember that you can filter nodes on Node::getNodes if you only need a list of
specific nodes or all nodes in some namespace.

The values of binary properties can potentially have a huge size and should
only loaded when really needed. If you just need the size, you can get the
property instance and do a $property->getSize() instead of
filesize($node->getPropertyValue). Any decent implementation will not preload
the binary stream when you access the property object.

When getting the properties from a node, you can use
Node::getPropertiesValues(filter, false). This allows the implementation to
avoid instantiating Property objects for the property values (and saves you
coding). The second boolean parameter tells wheter to dereference reference
properties. If you do not need the referenced objects, pass false and you will
get the UUID or path strings instead of node objects.(If you need one of them,
you can still get it with Session::getNodeByIdentifier. But then the
implementation will certainly not be able to optimize if you get several
referenced nodes.)

But request in one call as much as possible of what you need
------------------------------------------------------------

If you need to get several nodes where you know the paths, use
``Session::getNodes`` with an array of those nodes to get all of them in one
batch, saving round trip time to the storage backend.

You can also use ``Node::getNodes`` with a list of nodes rather than repeatedly calling
``Node::getNode``.

