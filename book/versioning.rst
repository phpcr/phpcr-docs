Versioning
==========

Versioning is used to track changes in nodes with the possibility to get back to older versions.

A node with the mixin type `mix:versionable` or `mix:simpleVersionable` can be
versioned. Versioned nodes have a version history, containing the root version
and all versions created. Each version contains the meta data (previous
versions, next versions and creation date) and provides a snapshot of the node
at that point, called "frozen node".

.. code-block:: php

    <?php
    //get the node from the session
    $node = $session->getNode('/data/node');

    $node->setProperty('foo', 'fafa');
    // mark the node as versionable
    $node->addMixin('mix:versionable');
    $session->save();

    // version operations are done through the VersionManager
    $versionManager = $session->getWorkspace()->getVersionManager();

    // put the versionable node into edit mode
    $versionManager->checkout($node->getPath());
    $node->setProperty('foo', 'bar'); // need a change to see something
    $session->save(); // you can only create versions of saved nodes
    // create a new version of the node with our changes
    $version = $versionManager->checkin($node->getPath());
    // Version extends the Node interface. The version is the node with additional functionality

    // walk back the versions
    $oldversion = $version->getLinearPredecessor();
    // the version objects are just the meta data. call getFrozenNode on them
    // to get a snapshot of the data when the version was created
    echo $version->getName() . ': ' . $version->getFrozenNode()->getPropertyValue('foo') . "\n"; // 1.1: bar
    echo $oldversion->getName() . ': ' . $oldversion->getFrozenNode()->getPropertyValue('foo'); // 1.0: fafa

    // get the full version history
    $history = $versionManager->getVersionHistory($node->getPath());
    foreach ($history->getAllFrozenNodes() as $node) {
        if ($node->hasProperty('foo')) {
            // the root version does not have the property
            echo $node->getPropertyValue('foo') . "\n";
        }
    }

    // restore an old version
    $node->setProperty('foo', 'different');
    $versionManager->checkout($node->getPath());
    $session->save(); // restoring is only possible if the session is clean
    $current = $versionManager->getBaseVersion($node->getPath());
    $versionManager->restore(true, $current);
    echo $node->getPropertyValue('foo'); // fafa
