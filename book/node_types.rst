Node Types
==========

PHPCR supports node types. Node types define what properties and children a node can or must have. The JCR specification explains exhaustivly what node types exist and what they are required to have or not: `JCR 2.0: 3.7.11 Standard Application Node Types <http://www.day.com/specs/jcr/2.0/3_Repository_Model.html#3.7.11%20Standard%20Application%20Node%20Types>`_

In a nutshell:

* ``nt:unstructured`` does not define any required properties but allows any property or child.
* ``nt:file`` and ``nt:folder`` are built-in node types useful to map a file structure in the repository. (With jackalope-jackrabbit, files and folders are exposed over webdav)
* If you **do not** want to enforce a schema on your node, use
  ``nt:unstructured``.
* If you need to store additional properties or children on existing node types like files, note that while a node can have only one primary type, every node can have any mixin types. Define a mixin type declaring your additional properties, register it with PHPCR and addMixin it to the nodes that need it.

You can define your own node types if you want the equivalent of a strictly defined database structure. See `JCR 2.0: 3.7 Node Types <http://www.day.com/specs/jcr/2.0/3_Repository_Model.html#3.7%20Node%20Types>`_ and `JCR 2.0: 19 Node Type Management <http://www.day.com/specs/jcr/2.0/19_Node_Type_Management.html>`_ / `PHPCR Node Type Namespace <http://phpcr.github.io/doc/html/index.html>`_.

