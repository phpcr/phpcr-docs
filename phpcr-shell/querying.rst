Querying
========

Selecting
---------

PHPCRSH currently supports the JCR-SQL2 query language when supported by the
implementation (currently all implementations support this language).

.. code-block:: bash

    PHPCRSH > SELECT title FROM slinpTest:article
    +--------------------------------------------+-----------------------------+
    | Path                                       | slinpTest:article.title     |
    +--------------------------------------------+-----------------------------+
    | /slinp/web/root                            | Slinp Web Content Framework |
    | /slinp/web/root/home                       | Home                        |
    | /slinp/web/root/articles/Faster-than-light | Faster than light           |
    +--------------------------------------------+-----------------------------+
    3 rows in set (0.01 sec)

    PHPCRSH > SELECT title FROM slinpTest:article WHERE title="Home"
    +----------------------+-------------------------+
    | Path                 | slinpTest:article.title |
    +----------------------+-------------------------+
    | /slinp/web/root/home | Home                    |
    +----------------------+-------------------------+
    1 rows in set (0.04 sec)

The JCR-SQL2 lanugage supports joins, column selection and a range of
operands (e.g. lowercase, uppercase, length, etc).

For more information on JCR-SQL2 refer to the articles on the 
`official PHPCR website <http://phpcr.github.io/documentation/>`_.

Update and Delete
-----------------

In addition to standard support for SELECT queries, PHPCRSH additionally
supports UPDATE and DELETE queries, these query grammers **are not standard**
and are specific to PHPCRSH.

.. note::

    UPDATE and DELETE operations are *experimental*. You are advised to test
    any updates before hand in a development environment and ensure that you
    have a backup. We can take no responsibility for lost data!

Updating
--------

The UPDATE Grammer extends the SELECT grammer:

.. code-block:: bash

    PHPCRSH > UPDATE [slinpTest:article] SET title="Away" WHERE title="Home"
    1 row(s) affected in 0.01s

    PHPCRSH > UPDATE [slinpTest:article] AS a LEFT JOIN [slinpTest:foobar] AS b ON a.uuid = b.content SET a.title="Away", b.title="Home"  WHERE a.title="Home"
    1 row(s) affected in 0.01s

Multivalue indexes
~~~~~~~~~~~~~~~~~~

You can update (or remove) specific multivalue indexes:

.. code-block:: bash

    PHPCRSH > UPDATE [slinpTest:article] SET title[1] = "Away" WHERE title="Home"
    1 row(s) affected in 0.01s

The above query will set the multivalue value at index 1 to "Away" when the
value "Home" matches *one of* the multivalue property values.

.. code-block:: bash

    PHPCRSH > UPDATE [slinpTest:article] SET title[1] = NULL WHERE title="Home"
    1 row(s) affected in 0.01s

Same as above but the value at index 1 will be removed.

.. code-block:: bash

    PHPCRSH > UPDATE [slinpTest:article] SET title[] = "Barfoo" WHERE title="Home"
    1 row(s) affected in 0.01s

The above will *add* the value "barfoo" to the multivalue properties (see also :ref:`phpcr_shell_query_function_arrayappend`)

See also: :ref:`phpcr_shell_query_function_arrayremove`, :ref:`phpcr_shell_query_function_arrayreplace`, :ref:`phpcr_shell_query_function_arrayappend`,

Functions
~~~~~~~~~

The ``UPDATE`` grammer also allows the use of functions (note that only UPDATE
supports functions).

.. _phpcr_shell_query_function_arrayremove:

array_remove
""""""""""""

Remove the multivalue property value matching the given value.

Usage:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] AS a SET a.tags = array_remove(a.tags, 'Planes') WHERE a.tags = 'Planes'

Arguments:

- **propertyName**: Property name (including selector) of the multivalue
  property
- **value**: Value to match and remove

.. _phpcr_shell_query_function_arrayreplace:

array_replace
"""""""""""""

Replace a given multivalue property value.

Usage:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] SET tags = array_replace(tags, 'Planes', 'Rockets') WHERE tags = 'Planes'

Arguments:

- **propertyName**: Property name (including selector) of the multivalue
  property
- **value**: Value to replace
- **replacement**: Replacement value

.. _phpcr_shell_query_function_arrayappend:

array_append
""""""""""""

Append a value to a multivalue property.

Usage:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] SET tags - array_append(tags, 'Planes') WHERE tags = 'Planes'

Arguments:

- **propertyName**: Property name (including selector) of the multivalue
  property
- **value**: Value to append

Deleting
--------

Delete is as you might expect, and is essentially gramatically identical to ``SELECT`` but
without the column selection:

.. code-block:: bash

    PHPCRSH > DELETE FROM [slinpTest:article] WHERE title="Home"
    1 row(s) affected in 0.01s
