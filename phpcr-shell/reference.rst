Reference
=========

.. note::

    This documentation is auto-generated from the command classes in the
    PHPCR-Shell. If you want to make a correction, please find the
    corresponding Command class in the https://github.com/phpcr/phpcr-shell
    repository and make the change there.

* :ref:`phpcr_shell_command_delete`
* :ref:`phpcr_shell_command_help`
* :ref:`phpcr_shell_command_list`
* :ref:`phpcr_shell_command_query`
* :ref:`phpcr_shell_command_select`
* :ref:`phpcr_shell_command_update`

file
----

* :ref:`phpcr_shell_command_fileimport`

lock
----

* :ref:`phpcr_shell_command_lockinfo`
* :ref:`phpcr_shell_command_locklock`
* :ref:`phpcr_shell_command_lockrefresh`
* :ref:`phpcr_shell_command_locktokenadd`
* :ref:`phpcr_shell_command_locktokenlist`
* :ref:`phpcr_shell_command_locktokenremove`
* :ref:`phpcr_shell_command_lockunlock`

node
----

* :ref:`phpcr_shell_command_nodeclone`
* :ref:`phpcr_shell_command_nodecopy`
* :ref:`phpcr_shell_command_nodecorresponding`
* :ref:`phpcr_shell_command_nodecreate`
* :ref:`phpcr_shell_command_nodeedit`
* :ref:`phpcr_shell_command_nodeinfo`
* :ref:`phpcr_shell_command_nodelist`
* :ref:`phpcr_shell_command_nodemixinadd`
* :ref:`phpcr_shell_command_nodemixinremove`
* :ref:`phpcr_shell_command_nodemove`
* :ref:`phpcr_shell_command_nodeorder-before`
* :ref:`phpcr_shell_command_nodepropertyremove`
* :ref:`phpcr_shell_command_nodepropertyset`
* :ref:`phpcr_shell_command_nodepropertyshow`
* :ref:`phpcr_shell_command_nodereferences`
* :ref:`phpcr_shell_command_noderemove`
* :ref:`phpcr_shell_command_noderename`
* :ref:`phpcr_shell_command_nodeset-primary-type`
* :ref:`phpcr_shell_command_nodeupdate`

node-type
---------

* :ref:`phpcr_shell_command_node-typeedit`
* :ref:`phpcr_shell_command_node-typelist`
* :ref:`phpcr_shell_command_node-typeload`
* :ref:`phpcr_shell_command_node-typeshow`

repository
----------

* :ref:`phpcr_shell_command_repositorydescriptorlist`

session
-------

* :ref:`phpcr_shell_command_sessionexportview`
* :ref:`phpcr_shell_command_sessionimport-xml`
* :ref:`phpcr_shell_command_sessioninfo`
* :ref:`phpcr_shell_command_sessionlogin`
* :ref:`phpcr_shell_command_sessionlogout`
* :ref:`phpcr_shell_command_sessionnamespacelist`
* :ref:`phpcr_shell_command_sessionnamespaceset`
* :ref:`phpcr_shell_command_sessionrefresh`
* :ref:`phpcr_shell_command_sessionsave`

shell
-----

* :ref:`phpcr_shell_command_shellaliaslist`
* :ref:`phpcr_shell_command_shellconfiginit`
* :ref:`phpcr_shell_command_shellconfigreload`
* :ref:`phpcr_shell_command_shellexit`
* :ref:`phpcr_shell_command_shellpathchange`
* :ref:`phpcr_shell_command_shellpathshow`

version
-------

* :ref:`phpcr_shell_command_versioncheckin`
* :ref:`phpcr_shell_command_versioncheckout`
* :ref:`phpcr_shell_command_versioncheckpoint`
* :ref:`phpcr_shell_command_versionhistory`
* :ref:`phpcr_shell_command_versionremove`
* :ref:`phpcr_shell_command_versionrestore`

workspace
---------

* :ref:`phpcr_shell_command_workspacecreate`
* :ref:`phpcr_shell_command_workspacedelete`
* :ref:`phpcr_shell_command_workspacelist`
* :ref:`phpcr_shell_command_workspacenamespacelist`
* :ref:`phpcr_shell_command_workspacenamespaceregister`
* :ref:`phpcr_shell_command_workspacenamespaceunregister`
* :ref:`phpcr_shell_command_workspaceuse`


.. _phpcr_shell_command_delete:

delete
------

* **Description:** Execute a literal JCR-SQL2 query
* **Usage:** ``delete [query]``

Execute a JCR-SQL2 query. Unlike other commands you can enter a query literally:


.. code-block:: bash

         DELETE FROM [nt:unstructured] WHERE title = 'foo';

You must call ``session:save`` to persist changes.

Note that this command is not part of the JCR-SQL2 language but is implemented specifically
for the PHPCR-Shell.

Arguments:
~~~~~~~~~~

query
"""""

* **Name:** ``query``
* **Is required:** no
* **Is array:** no
* **Description:** *<none>*
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_help:

help
----

* **Description:** Displays help for a command
* **Usage:** ``help [--xml] [--format="..."] [--raw] [command_name]``

The ``help`` command displays help for a given command:


.. code-block:: bash

    php ./bin/phpcrsh help list

You can also output the help in other formats by using the ``--format`` option:


.. code-block:: bash

    php ./bin/phpcrsh help --format=xml list

To display the list of available commands, please use the ``list`` command.

Arguments:
~~~~~~~~~~

command_name
""""""""""""

* **Name:** ``command_name``
* **Is required:** no
* **Is array:** no
* **Description:** The command name
* **Default:** ``'help'``


Options:
~~~~~~~~

xml
"""

* **Name:** ``--xml``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** To output help as XML
* **Default:** ``false``

format
""""""

* **Name:** ``--format``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** no
* **Description:** To output help in other formats
* **Default:** ``NULL``

raw
"""

* **Name:** ``--raw``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** To output raw command help
* **Default:** ``false``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_list:

list
----

* **Description:** Lists commands
* **Usage:** ``list [--xml] [--raw] [--format="..."] [namespace]``

The ``list`` command lists all commands:


.. code-block:: bash

    php ./bin/phpcrsh list

You can also display the commands for a specific namespace:


.. code-block:: bash

    php ./bin/phpcrsh list test

You can also output the information in other formats by using the ``--format`` option:


.. code-block:: bash

    php ./bin/phpcrsh list --format=xml

It's also possible to get raw list of commands (useful for embedding command runner):


Arguments:
~~~~~~~~~~

namespace
"""""""""

* **Name:** ``namespace``
* **Is required:** no
* **Is array:** no
* **Description:** The namespace name
* **Default:** ``NULL``


Options:
~~~~~~~~

xml
"""

* **Name:** ``--xml``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** To output list as XML
* **Default:** ``false``

raw
"""

* **Name:** ``--raw``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** To output raw command list
* **Default:** ``false``

format
""""""

* **Name:** ``--format``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** no
* **Description:** To output list in other formats
* **Default:** ``NULL``




.. _phpcr_shell_command_query:

query
-----

* **Description:** Execute a query 
* **Usage:** ``query [-l|--language[="..."]] [--limit[="..."]] [--offset[="..."]] [query]``

Execute an SQL query. This command differs from ``select`` in that it
is executed conventionally and not literally. The advantage is that you can
specify a specific query language and additional options:


Arguments:
~~~~~~~~~~

query
"""""

* **Name:** ``query``
* **Is required:** no
* **Is array:** no
* **Description:** *<none>*
* **Default:** ``NULL``


Options:
~~~~~~~~

language
""""""""

* **Name:** ``--language``
* **Accept value:** yes
* **Is value required:** no
* **Is multiple:** no
* **Description:** The query language (e.g. jcr-sql2
* **Default:** ``'JCR-SQL2'``

limit
"""""

* **Name:** ``--limit``
* **Accept value:** yes
* **Is value required:** no
* **Is multiple:** no
* **Description:** The query limit
* **Default:** ``0``

offset
""""""

* **Name:** ``--offset``
* **Accept value:** yes
* **Is value required:** no
* **Is multiple:** no
* **Description:** The query offset
* **Default:** ``0``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_select:

select
------

* **Description:** Execute a literal JCR-SQL2 query
* **Usage:** ``select [query]``

Execute a JCR-SQL2 query. Unlike other commands you can enter a query literally:


.. code-block:: bash

         SELECT * FROM [nt:unstructured];

This command only executes JCR-SQL2 queries at the moment.

Arguments:
~~~~~~~~~~

query
"""""

* **Name:** ``query``
* **Is required:** no
* **Is array:** no
* **Description:** *<none>*
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_update:

update
------

* **Description:** Execute an UPDATE JCR-SQL2 query
* **Usage:** ``update [query]``

Execute a JCR-SQL2 update query. Unlike other commands you can enter a query literally:


.. code-block:: bash

         UPDATE [nt:unstructured] AS a SET title = 'foobar' WHERE a.title = 'barfoo';

You must call ``session:save`` to persist changes.

Note that this command is not part of the JCR-SQL2 language but is implemented specifically
for the PHPCR-Shell.

Arguments:
~~~~~~~~~~

query
"""""

* **Name:** ``query``
* **Is required:** no
* **Is array:** no
* **Description:** *<none>*
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_fileimport:

file:import
-----------

* **Description:** Import a file at the given path
* **Usage:** ``file:import [--mime-type="..."] [--force] [--no-container] path file``

Import an external file into the repository.

The file will be imported as a node of built-in type ``nt:file``.

If a Node is specified as ``path`` then the filename of the imported file will be used
as the new node, otherwise, if the target ``path`` does not exist, then it is assumed
that the path is the target path for the new file, including the filename.


.. code-block:: bash

        PHPCRSH> file:import ./barfoo.png foobar.png

In the first example above will create ``/foobar.png``, whereas the second will create
``./barfoo.png``.

By default the file will be imported in a container, i.e. a node with type ``nt:file``. In
addition to the file data, the node will contain metadata.

Alternatively you can specify the ``--no-container`` option to import directly to a single property.

The mime-type of the file (in the case where a container is used) will be automatically determined unless
specified with ``--mime-type``.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path to import file to
* **Default:** ``NULL``

file
""""

* **Name:** ``file``
* **Is required:** yes
* **Is array:** no
* **Description:** Path to file to import
* **Default:** ``NULL``


Options:
~~~~~~~~

mime-type
"""""""""

* **Name:** ``--mime-type``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** no
* **Description:** Mime type (optional, auto-detected)
* **Default:** ``NULL``

force
"""""

* **Name:** ``--force``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Force overwriting any existing node
* **Default:** ``false``

no-container
""""""""""""

* **Name:** ``--no-container``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Do not wrap in a JCR nt:file, but write directly to the specified property
* **Default:** ``false``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_lockinfo:

lock:info
---------

* **Description:** Show details of the lock that applies to the specified node path
* **Usage:** ``lock:info path``

Shows the details of the lock that applies to the node at the specified
path.

This may be either of the lock on that node itself or a deep lock on a node
above that node.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of locked node
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_locklock:

lock:lock
---------

* **Description:** Lock the node at the given path
* **Usage:** ``lock:lock [--deep] [--session-scoped] [--timeout="..."] [--owner-info="..."] path``

Places a lock on the node at ``path``.

If successful, the node is said to hold the lock.

If ``deep`` option is given then the lock applies to the specified node and
all its descendant nodes; if false, the lock applies only to the
specified node. On a successful lock, the jcr:lockIsDeep property of the
locked node is set to this value.

If ``session-scoped`` is specified then this lock will expire upon the
expiration of the current session (either through an automatic or
explicit ``sesiion:logout``; if not given, this lock does not
expire until it is explicitly unlocked, it times out, or it is
automatically unlocked due to a implementation-specific limitation.

The ``timeout`` parameter specifies the number of seconds until the
lock times out (if it is not refreshed with LockInterface::refresh() in
the meantime). An implementation may use this information as a hint or
ignore it altogether. Clients can discover the actual timeout by
inspecting the returned Lock object.

The ``ownerInfo`` parameter can be used to pass a string holding
owner information relevant to the client. An implementation may either
use or ignore this parameter.

The addition or change of the properties jcr:lockIsDeep and
jcr:lockOwnerare persisted immediately; there is no need to call save.

It is possible to lock a node even if it is checked-in.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node to be locked
* **Default:** ``NULL``


Options:
~~~~~~~~

deep
""""

* **Name:** ``--deep``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** If given this lock will apply to this node and all its descendants; if not, it applies only to this node.
* **Default:** ``false``

session-scoped
""""""""""""""

* **Name:** ``--session-scoped``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** If given, this lock expires with the current session; if not it expires when explicitly or automatically unlocked for some other reason
* **Default:** ``false``

timeout
"""""""

* **Name:** ``--timeout``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** no
* **Description:** Desired lock timeout in seconds (servers are free to ignore this value). If not used lock will not timeout
* **Default:** ``NULL``

owner-info
""""""""""

* **Name:** ``--owner-info``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** no
* **Description:**  string containing owner information supplied by the client; servers are free to ignore this value. If none is specified, the implementation chooses one (i.e. user name of current backend authentication credentials
* **Default:** ``NULL``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_lockrefresh:

lock:refresh
------------

* **Description:** Refresh the TTL of the lock of the node at the given path
* **Usage:** ``lock:refresh path``

If this lock's time-to-live is governed by a timer, this command resets
that timer so that the lock does not timeout and expire.

If this lock's time-to-live is not governed by a timer, then this method
has no effect.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node containing the lock to be refreshed
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_locktokenadd:

lock:token:add
--------------

* **Description:** Add a lock token to the current session
* **Usage:** ``lock:token:add lockToken``

Adds the specified lock token to the current Session.

Holding a lock token makes the current Session the owner of the lock
specified by that particular lock token.

Arguments:
~~~~~~~~~~

lockToken
"""""""""

* **Name:** ``lockToken``
* **Is required:** yes
* **Is array:** no
* **Description:** Lock token
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_locktokenlist:

lock:token:list
---------------

* **Description:** List a lock token to the current session
* **Usage:** ``lock:token:list``

Show a list of previously registered tokens.

Displays all lock tokens currently held by the
current Session. Note that any such tokens will represent open-scoped
locks, since session-scoped locks do not have tokens.

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_locktokenremove:

lock:token:remove
-----------------

* **Description:** Remove a lock token to the current session
* **Usage:** ``lock:token:remove lockToken``

Removes the specified lock token from the current Session.

Arguments:
~~~~~~~~~~

lockToken
"""""""""

* **Name:** ``lockToken``
* **Is required:** yes
* **Is array:** no
* **Description:** Lock token
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_lockunlock:

lock:unlock
-----------

* **Description:** Unlock the node at the given path
* **Usage:** ``lock:unlock path``

Removes the lock on the node at path.

Also removes the properties jcr:lockOwner and jcr:lockIsDeep from that
node. As well, the corresponding lock token is removed from the set of
lock tokens held by the current Session.

If the node does not currently hold a lock or holds a lock for which
this Session is not the owner and is not a "lock-superuser", then a
\PHPCR\Lock\LockException is thrown.

``Note:``
However that the system may give permission to a non-owning session
to unlock a lock. Typically such "lock-superuser" capability is intended
to facilitate administrational clean-up of orphaned open-scoped locks.

Note that it is possible to unlock a node even if it is checked-in (the
lock-related properties will be changed despite the checked-in status).

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodeclone:

node:clone
----------

* **Description:** Clone a node
* **Usage:** ``node:clone [--remove-existing] srcPath destPath [srcWorkspace]``

Clones the subgraph at the node ``srcAbsPath`` in
``srcWorkspace</info> to the new location at <info>destAbsPath`` in
the current workspace.

Unlike the signature of copy that copies between workspaces, this method does
not assign new identifiers to the newly cloned nodes but preserves the
identifiers of their respective source nodes. This applies to both
referenceable and non-referenceable nodes.

In some implementations there may be cases where preservation of a
non-referenceable identifier is not possible, due to how non-referenceable
identifiers are constructed in that implementation. In such a case this method
will throw a RepositoryException.

If the ``--remove-existing`` option is set and an existing node in
this workspace (the destination workspace) has the same identifier as a node
being cloned from srcWorkspace, then the incoming node takes precedence, and
the existing node (and its subgraph) is removed. If
<info>--remove-existing<info> option is not set then an identifier collision
causes this method to throw an ItemExistsException and no changes are made.

If successful, the change is persisted immediately, there is no need to call
save.

The ``destAbsPath`` provided must not have an index on its final
element.  If it does then a RepositoryException is thrown.  If ordering is
supported by the node type of the parent node of the new location, then the new
clone of the node is appended to the end of the child node list.

This method cannot be used to clone just an individual property; it clones a
node and its subgraph.

Arguments:
~~~~~~~~~~

srcPath
"""""""

* **Name:** ``srcPath``
* **Is required:** yes
* **Is array:** no
* **Description:** Path to source node
* **Default:** ``NULL``

destPath
""""""""

* **Name:** ``destPath``
* **Is required:** yes
* **Is array:** no
* **Description:** Path to destination node
* **Default:** ``NULL``

srcWorkspace
""""""""""""

* **Name:** ``srcWorkspace``
* **Is required:** no
* **Is array:** no
* **Description:** If specified, copy from this workspace
* **Default:** ``NULL``


Options:
~~~~~~~~

remove-existing
"""""""""""""""

* **Name:** ``--remove-existing``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Remove existing nodes
* **Default:** ``false``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodecopy:

node:copy
---------

* **Description:** Copy a node
* **Usage:** ``node:copy srcPath destPath [srcWorkspace]``

Copies a Node including its children to a new location to the given workspace.

This method copies the subgraph rooted at, and including, the node at
``srcWorkspace</info> (if given) and <info>srcAbsPath`` to the new location in this
Workspace at ``destAbsPath``.

This is a workspace-write operation and therefore dispatches changes
immediately and does not require a save.

When a node N is copied to a path location where no node currently
exists, a new node N' is created at that location.
The subgraph rooted at and including N' (call it S') is created and is
identical to the subgraph rooted at and including N (call it S) with the
following exceptions:

- Every node in S' is given a new and distinct identifier

.. code-block:: bash

      distinct identifier.


.. code-block:: bash

      jcr:mixinTypes property of M' will reflect any change.


.. code-block:: bash

      reflect the new identifier assigned to M'.


.. code-block:: bash

      reference within the subgraph.

When a node N is copied to a location where a node N' already exists, the
repository may either immediately throw an ItemExistsException or attempt
to update the node N' by selectively replacing part of its subgraph with
a copy of the relevant part of the subgraph of N. If the node types of N
and N' are compatible, the implementation supports update-on-copy for
these node types and no other errors occur, then the copy will succeed.
Otherwise an ItemExistsException is thrown.

Which node types can be updated on copy and the details of any such
updates are implementation-dependent. For example, some implementations
may support update-on-copy for mix:versionable nodes. In such a case the
versioning-related properties of the target node would remain unchanged
(jcr:uuid, jcr:versionHistory, etc.) while the substantive content part
of the subgraph would be replaced with that of the source node.

The ``destAbsPath`` provided must not have an index on its final element. If
it does then a RepositoryException is thrown. Strictly speaking, the
``destAbsPath`` parameter is actually an absolute path to the parent node of
the new location, appended with the new name desired for the copied node.
It does not specify a position within the child node ordering. If ordering
is supported by the node type of the parent node of the new location, then
the new copy of the node is appended to the end of the child node list.

This method cannot be used to copy an individual property by itself. It
copies an entire node and its subgraph (including, of course, any
properties contained therein).

Arguments:
~~~~~~~~~~

srcPath
"""""""

* **Name:** ``srcPath``
* **Is required:** yes
* **Is array:** no
* **Description:** Path to source node
* **Default:** ``NULL``

destPath
""""""""

* **Name:** ``destPath``
* **Is required:** yes
* **Is array:** no
* **Description:** Path to destination node
* **Default:** ``NULL``

srcWorkspace
""""""""""""

* **Name:** ``srcWorkspace``
* **Is required:** no
* **Is array:** no
* **Description:** If specified, copy from this workspace
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodecorresponding:

node:corresponding
------------------

* **Description:** Show the path for the current nodes corresponding path in named workspace
* **Usage:** ``node:corresponding path workspaceName``

Returns the absolute path of the node in the specified workspace that
corresponds to this node.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``

workspaceName
"""""""""""""

* **Name:** ``workspaceName``
* **Is required:** yes
* **Is array:** no
* **Description:** The name of the workspace
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodecreate:

node:create
-----------

* **Description:** Create a node at the current path
* **Usage:** ``node:create path [primaryNodeTypeName]``

Creates a new node at the specified ``path``

This is session-write method, meaning that the addition of the new node
is dispatched upon SessionInterface::save().

The ``path`` provided must not have an index on its final element,
otherwise a RepositoryException is thrown.

If ordering is supported by the node type of the parent node of the new
node then the new node is appended to the end of the child node list.

If ``primaryNodeTypeName`` is specified, this type will be used (or a
ConstraintViolationException thrown if this child type is not allowed).
Otherwise the new node's primary node type will be determined by the
child node definitions in the node types of its parent. This may occur
either immediately, on dispatch (save, whether within or without
transactions) or on persist (save without transactions, commit within
a transaction), depending on the implementation.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node to create
* **Default:** ``NULL``

primaryNodeTypeName
"""""""""""""""""""

* **Name:** ``primaryNodeTypeName``
* **Is required:** no
* **Is array:** no
* **Description:** Optional name of primary node type to use
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodeedit:

node:edit
---------

* **Description:** Edit the given node in the EDITOR configured by the system
* **Usage:** ``node:edit [--type="..."] path``

Edit the given node

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``


Options:
~~~~~~~~

type
""""

* **Name:** ``--type``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** no
* **Description:** Optional type to use when creating new nodes
* **Default:** ``'nt:unstructured'``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodeinfo:

node:info
---------

* **Description:** Show information about the current node
* **Usage:** ``node:info path``

Show information about the current node

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodelist:

node:list
---------

* **Description:** List the children / properties of this node at the given path or with the given UUID
* **Usage:** ``node:list [--children] [--properties] [-f|--filter="..."] [-L|--level="..."] [-t|--template] [path]``

List both or one of the children and properties of this node.

Multiple levels can be shown by using the ``--level`` option.

The ``node:list`` command can also shows template nodes and properties as defined a nodes node-type by
using the ``--template`` option. Template nodes and properties are prefixed with the "@" symbol.

The command accepts wither a path (relative or absolute) to the node or a UUID.


Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** no
* **Is array:** no
* **Description:** Path of node
* **Default:** ``'.'``


Options:
~~~~~~~~

children
""""""""

* **Name:** ``--children``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** List only the children of this node
* **Default:** ``false``

properties
""""""""""

* **Name:** ``--properties``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** List only the properties of this node
* **Default:** ``false``

filter
""""""

* **Name:** ``--filter``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** yes
* **Description:** Optional filter to apply
* **Default:** ``array ()``

level
"""""

* **Name:** ``--level``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** no
* **Description:** Depth of tree to show
* **Default:** ``NULL``

template
""""""""

* **Name:** ``--template``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Show template nodes and properties
* **Default:** ``false``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodemixinadd:

node:mixin:add
--------------

* **Description:** Add the named mixin to the node
* **Usage:** ``node:mixin:add path mixinName``

Adds the mixin node type named ``mixinName`` to this node.

If this node is already of type ``mixinName`` (either due to a previously
added mixin or due to its primary type, through inheritance) then this
method has no effect. Otherwise ``mixinName`` is added to this node's
jcr:mixinTypes property.

Semantically, the new node type may take effect immediately, on dispatch
or on persist. The behavior is adopted must be the same as the behavior
adopted for NodeInterface::setPrimaryType() and the behavior that
occurs when a node is first created.

A ConstraintViolationException is thrown either immediately or on save
if a conflict with another assigned mixin or the primary node type
occurs or for an implementation-specific reason. Implementations may
differ on when this validation is done.

In some implementations it may only be possible to add mixin types
before a a node is persisted for the first time. In such cases any
later calls to ``addMixin`` will throw a ConstraintViolationException
either immediately, on dispatch or on persist.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``

mixinName
"""""""""

* **Name:** ``mixinName``
* **Is required:** yes
* **Is array:** no
* **Description:** The name of the mixin node type to be added
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodemixinremove:

node:mixin:remove
-----------------

* **Description:** Remove the named mixin to the current node
* **Usage:** ``node:mixin:remove mixinName``

Removes the specified mixin node type from this node and removes
mixinName from this node's jcr:mixinTypes property.

Both the semantic change in effective node type and the persistence of
the change to the jcr:mixinTypes  property occur on persist.

Arguments:
~~~~~~~~~~

mixinName
"""""""""

* **Name:** ``mixinName``
* **Is required:** yes
* **Is array:** no
* **Description:** The name of the mixin node type to be removeed
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodemove:

node:move
---------

* **Description:** Move a node in the current session
* **Usage:** ``node:move srcPath destPath``

Moves the node at ``srcPath`` (and its entire subgraph) to the new
location at ``destPath``.

This is a session-write command and therefor requires a save to dispatch
the change.

The identifiers of referenceable nodes must not be changed by a move.
The identifiers of non-referenceable nodes may change.

A ConstraintViolationException is thrown either immediately, on dispatch
or on persist, if performing this operation would violate a node type or
implementation-specific constraint. Implementations may differ on when
this validation is performed.

As well, a ConstraintViolationException will be thrown on persist if an
attempt is made to separately save either the source or destination
node.

Note that this behaviour differs from that of workspace::move
, which is a workspace-write command and therefore immediately dispatches
changes.

The ``destPath`` provided must not have an index on its final element. If
ordering is supported by the node type of the parent node of the new
location, then the newly moved node is appended to the end of the child
node list.

This command cannot be used to move an individual property by itself. It
moves an entire node and its subgraph.

Arguments:
~~~~~~~~~~

srcPath
"""""""

* **Name:** ``srcPath``
* **Is required:** yes
* **Is array:** no
* **Description:** The root of the subgraph to be moved.
* **Default:** ``NULL``

destPath
""""""""

* **Name:** ``destPath``
* **Is required:** yes
* **Is array:** no
* **Description:** The location to which the subgraph is to be moved
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodeorder-before:

node:order-before
-----------------

* **Description:** Reorder a child node of the current node
* **Usage:** ``node:order-before path srcChildRelPath destChildRelPath``

If this node supports child node ordering, this method inserts the child
node at ``srcChildRelPath`` into the child node list at the position
immediately before ``destChildRelPath``

To place the node ``srcChildRelPath`` at the end of the list, a
destChildRelPath of null is used.

Note that (apart from the case where ``destChildRelPath`` is null) both of
these arguments must be relative paths of depth one, in other words they
are the names of the child nodes, possibly suffixed with an index.

If ``srcChildRelPath</info> and <info>destChildRelPath`` are the same, then no change is
made.

This is session-write method, meaning that a change made by this method
is dispatched on save.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``

srcChildRelPath
"""""""""""""""

* **Name:** ``srcChildRelPath``
* **Is required:** yes
* **Is array:** no
* **Description:** The relative path to the child node to be moved in the ordering
* **Default:** ``NULL``

destChildRelPath
""""""""""""""""

* **Name:** ``destChildRelPath``
* **Is required:** yes
* **Is array:** no
* **Description:** The relative path to the child before which the node srcChildRelPath will be placed
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodepropertyremove:

node:property:remove
--------------------

* **Description:** Remove the property at the given absolute path
* **Usage:** ``node:property:remove absPath``

Remove the property from the current session at the given absolute path

Arguments:
~~~~~~~~~~

absPath
"""""""

* **Name:** ``absPath``
* **Is required:** yes
* **Is array:** no
* **Description:** Absolute path to property
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodepropertyset:

node:property:set
-----------------

* **Description:** Rename the node at the current path
* **Usage:** ``node:property:set [--type="..."] path [value]``

Defines a value for a property identified by its name.

Sets the property of this node called ``name`` to the specified value.
This method works as factory method to create new properties and as a
shortcut for PropertyInterface::setValue()

If the property does not yet exist, it is created and its property type
determined by the node type of this node. If, based on the name and
value passed, there is more than one property definition that applies,
the repository chooses one definition according to some implementation-
specific criteria.

Once property with name P has been created, the behavior of a subsequent
``node:set`` may differ across implementations. Some repositories
may allow P to be dynamically re-bound to a different property
definition (based for example, on the new value being of a different
type than the original value) while other repositories may not allow
such dynamic re-binding.

Passing a null as the second parameter removes the property. It is
equivalent to calling remove on the Property object itself. For example,
``node:set P``  would remove property called "P" of the
current node.

This is a session-write method, meaning that changes made through this
method are dispatched on SessionInterface::save().

If ``type`` is given:
The behavior of this method is identical to that of <info>node:set prop
value</info> except that the intended property type is explicitly specified.

``Note:``
Have a look at the JSR-283 spec and/or API documentation for more details
on what is supposed to happen for different types of values being passed
to this method.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of property - can include the node name
* **Default:** ``NULL``

value
"""""

* **Name:** ``value``
* **Is required:** no
* **Is array:** no
* **Description:** Value for named property
* **Default:** ``NULL``


Options:
~~~~~~~~

type
""""

* **Name:** ``--type``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** no
* **Description:** Type of named property
* **Default:** ``NULL``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodepropertyshow:

node:property:show
------------------

* **Description:** Show the property at the given absolute path
* **Usage:** ``node:property:show absPath``

Show the property at the given absolute path

Arguments:
~~~~~~~~~~

absPath
"""""""

* **Name:** ``absPath``
* **Is required:** yes
* **Is array:** no
* **Description:** Absolute path to property
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodereferences:

node:references
---------------

* **Description:** Returns all REFERENCE properties that refer to this node
* **Usage:** ``node:references path [name]``

This command returns all REFERENCE properties that refer to this node,
have the specified name and that are accessible through the current
Session.

If the ``name`` parameter is null then all referring REFERENCES are returned
regardless of name.

Some implementations may only return properties that have been
persisted. Some may return both properties that have been persisted and
those that have been dispatched but not persisted (for example, those
saved within a transaction but not yet committed) while others
implementations may return these two categories of property as well as
properties that are still pending and not yet dispatched.

In implementations that support versioning, this method does not return
properties that are part of the frozen state of a version in version
storage.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``

name
""""

* **Name:** ``name``
* **Is required:** no
* **Is array:** no
* **Description:** Limit references to given name
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_noderemove:

node:remove
-----------

* **Description:** Remove the node at path
* **Usage:** ``node:remove path``

Remove the node at the given path.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_noderename:

node:rename
-----------

* **Description:** Rename the node at the current path
* **Usage:** ``node:rename path newName``

Renames this node to the specified ``newName``. The ordering (if any) of
this node among it siblings remains unchanged.

This is a session-write method, meaning that the name change is
dispatched upon ``session:save``.

The ``newName`` provided must not have an index, otherwise a
RepositoryException is thrown.

An ItemExistsException will be thrown either immediately, on dispatch
(save, whether within or without transactions) or on persist (save
without transactions, commit within a transaction), if there already
exists a sibling item of this node with the specified name and
same-name-siblings are not allowed. Implementations may differ on when
this validation is performed.

A ConstraintViolationException will be thrown either immediately, on
dispatch (save, whether within or without transactions) or on persist
(save without transactions, commit within a transaction), if changing
the name would violate a node type or implementation-specific
constraint. Implementations may differ on when this validation is
performed.

A VersionException will be thrown either immediately, on dispatch (save,
whether within or without transactions) or on persist (save without
transactions, commit within a transaction), if this node is read-only
due to a checked-in node. Implementations may differ on when this
validation is performed.

A LockException will be thrown either immediately, on dispatch (save,
whether within or without transactions) or on persist (save without
transactions, commit within a transaction), if a lock prevents the name
change of the node. Implementations may differ on when this validation
is performed.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``

newName
"""""""

* **Name:** ``newName``
* **Is required:** yes
* **Is array:** no
* **Description:** The name of the node to create
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodeset-primary-type:

node:set-primary-type
---------------------

* **Description:** Set the primary type of the current node
* **Usage:** ``node:set-primary-type path nodeTypeName``

Changes the primary node type of this node to nodeTypeName.

Also immediately changes this node's jcr:primaryType property
appropriately. Semantically, the new node type may take effect
immediately or on dispatch but must take effect on persist. Whichever
behavior is adopted it must be the same as the behavior adopted for
addMixin() (see below) and the behavior that occurs when a node is first
created.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``

nodeTypeName
""""""""""""

* **Name:** ``nodeTypeName``
* **Is required:** yes
* **Is array:** no
* **Description:** New primary node type name
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_nodeupdate:

node:update
-----------

* **Description:** Updates a node corresponding to the current one in the given workspace
* **Usage:** ``node:update path srcWorkspace``

Updates a node corresponding to the current one in the given workspace.

If this node does have a corresponding node in the workspace
srcWorkspace, then this replaces this node and its subgraph with a clone
of the corresponding node and its subgraph.
If this node does not have a corresponding node in the workspace
srcWorkspace, then the update method has no effect.

If the update succeeds the changes made are persisted immediately, there
is no need to call save.

Note that update does not respect the checked-in status of nodes. An
update may change a node even if it is currently checked-in (This fact
is only relevant in an implementation that supports versioning).

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node
* **Default:** ``NULL``

srcWorkspace
""""""""""""

* **Name:** ``srcWorkspace``
* **Is required:** yes
* **Is array:** no
* **Description:** The name of the source workspace
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_node-typeedit:

node-type:edit
--------------

* **Description:** Edit or create a node type
* **Usage:** ``node-type:edit nodeTypeName``

Edit the given node type name with the editor defined in the EDITOR environment variable.

If the node type does not exist, it will be created. All node types must be prefixed with
a namespace prefix as shown in the ``session:namespace:list`` command


.. code-block:: bash

        $ node-type:edit nt:examplenode

Will open an editor with a new node type.

Arguments:
~~~~~~~~~~

nodeTypeName
""""""""""""

* **Name:** ``nodeTypeName``
* **Is required:** yes
* **Is array:** no
* **Description:** The name of the node type to edit or create
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_node-typelist:

node-type:list
--------------

* **Description:** List registered node types
* **Usage:** ``node-type:list [filter]``

List all node types (both primary and mixins)

Arguments:
~~~~~~~~~~

filter
""""""

* **Name:** ``filter``
* **Is required:** no
* **Is array:** no
* **Description:** Perl regexp pattern
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_node-typeload:

node-type:load
--------------

* **Description:** Load or create a node type
* **Usage:** ``node-type:load [--update] cndFile``

This command allows to register node types in the repository that are defined
in a CND (Compact Namespace and Node Type Definition) file as used by jackrabbit.

Custom node types can be used to define the structure of content repository
nodes, like allowed properties and child nodes together with the namespaces
and their prefix used for the names of node types and properties.

If you use ``--update`` existing node type definitions will be overwritten
in the repository.

Arguments:
~~~~~~~~~~

cndFile
"""""""

* **Name:** ``cndFile``
* **Is required:** yes
* **Is array:** no
* **Description:** The name file containing the CND data
* **Default:** ``NULL``


Options:
~~~~~~~~

update
""""""

* **Name:** ``--update``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Update existing node type
* **Default:** ``false``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_node-typeshow:

node-type:show
--------------

* **Description:** Show the CND of a node type
* **Usage:** ``node-type:show nodeTypeName``

Show the CND (Compact Node Definition) of a given node type.

Arguments:
~~~~~~~~~~

nodeTypeName
""""""""""""

* **Name:** ``nodeTypeName``
* **Is required:** yes
* **Is array:** no
* **Description:** The name of the node type to show
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_repositorydescriptorlist:

repository:descriptor:list
--------------------------

* **Description:** List the descriptors for the current repository
* **Usage:** ``repository:descriptor:list``

Repositories indicate support for the JCR specification via. descriptors. This
command lists all of the descriptor keys and values for the current repository.

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_sessionexportview:

session:export:view
-------------------

* **Description:** Export the system view
* **Usage:** ``session:export:view [--no-recurse] [--skip-binary] [--document] [--pretty] absPath file``

Serializes the node (and if ``--no-recurse`` is false, the whole subgraph) at
``absPath`` as an XML stream and outputs it to the supplied URI. The
resulting XML is in the system view form. Note that ``absPath`` must be
the path of a node, not a property.

If ``--skip-binary`` is true then any properties of PropertyType::BINARY will
be serialized as if they are empty. That is, the existence of the
property will be serialized, but its content will not appear in the
serialized output (the <sv:value> element will have no content). Note
that in the case of multi-value BINARY properties, the number of values
in the property will be reflected in the serialized output, though they
will all be empty. If ``--skip-binary`` is false then the actual value(s) of
each BINARY property is recorded using Base64 encoding.

If ``no-recurse</info> is true then only the node at <info>abs-path`` and its properties,
but not its child nodes, are serialized. If ``no-recurse`` is false then the
entire subgraph rooted at ``absPath`` is serialized.

If the user lacks read access to some subsection of the specified tree,
that section simply does not get serialized, since, from the user's
point of view, it is not there.

The serialized output will reflect the state of the current workspace as
modified by the state of this Session. This means that pending changes
(regardless of whether they are valid according to node type
constraints) and all namespace mappings in the namespace registry, as
modified by the current session-mappings, are reflected in the output.

The output XML will be encoded in UTF-8.

Arguments:
~~~~~~~~~~

absPath
"""""""

* **Name:** ``absPath``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node to export
* **Default:** ``NULL``

file
""""

* **Name:** ``file``
* **Is required:** yes
* **Is array:** no
* **Description:** File to export to
* **Default:** ``NULL``


Options:
~~~~~~~~

no-recurse
""""""""""

* **Name:** ``--no-recurse``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Do not recurse
* **Default:** ``false``

skip-binary
"""""""""""

* **Name:** ``--skip-binary``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Skip binary properties
* **Default:** ``false``

document
""""""""

* **Name:** ``--document``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Export the document view
* **Default:** ``false``

pretty
""""""

* **Name:** ``--pretty``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Export in human readable format
* **Default:** ``false``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_sessionimport-xml:

session:import-xml
------------------

* **Description:** Import content from an XML file
* **Usage:** ``session:import-xml [--uuid-behavior="..."] parentAbsPath file``

Deserializes an XML document and adds the resulting item subgraph as a
child of the node at ``parentAbsPath``.

If the incoming XML does not appear to be a JCR system view XML document
then it is interpreted as a document view XML document.

The tree of new items is built in the transient storage of the Session.
In order to persist the new content, save must be called. The advantage
of this through-the-session method is that (depending on what constraint
checks the implementation leaves until save) structures that violate
node type constraints can be imported, fixed and then saved. The
disadvantage is that a large import will result in a large cache of
pending nodes in the session. See WorkspaceInterface::importXML() for a
version of this method that does not go through the Session.

The option ``uuid-behavior`` governs how the identifiers of incoming nodes are
handled. There are four options:

- <info>import-uuid-create-new<info>: Incoming nodes are added

.. code-block:: bash

         the imported node with matching id otherwise.


.. code-block:: bash

         the removal and the new addition will be dispatched on save.


.. code-block:: bash

         save.


.. code-block:: bash

         then an ItemExistsException is thrown.

Unlike ``workspace:import``), this command does not
necessarily enforce all node type constraints during deserialization.
Those that would be immediately enforced in a normal write method
(NodeInterface::addNode(), NodeInterface::setProperty() etc.) of this
implementation cause an immediate ConstraintViolationException during
deserialization. All other constraints are checked on save, just as they
are in normal write operations. However, which node type constraints are
enforced depends upon whether node type information in the imported data
is respected, and this is an implementation-specific issue.

Arguments:
~~~~~~~~~~

parentAbsPath
"""""""""""""

* **Name:** ``parentAbsPath``
* **Is required:** yes
* **Is array:** no
* **Description:** Path of node to export
* **Default:** ``NULL``

file
""""

* **Name:** ``file``
* **Is required:** yes
* **Is array:** no
* **Description:** File to export to
* **Default:** ``NULL``


Options:
~~~~~~~~

uuid-behavior
"""""""""""""

* **Name:** ``--uuid-behavior``
* **Accept value:** yes
* **Is value required:** yes
* **Is multiple:** no
* **Description:** UUID behavior
* **Default:** ``'create-new'``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_sessioninfo:

session:info
------------

* **Description:** Display information about current session
* **Usage:** ``session:info``

The command shows some basic information about the current session.

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_sessionlogin:

session:login
-------------

* **Description:** Login or (relogin) to a session
* **Usage:** ``session:login userId password [workspaceName]``

Arguments:
~~~~~~~~~~

userId
""""""

* **Name:** ``userId``
* **Is required:** yes
* **Is array:** no
* **Description:** Unique identifier of user
* **Default:** ``NULL``

password
""""""""

* **Name:** ``password``
* **Is required:** yes
* **Is array:** no
* **Description:** Password
* **Default:** ``NULL``

workspaceName
"""""""""""""

* **Name:** ``workspaceName``
* **Is required:** no
* **Is array:** no
* **Description:** Optional workspace name
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_sessionlogout:

session:logout
--------------

* **Description:** Logout of the current session
* **Usage:** ``session:logout``

Releases all resources associated with this Session.

This command should be called when a Session is no longer needed.

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_sessionnamespacelist:

session:namespace:list
----------------------

* **Description:** List all namespace prefix to URI  mappings in current session
* **Usage:** ``session:namespace:list``

List all namespace prefix to URI  mappings in current session

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_sessionnamespaceset:

session:namespace:set
---------------------

* **Description:** Set a namespace in the current session
* **Usage:** ``session:namespace:set prefix uri``

Sets the name of a namespace prefix.

Within the scope of this Session, this method maps uri to prefix. The
remapping only affects operations done through this Session. To clear
all remappings, the client must acquire a new Session.
All local mappings already present in the Session that include either
the specified prefix or the specified uri are removed and the new
mapping is added.

Arguments:
~~~~~~~~~~

prefix
""""""

* **Name:** ``prefix``
* **Is required:** yes
* **Is array:** no
* **Description:** The namespace prefix to be set as identifier
* **Default:** ``NULL``

uri
"""

* **Name:** ``uri``
* **Is required:** yes
* **Is array:** no
* **Description:** The location of the namespace definition (usually a URI
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_sessionrefresh:

session:refresh
---------------

* **Description:** Refresh the current session
* **Usage:** ``session:refresh [--keep-changes]``

Reloads the current session.

If the ``keep-changes`` option is not given then this method discards
all pending changes currently recorded in this Session and returns all items to
reflect the current saved state. Outside a transaction this state is simply the
current state of persistent storage. Within a transaction, this state will
reflect persistent storage as modified by changes that have been saved but not
yet committed.

If ``keep-changes`` is true then pending change are not discarded but
items that do not have changes pending have their state refreshed to reflect
the current saved state, thus revealing changes made by other sessions.

Options:
~~~~~~~~

keep-changes
""""""""""""

* **Name:** ``--keep-changes``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Keep any changes that have been made in this session
* **Default:** ``false``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_sessionsave:

session:save
------------

* **Description:** Save the current session
* **Usage:** ``session:save``

Validates all pending changes currently recorded in this Session.

If validation of all pending changes succeeds, then this change
information is cleared from the Session.

If the save occurs outside a transaction, the changes are dispatched and
persisted. Upon being persisted the changes become potentially visible
to other Sessions bound to the same persistent workspace.

If the save occurs within a transaction, the changes are dispatched but
are not persisted until the transaction is committed.

If validation fails, then no pending changes are dispatched and they
remain recorded on the Session. There is no best-effort or partial save.

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_shellaliaslist:

shell:alias:list
----------------

* **Description:** List all the registered aliases
* **Usage:** ``shell:alias:list``

List the aliases as defined in ``~/.phpcrsh/aliases.yml``.

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_shellconfiginit:

shell:config:init
-----------------

* **Description:** Initialize a local configuration with default values
* **Usage:** ``shell:config:init``

Initialize a new configuration folder, ``.phpcrsh`` in the users HOME directory.

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_shellconfigreload:

shell:config:reload
-------------------

* **Description:** Reload the configuration
* **Usage:** ``shell:config:reload``

Reload the configuration

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_shellexit:

shell:exit
----------

* **Description:** Logout and quit the shell
* **Usage:** ``shell:exit``

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_shellpathchange:

shell:path:change
-----------------

* **Description:** Change the current path
* **Usage:** ``shell:path:change [path]``

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** no
* **Is array:** no
* **Description:** *<none>*
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_shellpathshow:

shell:path:show
---------------

* **Description:** Print Working Directory (or path)
* **Usage:** ``shell:path:show``

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_versioncheckin:

version:checkin
---------------

* **Description:** Checkin (commit) a node version
* **Usage:** ``version:checkin path``

Creates for the versionable node at ``path`` a new version with a system
generated version name and returns that version (which will be the new
base version of this node). Sets the ``jcr:checkedOut`` property to false
thus putting the node into the checked-in state. This means that the node
and its connected non-versionable subgraph become read-only. A node's
connected non-versionable subgraph is the set of non-versionable descendant
nodes reachable from that node through child links without encountering
any versionable nodes. In other words, the read-only status flows down
from the checked-in node along every child link until either a versionable
node is encountered or an item with no children is encountered. In a
system that supports only simple versioning the connected non-versionable
subgraph will be equivalent to the whole subgraph, since simple-versionable
nodes cannot have simple-versionable descendants.

Read-only status means that an item cannot be altered by the client using
standard API methods (addNode, setProperty, etc.). The only exceptions to
this rule are the restore(), restoreByLabel(), merge() and Node::update()
operations; these do not respect read-only status due to check-in. Note
that remove of a read-only node is possible, as long as its parent is not
read-only (since removal is an alteration of the parent node).

If this node is already checked-in, this method has no effect but returns
the current base version of this node.

If checkin succeeds, the change to the ``jcr:isCheckedOut`` property is
dispatched immediately.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Absolute path to node
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_versioncheckout:

version:checkout
----------------

* **Description:** Checkout a node version and enable changes to be made
* **Usage:** ``version:checkout path``

Sets the versionable node at ``path`` to checked-out status by setting
its jcr:isCheckedOut property to true. Under full versioning it also sets
the jcr:predecessors property to be a reference to the current base
version (the same value as held in ``jcr:baseVersion``).

This method puts the node into the checked-out state, making it and its
connected non-versionable subgraph no longer read-only (see ``version:checkin`` for
an explanation of the term "connected non-versionable subgraph". Under
simple versioning this will simply be the whole subgraph).

If successful, these changes are persisted immediately, there is no need
to call save.

If this node is already checked-out, this method has no effect.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Absolute path to node
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_versioncheckpoint:

version:checkpoint
------------------

* **Description:** Checkin and then checkout a node
* **Usage:** ``version:checkpoint path``

Performs a ``version:checkin</info> followed by a <info>version:checkout`` on the versionable node at
``path``

If this node is already checked-in, this method is equivalent to ``version:checkout``.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path to node
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_versionhistory:

version:history
---------------

* **Description:** Show version history of node at given absolute path
* **Usage:** ``version:history path``

Lists the version history of the node given at ``path``.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Absolute path to node
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_versionremove:

version:remove
--------------

* **Description:** Remove a node version
* **Usage:** ``version:remove path versionName``

Removes the named version from this version history and automatically
repairs the version graph.

If the version to be removed is V, V's predecessor set is P and V's
successor set is S, then the version graph is repaired s follows:

- For each member of P, remove the reference to V from its successor

.. code-block:: bash

      list and add references to each member of S.


.. code-block:: bash

      list and add references to each member of P.

``Note`` that this change is made immediately; there is no need to
call save. In fact, since the the version storage is read-only with
respect to normal repository methods, save does not even function in
this context.

Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path to node
* **Default:** ``NULL``

versionName
"""""""""""

* **Name:** ``versionName``
* **Is required:** yes
* **Is array:** no
* **Description:** Name of version to remove
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_versionrestore:

version:restore
---------------

* **Description:** Restore a node version
* **Usage:** ``version:restore [--remove-existing] path versionName``

Attempt to restore an old version of a node.

* If ``path</info> is given and <info>versionName`` is a version name:

.. code-block:: bash

     checked-in or not.


* If ``path</info> is given and <info>versionName`` is a VersionInterface instance:

.. code-block:: bash

      ConstraintViolationException is thrown.


* If ``versionName`` is VersionInterface instance:

.. code-block:: bash

      This method ignores checked-in status.


* If ``versionName`` is an array of VersionInterface instances:

.. code-block:: bash

      versions being restored define a set of (one or more) subgraphs.

If the restore succeeds the changes made are dispatched immediately;

there is no need to call save.

If an array of VersionInterface instances is restored, an identifier
collision occurs when the current workspace contains a node outside these
subgraphs that has the same identifier as one of the nodes that would be
introduced by the restore operation into one of these subgraphs.
Else, an identifier collision occurs when a node exists outside the
subgraph rooted at path with the same identifier as a node that would
be introduced by the restore operation into the affected subgraph.
The result in such a case is governed by the removeExisting flag. If
``removeExisting`` is true, then the incoming node takes precedence, and the
existing node (and its subgraph) is removed (if possible; otherwise a
RepositoryException is thrown). If ``removeExisting`` is false, then an
ItemExistsException is thrown and no changes are made. Note that this
applies not only to cases where the restored node itself conflicts with
an existing node but also to cases where a conflict occurs with any node
that would be introduced into the workspace by the restore operation. In
particular, conflicts involving subnodes of the restored node that have
OnParentVersion settings of COPY or VERSION are also governed by the
``removeExisting`` flag.

Note: 


Arguments:
~~~~~~~~~~

path
""""

* **Name:** ``path``
* **Is required:** yes
* **Is array:** no
* **Description:** Path to node
* **Default:** ``NULL``

versionName
"""""""""""

* **Name:** ``versionName``
* **Is required:** yes
* **Is array:** no
* **Description:** Name of version to retore
* **Default:** ``NULL``


Options:
~~~~~~~~

remove-existing
"""""""""""""""

* **Name:** ``--remove-existing``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Flag that governs what happens in case of identifier collision
* **Default:** ``false``

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_workspacecreate:

workspace:create
----------------

* **Description:** Create a new workspace
* **Usage:** ``workspace:create name [srcWorkspace]``

Creates a new Workspace with the specified name. The new workspace is
empty, meaning it contains only root node.

If ``srcWorkspace`` is given, then it
creates a new Workspace with the specified name initialized with a
clone of the content of the workspace srcWorkspace. Semantically,
this command is equivalent to creating a new workspace and manually
cloning ``srcWorkspace`` to it.

Arguments:
~~~~~~~~~~

name
""""

* **Name:** ``name``
* **Is required:** yes
* **Is array:** no
* **Description:** Name of new workspace
* **Default:** ``NULL``

srcWorkspace
""""""""""""

* **Name:** ``srcWorkspace``
* **Is required:** no
* **Is array:** no
* **Description:** If specified, clone from this workspace
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_workspacedelete:

workspace:delete
----------------

* **Description:** Delete a workspace
* **Usage:** ``workspace:delete name [srcWorkspace]``

Deletes the workspace with the specified name from the repository,
deleting all content within it.

Arguments:
~~~~~~~~~~

name
""""

* **Name:** ``name``
* **Is required:** yes
* **Is array:** no
* **Description:** Name of new workspace
* **Default:** ``NULL``

srcWorkspace
""""""""""""

* **Name:** ``srcWorkspace``
* **Is required:** no
* **Is array:** no
* **Description:** If specified, clone from this workspace
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_workspacelist:

workspace:list
--------------

* **Description:** Lists workspaces in the current repository
* **Usage:** ``workspace:list [srcWorkspace]``

Lists the workspaces accessible to the current user.

The current workspace is indicated by an asterix (*).

Lists the names of all workspaces in this
repository that are accessible to this user, given the Credentials that
were used to get the Session to which this Workspace is tied.
In order to access one of the listed workspaces, the user performs
another ``session:login``, specifying the name of the desired
workspace, and receives a new Session object.

Arguments:
~~~~~~~~~~

srcWorkspace
""""""""""""

* **Name:** ``srcWorkspace``
* **Is required:** no
* **Is array:** no
* **Description:** If specified, clone from this workspace
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_workspacenamespacelist:

workspace:namespace:list
------------------------

* **Description:** List all namespace prefix to URI  mappings in current workspace
* **Usage:** ``workspace:namespace:list``

List all namespace prefix to URI mappings in current workspace

Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_workspacenamespaceregister:

workspace:namespace:register
----------------------------

* **Description:** Sets a one-to-one mapping between prefix and uri in the global namespace
* **Usage:** ``workspace:namespace:register prefix uri``

List all namespace prefix to URI  mappings in current session

Arguments:
~~~~~~~~~~

prefix
""""""

* **Name:** ``prefix``
* **Is required:** yes
* **Is array:** no
* **Description:** The namespace prefix to be mapped
* **Default:** ``NULL``

uri
"""

* **Name:** ``uri``
* **Is required:** yes
* **Is array:** no
* **Description:** The URI to be mapped
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_workspacenamespaceunregister:

workspace:namespace:unregister
------------------------------

* **Description:** Unregister a namespace
* **Usage:** ``workspace:namespace:unregister uri``

Removes the specified namespace URI from namespace registry.

The following restrictions apply:

- Attempting to unregister a built-in namespace (jcr, nt, mix, sv, xml or

.. code-block:: bash

      the empty namespace) will throw a NamespaceException.


.. code-block:: bash

      will throw a NamespaceException.


Arguments:
~~~~~~~~~~

uri
"""

* **Name:** ``uri``
* **Is required:** yes
* **Is array:** no
* **Description:** The URI to be removed
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``










.. _phpcr_shell_command_workspaceuse:

workspace:use
-------------

* **Description:** Change the current workspace
* **Usage:** ``workspace:use name [srcWorkspace]``

Change the workspace.

Arguments:
~~~~~~~~~~

name
""""

* **Name:** ``name``
* **Is required:** yes
* **Is array:** no
* **Description:** Name of workspace to use
* **Default:** ``NULL``

srcWorkspace
""""""""""""

* **Name:** ``srcWorkspace``
* **Is required:** no
* **Is array:** no
* **Description:** If specified, clone from this workspace
* **Default:** ``NULL``


Options:
~~~~~~~~

help
""""

* **Name:** ``--help``
* **Accept value:** no
* **Is value required:** no
* **Is multiple:** no
* **Description:** Display this help message.
* **Default:** ``false``








