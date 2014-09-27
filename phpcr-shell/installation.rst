Installation
============

You can install PHPCR Shell either as an embedded application or as a PHAR, or
you can build it yourself (when you want the latest version).

.. _phpcrsh-connecting-installation-as-phar:

Install as a PHAR
-----------------

The latest release can be downloaded from the `Github releases page
<https://github.com/doctrine/DoctrinePHPCRBundle/>`_.

After downloading it is recommended to install it in a path accessible
by the system, for example:

.. code-block:: bash

    $ sudo mv phpcrsh.sh /usr/local/bin/phpcrsh
    $ sudo chmod a+x /usr/local/bin/phpcrsh

You can now run PHPCRSH from anywhere:

.. code-block:: bash

    $ phpcrsh --help

.. _phpcrsh-installation-embedded-application:

Install as an embedded application
----------------------------------

If you are using a Symfony2 application and a version of `DoctrinePHPCRBundle
<https://github.com/doctrine/DoctrinePHPCRBundle/>`_ greater than 1.2 then you
can easily integrate the PHPCR-Shell.

Simply add the shell to your ``composer.json`` file

.. code-block:: javascript

    { 
        ...
        require: {
            ...
            "phpcr-shell": "<latest version here>"
        }
        ...
    }

And you can connect directly:

.. code-block:: bash

    $ php app/console phpcr:shell

Build it from source
--------------------

PHPCRSH uses the box PHAR building tool, install it `here <http://box-project.org>`_.

Build the PHAR:

.. code-block:: bash

    $ cd phpcr-shell
    $ box build

This will produce the file ``phpcr.phar``, see :ref:`phpcrsh-connecting-installation-as-phar` for
further instructions.
