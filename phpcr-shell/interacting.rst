Interacting
===========

The PHPCRSH is designed to be a hybrid of a filesystem and an RDBMS shell. You can
both navigate the content hierarchy and execute queries.

.. note::

    PHPCRSH supports "aliases". In this chapter we will use aliases rather than the full
    version of the commands, for example "ls" instead of "node:list", "rm" instead of "node:remove" etc.
    See the chapter on :ref:`phpcrsh_configuration_aliases` for more information.

This chapter aims to highlight some but not all of the features of the shell. For a full
list of commands use the ``list`` command.

For help with a specific command use the ``--help`` option.

The current path 
----------------

You can navigate the content hierarchy using ``shell:path:change`` (or `cd` for short). The
`pwd` command is the alias for ``shell:path:show`` and displays the current working path:

.. code-block:: bash

    PHPCRSH > pwd
    /
    PHPCRSH > cd cms
    PHPCRSH > pwd
    /cms

Listing node contents
---------------------

You can list the contents of a node with the ``node:list`` command (or `ls`):

.. code-block:: bash

    PHPCRSH > ls
    / [nt:unstructured] > nt:base
    +-----------------+-----------------+-----------------+
    | cms/            | nt:unstructured |                 |
    | jcr:primaryType | NAME            | nt:unstructured |
    +-----------------+-----------------+-----------------+

Which also accepts a target:

.. code-block:: bash

    PHPCRSH > ls cms
    /cms [nt:unstructured] > nt:base
    +--------------------+-----------------+-----------------------------------+
    | pages/             | nt:unstructured |                                   |
    | posts/             | nt:unstructured |                                   |
    | routes/            | nt:unstructured |                                   |
    | jcr:primaryType    | NAME            | nt:unstructured                   |
    | jcr:mixinTypes     | NAME            | [0] phpcr:managed                 |
    | phpcr:class        | STRING          | Acme\BasicCmsBundle\Document\Site |
    | phpcr:classparents | STRING          |                                   |
    +--------------------+-----------------+-----------------------------------+

And a depth:

.. code-block:: bash

    PHPCRSH > ls -L2
    / [nt:unstructured] > nt:base
    +--------------------------------------------------------------------------+-----------------+-----------------------------------+
    | cms/                                                                     | nt:unstructured |                                   |
    |   pages/                                                                 | nt:unstructured |                                   |
    |   | main/                                                                | nt:unstructured |                                   |
    |   | jcr:primaryType                                                      | NAME            | nt:unstructured                   |
    |   posts/                                                                 | nt:unstructured |                                   |
    |   | Consequatur quisquam recusandae asperiores accusamus nihil repellat. | nt:unstructured |                                   |
    |   | Velit soluta explicabo eligendi occaecati debitis et saepe eum.      | nt:unstructured |                                   |
    |   | jcr:primaryType                                                      | NAME            | nt:unstructured                   |
    |   routes/                                                                | nt:unstructured |                                   |
    |     page/                                                                | nt:unstructured |                                   |
    |     post/                                                                | nt:unstructured |                                   |
    |     jcr:primaryType                                                      | NAME            | nt:unstructured                   |
    |   jcr:primaryType                                                        | NAME            | nt:unstructured                   |
    |   jcr:mixinTypes                                                         | NAME            | [0] phpcr:managed                 |
    |   phpcr:class                                                            | STRING          | Acme\BasicCmsBundle\Document\Site |
    |   phpcr:classparents                                                     | STRING          |                                   |
    | jcr:primaryType                                                          | NAME            | nt:unstructured                   |
    +--------------------------------------------------------------------------+-----------------+-----------------------------------+

In addition to listing the actual node content, you can also show the
node properties and children which are defined in the schema with the ``-t`` option
(**t** for template). The second of the following two examples illustrates this option:

.. code-block:: bash

    PHPCRSH> ls
    /cms/foo [nt:unstructured] > nt:base
    +--------------------+-------------------------+------------------------------------------------+
    | home               | slinpTest:article       | Home                                           |
    | jcr:primaryType    | NAME                    | slinpTest:article                              |
    | title              | STRING                  | Slinp Web Content Framework                    |
    +--------------------+-------------------------+------------------------------------------------+
    PHPCRSH> ls -t
    /cms/foo [nt:unstructured] > nt:base
    +--------------------+-------------------------+------------------------------------------------+
    | home               | slinpTest:article       | Home                                           |
    | @*                 | nt:base                 |                                                |
    | jcr:primaryType    | NAME                    | slinpTest:article                              |
    | title              | STRING                  | Slinp Web Content Framework                    |
    | @tags              | STRING                  |                                                |
    +--------------------+-------------------------+------------------------------------------------+

In the above examples you see first the "current" contents of the node, in the second we use the
``-t`` option to list "template" items, i.e. items which are defined in the node schema but which
are as yet unrealized. Template items are indicated with the ``@`` symbol. The ``*`` indicates zero or
many.

Wildcards
---------

It is possible to use wildcard expansion when listing node contents:

.. code-block:: bash


    PHPCRSH> node:list /cms/articles/*/*title

Wildcards also work on some other commands such as ``node:remove``

Editing nodes
-------------

You can edit nodes simply by using your system's default editor (as defined by the ``$EDITOR`` environment
variable).


.. code-block:: bash

    PHPCRSH> node:edit cms

The above will open an editor, e.g. VIM, with a YAML file similar to the following:

.. code-block:: yaml

    'jcr:primaryType':
        type: Name
        value: 'slinpTest:article'
    title:
        type: String
        value: Home
    tags:
        type: String
        value: [automobiles, trains, planes]

You can edit the node properties, then save and quit the editor, the node will then be
updated in the session.

Saving and refreshing the session
---------------------------------

Changes made to nodes in the session are not persisted immediately (with the exception
of ``node:copy`` which is a workspace command).

To persist changes to the repository you must call ``session:save`` (or ``save``).

You can also refresh (or reset) the session by calling ``session:refresh`` (or ``refresh``).
