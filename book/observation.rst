Observation
===========

Observation enables an application to receive notifications of persistent changes to a workspace.
JCR defines a general event model and specific APIs for asynchronous and journaled observation.
A repository may support asynchronous observation, journaled observation or both.

Note that Jackrabbit supports the full observation API but Jackalope currently only implements event journal reading.

Write operations in Jackalope will generate journal entries as expected.

.. code-block:: php

    <?php
    use PHPCR\Observation\EventInterface; // Contains the constants for event types

    // Get the observation manager
    $workspace = $session->getWorkspace();
    $observationManager = $workspace->getObservationManager();

    // Get the unfiltered event journal and go through its content
    $journal = $observationManager->getEventJournal();
    $journal->skipTo(strtotime('-1 day')); // Skip all the events prior to yesterday
    foreach ($journal as $event) {
        // Do something with $event (it's a Jackalope\Observation\Event instance)
        echo $event->getType() . ' - ' . $event->getPath();
    }

    // Filtering and using the journal as an iterator
    // You can filter the event journal on several criteria, here we keep events for node and properties added
    $journal = $observationManager->getEventJournal(EventInterface::NODE_ADDED | EventInterface::PROPERTY_ADDED);

    while ($journal->valid()) {
        $event = $journal->current();
        // Do something with $event
        $journal->next();
    }


