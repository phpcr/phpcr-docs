==================================================================================
JCR 2.0: 18 Lifecycle Management (Content Repository for Java Technology API v2.0)
==================================================================================

18 Lifecycle Management
=======================

A repository may support *lifecycle management*, enabling users to:

-  Discover the state of a node within a lifecycle.

-  Promote or demote nodes through a lifecycle by following a transition
   from the current state to a new state.

The names and semantics of the supported lifecycle states and
transitions are implementation-specific.

Whether an implementation supports lifecycle management can be
determined by querying the repository descriptor table with

Repository.OPTION\_LIFECYCLE\_SUPPORTED.

A return value of true indicates support (see §24.2 *Repository
Descriptors*).

18.1 mix:lifecycle
------------------

[mix:lifecycle]

mixin

- jcr:lifecyclePolicy (REFERENCE) protected INITIALIZE

- jcr:currentLifecycleState (STRING) protected INITIALIZE

| 
| Only nodes with mixin node type mix:lifecycle may participate in a
lifecycle. The mixin adds two properties:

-  jcr:lifecyclePolicy: This property is a reference to another node
   that contains lifecycle policy information. The definition of the
   referenced node is not specified.

-  jcr:currentLifecycleState: This property is a string identifying the
   current lifecycle state of this node. The format of this string is
   not specified.

18.2 Node Methods
-----------------

The Node interface provides the following methods related to lifecycles.
If the node does not have the mix:lifecycle mixin, the methods will
return UnsupportedRepositoryOperationException.

void Node.followLifecycleTransition(String transition)

causes the lifecycle state of this node to undergo the specified
transition.

This method may change the value of the jcr:currentLifecycleState
property, in most cases it is expected that the implementation will
change the value to that of the passed transition parameter, though this
is an implementation-specific issue. If the jcr:currentLifecycleState
property is changed the change is persisted immediately, there is no
need to call save.

String[] Node.getAllowedLifecycleTransitions()

returns the list of valid state transitions for this node.
