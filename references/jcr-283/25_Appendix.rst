======================================================================
JCR 2.0: 25 Appendix (Content Repository for Java Technology API v2.0)
======================================================================

25 Appendix
===========

25.1 Treatment of Identifiers
-----------------------------

A number of different methods in the API transfer node state from one
location to another. They often differ in how they treat the identifier
of the node. Some methods always behave the same way in this regard,
others have various options that control their behavior. The following
table summarizes the behaviors of the methods.

**Method**

**Referenceable Identifiers**

**Non-referenceable Identifiers**

| **Save
**

Identifiers *must* be preserved, with the possible exception of the
first save of a new node (see §3.7.1 *Identifier Assignment*). The state
of a transient node is saved to the persistent node with the same
identifier.

**Copy
**\ (within a workspace)

New identifiers *must* be created.

**Copy
**\ (between workspaces)

New referenceable identifiers *must* be created.

New non-referenceable identifiers *may* be created. The stability of
non-referenceable identifiers is a repository implementation variant.

**Move**

Referenceable identifiers *must* be preserved.

Non-referenceable identifiers *may* be preserved. The stability of
non-referenceable identifiers is a repository implementation variant.

**Clone, Restore**

Referenceable identifiers *must* be preserved. On conflict with an
existing node a flag governs whether the existing node is removed or an
exception thrown.

**Update, Merge**

Referenceable identifiers *must* be preserved. On conflict with an
existing node, that node is replaced at its existing location in the
target workspace.

**Import**

A flag determines whether new identifiers are created or incoming ones
preserved. On conflict with an existing node the options are to either
replace the existing node in place, remove the existing node, or throw
an exception.

25.2 Compact Node Type Definition Notation
------------------------------------------

The following grammar defines the compact node type definition (CND)
notation used to define node types throughout this specification.

25.2.1 String Literals in CND Grammar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Throughout this section string literals that appear in the syntactic
grammar defining CND must be interpreted as specified in §1.3.1 *String
Literals in Syntactic Grammars*.

25.2.2 Variant Node Type Definitions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In a CND, the presence of a question mark (“?”) indicates that an
attribute in question can vary across repository implementations (see
§3.7.10 *Base Primary Node Type* and 3.7.11 *Standard Application Node
Types*).

In the case of the queryable node type attribute, the absence of an
explicit keyword (either query or noquery) indicates that the attribute
is a variant.

Such *variant node type definitions* cannot be instantiated in a
repository as-is. If an implementation supports a variant node type its
node type registry must contain a definition of that node type in which
each variant attribute is resolved to a concrete value.

25.2.3 CND Grammar
~~~~~~~~~~~~~~~~~~

/\* A CND consists of zero or more blocks, each of which is

either a namespace declaration or a node type definition.

Namespace prefixes referenced in a node type definition

block must be declared in a preceding namespace declaration

block. \*/

**Cnd ::= {NamespaceMapping \| NodeTypeDef}**

| 

/\* A namespace declaration consists of prefix/URI pair. The

prefix must be a valid JCR namespace prefix, which is the

same as a valid XML namespace prefix. The URI can in fact be

any string. Just as in XML, it need not actually be a URI,

though adhering to that convention is recommended. \*/

**NamespaceMapping ::= '<' Prefix '=' Uri '>'**

**Prefix ::= String**

**Uri ::= String**

| 

/\* A node type definition consists of a node type name followed

by an optional supertypes block, an optional node type

attributes block and zero or more blocks, each of which is

either a property or child node definition. \*/

**NodeTypeDef ::= NodeTypeName [Supertypes]**

**[NodeTypeAttribute {NodeTypeAttribute}]**

**{PropertyDef \| ChildNodeDef}**

| 

/\* The node type name is delimited by square brackets and must

be a valid JCR name. \*/

**NodeTypeName ::= '[' String ']'**

| 

/\* The list of supertypes is prefixed by a '>'. If the node

type is not a mixin then it implicitly has nt:base as a

supertype even if neither nt:base nor a subtype of nt:base

appears in the list or if this element is absent. A question

mark indicates that the supertypes list is a variant. \*/

**Supertypes ::= '>' (StringList \| '?')**

| 

/\* The node type attributes are indicated by the presence or

absence of keywords. \*/

**NodeTypeAttribute ::= Orderable \| Mixin \| Abstract \| Query \|**

**PrimaryItem**

| 

/\* In the following, mention of a keyword, like 'orderable',

refers to all the forms of that keyword, including short

forms ('ord' and 'o', for example) \*/

| 

/\* If 'orderable' is present without a '?' then orderable child

nodes is supported. If 'orderable' is present with a '?'

then orderable child nodes is a variant. If 'orderable'

is absent then orderable child nodes is not supported. \*/

**Orderable ::= ('orderable' \| 'ord' \| 'o') ['?']**

| 

/\* If 'mixin' is present without a '?' then the node type is a

mixin. If 'mixin' is present with a '?' then the mixin

status is a variant. If 'mixin' is absent then the node type

is primary. \*/

**Mixin ::= ('mixin' \| 'mix' \| 'm') ['?']**

| 

/\* If 'abstract' is present without a '?' then the node type is

abstract. If 'abstract' is present with a '?' then the

abstract status is a variant. If 'abstract' is absent then

the node type is concrete. \*/

**Abstract ::= ('abstract' \| 'abs' \| 'a') ['?']**

| 

/\* If 'query' is present then the node type is

queryable. If 'noquery' is present then the node type is

not queryable. If neither query nor noquery are present then

the queryable setting of the node type is a variant. \*/

**Query ::= ('noquery' \| 'nq') \| ('query' \| 'q' )**

| 

/\* If 'primaryitem' is present without a '?' then the string

following it is the name of the primary item of the node

type. If 'primaryitem' is present with a '?' then

the primary item is a variant. If 'primaryitem' is absent

then the node type has no primary item. \*/

**PrimaryItem ::= ('primaryitem'\| '!')(String \| '?')**

| 

/\* A property definition consists of a property name element

followed by optional property type, default values, property

attributes and value constraints elements. \*/

**PropertyDef ::= PropertyName [PropertyType] [DefaultValues]**

**[PropertyAttribute {PropertyAttribute}]**

**[ValueConstraints]**

| 

/\* The property name, or '\*' to indicate a residual property

definition, is prefixed with a '-'. \*/

**PropertyName ::= '-' String**

| 

/\* The property type is delimited by parentheses ('\*' is a

synonym for UNDEFINED). If this element is absent,

STRING is assumed. A '?' indicates that this attribute is

a variant. \*/

**PropertyType ::= '(' ('STRING' \| 'BINARY' \| 'LONG' \| 'DOUBLE' \|**

**'BOOLEAN' \| 'DATE' \| 'NAME' \| 'PATH' \|**

**'REFERENCE' \| 'WEAKREFERENCE' \|**

**'DECIMAL' \| 'URI' \| 'UNDEFINED' \| '\*' \|
 '?') ')'**

| 

/\* The default values, if any, are listed after a '='. The

attribute is a list in order to accommodate multi-

value properties. The absence of this element indicates that

there is no static default value reportable. A '?' indicates

that this attribute is a variant \*/

**DefaultValues ::= '=' (StringList \| '?')**

| 

/\* The value constraints, if any, are listed after a '<'. The

absence of this element indicates that no value constraints

reportable within the value constraint syntax. A '?'

indicates that this attribute is a variant \*/

**ValueConstraints ::= '<' (StringList \| '?')**

| 

/\* A child node definition consists of a node name element

followed by optional required node types, default node types

and node attributes elements. \*/

**ChildNodeDef ::= NodeName [RequiredTypes] [DefaultType]**

**[NodeAttribute {NodeAttribute}]**

| 

/\* The node name, or '\*' to indicate a residual property

definition, is prefixed with a '+'. \*/

**NodeName ::= '+' String**

| 

/\* The required primary node type list is delimited by

parentheses. If this element is missing then a required

primary node type of nt:base is assumed. A '?' indicates

that the this attribute is a variant. \*/

**RequiredTypes ::= '(' (StringList \| '?') ')'**

| 

/\* The default primary node type is prefixed by a '='. If this

element is missing then no default primary node type is set.

A '?' indicates that this attribute is a variant \*/

**DefaultType ::= '=' (String \| '?')**

| 

/\* The property attributes are indicated by the presence or

absence of keywords. \*/

**PropertyAttribute ::= Autocreated \| Mandatory \| Protected \|**

**Opv \| Multiple \| QueryOps \| NoFullText \|**

**NoQueryOrder**

| 

/\* The node attributes are indicated by the presence or

absence of keywords. \*/

**NodeAttribute ::= Autocreated \| Mandatory \| Protected \|**

**Opv \| Sns**

| 

/\* If 'autocreated' is present without a '?' then the item

is autocreated. If 'autocreated' is present with a '?' then

the autocreated status is a variant. If 'autocreated' is

absent then the item is not autocreated. \*/

**Autocreated ::= ('autocreated' \| 'aut' \| 'a' )['?']**

| 

/\* If 'mandatory' is present without a '?' then the item

is mandatory. If 'mandatory' is present with a '?' then

the mandatory status is a variant. If 'mandatory' is

absent then the item is not mandatory. \*/

**Mandatory ::= ('mandatory' \| 'man' \| 'm') ['?']**

| 

/\* If 'protected' is present without a '?' then the item

is protected. If 'protected' is present with a '?' then

the protected status is a variant. If 'protected' is

absent then the item is not protected. \*/

**Protected ::= ('protected' \| 'pro' \| 'p') ['?']**

| 

/\* The OPV status of an item is indicated by the presence of

that corresponding keyword. If no OPV keyword is present

then an OPV status of COPY is assumed. If the keyword 'OPV'

followed by a '?' is present then the OPV status of the item

is a variant.

**Opv ::= 'COPY' \| 'VERSION' \| 'INITIALIZE' \| 'COMPUTE' \|**

**'IGNORE' \| 'ABORT' \| ('OPV' '?')**

| 

/\* If 'multiple' is present without a '?' then the property

is multi-valued. If 'multiple' is present with a '?' then

the multi-value status is a variant. If 'multiple' is

absent then the property is single-valued. \*/

**Multiple ::= ('multiple' \| 'mul' \| '\*') ['?']**

| 

/\* The available query comparison operators are listed after

the keyword 'queryops'. If 'queryops' is followed by a '?'

then this attribute is a variant. If this element is absent

then the full set of operators is available. \*/

**QueryOps ::= ('queryops' \| 'qop')**

**(('''Operator {','Operator}''') \| '?')**

**Operator ::= '=' \| '<>' \| '<' \| '<=' \| '>' \| '>=' \| 'LIKE'**

| 

/\* If 'nofulltext' is present without a '?' then the property

does not support full text search. If 'nofulltext' is

present with a '?' then this attribute is a variant. If

'nofulltext' is absent then the property does support full

text search. \*/

**NoFullText ::= ('nofulltext' \| 'nof') ['?']**

| 

/\* If 'noqueryorder' is present without a '?' then query

results cannot be ordered by this property. If

'noqueryorder' is present with a '?' then this attribute is

a variant. If 'noqueryorder' is absent then query results

can be ordered by this property. \*/

**NoQueryOrder ::= ('noqueryorder' \| 'nqord') ['?']**

| 

/\* If 'sns' is present without a '?' then the child node

supports same-name siblings. If 'sns' is present with a '?'

then this attribute is a variant. If 'sns' is absent then

the child node does support same-name siblings. \*/

**Sns ::= ('sns' \| '\*') ['?']**

| 

/\* Strings \*/

**StringList ::= String {',' String}**

**String ::= QuotedString \| UnquotedString**

| 

/\* Quotes are used to allow for strings (i.e., names, prefixes,

URIs, values or constraint strings) with characters that

would otherwise be interpreted as delimiters in CND. \*/

**QuotedString ::= SingleQuotedString \| DoubleQuotedString**

| 

/\* Within a SingleQuotedString, single quote literals (') must

be escaped. \*/

**SingleQuotedString ::= ''' UnquotedString '''**

| 

/\* Within a DoubleQuotedString, double quote literals (") must

be escaped. \*/

**DoubleQuotedString ::= '"' UnquotedString '"'**

**UnquotedString ::= XmlChar {XmlChar}**

**XmlChar ::= /\* see §3.2.2 Local Names \*/**

25.2.3.1 Case Insensitive Keywords
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The keywords of CND, though defined above as terminal strings with
specific cases, are in fact case-insensitive. For example, STRING can be
written string, String or even StRiNg.

25.2.3.2 Escaping
^^^^^^^^^^^^^^^^^

The standard Java escape sequences are supported:

\\n newline

\\t tab

\\b backspace

\\f form feed

\\r return

\\” double quote

\\' single quote

\\” double quote

\\\\ back slash

\\u\ *HHHH* Unicode character in hexadecimal

25.2.3.3 Comments
^^^^^^^^^^^^^^^^^

Comments can be included in the notation using either of the standard
Java forms. A comment is defined as:

**Comment ::= LineComment \| BlockComment**

**LineComment ::= "//" LineCommentText**

**BlockComment ::= "/\*" BlockCommentText "\*/"**

**LineCommentText ::= /\* Any text ending in a newline \*/**

**BlockComment ::= /\* Any text except the end-block-comment
 character pair \*/**

A comment can appear between any two valid tokens of the CND grammar.
Comments are not defined within the main CND grammar, but are intended
to be stripped during preprocessing, prior to the actual parsing of the
CND.

25.2.3.4 Extension Syntax
^^^^^^^^^^^^^^^^^^^^^^^^^

Vendor-specific extensions are supported through the extension syntax:

**VendorExtension ::= "{" Vendorname VendorBody "}"**

**VendorName ::= /\* A unique vendor-specific identifier
 containing no whitespace \*/**

**VendorBody ::= /\* Any string not including "}" \*/**

Like a comment, an extension can appear between any two tokens of the
CND grammar. Extensions are not defined within the main CND grammar, but
are intended to be handled during preprocessing, prior to the actual
parsing of the CND. The first whitespace-delimited token of the
extension should be a unique vendor-specific identifier. The semantics
of the extension body are implementation-specific.

25.2.3.5 Whitespace and Short Forms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The notation can be compacted by taking advantage of the following the
fact that spacing around keychars ([ ] > , - ( ) = <), newlines and
indentation are not required. So, the following is also well-formed:

[x]>y,z orderable mixin -p(DATE)=a,b primary mandatory autocreated
protected multiple VERSION <c,d

Additionally, though spaces are required around the keywords (orderable,
mixin, date, mandatory, etc.), short forms for keywords can be used. So,
this:

[x]>y,z o m-p(DATE)=a,b ! m a p \* VERSION <c,d

is also well-formed.

25.2.4 Examples
~~~~~~~~~~~~~~~

Here is a “worst-case scenario” example that demonstrates all the
features of the notation:

/\* An example node type definition \*/

| 

// The namespace declaration

<ns = 'http://namespace.com/ns'>

| 

// Node type name

[ns:NodeType]

| 

// Supertypes

> ns:ParentType1, ns:ParentType2

| 

// This node type is abstract

abstract

| 

// This node type supports orderable child nodes

orderable

| 

// This is a mixin node type

mixin

| 

// This node type is not queryable

noquery

| 

// ex:property is the primary item

primaryitem ex:property

| 

// A property called 'ex:property' of type STRING

- ex:property (STRING)

| 

// The default values for this (multi-value) property are...

= 'default1', 'default2'

| 

// This property is...

mandatory autocreated protected

| 

// ...and multi-valued.

| multiple

// It has an on-parent-version setting of...

VERSION

| 

// The constraint settings are...

< 'constraint1', 'constraint2'

| 

// The supported query operators are...

queryops '=, <>, <, <=, >, >=, LIKE'

| 

// The property is not full text searchable

nofulltext

| 

// query results are not orderable by this property

noqueryorder

| 

// A child node called ns:node which must be of

// at least the node types ns:reqType1 and ns:reqType2

+ ns:node (ns:reqType1, ns:reqType2)

| 

// with default primary node type is...

= ns:defaultType

| 

// This node is...

mandatory autocreated protected

| 

// supports same name siblings

sns

| 

// and has an on-parent-version setting of ...

VERSION

`1 <#sdfootnote1anc>`__ See http://unicode.org/charts/PDF/U0000.pdf.

`2 <#sdfootnote2anc>`__ See
http://tools.ietf.org/html/rfc3986#section-3.

`3 <#sdfootnote3anc>`__ See http://www.ietf.org/rfc/rfc3986.txt.

`4 <#sdfootnote4anc>`__ See http://www.ietf.org/rfc/rfc3986.txt.

`5 <#sdfootnote5anc>`__ see http://www.ietf.org/rfc/rfc4646.txt.

`6 <#sdfootnote6anc>`__ See http://www.iana.org/assignments/media-types.

`7 <#sdfootnote7anc>`__ See
http://www.iana.org/assignments/character-sets.

`8 <#sdfootnote8anc>`__ See http://www.ietf.org/rfc/rfc2616.txt §3.11.

| `9 <#sdfootnote9anc>`__ See
http://java.sun.com/j2se/1.4.2/docs/guide/jar/
| jar.html#Service%20Provider.

`10 <#sdfootnote10anc>`__ See the SQL:92 rules for <regular identifier>
(in ISO/IEC 9075:1992 §5.2 <token> and <separator>).

`11 <#sdfootnote11anc>`__ See the SQL:92 rules for <regular identifier>
(in ISO/IEC 9075:1992 §5.2 <token> and <separator>).

`12 <#sdfootnote12anc>`__ See http://tools.ietf.org/html/rfc4648 §4.

`13 <#sdfootnote13anc>`__ See http://www.w3.org/TR/REC-xml/#charsets,
http://www.w3.org/TR/REC-xml/#NT-CharRef, and
http://www.w3.org/TR/REC-xml/#wf-Legalchar.

`14 <#sdfootnote14anc>`__ See http://www.w3.org/TR/xmlschema-0/#ListDt
for more information about the XML Schema list type.

`15 <#sdfootnote15anc>`__ See http://www.w3.org/TR/REC-xml/#charsets,
http://www.w3.org/TR/REC-xml/#NT-CharRef, and
http://www.w3.org/TR/REC-xml/#wf-Legalchar.

`16 <#sdfootnote16anc>`__ This escaping scheme is based on the scheme
described in ISO/IEC 9075-14:2003 for converting arbitrary strings into
valid XML element and attribute names.

`17 <#sdfootnote17anc>`__ See http://www.w3.org/TR/xml/#syntax.

`18 <#sdfootnote18anc>`__ See http://www.w3.org/TR/xml/#charsets.

| `19 <#sdfootnote19anc>`__ See
http://java.sun.com/j2se/1.4.2/docs/api/org/xml/sax/
| ContentHandler.html.

`20 <#sdfootnote20anc>`__ One common case is a policy that affects both
its bound node and the subgraph below that node. However, any such
*deepness* attribute is internal to the policy and, like any other
internal characteristic of a policy, opaque to the JCR API except
insofar as it is part of the human-readable name and description. Note
also that, strictly speaking, a policy is not required to affect even
its bound node, though such an implementation would be uncommon.

`21 <#sdfootnote21anc>`__ Recall that *outside a transaction*
persistence of transient state occurs immediately upon a Session.save
while, within a transaction, the effect of any Session.save calls is
deferred until commit of the transaction.

`22 <#sdfootnote22anc>`__ In some systems this feature is called
“freeze” or “legal hold” (when the hold is applied due to legal
requirements).

`23 <#sdfootnote23anc>`__ See
http://java.sun.com/products/jta/index.html.

| 

1

|
