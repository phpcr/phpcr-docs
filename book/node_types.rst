Node Types
==========

Node types in PHPCR are anagagous to schemas in JCR. Node types enable you to
define which items (properties or child nodes) a node may or may not have. It
allows you to apply constraints to these items and to specify if items should
be automatically created when the node is created.

Node types can be defined as classes or as CND files. CND is an abbreviation
for Compact Namespace and Node Type Definition, and is part of the JCR-283
specification. This tutorial will show examples using both the class and CND
formats.

An Example
----------

As an example we will define the node types required by a canonical blog
application.

.. configuration-block::

    .. code-block:: php

        <?php

        use PHPCR\NodeType\NodeDefinitionInterface;
        use PHPCR\NodeType\NodeTypeDefinitionInterface;
        use PHPCR\NodeType\PropertyDefinitionInterface;

        class AcmeBlogNodeType implements NodeTypeDefinitionInterface
        {
            public function getName()
            {
                return 'acmeBlog:blog';
            }

            public function getDeclaredSupertypeNames()
            {
                return array(
                    'nt:base'
                );
            }

            public function isAbstract()
            {
                return false;
            }
            
            public function isMixin()
            {
                return false;
            }

            public function hasOrderableChildNodes()
            {
                return false;
            }

            public function isQueryable()
            {
                return false;
            }
            
            public function getPrimaryItemName()
            {
                return 'title';
            }

            public function getDeclaredPropertyDefinitions()
            {
                return array(
                    
                );
            }

            public function getDeclaredChildNodeDefinitions()
            {
                return array();
            }
        }

    .. code-block:: cnd

        <acmeBlog = "http://example.org/basiccms/ns/1.0">

        [acmeBlog:blog] > nt:base, mix:lastModified, mix:created
        - title
        + * (acmeBlog:post)

        [acmeBlog:post] > nt:base, mix:lastModified, mix:created
        - title (string) mandatory
        - date (date) mandatory
        - body (string) mandatory
        - tags (string) multiple
        + * (acmeBlog:comment)

        [acmeBlog:comment] > nt:base, mix:created
        - author (string) mandatory
        - comment (string) mandatory


Built-in Node Types
-------------------

nt:unstructured
~~~~~~~~~~~~~~~

This node type does not place any restrictions on its content. This
effectively makes the node act like a document in a "NoSQL" database.

nt:file & nt:folder
-------------------

``nt:file`` and ``nt:folder`` are built-in node types useful to map a file structure in the repository. (With jackalope-jackrabbit, files and folders are exposed over webdav).

TODO: List all built-in node types here

Further Reading
---------------

- `JCR 2.0: 3.7.11 Standard Application Node Types <http://www.day.com/specs/jcr/2.0/3_Repository_Model.html#3.7.11%20Standard%20Application%20Node%20Types>`_


* If you need to store additional properties or children on existing node types like files, note that while a node can have only one primary type, every node can have any mixin types. Define a mixin type declaring your additional properties, register it with PHPCR and addMixin it to the nodes that need it.

You can define your own node types if you want the equivalent of a strictly defined database structure. See `JCR 2.0: 3.7 Node Types <http://www.day.com/specs/jcr/2.0/3_Repository_Model.html#3.7%20Node%20Types>`_ and `JCR 2.0: 19 Node Type Management <http://www.day.com/specs/jcr/2.0/19_Node_Type_Management.html>`_ / `PHPCR Node Type Namespace <http://phpcr.github.io/doc/html/index.html>`_.

