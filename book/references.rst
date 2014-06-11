Node and property references
============================

Nodes can be referenced by unique id (if they are mix:referenceable) or by path. getValue returns the referenced node instance.
Properties can only be referenced by path because they can not have a unique id.

The test document we imported above does not contain the type information we
need to show this example. Lets create a special one and load it into the repository with Session::importXML:

.. code-block:: xml

    <sv:node
         xmlns:mix="http://www.jcp.org/jcr/mix/1.0"
         xmlns:nt="http://www.jcp.org/jcr/nt/1.0"
         xmlns:xs="http://www.w3.org/2001/XMLSchema"
         xmlns:jcr="http://www.jcp.org/jcr/1.0"
         xmlns:sv="http://www.jcp.org/jcr/sv/1.0"
         xmlns:rep="internal"

        sv:name="idExample"
    >
        <sv:property sv:name="jcr:primaryType" sv:type="Name">
            <sv:value>nt:unstructured</sv:value>
        </sv:property>

        <sv:node sv:name="target">
            <sv:property sv:name="jcr:primaryType" sv:type="Name">
                <sv:value>nt:unstructured</sv:value>
            </sv:property>
            <sv:property sv:name="jcr:mixinTypes" sv:type="Name">
                <sv:value>mix:referenceable</sv:value>
            </sv:property>
            <sv:property sv:name="jcr:uuid" sv:type="String">
                <sv:value>13543fc6-1abf-4708-bfcc-e49511754b40</sv:value>
            </sv:property>
            <sv:property sv:name="someproperty" sv:type="String">
                <sv:value>Some value</sv:value>
            </sv:property>
        </sv:node>

        <sv:node sv:name="source">
            <sv:property sv:name="jcr:primaryType" sv:type="Name">
                <sv:value>nt:unstructured</sv:value>
            </sv:property>
            <sv:property sv:name="reference" sv:type="WeakReference">
                <sv:value>13543fc6-1abf-4708-bfcc-e49511754b40</sv:value>
            </sv:property>
            <sv:property sv:name="path" sv:type="Path">
                <sv:value>../target/someproperty</sv:value>
            </sv:property>
        </sv:node>

    </sv:node>


Now import the contents of that file instead of the other one. With this data, you can do this:

.. code-block:: php

    <?php
    $node = $session->getNode('/idExample/source');
    // will return you a node if the property is of type REFERENCE or WEAKREFERENCE
    $othernode = $node->getPropertyValue('reference');

    // force a node
    $property = $node->getProperty('reference');
    // will additionally try to resolve a PATH or NAME property and even work
    // if the property is a STRING that happens to be a valid UUID or to
    // denote an existing path
    $othernode = $property->getNode();

    // get a referenced property
    $property = $node->getProperty('path');
    $otherproperty = $property->getProperty();
    echo $otherproperty->getName(); // someproperty
    echo $otherproperty->getValue(); // Some value

