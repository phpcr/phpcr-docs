================================================================================
JCR 2.0: 20 Retention and Hold (Content Repository for Java Technology API v2.0)
================================================================================

20 Retention and Hold
=====================

A repository may support *retention and hold*, which enables an external
retention management application to apply retention policies to
repository content and supports the concepts of hold and
release\ :sup:``:sup:`22` <#sdfootnote22sym>`__`.

Whether a particular implementation supports these features can be
determined by querying the repository descriptor table with

Repository.OPTION\_RETENTION\_SUPPORTED.

a return value of true indicates support (see §24.2 *Repository
Descriptors*).

This API is intended for use by a retention and hold management system
(often external to the repository). It should not be used as a
substitute for normal access control.

20.1 Retention Manager
----------------------

Retention and hold is exposed through a

javax.jcr.retention.RetentionManager

acquired from the Session using

RetentionManager Session.getRetentionManager().

All changes made through the retention and hold API are session-mediated
and therefore require a Session.save() to go into effect.

20.2 Placing a Hold
-------------------

The method

| Hold RetentionManager.
|  addHold(String absPath, String name, boolean isDeep)

places a hold on the node at absPath. If isDeep is false, a *shallow
hold* is placed. If isDeep is true, a *deep hold* is placed. The method
returns the resulting Hold object. The hold only takes effect upon
Session.save(). A node may have more than one hold.

The format and interpretation of the name is application-dependent. It
need not be unique.

20.3 Effect of a Hold
---------------------

A shallow hold in effect on a node N has the same effect as would be the
case if N were protected.

A deep hold in effect on a node N has the same effect as would be the
case if N and all nodes in its subgraph were protected (see §3.7.2.2
*Protected*).

20.4 Getting the Holds present on a Node
----------------------------------------

The method

Hold[] RetentionManager.getHolds(String absPath)

returns all holds on the node at absPath.

20.5 Removing a Hold
--------------------

The method

| void RetentionManager.
|  removeHold(String absPath, Hold hold)

removes the specified hold from the node at absPath. The removal only
takes effect upon Session.save().

20.6 Hold Object
----------------

The Hold interface defines two methods:

String Hold.getName()

which returns the name of the hold, and

boolean Hold.isDeep()

which reports whether the hold is deep or shallow.

20.7 Setting a Retention Policy
-------------------------------

| void RetentionManager.
|  setRetentionPolicy(String absPath, RetentionPolicy policy)

sets the retention policy of the node at absPath to that defined in the
specified retention policy object. The policy only takes effect upon
Session.save().

20.8 Getting a Retention Policy
-------------------------------

| RetentionPolicy RetentionManager.
|  getRetentionPolicy(String absPath)

returns the retention policy on the node at absPath or null if no
retention policy has been set on the node.

20.9 Effect of a Retention Policy
---------------------------------

Interpretation and enforcement of a retention policy is an
implementation issue. However, in all cases a retention policy in effect
on a node N:

-  prevents the removal of N and

-  prevents the addition and removal of all child nodes of N and

-  prevents the addition, removal and change of all properties of N.

20.10 RetentionPolicy object
----------------------------

The RetentionPolicy interface defines one method:

String RetentionPolicy.getName()

which returns the name of the policy.

20.11 Removing a Retention Policy
---------------------------------

void RetentionManager.removeRetentionPolicy(String absPath)

removes the current retention policy on this node, if any. The removal
only takes effect upon a call to Session.save().
