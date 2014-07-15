==========================================================================
JCR 2.0: 21 Transactions (Content Repository for Java Technology API v2.0)
==========================================================================

21 Transactions
===============

A repository may support *transactions*.

Whether a particular implementation supports transactions can be
determined by querying the repository descriptor table with

Repository.OPTION\_TRANSACTIONS\_SUPPORTED.

A return value of true indicates support for transactions (see
*Repository Descriptors*).

A repository that supports transactions must adhere to the Java
Transaction API (JTA)
specification\ :sup:``:sup:`23` <#sdfootnote23sym>`__`.

The actual methods used to control transaction boundaries are not
defined by this specification. For example, there are no *begin*,
*commit* or *rollback* methods in JCR API. These methods are defined by
the JTA specification.

The JTA provides for two general approaches to transactions, container
managed transactions and user managed transactions. In the first case,
container managed transactions, the transaction management is taken care
of by the application server and it is entirely transparent to the
application using the API. The JTA interfaces
javax.transaction.TransactionManager and javax.transaction.Transaction
are the relevant ones in this context (though the client, as mentioned,
will never have a need to use these).

In the second case, user managed transactions, the application using the
API may choose to control transaction boundaries from within the
application. In this case the relevant interface is
javax.transaction.UserTransaction. This is the interface that provides
the methods begin, commit, rollback and so forth. Note that behind the
scenes the javax.transaction.TransactionManager and
javax.transaction.Transaction are still employed, but again, the client
does not deal with these.

A content repository implementation must support both of these
approaches if it supports transactions.

21.1Container Managed Transactions: Sample Request Flow
-------------------------------------------------------

| Transactional
| Application

| 

| 

| 

| Application
| Server

| 

| 

| 

| Transaction
| Manager

| 

| 

| 

XARepository

| 

| 

| 

XASession

| 

| 

| 

XAResource

| 

| 

| 

| |image0|\ |image1|
| |image2|\ |image3|\ |image4|\ |image5|\ |image6|

begin

| 

| 

| 

|image7|\ |image8|

getSession

| 

| 

| 

|image9|

login

| 

| 

| 

|image10|\ |image11|

new

| 

| 

| 

new

| 

| 

| 

|image12|\ |image13|\ |image14|\ |image15|

getXAResource

| 

| 

| 

|image16|

enlistResource

| 

| 

| 

|image17|

start

| 

| 

| 

|image18|\ |image19|\ |image20|

application performs operations

| 

| 

| 

|image21|

logout

| 

| 

| 

|image22|

delistResource

| 

| 

| 

|image23|

end

| 

| 

| 

|image24|

commit

| 

| 

| 

|image25|

prepare

| 

| 

| 

|image26|

commit

| 

| 

| 

| |image27|\ |image28|\ |image29|\ |image30|\ |image31|\ |image32|\ |image33|\ |image34|\ |image35|

| 

| 

| 

21.2 User Managed Transactions: Sample Code
-------------------------------------------

// Get user transaction (for example, through JNDI)

UserTransaction utx = ...

| 

// Get a node

Node n = ...

| 

// Start a user transaction

utx.begin();

| 

// Do some work

n.setProperty("myapp:title", "A Tale of Two Cities")

n.save();

| 

// Do some more work

n.setProperty("myapp:author", "Charles Dickens")

n.save();

| 

// Commit the user transaction

utx.commit();

21.3 Save vs. Commit
--------------------

Throughout this specification we often mention the distinction between
*transient* and *persistent* levels. The persistent level refers to the
(one or more) workspaces that make up the actual content storage of the
repository. The transient level refers to in-memory storage associated
with a particular Session object.

In these discussions we usually assume that operations occur outside the
context of transactions; it is assumed that save and other
workspace-altering methods immediately effect changes to the persistent
layer, causing those changes to be made visible to other sessions.

*This is not the case, however, once transactions are introduced*.
Within a transaction, changes made by save (or other, workspace-direct,
methods) are transactionalized and are only persisted and published
(made visible to other sessions), upon commit of the transaction. A
rollback will, conversely, revert the effects of any saves or
workspace-direct methods called within the transaction.

Note, however, that changes made in the transient storage are *not*
recorded by a transaction. This means that a rollback will not revert
changes made to the transient storage of the Session. After a rollback
the Session object state will still contain any pending changes that
were present before the rollback.

21.4 Single Session Across Multiple Transactions
------------------------------------------------

Because modifications in the transient layer are not transactionalized,
the possibility exists for some implementations to allow a Session to be
shared across transactions. This possibility arises because in JTA, an
XAResource may be successively associated with different global
transactions and in many implementations the natural mapping will be to
make the Session implement the XAResource. The following code snippet
illustrates how an XAResource may be shared across two global
transactions:

| // Associate the resource (our Session) with a global
| // transaction xid1
| res.start(xid1, TMNOFLAGS);
| // Do something with res, on behalf of xid1
| // ...

| 
| // Suspend work on this transaction
| res.end(xid1, TMSUSPEND);
| // Associate (the same!) resource with another
| // global transaction xid2
| res.start(xid2, TMNOFLAGS);
| // Do something with res, on behalf of xid2
| // ...
| // End work
| res.end(xid2, TMSUCCESS);
| // Resume work with former transaction
| res.start(xid1, TMRESUME);
| // Commit work recorded when associated with xid2
| res.commit(xid2, true);

| 
| In cases where the XAResource corresponds to a Session (that is,
probably most implementations), items that have been obtained in the
context of xid1 would still be valid when the Session is effectively
associated with xid2. In other words, all transactions working on the
same Session would share the transient items obtained through that
Session.

In those implementations that adopt a copy-on-read approach to transient
storage (see §10.11.9 *Seeing Changes Made by Other Sessions*) this will
mean that the a session is disassociated from a global transaction. This
is however, outside the scope of this specification.

.. |image0| image:: jcr-spec_html_m56b9e288.gif
.. |image1| image:: jcr-spec_html_m56b9e288.gif
.. |image2| image:: jcr-spec_html_m56b9e288.gif
.. |image3| image:: jcr-spec_html_m56b9e288.gif
.. |image4| image:: jcr-spec_html_m56b9e288.gif
.. |image5| image:: jcr-spec_html_m56b9e288.gif
.. |image6| image:: jcr-spec_html_2c90ff11.gif
.. |image7| image:: jcr-spec_html_m696e4930.gif
.. |image8| image:: jcr-spec_html_m7bdceca7.gif
.. |image9| image:: jcr-spec_html_1a83eba0.gif
.. |image10| image:: jcr-spec_html_2c90ff11.gif
.. |image11| image:: jcr-spec_html_1a83eba0.gif
.. |image12| image:: jcr-spec_html_6fb3411e.gif
.. |image13| image:: jcr-spec_html_m696e4930.gif
.. |image14| image:: jcr-spec_html_m696e4930.gif
.. |image15| image:: jcr-spec_html_6dd64a19.gif
.. |image16| image:: jcr-spec_html_2c90ff11.gif
.. |image17| image:: jcr-spec_html_6dd64a19.gif
.. |image18| image:: jcr-spec_html_m696e4930.gif
.. |image19| image:: jcr-spec_html_m696e4930.gif
.. |image20| image:: jcr-spec_html_m5007cd92.gif
.. |image21| image:: jcr-spec_html_m5007cd92.gif
.. |image22| image:: jcr-spec_html_2c90ff11.gif
.. |image23| image:: jcr-spec_html_6dd64a19.gif
.. |image24| image:: jcr-spec_html_2c90ff11.gif
.. |image25| image:: jcr-spec_html_6dd64a19.gif
.. |image26| image:: jcr-spec_html_6dd64a19.gif
.. |image27| image:: jcr-spec_html_m696e4930.gif
.. |image28| image:: jcr-spec_html_m696e4930.gif
.. |image29| image:: jcr-spec_html_m696e4930.gif
.. |image30| image:: jcr-spec_html_m696e4930.gif
.. |image31| image:: jcr-spec_html_m696e4930.gif
.. |image32| image:: jcr-spec_html_5cea72e2.gif
.. |image33| image:: jcr-spec_html_5cea72e2.gif
.. |image34| image:: jcr-spec_html_733aaa7.gif
.. |image35| image:: jcr-spec_html_410fb51a.gif
