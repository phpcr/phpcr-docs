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


.. note::

    UPDATE and DELETE operations are performed in userland and are based upon
    underlying SELECT operations, so any overhead incurred in an equivalent
    SELECT will be the baseline for UPDATE or DELETE overheads.
    
Updating
--------

The UPDATE Grammer extends the SELECT grammer:

.. code-block:: bash

    PHPCRSH > UPDATE [slinpTest:article] SET title="Away" WHERE title="Home"
    1 row(s) affected in 0.01s

    PHPCRSH > UPDATE [slinpTest:article] AS a LEFT JOIN [slinpTest:foobar] AS b ON a.uuid = b.content SET a.title="Away", b.title="Home"  WHERE a.title="Home"
    1 row(s) affected in 0.01s

Functions
~~~~~~~~~

The ``UPDATE`` grammer also allows the use of functions (note that only UPDATE
supports functions).

Functions correspond to either ``SET`` or ``APPLY`` syntax. The ``APPLY``
functions take action on the node as a whole. All functions listed below are
for use with ``SET`` unless stated otherwise.

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

.. _phpcr_shell_query_function_array:

array
"""""

Provides an array value, analagous to the ``array`` keyword in PHP:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] SET tags = array('One', 'Two', 'Three')

Arguments:

- List of values

.. _phpcr_shell_query_function_arrayreplace:

array_replace
"""""""""""""

Replace a given multivalue property value, or remove it by setting it to
``NULL``.

Replace a value:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] SET tags = array_replace(tags, 'Planes', 'Rockets')

Remove matching values:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] SET tags = array_replace(tags, 'Planes', NULL)

Arguments:

- **propertyName**: Property name (including selector) of the multivalue
  property
- **value**: Value to replace, use ``NULL`` to remove a value
- **replacement**: Replacement value

.. _phpcr_shell_query_function_arrayreplaceat:

array_replace_at
""""""""""""""""

Replace a given multivalue property value at the specified index.

Usage:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] SET tags = array_replace_at(tags, 0, 'Rockets') WHERE tags = 'Planes'

Arguments:

- **propertyName**: Property name (including selector) of the multivalue
  property
- **index**: Index at which the new value should be set
- **value**: Value to set

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

expr
""""

Evaluate an expression. This function is very powerful in that it enables
you to use the `Symfony Expression Language`_ to evaluate an expression, the
result of which can be assigned to a property.

Within the expression you have access to the `row` object
(`RowInterface`_).

Set the value of ``a.title`` to the node name:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] AS a SET a.title = expr('row.getNode().getName()')

Set the value of ``a.title`` to the value of the property :

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] AS a SET a.title = expr('row.getNode().getPropertyValue("some_property")')

Increment the value of a property:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] AS a SET a.count = expr('row.getNode().getPropertyValue("count") + 1')

Set the value of ``a.title`` from the value of a joined node:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] AS a INNER JOIN [nt:something] AS b ON a.foo = b.bar SET a.title = expr('row.getNode("b").getPropertyValue("something")')

mixin_add
"""""""""

This function allows you to add a mixins to nodes. This is an APPLY function.

Usage:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] APPLY mixin_add('mix:versionable')

mixin_remove
""""""""""""

This function allows you to remove mixins from nodes. This is an APPLY function.

Usage:

.. code-block:: bash

    PHPCRSH> UPDATE [nt:unstructured] APPLY mixin_remove('mix:versionable')

Deleting
--------

Delete is as you might expect, and is essentially gramatically identical to ``SELECT`` but
without the column selection:

.. code-block:: bash

    PHPCRSH > DELETE FROM [slinpTest:article] WHERE title="Home"
    1 row(s) affected in 0.01s

.. _Symfony Expression Language: http://symfony.com/doc/current/components/expression_language/index.html
.. _RowInterface: http://phpcr.github.io/doc/html/files/phpcr.src.PHPCR.Query.RowInterface.html#\PHPCR\Query\RowInterface
