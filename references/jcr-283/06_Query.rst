==================================================================
JCR 2.0: 6 Query (Content Repository for Java Technology API v2.0)
==================================================================

6 Query
=======

A repository may support *query*.

The structure and evaluation semantics of a query are defined by an
*abstract query model* (AQM) for which two concrete language bindings
are specified:

-  *JCR-SQL2*, which expresses a query as a string with syntax similar
   to SQL, and

-  *JCR-JQOM* **** (JCR Java Query Object Model), which expresses a
   query as a tree of Java objects.

The languages are both direct mappings of the AQM and are therefore
equally expressive; any query expressed in one can be
machine-transformed to the other.

Whether an implementation supports query can be determined by querying
the repository descriptor table with the key

Repository.QUERY\_LANGUAGES.

The returned array contains the constants representing the supported
languages (see §24.2 *Repository Descriptors*). If a repository supports
query it must return at least the constants for the two JCR-defined
languages,

javax.jcr.query.JCR-JQOM and

javax.jcr.query.JCR-SQL2,

indicating support for those languages. In addition, a repository may
support other query languages. These can be either additional language
bindings to the AQM or completely independent of that model.

JCR 1.0 defines a dialect of SQL different from JCR-SQL2, as well as a
dialect of XPath. Support for these languages is deprecated.

6.1 Optional Joins
------------------

Support for *joins* is optional beyond support for query itself. The
extent of join support can be determined by querying the repository
descriptor table with the key

Repository.QUERY\_JOINS.

The value returned will be one of

-  QUERY\_JOINS\_NONE: Joins are not supported and therefore queries are
   limited to a single selector.

-  QUERY\_JOINS\_INNER: Inner joins are supported.

-  QUERY\_JOINS\_INNER\_OUTER: Inner and outer joins are supported.

6.2 Introduction to the Abstract Query Model
--------------------------------------------

This section introduces how queries are specified and evaluated in the
AQM.

6.2.1 Selectors
~~~~~~~~~~~~~~~

A query has one or more *selectors*. When the query is evaluated, each
selector independently selects a subset of the nodes in the workspace
based on node type.

In a repository that *does not* support *joins*, a query will have only
one selector.

6.2.2 Joins
~~~~~~~~~~~

If the query has more than one selector, it also has one or more *joins*
that transform the sets of nodes selected by each selector into a single
set of *node-tuples*.

The membership of the set of node-tuples depends on the *join type* and
*join condition* of each join. The join type can be *inner*,
*left-outer*, or *right-outer*. The join condition can test the equality
of properties' values or the hierarchical relationship between nodes.

If the query has *n* selectors, it has *n - 1* joins resulting in a set
of *n*-tuples. For example, if the query has two selectors, it will have
one join and produce a set of 2-tuples. If it has three selectors, it
will have two joins and produce a set of 3-tuples. If it has only one
selector, it will not have any joins and will produce a set of 1-tuples,
that is, the nodes selected by its only selector.

Support for *joins* is optional. In a repository that *does not* support
*joins*, the node-tuples produced are necessarily singletons. In other
words, each node in the set produced by the (one and only) selector is
converted directly into a node-tuple of size one. All further processing
within the query evaluation operates on these tuples just as it would on
tuples of size greater than one.

6.2.3 Constraints
~~~~~~~~~~~~~~~~~

A query can specify a *constraint* to filter the set of node-tuples by
any combination of:

-  Absolute or relative path, for example:

   -  The node reached by path /pictures/sunset.jpg

   -  Nodes that are children of /pictures

   -  Nodes that are descendants of /pictures

-  Name of the node, for example:

   -  Nodes named sunset.jpg

-  Value of a property, for example:

   -  Nodes whose jcr:created property is after 2007-03-14T00:00:00.000Z

-  Length of a property, for example:

   -  Nodes whose jcr:data property is longer than 100 KB

-  Existence of a property, for example:

   -  Nodes with a jcr:language property

-  Full-text search, for example:

   -  Nodes which have a property that contains the phrase “beautiful
      sunset”

6.2.4 Orderings
~~~~~~~~~~~~~~~

A query can specify *orderings* to sort the filtered node-tuples by
property value.

6.2.5 Query Results
~~~~~~~~~~~~~~~~~~~

The filtered and sorted node-tuples form the *query results*. The query
results are available in two formats:

-  A list of node-tuples. For each node-tuple, you can retrieve the node
   for each selector. In a repository that does not support *joins*
   there will be only one selector and consequently only one node per
   tuple.

-  A table whose rows are the node-tuples and whose columns are
   properties of the nodes in the node-tuples. This is referred to as
   the tabular view of the query results. A query can specify which
   properties appear as columns in the tabular view.

6.3 Equality and Comparison
---------------------------

When testing for equality or order of two property values of the same
type, the query operators conform to the definitions in §3.6.5
*Comparison of Values*.

When testing for equality or order of two property values of differing
type, the query operators perform standard property type conversion (see
§3.6.4 *Property Type Conversion*) and conform to standard value
comparison (see §3.6.5 *Comparison of Values*).

Support for equality and order comparison of BINARY values is not
required.

6.4 Query Validity
------------------

To be successfully evaluated and produce query results, a query must be
*valid*.

A query is *invalid* if:

-  it cannot be expressed in the AQM, or

-  it can be expressed in the AQM, but fails a validation constraint
   defined in §6.7 *Abstract Query Model and Language Bindings*.

An invalid query causes the repository to throw InvalidQueryException.
Which method invocation throws this exception is implementation
determined, but for an invalid query, the exception must be thrown no
later than completion of the Query.execute().

6.5 Search Scope
----------------

A query *must* search the persistent workspace associated with the
current session. It *may* take into account pending changes to the
persistent workspace; that is, changes which are either unsaved or,
within a transaction, saved but uncommitted.

6.6 Notations
-------------

Three notations are used in the following sections: the AQM type
grammar, the JCR-SQL2 EBNF grammar and the JCR-JQOM Java API.

6.6.1 AQM Notation
~~~~~~~~~~~~~~~~~~

The AQM is defined as a set of abstract types. The type grammar is
written like this:

type Alpha ::=

Foo foo,

Bar? bar,

Baz+ bazes,

Quux\* quuxes

| 

type Beta extends Alpha ::=

String name

| 

enum Foo ::=

Snap,

Crackle,

Pop

| 
| which means:

The type Alpha has 4 attributes:

foo: mandatory, of type Foo, which is an enumeration with possible
values Snap, Crackle and Pop.

bar: optional, of type Bar

bazes: a list of one or more Baz items

quuxes: a list of zero or more Quux items

The type Beta is a subtype of Alpha. It inherits Alpha's attributes, and
adds:

name: mandatory, a string

6.6.2 JCR-SQL2 Notation
~~~~~~~~~~~~~~~~~~~~~~~

JCR–SQL2 is a mapping of the AQM to a string serialization based on the
SQL language.

Each non-terminal in the JCR-SQL2 EBNF grammar corresponds to the type
of the same name in the AQM grammar. The semantics of each JCR-SQL2
production is described by reference to the semantics of the
corresponding AQM production. The two grammars are, however, entirely
distinct and self- contained. Care should be taken not to mix
productions from one grammar with those of the other.

The JCR-SQL2 grammar is written like this:

| Alpha ::= 'FOO' Foo ['BAR' Bar] 'BAZ' bazes
|  ['QUUX' quuxes]

| 

Foo ::= Snap \| Crackle \| Pop

| 

Snap ::= 'SNAP'

| 

Crackle ::= 'CRACKLE'

| 

Pop ::= 'POP'

| 

Bar ::= /\* a Bar \*/

| 

bazes ::= Baz {Baz}

| 

Baz ::= /\* a Baz \*/

| 

quuxes ::= Quux {Quux}

| 

Quux ::= /\* a Quux \*/

6.6.2.1 String Literals in JCR-SQL2 Grammar
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Throughout this section string literals that appear in the syntactic
grammar defining JCR-SQL2 must be interpreted as specified in §1.3.1
*String Literals in Syntactic Grammars* except that each character in
the string literal must be interpreted as representing both upper and
lower case versions. In other words, implementations must be
case-insensitive with regard to JCR-SQL2.

6.6.3 JCR-JQOM Notation
~~~~~~~~~~~~~~~~~~~~~~~

JCR-JQOM is a mapping of the AQM to a Java API.

Each method and parameter name of the JCR-JQOM Java API corresponds to
the type of the same name in the AQM grammar. The semantics of each
JCR-JQOM method is described by reference to the semantics of the
corresponding AQM production.

A JCR-JQOM query is built by assembling objects created using the
factory methods of QueryObjectModelFactory.

For each AQM type, the following are listed:

-  If the AQM type is a *non-enum* and *non-abstract* (in the AQM sense,
   not the Java sense) then the factory method of
   QueryObjectModelFactory used to create an instance of that type is
   listed.

-  If the AQM type is *non-enum* then the corresponding Java interface
   is listed.

-  If the AQM type is an *enum* then the corresponding constants of
   QueryObjectModelConstants are listed.

Unless otherwise indicated, the Java interfaces listed in this section
are in the package javax.jcr.query.qom.

6.7 Abstract Query Model and Language Bindings
----------------------------------------------

The following section describes the AQM grammar and its mapping to
JCR-SQL2 and JCR-JQOM. For each AQM production, a description of its
semantics is provided, followed by the corresponding JCR-SQL2 production
and the corresponding JCR-JQOM methods.

For queries with only one selector the JCR-SQL2 syntax permits the
selector name to be omitted. In such cases the implementation must
automatically generate a selector name for internal use. If the
resulting query is later examined through the JCR-JQOM API, the
automatically produced selector name will be seen.

6.7.1 Query
~~~~~~~~~~~

**AQM**

type Query ::=

Source source,

Constraint? constraint,

Ordering\* orderings,

Column\* columns

| 

A Query consists of:

-  A Source. When the query is evaluated, the Source evaluates its
   selectors and the joins between them to produce a (possibly empty)
   set of node-tuples. This is a set of 1-tuples if the query has one
   selector (and therefore no joins), a set of 2-tuples if the query has
   two selectors (and therefore one join), a set of 3-tuples if the
   query has three selectors (two joins), and so forth.

-  An optional Constraint. When the query is evaluated, the constraint
   filters the set of node-tuples.

-  A list of zero or more Orderings. The orderings specify the order in
   which the node-tuples appear in the query results. The relative order
   of two node-tuples is determined by evaluating the specified
   orderings, in list order, until encountering an ordering for which
   one node-tuple precedes the other. If no orderings are specified, or
   if there is no ordering specified in which one node-tuple precedes
   the other, then the relative order of the node-tuples is
   implementation determined (and may be arbitrary).

-  A list of zero or more Columns to include in the tabular view of the
   query results. If no columns are specified, the columns available in
   the tabular view are implementation determined, but minimally
   include, for each selector, a column for each single-valued
   non-residual property of the selector's node type.

**JCR-SQL2**

Query ::= 'SELECT' columns

'FROM' Source

['WHERE' Constraint]

['ORDER BY' orderings]

| 
| **JCR-JQOM**

A query is represented by a QueryObjectModel object, created with:

| QueryObjectModel QueryObjectModelFactory.
|  createQuery(Source source,
|  Constraint constraint,
|  Ordering[] orderings,
|  Column[] columns)

QueryObjectModel extends javax.jcr.query.Query and declares:

Source QueryObjectModel.getSource()

Constraint QueryObjectModel.getConstraint()

Ordering[] QueryObjectModel.getOrderings()

Column[] QueryObjectModel.getColumns()

6.7.2 Source
~~~~~~~~~~~~

**AQM**

abstract type Source

| 

Evaluates to a set of node-tuples.

**JCR-SQL2**

Source ::= Selector \| Join

| 
| **JCR-JQOM**

Source is an empty interface with subclasses Selector and Join.

6.7.3 Selector
~~~~~~~~~~~~~~

**AQM**

type Selector extends Source ::=

Name nodeType,

Name selectorName

| 

Selects a subset of the nodes in the workspace based on node type.

The query is invalid if nodeType refers to a node type that has a
*queryable node type* attribute of false (see §3.7.1.5 *Queryable Node
Type*). Otherwise, if the *queryable node type* attribute is true, the
following holds:

A selector selects every node in the workspace, subject to access
control constraints, that satisfies at least one of the following
conditions:

-  the node’s primary node type is nodeType, or

-  the node’s primary node type is a subtype of nodeType, or

-  the node has a mixin node type that is nodeType, or

-  the node has a mixin node type that is a subtype of nodeType.

A selector has a selectorName that can be used elsewhere in the query to
identify the selector.

The query is *invalid* if selectorName is identical to the selectorName
of another selector in the query.

The query is also *invalid* if nodeType is not a valid JCR name or is a
valid JCR name but not the name of a node type available in the
repository.

**JCR-SQL2**

Selector ::= nodeTypeName ['AS' selectorName]

| 

nodeTypeName ::= Name

| 
| **JCR-JQOM**

A Selector is created with:

| Selector QueryObjectModelFactory.
|  selector(String nodeTypeName, String selectorName)

Selector extends Source and declares:

String Selector.getNodeTypeName()

String Selector.getSelectorName()

6.7.4 Name
~~~~~~~~~~

**AQM**

type Name

| 

A JCR name.

The query is *invalid* if the name does not satisfy either the
ExpandedName production in §3.2.5.1 *Expanded Form* or the QualifiedName
production in §3.2.5.2 *Qualified Form*.

**JCR-SQL2**

| Name ::= '[' quotedName ']' \|
|  '[' simpleName ']' \|

simpleName

| 

quotedName ::= /\* A JCR Name \*/

| 

simpleName ::= /\* A JCR Name that is also a legal SQL
identifier\ :sup:``:sup:`10` <#sdfootnote10sym>`__` \*/

| 
| **JCR-JQOM**

A JCR name in String form (either qualified or expanded).

6.7.5 Join
~~~~~~~~~~

Support for *joins* is optional.

**AQM**

type Join extends Source ::=

Source left,

Source right,

JoinType joinType,

JoinCondition joinCondition

| 

Performs a join between two node-tuple sources.

If left evaluates to **L**, a set of *m*-tuples, and right evaluates to
**R**, a set of *n*-tuples, then the join evaluates to **J**, a set of
(*m + n*)-tuples. The members of **J** **** depend on the joinType and
joinCondition.

Let **L** x **R** be the Cartesian product of **L** and **R** as a set
of (*m + n*)-tuples

**L** x **R** = { ℓ r : ℓ \ **L**, r \ **R** }

and \ :sub:`c`\ (A) be the selection over **A** of its members
satisfying joinCondition \ :sub:`c`

\ :sub:`c`\ (**A**) = { a : a \ **A**, \ :sub:`c`\ (a) }

Then if joinType is Inner:

**J** = \ :sub:`c`\ (**L** x **R**)

Otherwise, if joinType is LeftOuter:

**J** = \ :sub:`c`\ (**L** x **R**) (\ **L** –
π\ :sub:`L`\ (:sub:`c`\ (**L** x **R**)))

where π\ :sub:`L`\ (:sub:`c`\ (**L** x **R**)) is the projection of the
*m*-tuples contributed by **L** from the *(m + n)*-tuples of
\ :sub:`c`\ (**L** x **R**).

Otherwise, if joinType is RightOuter:

**J** = \ :sub:`c`\ (**L** x **R**) (\ **R** –
π\ :sub:`R`\ (:sub:`c`\ (**L** x **R**)))

where π\ :sub:`R`\ (:sub:`c`\ (**L** x **R**)) is the projection of the
*n*-tuples contributed by **R** from the *(m + n)*-tuples of
\ :sub:`c`\ (**L** x **R**).

The query is *invalid* if left is the same source as right.

**JCR-SQL2**

Join ::= left [JoinType] 'JOIN' right 'ON' JoinCondition

// If JoinType is omitted INNER is assumed.

| 

left ::= Source

| 

right ::= Source

| 
| **JCR-JQOM**

A Join is created with:

| Join QueryObjectModelFactory.
|  join(Source left,
|  Source right,
|  String joinType,
|  JoinCondition joinCondition)

Join extends Source and declares:

Source Join.getLeft()

Source Join.getRight()

String Join.getJoinType()

JoinCondition Join.getJoinCondition()

6.7.6 JoinType
~~~~~~~~~~~~~~

Support for *joins* is optional.

**AQM**

enum JoinType ::=

Inner,

LeftOuter,

RightOuter

**
JCR-SQL2**

JoinType ::= Inner \| LeftOuter \| RightOuter

| 

Inner ::= 'INNER'

| 

LeftOuter ::= 'LEFT OUTER'

| 

RightOuter ::= 'RIGHT OUTER'

| 
| **JCR-JQOM**

A join type is a String constant. One of:

QueryObjectModelConstants.JCR\_JOIN\_TYPE\_INNER

QueryObjectModelConstants.JCR\_JOIN\_TYPE\_LEFT\_OUTER

QueryObjectModelConstants.JCR\_JOIN\_TYPE\_RIGHT\_OUTER

6.7.7 JoinCondition
~~~~~~~~~~~~~~~~~~~

Support for *joins* is optional.

**AQM**

abstract type JoinCondition

| 

Filters the set of node-tuples formed from a join.

**JCR-SQL2**

JoinCondition ::= EquiJoinCondition \|

SameNodeJoinCondition \|

ChildNodeJoinCondition \|

DescendantNodeJoinCondition

| 
| **JCR-JQOM**

JoinCondition is an empty interface with subclasses EquiJoinCondition,
SameNodeJoinCondition, ChildNodeJoinCondition and
DescendantNodeJoinCondition.

6.7.8 EquiJoinCondition
~~~~~~~~~~~~~~~~~~~~~~~

Support for *joins* is optional.

**AQM**

type EquiJoinCondition extends JoinCondition ::=

Name selector1Name,

Name property1Name,

Name selector2Name,

Name property2Name

| 

Tests whether the value of a property in a first selector is equal to
the value of a property in a second selector.

A node-tuple satisfies the constraint only if:

-  the selector1Name node has a property named property1Name, and

-  the selector2Name node has a property named property2Name, and

-  the value of property property1Name *is equal to* the value of
   property property2Name, as defined in §3.6.5 *Comparison of Values*.

The query is *invalid* if

-  either selector1Name or selector2Name is not the name of a selector
   in the query, or

-  selector1Name is equal to selector2Name, or

-  the property1Name is not the same property type as property2Name, or

-  either property1Name or property2Name is a multi-valued property, or

-  either property1Name or property2Name is a BINARY property and
   equality test for BINARY properties is not supported (see §3.6.6
   *Value.equals Method*).

**JCR-SQL2**

EquiJoinCondition ::= selector1Name'.'property1Name '='

selector2Name'.'property2Name

| 

selector1Name ::= selectorName

| 

selector2Name ::= selectorName

| 

property1Name ::= propertyName

| 

property2Name ::= propertyName

| 
| **JCR-JQOM**

An EquiJoinCondition is created with:

| EquiJoinCondition QueryObjectModelFactory.
|  equiJoinCondition(String selector1Name,
|  String property1Name,
|  String selector2Name,
|  String property2Name)

EquiJoinCondition extends JoinCondition and declares:

String EquiJoinCondition getSelector1Name()

String EquiJoinCondition getProperty1Name()

String EquiJoinCondition getSelector2Name()

String EquiJoinCondition getProperty2Name()

6.7.9 SameNodeJoinCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for *joins* is optional.

**AQM**

type SameNodeJoinCondition extends JoinCondition ::=

Name selector1Name,

Name selector2Name,

Path? selector2Path

| 

Tests whether two nodes are “the same” according to the Item.isSame
method.

If selector2Path is omitted:

-  Tests whether the selector1Name node is the same as the selector2Name
   node. A node-tuple satisfies the constraint only if:

selector1Node.isSame(selector2Node)

would return true, where selector1Node is the node for the selector
selector1Name and selector2Node is the node for the selector
selector2Name.

Otherwise, if selector2Path is specified:

-  Tests whether the selector1Name node is the same as a node identified
   by relative path selector2Path from the selector2Name node. A
   node-tuple satisfies the constraint only if:

| selector1Node.isSame(
|  selector2Node.getNode(selector2Path))

would return true, where selector1Node is the node for the selector
selector1Name and selector2Node is the node for the selector
selector2Name.

The query is *invalid* if:

-  selector1Name is not the name of a selector in the query, or

-  selector2Name is not the name of a selector in the query, or

-  selector1Name is the same as selector2Name, or

-  selector2Path is not a syntactically valid relative path, as defined
   in §3.4.3.3 *Lexical Path Grammar*. However, if selector2Path is
   syntactically valid but does not identify a node in the workspace
   visible to this session, the query is valid but the constraint is not
   satisfied.

**JCR-SQL2**

SameNodeJoinCondition ::=

'ISSAMENODE(' selector1Name ','

selector2Name

[',' selector2Path] ')'

| 

selector2Path ::= Path

| 
| **JCR-JQOM**

A SameNodeJoinCondition is created with:

| SameNodeJoinCondition QueryObjectModelFactory.
|  sameNodeJoinCondition(String selector1Name,
|  String selector2Name,
|  String selector2Path)

SameNodeJoinCondition extends JoinCondition and declares:

String SameNodeJoinCondition.getSelector1Name()

String SameNodeJoinCondition.getSelector2Name()

String SameNodeJoinCondition.getSelector2Path()

6.7.10 ChildNodeJoinCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for *joins* is optional.

**AQM**

type ChildNodeJoinCondition extends JoinCondition ::=

Name childSelectorName,

Name parentSelectorName

| 

Tests whether the childSelectorName node is a child of the
parentSelectorName node. A node-tuple satisfies the constraint only if:

childSelectorNode.getParent().isSame(parentSelectorNode)

would return true, where childSelectorNode is the node for the selector
childSelectorName and parentSelectorNode is the node for the selector
parentSelectorName.

The query is *invalid* if:

-  childSelectorName is not the name of a selector in the query, or

-  parentSelectorName is not the name of a selector in the query, or

-  childSelectorName is the same as parentSelectorName.

**JCR-SQL2**

ChildNodeJoinCondition ::=

'ISCHILDNODE(' childSelectorName ','

parentSelectorName ')'

| 

childSelectorName ::= selectorName

| 

parentSelectorName ::= selectorName

| 
| **JCR-JQOM**

A ChildNodeJoinCondition is created with:

| ChildNodeJoinCondition QueryObjectModelFactory.
|  childNodeJoinCondition(String childSelectorName,
|  String parentSelectorName)

ChildNodeJoinCondition extends JoinCondition and declares:

String ChildNodeJoinCondition.getChildSelectorName()

String ChildNodeJoinCondition.getParentSelectorName()

6.7.11 DescendantNodeJoinCondition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Support for *joins* is optional.

**AQM**

type DescendantNodeJoinCondition

extends JoinCondition ::=

Name descendantSelectorName,

Name ancestorSelectorName

| 

Tests whether the descendantSelectorName node is a descendant of the
ancestorSelectorName node. A node-tuple satisfies the constraint only
if:

| descendantSelectorNode.getAncestor(n).
|  isSame(ancestorSelectorNode) &&
|  descendantSelectorNode.getDepth() > n

would return true for some non-negative integer n, where
descendantSelectorNode is the node for the selector
descendantSelectorName and ancestorSelectorNode is the node for the
selector ancestorSelectorName.

The query is *invalid* if:

-  descendantSelectorName is not the name of a selector in the query, or

-  ancestorSelectorName is not the name of a selector in the query, or

-  descendantSelectorName is the same as ancestorSelectorName.

**JCR-SQL2**

DescendantNodeJoinCondition ::=

'ISDESCENDANTNODE(' descendantSelectorName ','

ancestorSelectorName ')'

| 

descendantSelectorName ::= selectorName

| 

ancestorSelectorName ::= selectorName

| 
| **JCR-JQOM**

A DescendantNodeJoinCondition is created with:

| DescendantNodeJoinCondition QueryObjectModelFactory.
|  descendantNodeJoinCondition(String descendantSelectorName,
|  String ancestorSelectorName)

DescendantNodeJoinCondition extends JoinCondition and declares:

String DescendantNodeJoinCondition.getDescendantSelectorName()

String DescendantNodeJoinCondition.getAncestorSelectorName()

6.7.12 Constraint
~~~~~~~~~~~~~~~~~

**AQM**

abstract type Constraint

| 

Filters the set of node-tuples formed by evaluating the query's
selectors and the joins between them.

To be included in the query results, a node-tuple must satisfy the
constraint.

**JCR-SQL2**

Constraint ::= And \| Or \| Not \| Comparison \|

PropertyExistence \| FullTextSearch \|

SameNode \| ChildNode \| DescendantNode

| 
| In JCR-SQL2, the following precedence classes apply, in order of
evaluation:

**Class**

**Constraint Production**

**JCR-SQL2 Syntax**

1

() *(grouping with parentheses)*

2

Comparison

PropertyExistence

FullTextSearch

SameNode

ChildNode

DescendantNode

= , <>, <, <=, >, >=, LIKE

IS NOT NULL

CONTAINS()

ISSAMENODE()

ISCHILDNODE()

ISDESCENDANTNODE()

3

Not

NOT

4

And

AND

5

Or

OR

| 

**JCR-JQOM**

Constraint is an empty interface with subclasses And, Or, Not,
Comparison, PropertyExistence, FullTextSearch, SameNode, ChildNode and
DescendantNode.

6.7.13 And
~~~~~~~~~~

**AQM**

type And extends Constraint ::=

Constraint constraint1,

Constraint constraint2

| 

Performs a logical conjunction of two other constraints.

To satisfy the And constraint, a node-tuple must satisfy both
constraint1 and constraint2.

**JCR-SQL2**

And ::= constraint1 'AND' constraint2

| 

constraint1 ::= Constraint

| 

constraint2 ::= Constraint

| 
| **JCR-JQOM**

An And is created with:

| And QueryObjectModelFactory.
|  and(Constraint constraint1, Constraint constraint2)

And extends Constraint and declares:

Constraint And.getConstraint1()

Constraint And.getConstraint2()

6.7.14 Or
~~~~~~~~~

**AQM**

type Or extends Constraint ::=

Constraint constraint1,

Constraint constraint2

| 

Performs a logical disjunction of two other constraints.

To satisfy the Or constraint, the node-tuple must either:

-  satisfy constraint1 but not constraint2, or

-  satisfy constraint2 but not constraint1, or

-  satisfy both constraint1 and constraint2.

**JCR-SQL2**

Or ::= constraint1 'OR' constraint2

| 
| **JCR-JQOM**

An Or is created with:

| Or QueryObjectModelFactory.
|  or(Constraint constraint1, Constraint constraint2)

Or extends Constraint and declares:

Constraint Or.getConstraint1()

Constraint Or.getConstraint2()

6.7.15 Not
~~~~~~~~~~

**AQM**

type Not extends Constraint ::=

Constraint constraint

| 

Performs a logical negation of another constraint.

To satisfy the Not constraint, the node-tuple must *not* satisfy
constraint.

**JCR-SQL2**

Not ::= 'NOT' Constraint

| 
| **JCR-JQOM**

A Not is created with:

| Not QueryObjectModelFactory.
|  not(Constraint constraint)

Not extends Constraint and declares:

Constraint Not.getConstraint()

6.7.16 Comparison
~~~~~~~~~~~~~~~~~

**AQM**

type Comparison extends Constraint ::=

DynamicOperand operand1,

Operator operator,

StaticOperand operand2

| 

Filters node-tuples based on the outcome of a binary operation.

For any comparison, operand2 always evaluates to a scalar value. In
contrast, operand1 may evaluate to an array of values (for example, the
values of a multi-valued property), in which case the comparison is
separately performed for each element of the array, and the Comparison
constraint is satisfied as a whole if the comparison against *any*
element of the array is satisfied.

If operand1 and operand2 evaluate to values of different property types,
the value of operand2 is converted to the property type of the value of
operand1 as described in §3.6.4 *Property Type Conversion*. If the type
conversion fails, the query is *invalid*.

Given an operator O and a property instance P of property type T, P can
be compared using O only if:

-  The implementation supports comparison of properties of type T using
   O. For example, some implementations may permit EqualTo and
   NotEqualTo as comparison operators for BINARY properties while others
   may not.

-  Assuming that comparison of properties of type T is supported in
   general, the property definition that applies to P (found in the node
   type of P's parent node) must also list O among its *available query
   operators* (see §3.7.3.3 *Available Query Operators*).

If operator is not supported for the property type of operand1, the
query is *invalid*.

If operand1 evaluates to null (for example, if the operand evaluates the
value of a property which does not exist), the constraint is not
satisfied.

The EqualTo operator is satisfied *only if* the value of operand1 *is
equal to* the value of operand2, as described in §3.6.5 *Comparison of
Values*.

The NotEqualTo operator is satisfied *unless* the value of operand1 *is
equal to* the value of operand2, as described in §3.6.5 *Comparison of
Values*.

The LessThan operator is satisfied *only if* the value of operand1 *is
ordered* *before* the value of operand2, as described in §3.6.5
*Comparison of Values*.

The LessThanOrEqualTo operator is satisfied *unless* the value of
operand1 *is ordered* *after* the value of operand2, as described in
§3.6.5 *Comparison of Values*.

The GreaterThan operator is satisfied *only if* the value of operand1
*is ordered* *after* the value of operand2, as described in §3.6.5
*Comparison of Values*.

The GreaterThanOrEqualTo operator is satisfied *unless* the value of
operand1 *is ordered* *before* the value of operand2, as described in
§3.6.5 *Comparison of Values*.

The Like operator is satisfied *only if* the value of operand1 *matches*
the pattern specified by the value of operand2, where in the pattern:

-  the character “%” matches zero or more characters, and

-  the character “\_” (underscore) matches exactly one character, and

-  the string “\\\ *x*\ ” matches the character “\ *x*\ ”, and

-  all other characters match themselves.

**JCR-SQL2**

Comparison ::= DynamicOperand Operator StaticOperand

| 
| **JCR-JQOM**

A Comparison is created with:

| Comparison QueryObjectModelFactory.
|  comparison(DynamicOperand operand1,
|  String operator,
|  StaticOperand operand2)

Comparison extends Constraint and declares:

DynamicOperand Comparsion.getOperand1()

String Comparison.getOperator()

StaticOperand Comparison.getOperand2()

6.7.17 Operator
~~~~~~~~~~~~~~~

**AQM**

enum Operator ::=

EqualTo,

NotEqualTo,

LessThan,

LessThanOrEqualTo,

GreaterThan,

GreaterThanOrEqualTo,

Like

| 

**JCR-SQL2**

Operator ::= EqualTo \| NotEqualTo \| LessThan \|

LessThanOrEqualTo \| GreaterThan \|

GreaterThanOrEqualTo \| Like

| 

EqualTo ::= '='

| 

NotEqualTo ::= '<>'

| 

LessThan ::= '<'

| 

LessThanOrEqualTo ::= '<='

| 

GreaterThan ::= '>'

| 

GreaterThanOrEqualTo ::= '>='

| 

Like ::= 'LIKE'

| 
| **JCR-JQOM**

An operator is a String constant. One of:

QueryObjectModelConstants.JCR\_OPERATOR\_EQUAL\_TO

QueryObjectModelConstants.JCR\_OPERATOR\_GREATER\_THAN

QueryObjectModelConstants.JCR\_OPERATOR\_GREATER\_THAN\_OR\_EQUAL\_TO

QueryObjectModelConstants.JCR\_OPERATOR\_LESS\_THAN

QueryObjectModelConstants.JCR\_OPERATOR\_LESS\_THAN\_OR\_EQUAL\_TO

QueryObjectModelConstants.JCR\_OPERATOR\_LIKE

QueryObjectModelConstants.JCR\_OPERATOR\_NOT\_EQUAL\_TO

6.7.18 PropertyExistence
~~~~~~~~~~~~~~~~~~~~~~~~

**AQM**

type PropertyExistence extends Constraint ::=

Name selectorName,

Name propertyName

| 

Tests the existence of a property.

A node-tuple satisfies the constraint if the selectorName node has a
property named propertyName.

The query is *invalid* if selectorName is not the name of a selector in
the query.

**JCR-SQL2**

PropertyExistence ::=

selectorName'.'propertyName 'IS NOT NULL' \|

| propertyName 'IS NOT NULL' /\* If only one
|  selector exists in
|  this query\*/

| /\* Note: The negation, 'NOT x IS NOT NULL'
|  can be written 'x IS NULL' \*/

| 
| **JCR-JQOM**

A PropertyExistence is created with:

| PropertyExistence QueryObjectModelFactory.
|  propertyExistence(String selectorName, String propertyName)

PropertyExistence extends Constraint and declares:

String PropertyExistence.getSelectorName()

String PropertyExistence.getPropertyName()

6.7.19 FullTextSearch
~~~~~~~~~~~~~~~~~~~~~

**AQM**

type FullTextSearch extends Constraint ::=

Name selectorName,

Name? propertyName,

StaticOperand fullTextSearchExpression

| 

Performs a full-text search.

The full-text search expression is evaluated against the set of
full-text indexed properties within the full-text search scope. If
propertyName is specified, the full-text search scope is the property of
that name on the selectorName node in the node-tuple; otherwise the
full-text search scope is implementation determined.

Whether a particular property is full-text indexed can be determined by
the *full-text searchable* attribute of its property definition (see
§3.7.3.4 *Full-Text Searchable*).

It is implementation-determined whether fullTextSearchExpression is
independently evaluated against each full-text indexed property in the
full-text search scope, or collectively evaluated against the set of
such properties using some implementation-determined mechanism.

Similarly, for multi-valued properties, it is implementation-determined
whether fullTextSearchExpression is independently evaluated against each
element in the array of values, or collectively evaluated against the
array of values using some implementation-determined mechanism.

The fullTextSearchExpression is a StaticOperand, meaning that it may be
either a literal JCR value or a bound variable (which evaluates to a JCR
value). The value must be a STRING (or convertible to a STRING) that
conforms to the following grammar:

| FullTextSearchLiteral ::= Disjunct
|  {Space 'OR' Space Disjunct}

| 

Disjunct ::= Term {Space Term}

| 

Term ::= ['-'] SimpleTerm

| 

SimpleTerm ::= Word \| '"' Word {Space Word} '"'

| 

Word ::= NonSpaceChar {NonSpaceChar}

| 

Space ::= SpaceChar {SpaceChar}

| 

| NonSpaceChar ::= Char – SpaceChar
|  /\* Any Char except SpaceChar \*/

| 

SpaceChar ::= ' ' /\* Unicode character U+0020 \*/

| 

Char ::= /\* Any character \*/

| 

/\* See §1.3.1 String Literals in Syntactic Grammars for details

on the interpetation of string literals in this grammar \*/

A query satisfies a FullTextSearch constraint if the value (or values)
of the full-text indexed properties within the full-text search scope
satisfy the specified fullTextSearchExpression, evaluated as follows:

-  A term *not* preceded with “-” (minus sign) is satisfied only if the
   value *contains* that term.

-  A term preceded with “-” (minus sign) is satisfied only if the value
   *does not contain* that term.

-  Terms separated by whitespace are implicitly “ANDed”.

-  Terms separated by “OR” are “ORed”.

-  “AND” has higher precedence than “OR”.

-  Within a term, each “"” (double quote), “-” (minus sign), and “\\”
   (backslash) must be escaped by a preceding “\\”.

The query is *invalid* if:

-  selectorName is not the name of a selector in the query, or

-  fullTextSearchExpression does not conform to the above grammar (as
   augmented by the implementation).

The grammar and semantics described above defines the *minimal*
requirement, meaning that any search string accepted as valid by an
implementation must conform to this grammar. An implementation may,
however, restrict acceptable search strings further by augmenting this
grammar and expanding the semantics appropriately.

If propertyName is specified but, for a node-tuple, the selectorName
node does not have a property named propertyName, the query is *valid*
but the constraint is not satisfied.

**JCR-SQL2**

| FullTextSearch ::=
|  'CONTAINS(' ([selectorName'.']propertyName \|
|  selectorName'.\*') ','

FullTextSearchExpression ')'

| /\* If only one selector exists in this query,
|  explicit specification of the selectorName
|  preceding the propertyName is optional \*/

| 

FullTextSearchExpression ::= BindVariable \|

''' FullTextSearchLiteral '''

/\* see above \*/

| 
| **JCR-JQOM**

A FullTextSearch is created with:

| FullTextSearch QueryObjectModelFactory.
|  fullTextSearch(String selectorName,
|  String propertyName,
|  StaticOperand fullTextSearchExpression)

FullTextSearch extends Constraint and declares:

String FullTextSearch.getSelectorName()

String FullTextSearch.getPropertyName()

StaticOperand FullTextSearch.getFullTextSearchExpression()

6.7.20 SameNode
~~~~~~~~~~~~~~~

**AQM**

type SameNode extends Constraint ::=

Name selectorName,

Path path

| 

Tests whether the selectorName node is reachable by the absolute path
specified. A node-tuple satisfies the constraint only if:

selectorNode.isSame(session.getNode(path))

would return true, where selectorNode is the node for the specified
selector.

The query is *invalid* if:

-  selectorName is not the name of a selector in the query, or

-  path is not a syntactically valid absolute path (see §3.3.4 *Lexical
   Path Grammar*). Note, however, that if path is syntactically valid
   but does not identify a node in the workspace (or the node is not
   visible to this session, because of access control constraints), the
   query is *valid* but the constraint is not satisfied.

**JCR-SQL2**

SameNode ::= 'ISSAMENODE(' [selectorName ','] Path ')'

| /\* If only one selector exists in this query, explicit
|  specification of the selectorName is optional \*/

| 
| **JCR-JQOM**

A SameNode is created with:

| SameNode QueryObjectModelFactory.
|  sameNode(String selectorName, String path)

SameNode extends Constraint and declares:

String SameNode.getSelectorName()

String SameNode.getPath()

6.7.21 ChildNode
~~~~~~~~~~~~~~~~

**AQM**

type ChildNode extends Constraint ::=

Name selectorName,

Path path

| 

Tests whether the selectorName node is a child of a node reachable by
the absolute path specified. A node-tuple satisfies the constraint only
if:

selectorNode.getParent().isSame(session.getNode(path))

would return true, where selectorNode is the node for the specified
selector.

The query is *invalid* if:

-  selectorName is not the name of a selector in the query, or

-  path is not a syntactically valid absolute path (see §3.3.4 *Lexical
   Path Grammar*). Note, however, that if path is syntactically valid
   but does not identify a node in the workspace (or the node is not
   visible to this session, because of access control constraints), the
   query is *valid* but the constraint is not satisfied.

**JCR-SQL2**

ChildNode ::= 'ISCHILDNODE(' [selectorName ','] Path ')'

| /\* If only one selector exists in this query, explicit
|  specification of the selectorName is optional \*/

| 
| **JCR-JQOM**

A ChildNode is created with:

| ChildNode QueryObjectModelFactory.
|  childNode(String selectorName, String path)

ChildNode extends Constraint and declares:

String ChildNode.getSelectorName()

String ChildNode.getParentPath()

6.7.22 DescendantNode
~~~~~~~~~~~~~~~~~~~~~

**AQM**

type DescendantNode extends Constraint ::=

Name selectorName,

Path path

| 

Tests whether the selectorName node is a descendant of a node reachable
by the absolute path specified. A node-tuple satisfies the constraint
only if:

| selectorNode.getAncestor(n).isSame(session.getNode(path))
|  && selectorNode.getDepth() > n

would return true for some non-negative integer n, where selectorNode is
the node for the specified selector.

The query is *invalid* if:

-  selectorName is not the name of a selector in the query, or

-  path is not a syntactically valid absolute path (see §3.3.4 *Lexical
   Path Grammar*). Note, however, that if path is syntactically valid
   but does not identify a node in the workspace (or the node is not
   visible to this session, because of access control constraints), the
   query is *valid* but the constraint is not satisfied.

**JCR-SQL2**

DescendantNode ::=

'ISDESCENDANTNODE(' [selectorName ','] Path ')'

| /\* If only one selector exists in this query, explicit
|  specification of the selectorName is optional \*/

| 
| **JCR-JQOM**

A DescendantNode is created with:

| DescendantNode QueryObjectModelFactory.
|  descendantNode(String selectorName, String path)

DescendantNode extends Constraint and declares:

String DescendantNode.getSelectorName()

String DescendantNode.getAncestorPath()

6.7.23 Path
~~~~~~~~~~~

**AQM**

type Path

| 

A JCR path.

**JCR-SQL2**

| Path ::= '[' quotedPath ']' \|
|  '[' simplePath ']' \|

simplePath

| 

| quotedPath ::= /\* A JCR Path that contains non-SQL-legal
|  characters \*/

| 

| simplePath ::= /\* A JCR Name that contains only SQL-legal
|  characters\ :sup:``:sup:`11` <#sdfootnote11sym>`__` \*/

| 
| **JCR-JQOM**

A JCR path in string form (standard, non-standard, normalized or
non-normalized, see §3.3.5 *Standard and Non-Standard Form* and §3.3.6.3
*Normalized Paths*).

6.7.24 Operand
~~~~~~~~~~~~~~

**AQM**

abstract type Operand

| 

**JCR-SQL2**

Operand ::= StaticOperand \| DynamicOperand

/\* 'Operand' not referenced in JCR-SQL2

grammar. For possible future use. \*/

| 
| **JCR-JQOM**

Operand is an empty interface with subclasses StaticOperand and
DynamicOperand.

6.7.25 StaticOperand
~~~~~~~~~~~~~~~~~~~~

**AQM**

abstract type StaticOperand extends Operand

| 

An operand whose value can be determined from static analysis of the
query, prior to its evaluation.

**JCR-SQL2**

StaticOperand ::= Literal \| BindVariableValue

| 
| **JCR-JQOM**

StaticOperand is an empty interface with subclasses Literal and
BindVariableValue.

6.7.26 DynamicOperand
~~~~~~~~~~~~~~~~~~~~~

**AQM**

abstract type DynamicOperand extends Operand

| 

An operand whose value can only be determined in evaluating the query.

**JCR-SQL2**

DynamicOperand ::= PropertyValue \| Length \| NodeName \|

NodeLocalName \| FullTextSearchScore \|

LowerCase \| UpperCase

| 
| **JCR-JQOM**

DynamicOperand is an empty interface with subclasses PropertyValue,
Length, NodeName, NodeLocalName, FullTextSearchScore, LowerCase and
UpperCase.

6.7.27 PropertyValue
~~~~~~~~~~~~~~~~~~~~

**AQM**

type PropertyValue extends DynamicOperand ::=

Name selectorName,

Name propertyName

| 

Evaluates to the value (or values, if multi-valued) of a property.

If, for a node-tuple, the selectorName node does not have a property
named propertyName, the operand evaluates to null.

The query is *invalid* if selectorName is not the name of a selector in
the query.

**JCR-SQL2**

PropertyValue ::= [selectorName'.'] propertyName

| /\* If only one selector exists in this query,
|  explicit specification of the selectorName is
|  optional \*/

| 
| **JCR-JQOM**

A PropertyValue is created with:

| PropertyValue QueryObjectModelFactory.
|  propertyValue(String selectorName, String propertyName)

PropertyValue extends DynamicOperand and declares:

String PropertyValue.getSelectorName()

String PropertyValue.getPropertyName()

6.7.28 Length
~~~~~~~~~~~~~

**AQM**

type Length extends DynamicOperand ::=

PropertyValue propertyValue

| 

Evaluates to the length (or lengths, if multi-valued) of a property. In
evaluating this operand, a repository *should* use the semantics defined
in §3.6.7 *Length of a Value*.

If propertyValue evaluates to null, the Length operand also evaluates to
null.

**JCR-SQL2**

Length ::= 'LENGTH(' PropertyValue ')'

| 
| **JCR-JQOM**

A Length is created with:

| Length QueryObjectModelFactory.
|  length(PropertyValue propertyValue)

Length extends DynamicOperand and declares:

PropertyValue Length.getPropertyValue()

6.7.29 NodeName
~~~~~~~~~~~~~~~

**AQM**

type NodeName extends DynamicOperand ::=

Name selectorName

| 

Evaluates to a NAME value equal to the *JCR name* of a node.

The query is *invalid* if selectorName is not the name of a selector in
the query.

**JCR-SQL2**

NodeName ::= 'NAME(' [selectorName] ')'

| /\* If only one selector exists in this query, explicit
|  specification of the selectorName is optional \*/

| 
| **JCR-JQOM**

A NodeName is created with:

| NodeName QueryObjectModelFactory.
|  nodeName(String selectorName)

NodeName extends DynamicOperand and declares:

String NodeName.getSelectorName()

6.7.30 NodeLocalName
~~~~~~~~~~~~~~~~~~~~

**AQM**

type NodeLocalName extends DynamicOperand ::=

Name selectorName

| 

Evaluates to a STRING value equal to the *JCR local name* of a node.

The query is *invalid* if selectorName is not the name of a selector in
the query.

**JCR-SQL2**

NodeLocalName ::= 'LOCALNAME(' [selectorName] ')'

| /\* If only one selector exists in this query,
|  explicit specification of the selectorName is
|  optional \*/

| 
| **JCR-JQOM**

A NodeLocalName is created with:

| NodeLocalName QueryObjectModelFactory.
|  nodeLocalName(String selectorName)

NodeLocalName extends DynamicOperand and declares:

String NodeLocalName.getSelector()

6.7.31 FullTextSearchScore
~~~~~~~~~~~~~~~~~~~~~~~~~~

**AQM**

type FullTextSearchScore extends DynamicOperand ::=

Name selectorName

| 

Evaluates to a DOUBLE value equal to the full-text search score of a
node.

Full-text search score ranks a selector's nodes by their relevance to
the fullTextSearchExpression specified in a FullTextSearch. The values
to which FullTextSearchScore evaluates and the interpretation of those
values are implementation specific. FullTextSearchScore may evaluate to
a constant value in a repository that does not support full-text search
scoring or has no full-text indexed properties.

The query is *invalid* if selector is not the name of a selector in the
query.

**JCR-SQL2**

FullTextSearchScore ::= 'SCORE(' [selectorName] ')'

| /\* If only one selector exists in this query,
|  explicit specification of the selectorName
|  is optional \*/

| 
| **JCR-JQOM**

A FullTextSearchScore is created with:

| FullTextSearchScore QueryObjectModelFactory.
|  fullTextSearchScore(String selectorName)

FullTextSearchScore extends DynamicOperand and declares:

String FullTextSearchScore.getSelector()

6.7.32 LowerCase
~~~~~~~~~~~~~~~~

**AQM**

type LowerCase extends DynamicOperand ::=

DynamicOperand operand

| 

Evaluates to the lower-case string value (or values, if multi-valued) of
operand.

If operand does not evaluate to a string value, its value is first
converted to a string as described in §3.6.4 *Property Type Conversion*.
The lower-case string value is computed as though the toLowerCase()
method of java.lang.String were called.

If operand evaluates to null, the LowerCase operand also evaluates to
null.

**JCR-SQL2**

LowerCase ::= 'LOWER(' DynamicOperand ')'

| 
| **JCR-JQOM**

A LowerCase is created with:

| LowerCase QueryObjectModelFactory.
|  lowerCase(DynamicOperand operand)

LowerCase extends DynamicOperand and declares:

DynamicOperand LowerCase.getOperand()

6.7.33 UpperCase
~~~~~~~~~~~~~~~~

**AQM**

type UpperCase extends DynamicOperand ::=

DynamicOperand operand

Evaluates to the upper-case string value (or values, if multi-valued) of
operand.

If operand does not evaluate to a string value, its value is first
converted to a string as described in §3.6.4 *Property Type Conversion*.
The upper-case string value is computed as though the toUpperCase()
method of java.lang.String were called.

If operand evaluates to null, the UpperCase operand also evaluates to
null.

**JCR-SQL2**

UpperCase ::= 'UPPER(' DynamicOperand ')'

| 
| **JCR-JQOM**

An UpperCase is created with:

| UpperCase QueryObjectModelFactory.
|  upperCase(DynamicOperand operand)

UpperCase extends DynamicOperand and declares:

DynamicOperand UpperCase.getOperand()

6.7.34 Literal
~~~~~~~~~~~~~~

**AQM**

type Literal extends StaticOperand ::=

javax.jcr.Value Value

| 

A JCR value.

**JCR-SQL2**

Literal ::= CastLiteral \| UncastLiteral

| 

CastLiteral ::= 'CAST(' UncastLiteral ' AS ' PropertyType ')'

| 

PropertyType ::= 'STRING' \| 'BINARY' \| 'DATE' \| 'LONG' \| 'DOUBLE' \|

'DECIMAL' \| 'BOOLEAN' \| 'NAME' \| 'PATH' \|

'REFERENCE' \| 'WEAKREFERENCE' \| 'URI'

| 

UncastLiteral ::= UnquotedLiteral \| ''' UnquotedLiteral ''' \|

'“' UnquotedLiteral '“'

| 

UnquotedLiteral ::= /\* String form of a JCR Value, as defined in

§3.5.4 Conversion of Values \*/

| 
| An UncastLiteral may be interpreted as a Value of property type STRING
or some other type inferred from static analysis. A CastLiteral, on the
other hand, is interpreted as the string form of a Value of the
PropertyType indicated.

**JCR-JQOM**

A JCR Value. A Value object can be created using ValueFactory (see §6.10
*Literal Values*). Note that unlike in the case of JCR-SQL2, property
type information is intrinsic to the Value object, so no equivalent of
the CAST function is needed in JCR-JQOM.

6.7.35 BindVariable
~~~~~~~~~~~~~~~~~~~

**AQM**

type BindVariableValue extends StaticOperand ::=

Prefix bindVariableName

| 

Evaluates to the value of a bind variable.

The query is *invalid* if no value is bound to bindVariableName.

**JCR-SQL2**

BindVariableValue ::= '$'bindVariableName

| 

bindVariableName ::= Prefix

| 
| **JCR-JQOM**

A BindVariableValue is created with:

| BindVariableValue QueryObjectModelFactory.
|  bindVariableValue(String bindVariableName)

BindVariableValue extends StaticOperand and declares:

StaticOperand BindVariableValue.getBindVariableName()

6.7.36 Prefix
~~~~~~~~~~~~~

**AQM**

type Prefix

| 

A JCR prefix.

The query is *invalid* if the prefix does not satisfy the prefix
production in §3.2.5.2 *Qualified Form*.

**JCR-SQL2**

| Prefix ::= /\* A String that conforms to the JCR Name
|  prefix syntax. Not required to be an actual
|  prefix in use in the repository. The prefix
|  syntax is used simply to characterize the
|  range of possible variables. \*/

| 
| **JCR-JQOM**

A string that conforms to the JCR Name prefix syntax. This is not
required to be an actual prefix in use in the repository. The prefix
syntax is used simply to characterize the range of possible variables.

6.7.37 Ordering
~~~~~~~~~~~~~~~

**AQM**

type Ordering ::=

DynamicOperand operand,

Order order

| 

Determines the relative order of two node-tuples by evaluating operand
for each.

For a first node-tuple, nt1, for which operand evaluates to v1, and a
second node-tuple, nt2, for which operand evaluates to v2:

If operand is a PropertyValue (see §6.7.27 *PropertyValue*) of a
property P and the *query-orderable* attribute of the property
definition of P is false (see §3.7.3.5 *Query-Orderable*) then the
relative order of nt1 and nt2 is implementation determined, otherwise,
if the *query-orderable* attribute is true, then:

If order is Ascending, then:

-  if either v1 is null, v2 is null, or both v1 and v2 are null, the
   relative order of nt1 and nt2 is implementation determined, otherwise

-  if v1 is a different property type than v2, the relative order of nt1
   and nt2 is implementation determined, otherwise

-  if v1 *is ordered* *before* v2, as described in §3.6.5 *Comparison of
   Values*, then nt1 precedes nt2, otherwise

-  if v1 *is ordered* *after* v2, as described in §3.6.5 *Comparison of
   Values*, then nt2 precedes nt1, otherwise

-  the relative order of nt1 and nt2 is implementation determined and
   may be arbitrary.

Otherwise, if order is Descending, then:

-  if either v1 is null, v2 is null, or both v1 and v2 are null, the
   relative order of nt1 and nt2 is implementation determined, otherwise

-  if v1 is a different property type than v2, the relative order of nt1
   and nt2 is implementation determined, otherwise

-  if v1 *is ordered* *before* v2, as described in §3.6.5 *Comparison of
   Values*, then nt2 precedes nt1, otherwise

-  if v1 *is ordered* *after* v2, as described in §3.6.5 *Comparison of
   Values*, then nt1 precedes nt2, otherwise

-  the relative order of nt1 and nt2 is implementation determined and
   may be arbitrary.

The query is *invalid* if operand does not evaluate to a scalar value.

**JCR-SQL2**

orderings ::= Ordering {',' Ordering}

| 

Ordering ::= DynamicOperand [Order]

| 
| If Order is omitted in the JCR-SQL2 statement the default is ASC (see
§6.7.38 *Order*).

**JCR-JQOM**

An ascending Ordering is created with:

| Ordering QueryObjectModelFactory.
|  ascending(DynamicOperand operand)

A descending Ordering is created with:

| Ordering QueryObjectModelFactory.
|  descending(DynamicOperand operand)

Ordering declares:

DynamicOperand Ordering.getOperand()

String Ordering.getOrder()

6.7.38 Order
~~~~~~~~~~~~

**AQM**

enum Order ::=

Ascending,

Descending

| 
| Order is either Ascending or Descending.

**JCR-SQL2**

Order ::= Ascending \| Descending

| 

Ascending ::= 'ASC'

| 

Descending ::= 'DESC'

| 
| **JCR-JQOM**

An order is a String constant. One of:

QueryObjectModelConstants.JCR\_ORDER\_ASCENDING

QueryObjectModelConstants.JCR\_ORDER\_DESCENDING

6.7.39 Column
~~~~~~~~~~~~~

**AQM**

type Column ::=

Name selectorName,

Name? propertyName,

Name? columnName

| 

Defines a column to include in the tabular view of query results.

If propertyName is not specified, a column is included for each
single-valued non-residual property of the node type specified by the
nodeType attribute of the selector selectorName.

If propertyName is specified, columnName is required and used to name
the column in the tabular results. If propertyName is not specified,
columnName must not be specified, and the included columns will be named
“\ *selectorName.propertyName*\ ”.

The query is *invalid* if:

-  selectorName is not the name of a selector in the query, or

-  propertyName is specified but does not evaluate to a scalar value, or

-  propertyName is specified but columnName is omitted, or

-  propertyName is omitted but columnName is specified, or

-  the columns in the tabular view are not uniquely named, whether those
   column names are specified by columnName (if propertyName is
   specified) or generated as described above (if propertyName is
   omitted).

If propertyName is specified but, for a node-tuple, the selectorName
node does not have a property named propertyName, the query is *valid*
and the column has null value.

**JCR-SQL2**

columns ::= (Column ',' {Column}) \| '\*'

| 

Column ::= ([selectorName'.']propertyName

['AS' columnName]) \|

(selectorName'.\*')

| /\* If only one selector exists in this query, explicit
|  specification of the selectorName preceding the
|  propertyName is optional \*/

| 

selectorName ::= Name

| 

propertyName ::= Name

| 

columnName ::= Name

| 
| **JCR-JQOM**

A Column is created with:

| Column QueryObjectModelFactory.
|  column(String selectorName,
|  String propertyName,
|  String columnName)

Column declares:

String Column.getSelectorName()

String Column.getPropertyName()

String Column.getColumnName()

6.8 QueryManager
----------------

The query function is accessed through the QueryManager object, acquired
through

QueryManager Workspace.getQueryManager().

6.8.1 Supported Languages
~~~~~~~~~~~~~~~~~~~~~~~~~

String[] QueryManager.getSupportedQueryLanguages()

returns an array of strings representing the supported query languages.
In all repositories that support query, the array will contain at least
the string constants

Query.JCR\_SQL2 and

Query.JCR\_JQOM.

Any additional languages also supported will also be listed in the
returned array.

6.9 Query Object
----------------

A new Query object can be created with

| Query QueryManager.
|  createQuery(String statement, String language).

The language parameter is a string representing one of the supported
languages. The statement parameter is the query statement itself. This
method is used for languages that are string-based (i.e., most
languages, such as JCR-SQL2) as well as for the *string serializations*
of non-string-based languages (such as JCR-JQOM). For example, the call

QM.createQuery(S, Query.JCR\_SQL2),

where QM is the QueryManager and S is a JCR-SQL2 statement, returns a
Query object encapsulating S.

However, the call

QM.createQuery(S, Query.JCR\_JQOM)

also works. It returns a QueryObjectModel (a subclass of Query) holding
the JCR-JQOM object tree equivalent to S.

In either case the returned Query object encapsulates the resulting
query. In some repositories the first method call (with JCR-SQL2
specified) may also result in a QueryObjectModel, though this is not
required.

6.9.1 QueryObjectModelFactory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To programmatically build a query tree using JCR-JQOM the user acquires
a QueryObjectModelFactory using

QueryObjectModelFactory QueryManager.getQOMFactory().

The user then builds the query tree using the factory methods of
QueryObjectModelFactory, ultimately resulting in a QueryObjectModel
object (a subclass of Query) representing the query.

6.9.1.1 Serialized Query Object Model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The JCR-SQL2 language, in addition to being a query language in its own
right is also the standard serialization of a valid JCR-JQOM object
tree. Since the two languages are formally equivalent they can always be
roundtripped.

6.9.2 Getting the Statement
~~~~~~~~~~~~~~~~~~~~~~~~~~~

String Query.getStatement()

returns the statement set for the query. If the Query was created with
an explicitly supplied statement string parameter using
QueryManager.createQuery then this method returns that statement. The
statement returned must be semantically identical to the original
statement but need not be an identical string (for example, it may be
normalized).

If the Query is actually a QueryObjectModel created with
QueryObjectModelFactory.createQuery then Query.getStatement must return
the serialized form of the query, in JCR-SQL2 syntax.

6.9.3 Getting the Language
~~~~~~~~~~~~~~~~~~~~~~~~~~

String Query.getLanguage()

returns the language in which the query is specified. If the Query was
created with an explicitly supplied language string parameter using
QueryManager.createQuery then this method returns that string.

If the Query is actually a QueryObjectModel created with
QueryObjectModelFactory.createQuery then Query.getLanguage will return
the string constant Query.JCR\_SQL2.

6.9.4 Query Limit
~~~~~~~~~~~~~~~~~

Query.setLimit(long limit)

Sets the maximum size of the result set, expressed in terms of the
number of Rows, as found in the table-view of the QueryResult (see §6.11
*QueryResult*).

6.9.5 Query Offset
~~~~~~~~~~~~~~~~~~

Query.setOffset(long offset)

Sets the offset within the full result set at which the returned result
set should start, expressed in terms of the number of Rows to skip, as
found in the table-view of the QueryResult (see §6.11 *QueryResult*).

6.9.6 Bind Variables
~~~~~~~~~~~~~~~~~~~~

A query may contain variables.

void Query.bindValue(String varName, Value value)

binds value to the variable varName.

In JCR-SQL2 a bind variable is indicated by a leading dollar-sign. In
JCR-JQOM it is a QOM object created with the QueryObjectModelFactory
(see §6.7.35 *BindVariable*).

The method

String[] Query.getBindVariableNames()

returns the names of the bind variables in the query. If the query does
not contains any bind variables then an empty array is returned.

6.9.7 Stored Query
~~~~~~~~~~~~~~~~~~

When a new Query object is first created it is a *transient query*. If
the repository supports the node type nt:query, then a transient query
can be stored in content by calling

Node Query.storeAsNode(String absPath).

This creates an nt:query node at the specified path. A save is required
to persist the node.

6.9.7.1 nt:query
^^^^^^^^^^^^^^^^

The nt:query node type is defined as follows:

[nt:query]

- jcr:statement (STRING)

- jcr:language (STRING)

jcr:statement holds the string returned by Query.getStatement().

jcr:language holds the string returned by Query.getLanguage().

If the language of this query is JCR-JQOM, jcr:statement will hold the
JCR-SQL2 serialization of the JCR-JQOM object tree and
Query.getStatement() will return that string. Also, since the original
query was constructed using JCR-JQOM, jcr:language records the language
as “JCR-JQOM” and Query.getLanguage() returns “JCR-JQOM”.

6.9.7.2 Stored Query Path
^^^^^^^^^^^^^^^^^^^^^^^^^

String Query.getStoredQueryPath()

returns the absolute path of a Query that has been stored as a node.

6.9.7.3 Retrieving a Stored Query
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Query QueryManager.getQuery(Node node)

retrieves a previously persisted query and instantiates it as a Query
object.

6.9.7.4 Namespace Fragility
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Note that the query statement stored within a stored query (the value of
the property jcr:statement) is stored as a simple string. Therefore, if
it contains qualified JCR names it will be *namespace-fragile*. If the
stored query is run in a context where a prefix used maps to a different
namespace than it did upon creation then the query will not reproduce
the original result. To mitigate this, users should either,

-  always use expanded form names within queries, or

-  always ensure that appropriate namespace mappings are in place when a
   stored query is executed.

6.10 Literal Values
-------------------

When creating a Comparison object (see 6.7.16 *Comparison*) a user may
wish to pass a literal property value (see 6.7.34 *Literal*) in the form
of a Value object. Value objects are created using the ValueFactory
acquired through

ValueFactory Session.getValueFactory().

(see §10.4.3 *Creating Value Objects*).

6.11 QueryResult
----------------

Once a query has been defined, it can be executed. The method

QueryResult Query.execute()

returns the a QueryResult object. The QueryResult is returned in two
formats: as a table and as a list of nodes.

6.11.1 Table View
~~~~~~~~~~~~~~~~~

The table view of a result is accessed with

RowIterator QueryResult.getRows()

The returned RowIterator holds a series of Row objects. A Row object
represents a single row of the query result table which corresponds to a
node-tuple returned by the query.

6.11.1.1 Row
^^^^^^^^^^^^

Upon retrieving an individual Row, the set of Values making up that row
can be retrieved with

Value[] Row.getValues()

The values are returned in that same order as their corresponding column
names are returned by QueryResult.getColumns.

Value Row.getValue(String columnName)

returns the Value of the indicated column of the Row. The names of the
columns can be retrieved with

String[] QueryResult.getColumnNames().

In queries with only one selector included among the specified columns,
each Row corresponds to a single Node. In such cases

Node Row.getNode()

returns that Node.

In queries with more than one selector included among the specified
columns, a particular selector must be indicated in order to retrieve
its corresponding Node . This is done using

Node Row.getNode(String selectorName).

The available selector names can be retrieved with

String[] QueryResult.getSelectorNames().

If the Row is from a result involving outer joins, it may have no Node
corresponding to the specified selector, in which case this method
returns null.

The methods

String Row.getPath() and

String Row.getPath(String selectorName)

| are equivalent to Row.getNode().getPath() and
| Row.getNode(String selectorName).getPath(), respectively. However,
some implementations may be able gain efficiency by not resolving the
actual Node.

The method

double Row.getScore(String selectorName)

returns the full text search score for this row that is associated with
the specified selector. This is equivalent to the score of the Node
associated with that this Row and that selector.

If no FullTextSearchScore AQM object (see §6.7.31 *FullTextSearchScore*)
is associated with the specified selector this method will still return
a value but that value may not be meaningful or may simply reflect the
minimum possible relevance level (for example, in some systems this
might be a score of 0).

If this Row is from a result involving outer joins, it may have no Node
corresponding to the specified selector, in which case this method
returns an implementation selected value, as it would if there were no
FullTextSearchScore associated with the selector.

The method

double Row.getScore()

works identically to Row.getScore(String selectorName), but only in
cases where there is exactly one selector and therefore its name need
not be explicitly specified.

6.11.2 Node View
~~~~~~~~~~~~~~~~

For queries with only one selector

QueryResult.getNodes()

returns an iterator over all matching nodes in the order specified by
the query. For queries with more than one selector the order in which
nodes are returned is implementation-specific.

6.12 Query Scope
----------------

Each Query is bound to a Session object via the QueryManager through
which it was created and the Workspace object through which that
QueryManager was acquired. Through its associated Workspace and Session
objects a query is therefore bound to a single persistent workspace and
a single transient store.

6.12.1 Access Restrictions
~~~~~~~~~~~~~~~~~~~~~~~~~~

A query result always respects the access restrictions of its bound
Session. This includes all restrictions, as reflected in the
*capabilities* of the Session, which encompasses *privileges*,
*permissions* and *other restrictions* (see §9 *Permissions and
Capabilities*).

In general, if the bound Session does not have read access to a
particular item, then that item will not be included in the result set
even if it would otherwise constitute a match.

6.12.2 Queryable Content
~~~~~~~~~~~~~~~~~~~~~~~~

A query runs against *either*

-  the content of its bound persistent workspace, *without regard to any
   pending changes* in its bound transient store, or

-  the content of its bound persistent workspace *as modified by the
   pending changes* in its bound transient store.

The choice of which scope to use is an implementation-variant.

6.12.3 Query Result Items
~~~~~~~~~~~~~~~~~~~~~~~~~

Regardless of which scope is used, when an item is accessed from within
a QueryResult object, the state of the item returned will obey the same
semantics as if it were retrieved using a normal Node.getNode or
Node.getProperty: the item state will reflect any pending changes in
transient store of the Session. As a result, it is possible that an item
returned as a match will not reflect the state that caused it to *be* a
match (i.e., its persistent state). Applications can clear the Session
(either through save or refresh(false)) before running a query in order
to avoid such discrepancies.
