Reading data and traversal
==========================

You can wrap any code into try catch blocks. See the `API doc <http://phpcr.github.com/doc/html/index.html>`_ for what exceptions to expect on which calls. With PHPCR being ported from Java, there is a lot of Exceptions defined.
But as this is PHP, you don't have to catch them. As long as your content is as the code expects, it won't matter.

.. code-block:: php

    <?php
    $node = $session->getNode('/data/node');
    echo $node->getName(); // will be 'node'
    echo $node->getPath(); // will be '/data/node'

Reading properties
------------------

.. code-block:: php

    <?php

    //get the node from the session
    $node = $session->getNode('/data/node');

    // get the php value of a property (type automatically determined from stored information)
    echo $node->getPropertyValue('title');

    // get the Property object to operate on
    $property = $node->getProperty('content');
    echo 'Size of '.$property->getPath().' is '.$property->getLength();

    // read a property that could be very long
    $property = $node->getProperty('content');

    // if it is binary convert into string
    $data = $property->getString();
    echo $data;

    // get binary stream. could be more performant with binary property
    $stream = $property->getBinary();
    fpassthru($stream);
    fclose($stream);

    // the above in short if you just want to dump a file that is in a binary propery:
    // fpassthru($node->getPropertyValue('binary-prop'));

Note: the backend stores the property types. When getting property values, they are returned
with that type, unless you use one of the explicit PropertyInterface::getXX methods.
For that case, type conversion is attempted and an exception thrown if this is not possible.

See the API doc for a list of all supported types.

.. code-block:: php

    <?php
    // get all properties of this node
    foreach ($node->getPropertiesValues() as $name => $value) {
        echo "$name: $value\n";
    }
    // get the properties of this node with a name starting with 't'
    foreach ($node->getPropertiesValues("t*") as $name => $value) {
        echo "$name: $value\n";
    }

Traversing the hierarchy
------------------------

.. code-block:: php

    <?php
    //get the node from the session
    $node = $session->getNode('/data/node');

    // getting a node by path relative to the node
    $othernode = $node->getNode('../sibling'); // /sibling

    // get all child nodes. the $node is Iterable, the iterator being all children
    $node = $session->getNode('/data/sibling');
    foreach ($node as $name => $child) {
        if ($child->hasProperties()) {
            echo "$name has properties\n";
        } else {
            echo "$name does not have properties\n";
        }
    }

    // get child nodes with the name starting with 'c'
    foreach ($node->getNodes('c*') as $name => $child) {
        echo "$name\n";
    }

    // get child nodes with the name starting with 'o' or ending with '2' or named 'yetanother'
    foreach ($node->getNodes(array('o*', '*2', 'yetanother')) as $name => $child) {
        echo "$name\n";
    }

    // get the parent node
    $parent = $node->getParent(); // /

    // build a breadcrumb of the node ancestry
    $node = $session->getNode('/data/sibling/yetanother');
    $i = 0;
    $breadcrumb = array();
    do {
        $i++;
        $parent = $node->getAncestor($i);
        $breadcrumb[$parent->getPath()] = $parent->getName();
    } while ($parent != $node);
    var_dump($breadcrumb);


