Connecting
==========

Manually
--------

.. note::

    The following sections detail how to create a connection, you should
    however only do this once and create a profile. With a profile you
    can reuse connection settings, see :ref:`phpcrsh_profile`.

Jackrabbit
~~~~~~~~~~

The following should work with the default 

.. code-block:: bash

    $ phpcrsh --transport=jackrabbit

Parameters:

- **repo-url**: URL for server, default ``http://localhost:8080/server``

Doctrine-Dbal
~~~~~~~~~~~~~

General connections
"""""""""""""""""""

The following is the minimal required parameters to connect to a MySQL database:

.. code-block:: bash

    $ phpcrsh --transport=doctrine-dbal --db-name="mydb"

Parameters:

- **db-name**: Name of database to connect to
- **db-user**: Username for database, default ``root``
- **db-password**: Password for database, default empty
- **db-host**: Host for database, default ``localhost``
- **db-path**: Path to sqlite database

Connect to Sqlite database
""""""""""""""""""""""""""

.. code-block:: bash

    $ phpcrsh --transport=doctrine-dbal --db-path=/path/to/app.sqlite

More settings
~~~~~~~~~~~~~

For a full list of settings run:

.. code-block:: bash

    $ phpcrsh --help

.. _phpcrsh_profile:

Profiles
--------

You can create or use a profile using a single option, `--profile` or `-p` for short.

For example:

.. code-block:: bash

    $ phpcrsh -pmyapp --transport=doctrine-dbal --db-path=/path/to/app.sqlite

Will *create* a profile called ``myapp``. Profiles are stored as YAML files in
``$HOME:./.phpcrsh/profiles/<profilename>``. And can be manually edited.

To select a profile launch PHPCRSH without any arguments

.. code-block:: bash

    $ phpcrsh
    No connection parameters, given. Select an existing profile:

      (0) dtlweb
      (1) ezcmf
      (2) jackrabbit
      (3) ratest
      (4) slinp_test
      (5) slinptest
      (6) sulucmf

    Enter profile number: []

To explicitly use a profile use the `-p` option again:

.. code-block:: bash

    $ phpcrsh --profile ratest 
    # or
    $ phpcrsh -pratest

.. note::

    A profile is only created if the ``transport`` option is set.

Connect to an embedded PHPCR shell
----------------------------------

This is the easiest way to connect if you have are developing a Symfony 2 application

See :ref:`phpcrsh-installation-embedded-application`.

You can then connect simply using:

.. code-block:: bash

    $ php app/console phpcr:shell

And you can execute specific commands:

.. code-block:: bash

    $ php app/console phpcr:shell node:list /cms

Queries or commands with options must be escapted due to limitations with the Symfony
console component:

.. code-block:: bash

    $ php app/console phpcr:shell "SELECT * FROM [nt:unstructured]"
    $ php app/console phpcr:shell "node:list -L2"
