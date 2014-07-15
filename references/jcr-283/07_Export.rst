===================================================================
JCR 2.0: 7 Export (Content Repository for Java Technology API v2.0)
===================================================================

7 Export
========

A JCR repository must support export of content to two XML formats:
*system view* and *document view*.

7.1 Exporting a Subgraph
------------------------

Export operates on a subgraph of a workspace. Given a repository *R*
with workspace *W* and a node *N* within *W* the following sections
describe the algorithm for producing the system view and document view
serializations of the subgraph rooted at *N*.

In a repository that supports *shareable nodes* the set of nodes below
*N* may not be a tree, it may, more generally, be a subgraph with unique
source *N* (see §3.9 *Shareable Nodes Model*).

7.2 System View
---------------

The exported system view XML document is constructed as follows:

#. For every namespace used within the subgraph rooted at *N*, the
   corresponding JCR namespace mapping in the current session *is
   included* as an XML namespace declaration such that any use of a
   namespace prefix is within the scope of the appropriate namespace
   declaration.

#. Other JCR namespace mappings in the current session *may be included*
   as XML namespace declarations in the exported document.

#. The JCR namespace mapping of the prefix xml *may be excluded* from
   the namespace declarations in the exported document.

#. A namespace declaration for the URI http://www.jcp.org/jcr/sv/1.0, is
   included such that any use of the corresponding namespace prefix is
   within the scope of the declaration. In this section the prefix sv is
   assumed, making the declaration
   xmlns:sv=“http://www.jcp.org/jcr/sv/1.0”.

#. Each JCR node becomes an XML element <sv:node>.

#. Each JCR property becomes an XML element <sv:property>.

#. The name of each JCR node or property becomes the value of the
   sv:name attribute of the corresponding <sv:node> or <sv:property>
   element.

#. If the root node of a workspace is included in the serialized
   subgraph, it receives the name jcr:root.

#. The property type of each content repository property is recorded in
   the sv:type attribute of the corresponding <sv:property> element,
   using the standard string forms for property type names as returned
   by the method PropertyType.nameFromValue.

#. The value of each BINARY JCR property is
   Base64\ :sup:``:sup:`12` <#sdfootnote12sym>`__` encoded and the
   resulting string is included as XML text within an <sv:value> element
   within the <sv:property> element.

#. The value of each non-BINARY JCR property is converted to string form
   according to the standard conversion (see §3.6.4 *Property Type
   Conversion*) and the resulting string is included as XML text within
   an <sv:value> element within the <sv:property> element.

   #. Entity references are used to escape characters which cannot be
      included as literals within XML text (see §7.5 *Escaping of
      Values*).

   #. If, after conversion to string and entity escaping is performed,
      the string form of a value still contains characters which cannot
      appear in an XML document (neither as literals nor as character
      references\ :sup:``:sup:`13` <#sdfootnote13sym>`__`) then:

      #. The string form is further encoded using Base64 encoding.

      #. The attribute xsi:type=“xsd:base64Binary” is added to the
         <sv:value> element.

      #. The namespace mappings for xsi and xsd are added to the
         exported XML document so that the xsi:type attribute is within
         their scope. The namespace declarations required are
         xmlns:xsd=“http://www.w3.org/2001/XMLSchema” and
         xmlns:xsi=“http://www.w3.org/2001/XMLSchema-instance”. Note
         that the prefixes representing these two namespaces need not be
         *literally* “xsd” and “xsi”. Any two prefixes are permitted as
         long as the corresponding namespace declarations are changed
         accordingly.

#. A multi-value property is converted to an <sv:property> element
   containing multiple <sv:value> elements. The order of the <sv:value>
   elements reflects the order of the value array returned by
   Property.getValues. If a property is multi-valued but happens to have
   only one value, then the attribute sv:multiple=“true” *must* be added
   to the corresponding <sv:property> element. If the property is
   multi-valued and has more than one value then the sv:multiple=“true”
   attribute *may* be added.

#. The hierarchy of the content repository nodes and properties is
   reflected in the hierarchy of the corresponding XML elements.

#. Within an <sv:node> element all <sv:property> subelements must occur
   before the first <sv:node> subelement.

#. The first <sv:property> element in an <sv:node> element must be
   jcr:primaryType (see §3.7.10 *Base Primary Node Type*).

#. If a node has a jcr:mixinTypes property, then the second
   <sv:property> element in the <sv:node> element must be jcr:mixinTypes
   (see §3.7.10 *Base Primary Node Type*).

#. In the case of referenceable nodes, the third <sv:property> element
   in the <sv:node> element must be jcr:uuid (see §3.8.1.1
   *mix:referenceable*).

#. The order of the <sv:node> subelements of a parent <sv:node> must
   reflect the order in which the corresponding child nodes are returned
   by Node.getNodes().

#. Shared nodes are exported as described in §14.7 *Export*.

A writable repository may support import using system view (see §11
*Import*).

7.3 Document View
-----------------

The document view provides a more human-readable serialization than
system view. Unlike system view, document view is lossy. It does not
preserve all information in the subgraph.

#. For every namespace used within the subgraph rooted at *N*, the
   corresponding JCR namespace mapping in the current session *is
   included* in the exported document such that any use of the namespace
   prefix in the exported document is within the scope of the
   appropriate namespace declaration.

#. Other JCR namespace mappings in the current session *may be included*
   as XML namespace declarations in the exported document.

#. The JCR namespace mapping of the prefix xml *may be excluded* from
   the namespace declarations in the exported document.

#. Each JCR node N becomes an XML element of the same name, N.

#. If the root node of a workspace is included in the serialized
   subgraph, it becomes an XML elements with the name jcr:root.

#. Each child node C of N becomes a subelement C of XML element N.

#. The order of the subelements of element N must reflect the order in
   which the corresponding child nodes are returned by Node.getNodes.

#. Each property P of node N becomes an XML attribute P of XML element
   N.

#. If P is a BINARY property its value is Base64 encoded. The resulting
   string becomes the value of the XML attribute P.

#. If P is a non-BINARY property its value is converted to string form
   according to the standard conversion (see §3.6.4 *Property Type
   Conversion*). Entity references are used to escape characters which
   cannot be included as literals within attribute values (see §7.5
   *Escaping of Values*).

A writable repository may **** support document view import (see §11.1
*Importing Arbitrary XML*).

The following sections describe the exceptions to the above general
rules.

7.3.1 XML Text
~~~~~~~~~~~~~~

In a repository that supports it, on document view import XML text is
converted to the special node/property structure
jcr:xmltext/jcr:xmlcharacters (see §11.1 *Importing Document View*).
When this structure is exported back to XML the process is reversed.

If a child node of N called jcr:xmltext is encountered and that
jcr:xmltext node has one and only one child item and that item is a
single-valued property called jcr:xmlcharacters, then the jcr:xmltext
node is not converted into an XML element. Instead, the value of the
jcr:xmlcharacters property becomes text within the body of the XML
element N. Entity references are used to escape characters which cannot
be included as literals within XML text (see §7.5 *Escaping of Values*)
however, escaping of whitespace is not performed (see §7.3.3
*Multi-Value Properties*). Two or more jcr:xmltext nodes adjacent within
the ordering of a child node set will have the values of their
respective jcr:xmlcharacters concatenated into a single resulting XML
text node.

7.3.2 Invalid Item Names
~~~~~~~~~~~~~~~~~~~~~~~~

If the name of a content repository item I is not a valid XML element or
attribute name (as the case may be) then on export the repository may
either ignore the item in question or employ the escaping scheme
described in §7.4 *Escaping of Names*. Which approach is taken is
implementation-dependent.

7.3.3 Multi-Value Properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a multi-value property P is encountered on export, the repository may
either ignore the multi-value property or serialize it as an attribute
whose value is an XML Schema list
type\ :sup:``:sup:`14` <#sdfootnote14sym>`__` (i.e., a
whitespace-delimited list of strings). If the latter approach is taken
then:

-  Each value in the property is converted to a string according to
   standard conversion, see §3.6.4 *Property Type Conversion*. If the
   multi-value property contains no values, then it is serialized as an
   empty string.

-  All literal whitespace within each string is escaped, as well as any
   characters that should not be included as literals in any case, see
   §7.5 *Escaping of Values*.

-  The final attribute value is constructed by concatenating the
   resulting strings, with the addition of the space delimiter, into a
   single string. The order of concatenation must be the same as the
   order in which the values appear in the Value array returned by
   Property.getValues.

-  Furthermore, if multi-value property serialization is supported, then
   a mechanism must be adopted whereby upon re-import the distinction
   between multi- and single- value properties is not lost, see §7.5
   *Escaping of Values*.

-  Note that this escaping of space literals does not apply to the value
   of jcr:xmltext/jcr:xmlcharacters when it is converted to XML text. In
   that case only the standard XML entity escaping is required,
   regardless of whether multi-value property serialization is supported
   (see §7.3.1 *XML Text* and §7.5 *Escaping of Values*).

7.3.4 Invalid Characters in Values
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the string form of the value of property P contains characters which
cannot appear in XML documents at all (neither as literals nor as
character references\ :sup:``:sup:`15` <#sdfootnote15sym>`__`) then the
attribute P is simply excluded from the document view serialization and
does not appear at all.

7.4 Escaping of Names
---------------------

Though a JCR prefix is always a valid XML prefix, the JCR local name may
not be a valid XML name. Consequently, for document view serialization,
each JCR name is converted to a valid XML name (as defined by XML 1.0)
by translating invalid characters into escaped numeric entity
encodings\ :sup:``:sup:`16` <#sdfootnote16sym>`__`.

The escape character is the underscore (“\_”). Any invalid character is
escaped as \_x\ *HHHH*\ \_, where *HHHH* is the four-digit hexadecimal
UTF-16 code for the character. When producing escape sequences the
implementation should use lowercase letters for the hex digits a-f. When
unescaping, however, both upper and lowercase alphabetic hexadecimal
characters must be recognized.

Escaping and unescaping is done by parsing the name from left to right.

The underscore character (“\_”), when appearing as literal, is itself
escaped if it is followed by *xHHHH* where *H* is one of the following
characters: 0123456789abcdefABCDEF.

For example,

“My Documents” is encoded as “My\_x0020\_Documents”.

“My\_Documents” is not encoded.

“My\_x0020Documents” is encoded as “My\_x005f\_x0020Documents”.

“My\_x0020\_Documents” is encoded as “My\_x005f\_x0020\_Documents”.

“My\_x0020 Documents” is encoded as
“My\_x005f\_x0020\_x0020\_Documents”.

7.5 Escaping of Values
----------------------

When a non-BINARY value is serialized during either system view or
document view export, it is first converted to string form using
standard value conversion, see §3.6.4 *Property Type Conversion.* BINARY
values are encoded using Base64. The resulting string then undergoes any
further changes required by the standard XML escaping
rules\ :sup:``:sup:`17` <#sdfootnote17sym>`__`.

In document view serialization, if the property being serialized is
multi-valued (or if the implementation chooses to encode spaces in
single-value properties as well, see below) then the value or values
must be further encoded by escaping any occurrence of one of the four
whitespace characters: space, tab, carriage return and line feed. The
scheme used to encode these characters is the same as that described in
§7.4 *Escaping of Names*. Note that in this restricted context, applying
those escaping rules amounts to the following: a space becomes
\_x0020\_, a tab becomes \_x0009\_, a carriage return becomes \_x000D\_,
a line feed becomes \_x000A\_ and any underscore (\_) that occurs as the
first character of a sequence that could be misinterpreted as an escape
sequence becomes \_x005f\_.

Finally, in document view export, the value of the attribute
representing a multi-value property is constructed by concatenating the
results of the above escaping into a space-delimited list.

In document view export (though not in system view), if multi-value
property serialization is supported (see §7.3.3 *Multi-Value
Properties*) then a mechanism must be adopted whereby upon re-import the
distinction between multi- and single- value properties is not lost. One
option is that escaping of space literals must be applied to the value
of all single-value properties as well. Another option is that when an
XML document is imported in document view, each attribute is assumed to
be a single-value property unless out-of-band information defines it to
be multi-valued (for example, if the applicable node type defines the
property as multi-valued or the XML document is associated with a schema
definition that indicates that the attribute is a list value). The
approach taken is implementation-specific.

Note that the value of a jcr:xmlcharacters property used to represent
XML text (see §7.3.1 *XML Text*) is not space-escaped, regardless of the
prevailing multi-value property serialization policy.

7.6 Export API
--------------

Exported XML can be output either as a stream or as a series of SAX
events. The export methods are found in the Session object.

7.6.1 System View Export
~~~~~~~~~~~~~~~~~~~~~~~~

The methods

| void Session.exportSystemView(String absPath,
|  ContentHandler contentHandler,
|  boolean skipBinary,
|  boolean noRecurse)

and

| void Session.exportSystemView(String absPath,
|  OutputStream out,
|  boolean skipBinary,
|  boolean noRecurse)

serialize the item subgraph starting at absPath.

The first method serializes content to XML as a series of SAX events
triggered by the repository calling the methods of the supplied
org.xml.sax.ContentHandler.

The second method serializes content to an XML stream and outputs it to
the supplied java.io.OutputStream.

The resulting XML is in the system view form.

If skipBinary is true then any properties of type BINARY will be
serialized with empty sv:value elements. In the case of multi-value
BINARY properties, the number of values in the property will be
reflected in the serialized output, though they will all be empty.

If skipBinary is false then the actual values of each BINARY property
are serialized.

If noRecurse is true then only the node at absPath and its properties,
but not its child nodes, are serialized. If noRecurse is false then the
entire subgraph is serialized.

7.6.2 Document View Export
~~~~~~~~~~~~~~~~~~~~~~~~~~

The methods

| void Session.exportDocumentView(String absPath,
|  ContentHandler contentHandler,
|  boolean skipBinary,
|  boolean noRecurse)

and

| void Session.exportDocumentView(String absPath,
|  OutputStream out,
|  boolean skipBinary,
|  boolean noRecurse)

work identically to their respective system view variants, except that
the resulting XML is in the document view form.

7.7 Export Scope
----------------

Export obeys the access restrictions of the bound Session. If the
Session lacks read access to some subsection of the specified content,
that section is not exported.

The exported output reflects the state of the bound persistent workspace
as modified by the transient store of the bound Session. This means that
pending changes and all namespace mappings in the namespace registry, as
modified by the current session-mappings, are reflected in the output.

7.8 Encoding
------------

XML streams produced by export must be encoded in UTF-8 or UTF-16 as per
the XML specification\ :sup:``:sup:`18` <#sdfootnote18sym>`__`.
