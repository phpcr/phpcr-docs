=========================================================================================
JCR 2.0: 9 Permissions and Capabilities (Content Repository for Java Technology API v2.0)
=========================================================================================

9 Permissions and Capabilities
==============================

9.1 Permissions
---------------

*Permissions* encompass the restrictions imposed by any access control
restrictions that may be in effect upon the content of a repository,
either implementation specific or JCR-defined (see §16 *Access Control
Management*).

In repositories that support *Access Control* this will include the
restrictions governed by privileges but may also include any additional
policy-internal refinements with effects too fine-grained to be exposed
through privilege discovery (see §16.2 *Privilege Discovery*).

Permissions are reported through

boolean Session.hasPermission(String absPath, String actions)

which returns true if this Session has permission to perform all of the
specified actions at the specified absPath and returns false otherwise.
Similarly,

void Session.checkPermission(String absPath, String actions)

throws an AccessDeniedException if the this Session does not have
permission to perform the specified actions and returns quietly if it
does.

The actions parameter is a comma separated list of action strings, of
which there are four, defined as follows:

add\_node: The permission to add a node at absPath.

set\_property: The permission to set (add or change) a property at
absPath.

remove: The permission to remove an item at absPath.

read: The permission to retrieve (and read the value of, in the case of
a property) an item at absPath.

The permission actions add\_node, set\_property and remove will only be
relevant in a *writable repository*. In a read-only repository they will
always return false.

The information returned through these methods only reflects access
control-related restrictions, not other kinds of restrictions such as
node type constraints. For example, even though hasPermission may
indicate that a particular Session may add a property at /A/B/C, the
node type of the node at /A/B may prevent the addition of a property
called C.

Methods for testing restrictions more broadly are provided by the
*capabilities* feature (see §9.2 *Capabilities*). For information on the
relationships among *permissions*, *privileges* and *capabilities*, see
§16.6 *Privileges Permissions and Capabilities*.

9.2 Capabilities
----------------

*Capabilities* encompass the restrictions imposed by permissions, but
also include any further restrictions unrelated to access control. The
method

| boolean Session.hasCapability(String methodName,
|  Object target,
|  Object[] arguments)

checks whether an operation can be performed given as much context as
can be determined by the repository, including:

-  Permissions granted to the current user, including access control
   privileges.

-  Current state of the target object (reflecting locks, checked-out
   status, retention and hold status etc.).

-  Repository capabilities.

-  Node type-enforced restrictions.

-  Repository configuration-specific restrictions.

The implementation of this method is best effort: returning false
guarantees that the operation cannot be performed, but returning true
does not guarantee the opposite.

The methodName parameter identifies the method in question by its name
as defined in the Javadoc.

The target parameter identifies the object on which the specified method
is called.

The arguments parameter contains an array of type Object consisting of
the arguments to be passed to the method in question. In cases where a
parameter is a Java primitive type it must be converted to its
corresponding Java object form.

For example, given a Session S and Node N then

boolean b = S.hasCapability("addNode", N, new Object[]{"foo"});

will result in b == false if a child node called foo cannot be added to
the node N within the session S.
