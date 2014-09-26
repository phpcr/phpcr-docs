Transactions
============

The PHPCR API in itself uses some sort of 'transaction' model by only
persisting changes on session save. If you need transactions over more than one
save operation or including workspace operations that are dispatched immediately,
you can use transactions.

Note that Jackalope does not support the full transactions:

.. code-block:: php

    <?php
    // get the transaction manager.
    $workspace = $session->getWorkspace();
    $transactionManager = $workspace->getTransactionManager();
    // start a transaction
    $transactionManager->begin();
    $session->removeNode('/data/sibling');
    $session->getRootNode()->addNode('insideTransaction');
    $session->save(); // wrote to the backend but not yet visible to other sessions
    $workspace->move('/data/node', '/new'); // will only move the new node if session has been saved. still not visible to other sessions
    $transactionManager->commit(); // now everything become persistent and visible to others

    // you can abort a transaction
    try {
        ...
    } catch(\Exception $e) {
        if ($transactionManager->inTransaction()) {
            $transactionManager->rollback();
        }
        ...
    }
