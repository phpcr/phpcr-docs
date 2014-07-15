====================================================================
JCR 2.0: 11 Import (Content Repository for Java Technology API v2.0)
====================================================================

11 Import
=========

A repository may support the bulk *import* of content from XML. Two XML
mappings are defined: *document view* and *system view*. The former is
used primarily for the import of arbitrary XML into the repository while
the latter is a full serialization of repository content (see §7
*Export*). A repository that supports import must support both formats.

Whether an implementation supports import can be determined by querying
the repository descriptor table with

Repository.OPTION\_XML\_IMPORT\_SUPPORTED.

A return value of true indicates support (see §24.2 *Repository
Descriptors*).

11.1 Importing Document View
----------------------------

The *document view* XML mapping (see §7.3 *Document View*) allows the
import of arbitrary XML into the repository. On import, the repository
first checks if the incoming XML appears to be a system view document.
If it does not, then it is assumed to be in document view form, and the
following occurs:

#. For each XML namespace declaration with prefix P and URI U:

   #. If the namespace registry already contains a mapping of some
      prefix P' to U (where P' may or may not be equal to P) then the
      namespace registry is left unchanged.

   #. If the namespace registry does not contain a mapping to U then
      such a mapping is added to the registry. The prefix assigned may
      be *P*, if *P* is not already used in the registry, otherwise the
      repository must generate and assign a new, previously unused,
      prefix.

#. Each XML element E becomes a JCR node of the same name, E.

#. The node type of the JCR node E is determined by the implementation
   in accordance with its policy on respecting property semantics (see
   §11.3 *Respecting Property Semantics* and §11.4 *Determining Node
   Types*).

#. Each child XML element C of XML element E becomes a JCR child node C
   of node E.

#. Each XML attribute A within an XML element E becomes a property A of
   JCR node E. The value of each XML attribute A becomes the value of
   the corresponding property A.

#. The type of each imported property is determined by the
   implementation in accordance with its policy on respecting property
   semantics (see §11.3 *Respecting Property Semantics* and §11.4
   *Determining Node Types*).

#. Escape sequences representing non-XML-valid characters in element
   names and whitespace in attribute values may be encountered (for
   example, if the incoming XML stream is the product of an earlier
   document view export). In such cases, whether the escape sequences
   are decoded is left up to the implementation. Note that the
   predefined entity references &amp;, &lt;, &gt;, &apos; and &quot;, as
   well as all other entity and character references, must be decoded in
   any case, in accordance with the XML specification.

#. An implementation that respects node type information may be able to
   determine whether a particular attribute is intended to be a single
   or multi-value property, and treat any spaces embedded in the value
   accordingly (either as delimiters or as literal spaces).
   Implementations are also free to rely on information external to this
   specification (such as any schema associated by the incoming XML) to
   help determine the intended interpretation of whitespace within a
   particular incoming attribute value.

#. Text within an XML element E becomes a STRING property called
   jcr:xmlcharacters of a JCR node called jcr:xmltext, which itself
   becomes a JCR child node of the node E. The value of
   E/jcr:xmltext/jcr:xmlcharacters will be the character data passed to
   ContentHandler.characters.

#. If import is done through the ContentHandler returned by
   getImportContentHandler, data passed to
   ContentHandler.ignorableWhitespace is ignored.

#. If import is done through importXML, pure whitespace between elements
   (that is, a string containing no non-whitespace characters) is
   ignored. However, whitespace leading, trailing and between
   non-whitespace characters is included in the text that is stored in
   E/jcr:xmltext/jcr:xmlcharacters.

11.1.1 Roundtripping
~~~~~~~~~~~~~~~~~~~~

Not all information within the infoset of an XML document is maintained
on import to document view. Information lost will include processing
instructions, the distinction between text and CDATA and namespace
scoping at the sub-document level. As a result, perfect roundtripping of
a full XML infoset is not possible through document view.

On document view import, the repository will automatically add
repository metadata in the form of JCR properties (at least
jcr:primaryType, for example), if these are not already present in the
incoming XML. When re-exported using document view, the resulting XML
will contain these properties in the form of XML attributes. As a
result, the application must take care of stripping out unwanted
repository metadata.

11.2 Import System View
-----------------------

Given a system view XML document the subgraph constructed upon import is
determined by reversing the mapping discussed in §7.2 *System View*.
Though the mapping is largely straightforward some special
considerations are discussed in §11.3 *Respecting Property Semantics*
and §11.9 *Importing jcr:root*.

11.3 Respecting Property Semantics
----------------------------------

During either system or document view import, XML elements (in system
view) or XML attributes (in document view) may be encountered that
correspond to JCR properties with repository-level semantics such as the
jcr-prefixed properties of such node types as nt:base, mix:referenceable
or mix:versionable, among others.

When an element or attribute representing such a property is
encountered, an implementation may either *skip* it or *respect* it.

-  A repository that respects a particular element or attribute must
   import it and alter the internal state of the repository in
   accordance with the semantics of the property given the configuration
   of that repository instance. For example, a repository that respects
   jcr:primaryType will attempt to create a node of the indicated
   primary node type. If that node type is not supported, the repository
   will throw an exception.

-  A repository that skips an element or attribute must not import it
   all. *It must not import it but then ignore the semantics of the
   resulting property*.

The implementation-specific policy regarding what to skip and what to
respect must be internally consistent. For example, it makes no sense to
skip jcr:mixinTypes (thus missing the presence of mix:lockable, for
example) and yet respect jcr:lockOwner and jcr:lockIsDeep.

If an implementation chooses to skip jcr:primaryType, the node type of
the imported node is determined by the implementation (see §11.5
*Determining Node Types*).

11.4 Determining Node Types
---------------------------

In cases of XML import where primary node type information is
unavailable, either because it is skipped or because it is not available
(as is the case on document view import of arbitrary XML), the
implementation must determine an appropriate node type to assign to each
newly created node. How this is done is implementation-dependent.

11.5 Determining Property Types
-------------------------------

On import of arbitrary XML using document view, the implementation must
determine a suitable property type for each incoming property.
Determination of the property type must be done as follows:

-  If the property type is determinable from the node type assigned to
   its node (regardless of how this node type is itself determined; see
   §11.5 *Determining Node Types*) then that property type is used.

-  If the property type is not determinable from the node type assigned
   to its node then the determination of the property is left up to the
   implementation. For example, an implementation may use STRING
   properties exclusively, or attempt to “guess” the type according to
   an analysis of the content.

11.6 Event-Based Import Methods
-------------------------------

The Workspace and Session interfaces provide the following event-based
import methods:

| org.xml.sax.ContentHandler
|  Workspace.getImportContentHandler(String parentAbsPath,
|  int uuidBehavior)

and

| org.xml.sax.ContentHandler
|  Session.getImportContentHandler(String parentAbsPath,
|  int uuidBehavior)

These methods return an org.xml.sax.ContentHandler without altering
either the Workspace or Session. The actual changes to the repository
are made through the methods of the
ContentHandler\ :sup:``:sup:`19` <#sdfootnote19sym>`__`. Invalid XML
data will cause the ContentHandler to throw a SAXException.

If the incoming XML is a *system view* XML document then it is
interpreted as such, otherwise it is imported as *document view*.

The incoming XML is imported into a subgraph of items immediately below
the node at parentAbsPath.

11.6.1 Workspace Event-Based Import
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ContentHandler acquired through the Workspace method dispatches
changes immediately. Node type constraints are enforced by the
ContentHandler by throwing a SAXException during deserialization.
However, which node type constraints are enforced depends upon whether
node type information in the imported data is respected, and this is an
implementation-specific issue (see §11.3 *Respecting Property
Semantics*).

11.6.2 Session Event-Based Import
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ContentHandler acquired through the Session will build the graph of
new items in the transient session store. The changes are then
dispatched on save.

Different node type constraints may be enforced at different times.
Those that would be immediately enforced on a core write method (see
§10.2 *Core Write Methods*) of that particular implementation will cause
the returned ContentHandler to throw an immediate SAXException. All
other node type constraints are enforced as they would be if made
through the core write methods. However, which node type constraints are
enforced also depends upon whether node type information in the imported
data is respected, which is an implementation-specific issue (see §11.3
*Respecting Property Semantics*).

11.7 Stream-Based Import Methods
--------------------------------

The Workspace and Session interfaces provide the following stream-based
import methods:

| void Workspace.importXML(String parentAbsPath,
|  InputStream in,
|  int uuidBehavior)

and

| void Session.importXML(String parentAbsPath,
|  InputStream in,
|  int uuidBehavior)

These methods import the XML document in the input stream and add the
resulting item subgraph as a child of the node at parentAbsPath. If the
incoming XML is a *system view* XML document then it is interpreted as
such, otherwise it is imported as *document view*.

11.7.1 Workspace Stream-Based Import
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Workspace.importXML changes are dispatched immediately. Node type
constraints are enforced by throwing a ConstraintViolationException.
However, which node type constraints are enforced depends upon whether
node type information in the imported data is respected, which is an
implementation-specific issue (see §11.3 *Respecting Property
Semantics*).

11.7.2 Session Stream-Based Import
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Session.importXML changes remain pending until dispatched on save.
Node type constraints that would be immediately enforced on a core write
method (see §10.2 *Core Write Methods*) of that particular
implementation will cause an immediate ConstraintViolationException
during import. All other node type constraints are enforced as they
would be if made through the core write methods. However, which node
type constraints are enforced depends upon whether node type information
in the imported data is respected, and this is an
implementation-specific issue (see §11.3 *Respecting Property
Semantics*).

11.8 Identifier Handling
------------------------

The uuidBehavior flag governs how the identifiers of imported nodes are
handled. There are four options, defined as constants in the interface
javax.jcr.ImportUUIDBehavior:

11.8.1 Create New Identifiers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IMPORT\_UUID\_CREATE\_NEW: Incoming nodes are assigned newly created
identifiers upon addition to the workspace. As a result, identifier
collisions never occur.

11.8.2 Remove Existing Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~

IMPORT\_UUID\_COLLISION\_REMOVE\_EXISTING: If an incoming non-shareable
node has the same identifier as a node already existing in the workspace
then the already existing node (and its subgraph) is removed from
wherever it may be in the workspace before the incoming node is added.
Note that this can result in nodes “disappearing” from locations in the
workspace that are remote from the location to which the incoming
subgraph is being written. In the case of shareable node, however, the
behavior differs (see §14.1.2 *Shared Node Creation on Import*).

11.8.3 Replace Existing Node
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IMPORT\_UUID\_COLLISION\_REPLACE\_EXISTING: If an incoming non-shareable
node has the same identifier as a node already existing in the
workspace, then the already existing node is replaced by the incoming
node in the same position as the existing node. Note that this may
result in the incoming subgraph being disaggregated and “spread around”
to different locations in the workspace. In the most extreme case this
behavior may result in no node at all being added as child of
parentAbsPath. This will occur if the topmost element of the incoming
XML has the same identifier as an existing node elsewhere in the
workspace. In the case of shareable node, however, the behavior differs
(see §14.1.2 *Shared Node Creation on Import*).

11.8.4 Throw on Identifier Collision
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

IMPORT\_UUID\_COLLISION\_THROW: If an incoming non-shareable node has
the same identifier as a node already existing in the workspace, then
either a SAXException is thrown by the ContentHandler (in the case of
event-based import) or an ItemExistsException is thrown by the importXML
method (in the case of stream-based import). In the case of shareable
nodes, the behavior differs (see §14.1.2 *Shared Node Creation on
Import*).

11.8.5 Usage of Term UUID
~~~~~~~~~~~~~~~~~~~~~~~~~

The term “UUID” occurs in the names of certain properties, classes and
methods in JCR 1.0. This usage is maintained in JCR 2.0 to preserve
compatibility with JCR 1.0. However, in the context of JCR 2.0 these
names should be understood to apply to identifiers *in general* and not
just identifiers that use of the UUID syntax, or that possess global
uniqueness.

11.9 Importing *jcr:root*
-------------------------

If the root node of a workspace is exported it will be rendered in XML
(in either view) under the name jcr:root. In addition, if the root node
is referenceable this will be recorded in the serialization of the
jcr:uuid property.

If this XML document is imported back into the workspace a number of
different results may occur, depending on the methods and settings used
to perform the import. The following summarizes the possible results of
using various uuidBehavior values (in either using either
Workspace.getImportContentHandler or Workspace.importXML) when a node
with the same identifier as the existing root node is encountered on
import (the constants below are defined in the interface
javax.jcr.ImportUUIDBehavior).

IMPORT\_UUID\_CREATE\_NEW: The XML element representing jcr:root is
rendered as a normal node at the position specified (with the name
jcr:root). It gets a new identifier, so there is no effect on the
existing root node of the workspace.

IMPORT\_UUID\_COLLISION\_REMOVE\_EXISTING: If deserialization is done
through a ContentHandler (acquired by getImportContentHandler) a
SAXException will be thrown. Similarly, if deserialization is done
through importXML a ConstraintViolationException will be thrown. Note
that this is simply a special case of the general rule that under this
uuidBehavior setting, an exception will be thrown on any attempt to
import a node with the same identifier as the node at parentAbsPath *or
any of its ancestors* (which, of course, includes the root node).

IMPORT\_UUID\_COLLISION\_REPLACE\_EXISTING: This setting is equivalent
to importing into the Session and then calling save since save always
operates according to identifier. In both cases the result is that the
root node of the workspace will be replaced along with its subgraph
(i.e., the whole workspace), just as if the root node had been altered
through the normal getNode-\ *make* *change*-save cycle.

IMPORT\_UUID\_COLLISION\_THROW: Under this setting a ContentHandler will
throw a SAXException and the importXML method will throw
ItemExistsException.

Note that an implementation is always free to prevent the replacement of
a root node (or indeed any node) either through access control
restrictions or other implementation-specific restrictions.
