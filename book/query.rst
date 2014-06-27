Query: Search the database
==========================

.. code-block:: php

    <?php
    // get the query interface from the workspace
    $workspace = $session->getWorkspace();
    $queryManager = $workspace->getQueryManager();

    $sql = "SELECT * FROM [nt:unstructured]
        WHERE [nt:unstructured].[title] = 'Test'
        ORDER BY [nt:unstructured].content";
    $query = $queryManager->createQuery($sql, 'JCR-SQL2');
    $query->setLimit(10); // limit number of results to be returned
    $query->setOffset(1); // set an offset to skip first n results
    $queryResult = $query->execute();

    foreach ($queryResult->getNodes() as $path => $node) {
        echo $node->getName();
    }

Without building nodes
----------------------

There can be a little performance boost if you do not need to fetch the nodes
but just want to access one value of each node:

.. code-block:: php

    <?php
    foreach ($queryResult as $path => $row) {
        echo $path . ' scored ' . $row->getScore();

        $row->getValue('a-value-you-know-exists');
    }

Large search results can be dangerous for performance. See below for some
performance tips.


Using Query Object Model (QOM) for building complex queries
-----------------------------------------------------------

PHPCR provides two languages to build complex queries. SQL2 and Query Object Model (QOM). While SQL2 expresses a query in a syntax similar to SQL, QOM expresses the query as a tree of PHPCR objects.

In this section we will cover QOM. See the `JCR docs <http://phpcr.github.com/doc/html/index.html>`_ for an exposition of both languages.

You can access the QueryObjectModelFactory from the session:

.. code-block:: php

    <?php
    $qomFactory = $mySession->getWorkspace()->getQueryManager()->getQOMFactory();

The QOM factory has a method to build a QOM query given four parameters, and `provides methods <http://phpcr.github.com/doc/html/phpcr/query/qom/queryobjectmodelfactoryinterface.html>`_ to build these four parameters:

.. code-block:: php

    <?php
    $queryObjectModel = $QOMFactory->createQuery(SourceInterface source, ConstraintInterface constraint, array orderings, array columns);

- ``source`` is made out of one or more selectors. Each selector selects a subset of nodes. Queries with more than one selector have joins. A query with two selectors will have a join, a query with three selectors will have two joins, and so on.

``constraint`` filters the set of node-tuples to be retrieved. Constraint may be combined in a tree of constraints to perform a more complex filtering. Examples of constraints are:

    - Absolute or relative paths: nodes descendant of a path, nodes children of a path, nodes reachable by a path.
    - Name of the node.
    - Value of a property.
    - Length of a property.
    - Existence of a property.
    - Full text search.

- ``orderings`` determine the order in which the filtered node-tuples will appear in the query results. The relative order of two node-tuples is determined by evaluating the specified orderings, in list order, until encountering an ordering for which one node-tuple precedes the other.

- ``columns`` are the columns to be included in the tabular view of query results. If no columns are specified, the columns available in the tabular view are implementation determined. In Jackalope include, for each selector, a column for each single-valued non-residual property of the selector's node type.

The simplest case is to select all ``[nt:unstructured]`` nodes:

.. code-block:: php

    <?php
    $source = $qomFactory->selector('a', '[nt:unstructured]');
    $query = $qomFactory->createQuery($source, null, array(), array());
    $queryResult = $query->execute();


The Query Builder: a fluent interface for QOM
---------------------------------------------

Sometimes you may prefer to build a query in several steps. For that reason, the phpcr-utils library provides a fluent wrapper for QOM: the QueryBuilder. It works with any PHPCR implementation.

An example of query built with QueryBuilder:

.. code-block:: php

    <?php
    use PHPCR\Query\QOM\QueryObjectModelConstantsInterface;
    use PHPCR\Util\QOM\QueryBuilder;

    $qf = $qomFactory;
    $qb = new QueryBuilder($qomFactory);
    //add the source
    $qb->from($qomFactory->selector('a', 'nt:unstructured'))
        //some composed constraint
        ->andWhere($qf->comparison($qf->propertyValue('a', 'title'),
        QueryObjectModelConstantsInterface::JCR_OPERATOR_EQUAL_TO,
        $qf->literal('Test')))
        //orderings (descending by default)
        ->orderBy($qf->propertyValue('a', 'content'))
        //set an offset
        ->setFirstResult(0)
        //and the maximum number of node-tuples to retrieve
        ->setMaxResults(25);
    $result = $qb->execute();

    foreach ($result->getNodes() as $node) {
        echo $node->getName() . " has content: " . $node->getPropertyValue('content') . "\n";
    }
    //node has content: This is some test content
    //sibling has content: This is another test content
