Import and export data
======================

As promised, here are some more details on importing and exporting data. There
are two formats:

* The *document view* translates the data into a XML document with node names
    as xml elements and properties as attributes and thus very readable. Type
    information is lost, and illegal XML characters are encoded.
* The *system view* is a more strict XML document defining the exact structure
    of the repository with all type information. However, it is more verbose.

As an analogy, think about an SQL dump file with SQL statements and the dump of
an SQL table into a csv file. You can restore the data from both, but the SQL
dump knows every detail about your field types and so on while the CSV just
knows the data.

When exporting, you tell explicitly to which format you want to export:

.. code-block:: php

    <?php
    $file = fopen('/tmp/document.xml', 'w+');

    // dump the tree at /foo/bar into a document view file
    $session->exportDocumentView(
        '/data/sibling',
        $file,
        true, // skip binary properties to not have large files in the dump
        false // recursivly output the child nodes as well
    );

    fclose($file);

    $file = fopen('/tmp/system.xml', 'w+');
    // export the tree at /foo/bar into a system view xml file
    $session->exportSystemView(
        '/data/sibling',
        $file,
        false, // do not skip binary properties
        false
    );

    fclose($file);

Importing detects the format automatically. If the document is a valid JCR
system view, it is interpreted according to that format, otherwise if it is a
valid XML document it is imported as document:

.. code-block:: php

    <?php
    $filename = 'dump.xml';
    $session->getRootNode()->addNode('imported_data', 'nt:unstructured');
    $session->importXML(
        '/imported_data', // attach the imported data at this node
        $filename,
        ImportUUIDBehaviorInterface::IMPORT_UUID_CREATE_NEW
    );

When importing nodes with a uuid, a couple of different behaviors can be used:

* `IMPORT_UUID_CREATE_NEW`: Create new UUIDs for nodes that are imported, so you never get collisions.
* `IMPORT_UUID_COLLISION_THROW`: Throw an exception if a node with the same UUID already exists.
* `IMPORT_UUID_COLLISION_REMOVE_EXISTING`: Remove an existing node if an imported node has the same UUID.
* `IMPORT_UUID_COLLISION_REPLACE_EXISTING`: Replace existing node with the imported node. This can lead to the imported data being put in various places.
