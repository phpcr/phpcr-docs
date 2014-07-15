=====================================================================
JCR 2.0: 17 Locking (Content Repository for Java Technology API v2.0)
=====================================================================

17 Locking
==========

A repository may support *locking*, which enables a user to temporarily
prevent other users from changing a node or subgraph of nodes.

Whether an implementation supports locking can be determined by querying
the repository descriptor table with

Repository.OPTION\_LOCKING\_SUPPORTED.

A return value of true indicates support (see §24.2 *Repository
Descriptors*).

17.1 Lockable
-------------

A lock is placed on a node by calling LockManager.lock (see §17.11.1
*LockManager.lock*). The node on which a lock is placed is called the
*holding node* of that lock. Only nodes with mixin node type
mix:lockable (inherited as part of their primary node type or explicitly
assigned) may hold locks. The definition of mix:lockable is:

[mix:lockable]

mixin

- jcr:lockOwner (STRING) protected IGNORE

- jcr:lockIsDeep (BOOLEAN) protected IGNORE

17.2 Shallow and Deep Locks
---------------------------

A lock can be specified as either *shallow* or *deep*. A shallow lock
applies only to its holding node and its properties. A deep lock applies
to its holding node and all its descendants. Consequently, there is a
distinction between a lock *being held by* a node and a lock *applying
to* a node. A lock always applies to its holding node. However, if it is
a deep lock, it also applies to all nodes in the holding node's
subgraph. When a lock applies to a node, that node is said to be
*locked*.

Since a deep lock applies to all nodes in the lock-holding node's
subgraph, this may include both mix:lockable nodes and non-mix:lockable
nodes. The deep lock applies to both categories of node equally and it
*does not* add any jcr:lockOwner or jcr:lockIsDeep properties to any of
the deep-locked mix:lockable nodes. However, if any such nodes exist and
they already have these properties, this means that they are already
locked, and hence the attempt to deep lock above them will fail.

Additionally, assuming a deep lock exists above a mix:lockable node, any
attempt to lock this lower level mix:lockable node will also fail,
because it is already locked from above.

17.3 Lock Owner
---------------

Initially, the session through which a lock is placed is the *owner* of
that lock. This means the session has the power to alter the locked node
and to remove the lock. In the case of open-scoped locks (as opposed to
session-scoped, see §17.7 *Session-Scoped and Open-Scoped Locks*)
control of the lock may be given to another session during the lifetime
of that lock. In some implementations giving control of a lock to
another session will remove control from the previous session, in
others, more than one session may simultaneously own the same
open-scoped lock.

Repositories may support client-specified lock owner information. If
this is the case, the jcr:lockOwner property will be set to the value
supplied upon lock creation, and will not change during the lifetime of
the lock. Otherwise, when a lock is created, the jcr:lockOwner property
is set to the user ID bound to the locking Session (that is, the string
returned by Session.getUserID) or another implementation-dependent
string identifying the user.

In implementations that do not support client-specified lock owner
information, when an open-scoped lock is moved to a new owner, or
assigned an additional one (if supported), the jcr:lockOwner property
may be automatically altered to reflect the change.

Strictly speaking it is the session, not the user, that owns a
particular lock at a particular time. The jcr:lockOwner property is used
for informational purposes, so that a client application can, for
example, display this information to other users. For this reason the
user is sometimes informally referred to as the lock owner.

In implementations that record the user ID in jcr:lockOwner, that user
will not automatically have the ability to alter the locked node if
accessing it through another session. Transfer (or, if supported,
addition) of ownership must be done explicitly from one session to
another and is not governed by the user ID associated with a session.

17.4 Placing and Removing a Lock
--------------------------------

When LockManager.lock is performed on a mix:lockable node, the
properties defined in that node type are automatically created and set
as follows:

-  jcr:lockOwner is set to the supplied owner info, the user ID
   associated with the session that set the lock (this is the value
   returned by Session.getUserID) or another implementation-dependent
   string identifying the user.

jcr:lockIsDeep is set to reflect whether the lock is deep or not.

When LockManager.unlock is performed on a locked mix:lockable node,
through a session that owns the lock these two properties are removed.

Additionally, the content repository may give permission to some
sessions to remove locks for which they are not the owner. Typically
such “lock-superuser” capability is intended to facilitate
administrational clean-up of orphaned open-scoped locks.

An attempt to call LockManager.lock or LockManager.unlock for a node
that is not mix:lockable will throw a LockException, as will an attempt
to lock an already locked node or unlock an already unlocked node.

17.5 Lock Token
---------------

The method LockManager.lock returns a Lock object. If the lock is
open-scoped the lock will contain a lock token. A lock token is a string
that uniquely identifies a particular lock and acts as a key granting
lock ownership to any session that hold the token.

In order to use the lock token as a key, it must be added to the
session, thus permitting that session to alter the nodes to which the
lock applies or to remove the lock. When a lock token is attached to a
Session, the session becomes an owner of the lock.

The method LockManager.lock automatically adds the lock token for a
newly placed open-scoped lock to the current session.

The client can also control which lock tokens are attached to the
session through the LockManager methods addLockToken, removeLockToken
and getLockTokens.

17.6 Session-Scoped and Open-Scoped Locks
-----------------------------------------

When a lock is placed on a node, it can be specified to be either a
session-scoped lock or an open-scoped lock. A session-scoped lock
automatically expires when the session through which the lock owner
placed the lock expires. An open-scoped lock does not expire until it is
explicitly unlocked, it times out or an implementation-specific
limitation intervenes.

In the case of open-scoped locks, the lock token must be attached to the
current session in order to alter any nodes locked by that token's lock.

In the case of session-scoped locks, the user need not explicitly do
anything since the lock is automatically associated with the session and
expires with it in any case.

With open–scoped locks the token is automatically attached to the
session. However, the user must additionally ensure that a reference to
the lock token is preserved separately so that it can later be attached
to another session since, presumably, an open-scoped lock is being used
to avoid co-expiration with the initial session. It is for handling
these cases of attaching an existing lock token from a previous session
to a new session that the methods LockManager.addLockToken,
LockManager.removeLockToken and LockManager.getLockTokens are provided
(see §17.11 *LockManager Object*).

To determine an existing lock’s scoping, the method Lock.isSessionScoped
is provided.

If a Lock is session-scoped, the method Lock.isLockOwningSession can be
used to determine whether the current session is the lock owner.

An implementation *may* support simultaneous ownership of open-scoped
locks across sessions.

17.7 Effect of a Lock
---------------------

If a lock applies to a node (i.e., the node either holds the lock or is
a descendant of a node holding a deep lock), then to all sessions except
the lock-owning session, the same restrictions apply with respect to the
node as would apply if the node were protected (see §3.7.2.2
*Protected*).

Removing a node is considered an alteration of *its parent*. This means
that a node within the scope of a lock may be removed by a session that
is not an owner of that lock, assuming no other restriction prevents the
removal. Similarly, a locked node and its subgraph may be moved by a
non-lock-owning session if no restriction prevents the alteration of the
source and destination parent nodes.

Locked nodes can always be read and copied by any session with
sufficient access privileges.

When an action is prevented due to a lock, a LockException is thrown
either immediately or on the subsequent save. Implementations may differ
on which of these behaviors is used to enforce locking.

There is at most one lock on any node at one time.

17.8 Timing Out
---------------

Implementations may support client-supplied timeout information, but are
not required to do so. Additionally, an implementation may remove
(unlock) any lock at any time due to implementation-specific criteria.

17.9 Locks and Persistence
--------------------------

When a new node is added below a deep lock by that lock's owning session
LockManager.isLocked(Node) will report true *even before the node is
persisted*\ :sup:`*`:sup:`21` <#sdfootnote21sym>`__*`. However, since
the node is not visible to other Sessions, its locked status has no
effect until it is persisted.

17.10 Locks and Transactions
----------------------------

Locking and unlocking are treated just like any other operation in the
context of a transaction. For example, consider the following series of
operations:

| *begin*
|  lock
| *do A
* save
| *do B
* save
|  unlock
| *commit*

In this example the lock and unlock have no effect. This series of
operations is equivalent to:

| *begin*
|  *do A
* save
| *do B
* save
| *commit*

The reason for this is that changes to a workspace are only made visible
to other Sessions upon commit of the transaction, and this includes
changes in the locked status of a node. As a result, if a lock is
enabled and then disabled within the same transaction, its effect never
makes it to the persistent workspace and therefore it does nothing.

In order to use locks properly (that is, to prevent the “lost update
problem”), locking and unlocking must be done in separate transactions.
For example:

| *begin*
|  lock
| *commit*

| *begin*
|  *do A
* save
| *do B
* save
|  unlock
| *commit*

This series of operations would ensure that the actions *A* and *B* are
protected by the lock.

17.11 LockManager Object
------------------------

The methods for locking, unlocking and querying the locking status of a
node are found in the LockManager, acquired through

LockManager Workspace.getLockManager().

17.11.1 Locking a Node
~~~~~~~~~~~~~~~~~~~~~~

| Lock LockManager.lock(String absPath,
|  boolean isDeep,
|  boolean isSessionScoped,
|  long timeout,
|  String ownerInfo)

places a lock on the node at absPath. If successful, the node is said to
*hold* the lock.

If isDeep is true then the lock *applies* to the specified node and all
its descendant nodes; if false, the lock applies only to the specified
node. On a successful lock, the jcr:lockIsDeep property of the locked
node is set to this value.

If isSessionScoped is true then this lock will expire upon the
expiration of the current session (either through an automatic or
explicit Session.logout); if false, this lock does not expire until it
is explicitly unlocked, it times out, or it is automatically unlocked
due to an implementation-specific limitation.

The timeout parameter specifies the number of seconds until the lock
times out (if it is not refreshed in the meantime, see §10.11.1
*Refresh*). An implementation may use this information as a hint or
ignore it altogether. Clients can discover the actual timeout by
inspecting the returned Lock object.

The ownerInfo parameter can be used to pass a string holding owner
information relevant to the client. An implementation may either use or
ignore this parameter. If it uses the parameter it must set the
jcr:lockOwner property of the locked node to this value and return this
value on Lock.getLockOwner. If it ignores this parameter the
jcr:lockOwner property (and the value returned by Lock.getLockOwner) is
set to either the value returned by Session.getUserID of the owning
session or an implementation-specific string identifying the owner.

The method returns a Lock object representing the new lock.

If the lock is open-scoped the returned lock will include a lock token.
The lock token is also automatically added to the set of lock tokens
held by the current Session.

The addition or change of the properties jcr:lockIsDeep and
jcr:lockOwner are persisted immediately; there is no need to call save.

It is possible to lock a node even if it is checked-in (see §15.2.2
*Read-Only on Check-In*).

17.11.2 Getting a Lock
~~~~~~~~~~~~~~~~~~~~~~

**Lock LockManager.getLock(String absPath)**

returns the Lock object that applies to the node at absPath. This may be
either a lock on the node itself or a deep lock on a node above that
node.

If the current session holds the lock token for this lock and the lock
is open-scoped, then the returned Lock object contains that lock token
(accessible through Lock.getLockToken). If this Session does not hold
the applicable lock token and the lock is open-scoped, the returned Lock
object *may* return the lock token. Otherwise, the returned Lock object
will not contain the lock token and its Lock.getLockToken method will
return null (see §17.12.4 *Getting a Lock Token*).

17.11.3 Unlocking a Node
~~~~~~~~~~~~~~~~~~~~~~~~

void LockManager.unlock(String absPath)

Removes the lock, and the properties jcr:lockOwner and jcr:lockIsDeep,
from the node at absPath. These changes are persisted automatically;
there is no need to call save. As well, the corresponding lock token is
removed from the set of lock tokens held by the current session.

If this node does not currently hold a lock or holds a lock for which
this Session is not the owner, then a LockException is thrown.

The system may give permission to a non-owning session to unlock a lock.
Typically such “lock-superuser” capability is intended to facilitate
administrational clean-up of orphaned open-scoped locks.

It is possible to unlock a node even if it is checked-in (see §15.2.2
*Read-Only on Check-In*).

17.11.4 Testing for Lock Holding
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

boolean LockManager.holdsLock(String absPath)

returns true if the node at absPath holds a lock; otherwise returns
false. To *hold* a lock means that the node has actually had a lock
placed on it specifically, as opposed to having a lock *apply* to it due
to a deep lock held by a node above.

17.11.5 Testing for Locked Status
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

boolean LockManager.isLocked(String absPath)

returns true if the node at absPath is locked either as a result of a
lock held by the specified node or by a deep lock on a node above that
node; otherwise returns false.

Alternatively, the method

boolean Node.isLocked()

can be used directly on the node in question.

17.11.6 Adding a Lock Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~

void LockManager.addLockToken(String lockToken)

adds the specified lock token to the current session. Holding a lock
token makes this session the owner of the lock specified by that
particular lock token. If the implementation does not support
simultaneous lock ownership this method will transfer ownership of the
lock corresponding to the specified lockToken to the current session,
otherwise the current session will become an additional owner of that
lock. In either case, if the implementation does not support
client-specified lock owner information, this method may cause a change
in the jcr:lockOwner property (and the value returned by
Lock.getLockOwner) of the lock corresponding to the specified lockToken
(see §17.5 *Lock Token*).

17.11.7 Getting Lock Tokens
~~~~~~~~~~~~~~~~~~~~~~~~~~~

String[] LockManager.getLockTokens()

returns an array containing all lock tokens currently held by the
current session. Note that any such tokens will represent open-scoped
locks, since session–scoped locks do not have tokens.

17.11.8 Removing a Lock Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

void LockManager.removeLockToken(String lockToken)

Removes the specified lockToken from the current session, causing the
session to no longer be an owner of the lock associated with the
lockToken. If the implementation does not support client-specified lock
owner information, this method may cause a change in the jcr:lockOwner
property (and the value returned by Lock.getLockOwner) of the lock
corresponding to the specified lockToken (see §17.5 *Lock Token*).

17.12 Lock Object
-----------------

The Lock object represents a lock on a particular node. It is acquired
either on lock creation through LockManager.lock or after lock creation
through LockManager.getLock.

17.12.1 Getting the Lock Owner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

String Lock.getLockOwner()

returns the value of the jcr:lockOwner property. This is either the
client-supplied lock owner information, the user ID bound to the session
that holds the lock or an implementation-specific string identifying the
user (see §4.4.1 *User*).

The lock owner's identity is only provided for informational purposes.
It does not govern who can perform an unlock or make changes to the
locked nodes; that depends entirely upon the session that holds the lock
token.

17.12.2 Testing Lock Depth
~~~~~~~~~~~~~~~~~~~~~~~~~~

boolean Lock.isDeep()

returns true if this is a deep lock; false otherwise.

17.12.3 Getting the Lock Holding Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Node Lock.getNode()

returns the lock holding node. Note that N.getLock().getNode() (where N
is a locked node) will only return N if N is the lock holder. If N is in
the subgraph of the lock holder, H, then this call will return H.

17.12.4 Getting a Lock Token
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

String Lock.getLockToken()

may return the lock token for this lock. If this lock is open-scoped and
the current session holds the lock token for this lock, then this method
will return that lock token. If the lock is open-scoped and the current
session does not hold the lock token, it *may* return the lock token.
Otherwise this method will return null.

17.12.5 Testing Lock Aliveness
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

boolean Lock.isLive()

returns true if this Lock object represents a lock that is currently in
effect. If this lock has been unlocked either explicitly or due to an
implementation-specific limitation (like a timeout) then it returns
false. Note that this method is intended for those cases where one is
holding a Lock Java object and wants to find out whether the lock (the
repository-level entity that is attached to the lockable node) that this
object originally represented still exists. For example, a timeout or
explicit unlock will remove a lock from a node but the Lock Java object
corresponding to that lock may still exist, and in that case its isLive
method will return false.

17.12.6 Testing Lock Scope
~~~~~~~~~~~~~~~~~~~~~~~~~~

boolean Lock.isSessionScoped()

Returns true if this is a session-scoped lock and the scope is bound to
the current session. Returns false otherwise.

17.12.7 Testing Lock Owning Session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

boolean Lock.isLockOwningSession()

Returns true if the current session is the owner of this lock, either
because it is session-scoped and bound to this session or open-scoped
and this session currently holds the token for this lock. Returns false
otherwise.

17.12.8 Getting Seconds Remaining
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

long Lock.getSecondsRemaining()

If this lock's time-to-live is governed by a timer, the number of
remaining seconds until time out is returned. If this lock's
time-to-live is not governed by a timer, then this method returns
Long.MAX\_VALUE.

17.12.9 Refreshing a Lock
~~~~~~~~~~~~~~~~~~~~~~~~~

void Lock.refresh()

If this lock's time-to-live is governed by a timer, this method resets
that timer. If this lock's time-to-live is not governed by a timer, then
this method has no effect.

17.13 LockException
-------------------

When a method fails due to the presence or absence of a lock on a
particular node a LockException is thrown.

LockException extends RepositoryException, adding the method

String LockException.getFailureNodePath(),

which returns the absolute path of the node that caused the error, or
null if the implementation chooses not to, or cannot, return a path.
