Getting Stated
==============

This is an introduction into the PHP content repository. You will mostly see code examples. It should work with any PHPCR implementation. We propose using [Jackalope Jackrabbit](https://github.com/jackalope/jackalope-jackrabbit) to get started as it supports all features described here.

Installing Jackalope
--------------------

Just follow the README of the [jackalope-jackrabbit](https://github.com/jackalope/jackalope-jackrabbit/blob/master/README.md) repository.

Browser to see what is in the repository
----------------------------------------

There are currently two options for browsing and modifying the contents of the PHPCR repository.

- <a href="/documentation/phpcr-shell">PHPCR Shell</a>: Aims to provide a full command line shell interface to PHPCR content repositories. A pre-compiled PHAR archive is available on the github homepage.
- <a href="https://github.com/marmelab/phpcr-browser">Marmelab PHPCR Browser</a>: A web based PHPCR browser.

In a nutshell
-------------

The shortest self-contained example should output a line with 'value':

.. code-block:: php

    <?php
    require("/path/to/jackalope-jackrabbit/vendor/autoload.php");

    $factoryclass = '\Jackalope\RepositoryFactoryJackrabbit';
    $parameters = array('jackalope.jackrabbit_uri' => 'http://localhost:8080/server');
    // end of implementation specific configuration

    $factory = new $factoryclass();
    $repository = $factory->getRepository($parameters);
    $credentials = new \PHPCR\SimpleCredentials('admin','admin');
    $session = $repository->login($credentials, 'default');
    $root = $session->getRootNode();
    $node = $root->addNode('test', 'nt:unstructured');
    $node->setProperty('prop', 'value');
    $session->save();

    // data is stored now. in a follow-up request you can do
    $node = $session->getNode('/test');
    echo $node->getPropertyValue('prop'); // outputs "value"

Still with us? Good, lets get in a bit deeper...

Get some data into the repository
---------------------------------

We will discuss the import feature in more detail later, but to have some data, we just import something here. Create an XML file test.xml like this:

.. code-block:: xml

    <data xmlns:jcr="http://www.jcp.org/jcr/1.0" xmlns:nt="http://www.jcp.org/jcr/nt/1.0">
        <node title="Test" content="This is some test content" />
        <sibling title="Test" content="This is another test content">
            <child1 title="Child1 title" />
            <child2 title="Child2 title" />
            <otherchild title="Otherchild title"/>
            <yetanother title="Yetanother title">
                <child title="Child title" />
            </yetanother>
        </sibling>
    </data>

Now import this into the repository:

.. code-block:: php

    <?php
    $session->importXML('/', 'test.xml', \PHPCR\ImportUUIDBehaviorInterface::IMPORT_UUID_CREATE_NEW);
    $session->save();

