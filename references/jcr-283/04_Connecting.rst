=======================================================================
JCR 2.0: 4 Connecting (Content Repository for Java Technology API v2.0)
=======================================================================

4 Connecting
============

4.1 Repository Object
---------------------

To begin using a repository, an application must acquire a Repository
object.

Access to a Repository object may be provided through a number of
standard Java naming and discovery mechanisms, but *must* at the minimum
be provided through an implementation of the RepositoryFactory
interface.

Any implementation of RepositoryFactory must have a zero-argument public
constructor. Repository factories may be installed in an instance of the
Java platform as extensions, that is, jar files placed into any of the
usual extension directories. Factories may also be made available by
adding them to the applet or application class path or by some other
platform-specific means.

A repository factory implementation should support the Java Standard
Edition Service Provider
mechanism\ :sup:``:sup:`9` <#sdfootnote9sym>`__`, that is, an
implementation should include the file
META-INF/services/javax.jcr.RepositoryFactory. This file contains the
fully qualified name of the class that implements RepositoryFactory.

Once the RepositoryFactory is acquired, the Repository object itself is
acquired through

Repository RepositoryFactory.getRepository(Map parameters)

which attempts to retrieve a Repository object using the given
parameters.

Parameters are passed in a Map of String key/value pairs. The keys are
not specified by JCR and are implementation specific. However, vendors
should use keys that are namespace qualified in the Java package style
to distinguish their key names. Alternatively, a client may request a
default repository instance by passing a null.

The implementation must return null if a default repository instance is
requested and the factory is not able to identify such a repository or
if parameters are passed and the factory does not understand them. See
the associated Javadoc for example connection code.

4.1.1 Example Repository Acquisition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An application may explicitly specify the repository factory
implementation. For example:

Map parameters = new HashMap();

| 

parameters.put("com.vendor.address",

"vendor://localhost:9999/repo");

| 

RepositoryFactory factory = (RepositoryFactory)

Class.forName("com.vendor.RepositoryFactoryImpl");

| 

Repository repo = factory.getRepository(parameters);

Some implementations may allow acquisition of a RepositoryFactory
through the ServiceLoader in Java SE 6. For example:

Map parameters = new HashMap();

| 

parameters.put("com.vendor.address",

"vendor://localhost:9999/repo");

| 

Repository repo = null;

| 

for (RepositoryFactory factory :

ServiceLoader.load(RepositoryFactory.class)) {

repo = factory.getRepository(parameters);

if (repo != null) {

// factory accepted parameters

break;

}

}

Note that in Java SE prior to version 6, one may use the class
javax.imageio.spi.ServiceRegistry to look up the available
RepositoryFactory implementations.

4.1.2 Thread Safety
~~~~~~~~~~~~~~~~~~~

A repository implementation must provide thread-safe implementations of
all the methods of the RepositoryFactory and Repository interfaces. A
repository implementation is not required to provide thread-safe
implementations of any other interface. As a consequence, an application
which concurrently or sequentially operates against objects having
affinity to a particular Session through more than one thread must
provide synchronization sufficient to ensure no more than one thread
concurrently operates against that Session and changes made by one
thread are visible to other threads.

4.2 Login
---------

Interaction with the repository begins with the user acquiring a Session
through a call to Repository.login. In the most general case, the client
supplies a Credentials object and a workspace name:

| Session Repository.login(Credentials credentials,
|  String workspaceName).

Other signatures of login are also provided (see §4.2.4 *External
Authentication*).

4.2.1 Credentials
~~~~~~~~~~~~~~~~~

The Credentials interface is an empty marker for the object that carries
the information necessary to authenticate and authorize the user. A
repository may use the supplied SimpleCredentials implementation or its
own implementation.

4.2.2 Guest Credentials
~~~~~~~~~~~~~~~~~~~~~~~

GuestCredentials is used to acquire an anonymous session.

4.2.3 Workspace Name
~~~~~~~~~~~~~~~~~~~~

The workspaceName passed on login identifies one of the persistent
workspaces of the repository. More than one Session can be
simultaneously bound to the same persistent workspace.

4.2.4 External Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By providing a signature of Repository.login that does not require
Credentials, the content repository allows for authorization and
authentication to be handled by JAAS (or another external mechanism) if
the implementer so chooses.

To use such an external mechanism to create sessions with end-user
identity, invocations of the Repository.login method that do not specify
Credentials (i.e., either a null Credentials is passed or a signature
without the Credentials parameter is used) should obtain the identity of
the already-authenticated user through that external mechanism.

4.3 Impersonate
---------------

A client may also open a new Session from within an existing one using

Session Session.impersonate(Credentials credentials).

The returned Session is bound to the same workspace as the current
Session, though it may (and typically will) have a different
authorization. The implementation is free to take both the supplied
Credentials and the authorization of the current Session into account in
determining the authorization of the returned Session.

4.4 Session
-----------

The Session object is granted a set of permissions toward the specified
persistent workspace. These are determined by the Session's credentials
combined with any access control restrictions, either JCR-defined or
implementation-specific, which may apply (see §9.1 *Permissions*).

4.4.1 User
~~~~~~~~~~

Each Session has a user ID, accessed through

String Session.getUserID().

How the user ID is set is up to the implementation. It may be passed in
as part of the Credentials or it may be acquired in some other way. This
method is free to return an “anonymous user ID” or null.

4.4.2 Attributes
~~~~~~~~~~~~~~~~

A Session may have arbitrary, implementation-specific named attributes
bound to its Credentials. The method

String[] Session.getAttributeNames()

returns the set of attribute names, and the method

Object Session.getAttribute(String name)

returns the value of a named attribute.

4.4.3 Session to Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Repository object through which a Session was acquired is retrieved
with

Session.getRepository().

4.4.4 Live Status
~~~~~~~~~~~~~~~~~

The method

boolean Session.isLive()

is used to check whether a Session object represents a live, logged-in
session.

4.4.5 Logout
~~~~~~~~~~~~

A Session is closed using

void Session.logout().

4.5 Workspace
-------------

Though more than one Session can be bound to the same *persistent
workspace*, each Session object has a single distinct corresponding
Workspace object that *represents* the actual persistent workspace to
which the Session is bound. A Workspace object can be thought of as a
*view* on to the persistent workspace as seen through the permissions
granted to its corresponding Session (see §10 *Writing*).

4.5.1 Session to Workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~

Workspace Session.getWorkspace().

returns the Workspace object representing the actual persistent
workspace to which a Session is bound.

Despite their one-to-one relationship, Session and Workspace are defined
as distinct interfaces in order to separate two types of write behavior:
*transient* vs. *immediately persistent*, though this distinction is
only strictly relevant in writable repositories.

4.5.2 Workspace to Session
~~~~~~~~~~~~~~~~~~~~~~~~~~

Session Workspace.getSession()

returns the Session object to which a Workspace object is bound.

4.5.3 Workspace Name
~~~~~~~~~~~~~~~~~~~~

String Workspace.getName()

returns the name of the persistent workspace represented by a Workspace
object.

4.5.4 Accessible Workspaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~

String[] Workspace.getAccessibleWorkspaceNames()

returns an array holding the names of all persistent workspaces
accessible from a Workspace object. Accessibility is determined by the
permissions granted to the Session to which the Workspace object is
bound. In order to access one of the listed workspaces, the user
performs another Repository.login, specifying the name of the desired
workspace, and receives a new Session object.
