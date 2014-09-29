Getting Stated
==============

This aims to provide a rounded general reference to PHPCR. You will mostly see
code examples. It should work with any PHPCR implementation. We propose using
`Jackalope Jackrabbit <https://github.com/jackalope/jackalope-jackrabbit>`_ to
get started as it supports all features described here.

Installing Jackalope
--------------------

Just follow the README of the
`jackalope-jackrabbit <https://github.com/jackalope/jackalope-jackrabbit/blob/master/README.md>`_
repository.

Browser to see what is in the repository
----------------------------------------

There are currently two options for browsing and modifying the contents of the
PHPCR repository.

- `PHPCR Shell <https://github.com/phpcr/phpcr-shell>`_: Aims to provide a full
  command line shell interface to PHPCR content repositories. A pre-compiled
  PHAR archive is available on the github homepage. 

- `Marmelab PHPCR Browser <https://github.com/marmelab/phpcr-browser>`_:
  A user-friendly web based PHPCR browser.

The shell is currently more feature complete, but the PHPCR Browser is more
user friendly. We suggest you try both.

In a nutshell
-------------

The shortest self-contained example should output a line with 'value':

.. code-block:: php

    <?php
    require('/path/to/jackalope-jackrabbit/vendor/autoload.php');

    $factoryclass = '\Jackalope\RepositoryFactoryJackrabbit';
    $parameters = array('jackalope.jackrabbit_uri' => 'http://localhost:8080/server');

    // end of implementation specific configuration

    // get a new PHPCR repository instance from the factory class defined above
    $factory = new $factoryclass();
    $repository = $factory->getRepository($parameters);

    // create the credentials object to authenticate with the repository
    $credentials = new \PHPCR\SimpleCredentials('admin', 'admin');

    // login to the repository and retrieve the session
    $session = $repository->login($credentials, 'default');

    // retrieve the root node of the repository ("/")
    $root = $session->getRootNode();

    // add a new node
    $node = $root->addNode('test', 'nt:unstructured');

    // set a property on the newly created property
    $node->setProperty('prop', 'value');

    // save the session, i.e. persist the data
    $session->save();

    // retrieve the newly created node
    $node = $session->getNode('/test');
    echo $node->getPropertyValue('prop'); // outputs "value"


Still with us? Good, lets get in a bit deeper...

Get some data into the repository
---------------------------------

We will now use the PHPCR import feature to import some initial data into
the repository. First create an XML file called `test.xml``:

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

You may also use the PHPCR Shell to import data:

.. code-block:: bash

   phpcrsh -pmyprofile -c "session:import-xml test.xml"

.. note::

    The import feature is explored in the :doc:`import_export` chapter.
