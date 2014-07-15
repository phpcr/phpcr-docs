====================================================================
JCR 2.0: 1 Preface (Content Repository for Java Technology API v2.0)
====================================================================

1 Preface
=========

The Content Repository API for Java™ Technology Specification, Version
2.0 (JCR 2.0 Specification) consists of a normative part and a
non-normative part.

The normative part consists of:

-  This document, excluding the appendix.

-  The source code of javax.jcr and its subpackages.

-  The Javadoc reference.

In case of a conflict this document takes precedence over the source
code and the source code takes precedence over the Javadoc.

The non-normative part consists of:

-  The appendix of this document.

-  The jar file of javax.jcr and its subpackages.

The JCR 2.0 Specification was created and released through the Java
Community Process (JCP) under Java Specification Request 283 (JSR 283).

1.1 Previous Versions
---------------------

The Content Repository for Java™ Technology API Specification, Version
1.0 (JCR 1.0 Specification) was created and released through the Java
Community Process (JCP) under Java Specification Request 170 (JSR 170).

1.2 Coverage
------------

This document describes the abstract repository model and Java API of
JCR. The API is described from a high-level, functional perspective.
Consult the accompanying Javadoc for full information on signature
variants and exceptions.

1.2.1 Classes and Interfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unless otherwise indicated, all Java classes and interfaces mentioned
are in the package javax.jcr and its subpackages. Non-JCR classes
mentioned are always fully qualified. The only exception is
java.lang.String, which is used throughout and written simply as String.

1.2.2 Null Parameters
~~~~~~~~~~~~~~~~~~~~~

When describing JCR API methods, this specification and the Javadoc
assume that all parameters passed are non-null, unless otherwise stated.
If null is passed as parameter and its behavior is not explicitly
described in this specification or in the Javadoc, then the behavior of
the method in that case is implementation-specific.

1.3 Typographical Conventions
-----------------------------

A monospaced font is used for JCR names and paths, and all instances of
machine-readable text (Java code, XML, grammars, JCR-SQL2 examples,
URIs, etc.).

1.3.1 String Literals in Syntactic Grammars
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Formal grammars are used at various places in the specification to
define the syntax of string-based entities such as names, paths, search
languages and other notations.

When a *string literal* appears as a terminal symbol within a grammar,
each character literal in that string corresponds to exactly one Unicode
code point.

The intended code point of such a character literal must be determined
only by reference to the Unicode Basic Latin code
chart\ :sup:``:sup:`1` <#sdfootnote1sym>`__` and no other part of the
Unicode character set.

Any code point outside the Basic Latin set *cannot* be the intended code
point of such a character literal, even if the grapheme of the code
point superficially resembles that of the character literal.

For example, in the following production (excerpted from §3.2.2 *Local
Names*).

InvalidChar ::= '/' \| ':' \| '[' \| ']' \| '\|' \| '\*'

The code points indicated by the character literals are, respectively,
U+002F (“/”), U+003A (“:”), U+005B (“[“), U+005D (“]”), U+007C (“\|”)
and U+002A (“\*”).

1.4 System Requirements
-----------------------

The JCR 2.0 requires Java Runtime Environment (JRE) 1.4 or greater.

1.5 License
-----------

Day Management AG (“Licensor”) is willing to license this specification
to you ONLY UPON THE CONDITION THAT YOU ACCEPT ALL OF THE TERMS
CONTAINED IN THIS LICENSE AGREEMENT (“Agreement”). Please read the terms
and conditions of this Agreement carefully.

| Content Repository for Java Technology API 2.0 Specification
(“Specification”)
| Status: FCS
| Release: 10 August 2009

| Copyright 2009 Day Management AG
| Barfuesserplatz 6, 4001 Basel, Switzerland.
| All rights reserved.

NOTICE; LIMITED LICENSE GRANTS

1. License for Purposes of Evaluation and Developing Applications.
Licensor hereby grants you a fully-paid, non-exclusive,
non-transferable, worldwide, limited license (without the right to
sublicense), under Licensor's applicable intellectual property rights to
view, download, use and reproduce the Specification only for the purpose
of internal evaluation. This includes developing applications intended
to run on an implementation of the Specification provided that such
applications do not themselves implement any portion(s) of the
Specification.

2. License for the Distribution of Compliant Implementations. Licensor
also grants you a perpetual, non-exclusive, non-transferable, worldwide,
fully paid-up, royalty free, limited license (without the right to
sublicense) under any applicable copyrights or, subject to the
provisions of subsection 4 below, patent rights it may have covering the
Specification to create and/or distribute an Independent Implementation
of the Specification that: (a) fully implements the Specification
including all its required interfaces and functionality; (b) does not
modify, subset, superset or otherwise extend the Licensor Name Space, or
include any public or protected packages, classes, Java interfaces,
fields or methods within the Licensor Name Space other than those
required/authorized by the Specification or Specifications being
implemented; and (c) passes the Technology Compatibility Kit (including
satisfying the requirements of the applicable TCK Users Guide) for such
Specification (“Compliant Implementation”). In addition, the foregoing
license is expressly conditioned on your not acting outside its scope.
No license is granted hereunder for any other purpose (including, for
example, modifying the Specification, other than to the extent of your
fair use rights, or distributing the Specification to third parties).

3. Pass-through Conditions. You need not include limitations (a)-(c)
from the previous paragraph or any other particular “pass through”
requirements in any license You grant concerning the use of your
Independent Implementation or products derived from it. However, except
with respect to Independent Implementations (and products derived from
them) that satisfy limitations (a)-(c) from the previous paragraph, You
may neither: (a) grant or otherwise pass through to your licensees any
licenses under Licensor's applicable intellectual property rights; nor
(b) authorize your licensees to make any claims concerning their
implementation's compliance with the Specification.

4. Reciprocity Concerning Patent Licenses. With respect to any patent
claims covered by the license granted under subparagraph 2 above that
would be infringed by all technically feasible implementations of the
Specification, such license is conditioned upon your offering on fair,
reasonable and non-discriminatory terms, to any party seeking it from
You, a perpetual, non-exclusive, non-transferable, worldwide license
under Your patent rights that are or would be infringed by all
technically feasible implementations of the Specification to develop,
distribute and use a Compliant Implementation.

5. Definitions. For the purposes of this Agreement: “Independent
Implementation” shall mean an implementation of the Specification that
neither derives from any of Licensor's source code or binary code
materials nor, except with an appropriate and separate license from
Licensor, includes any of Licensor's source code or binary code
materials; “Licensor Name Space” shall mean the public class or
interface declarations whose names begin with “java”, “javax”,
“javax.jcr” or their equivalents in any subsequent naming convention
adopted by Licensor through the Java Community Process, or any
recognized successors or replacements thereof; and “Technology
Compatibility Kit” or “TCK” shall mean the test suite and accompanying
TCK User's Guide provided by Licensor which corresponds to the
particular version of the Specification being tested.

6. Termination. This Agreement will terminate immediately without notice
from Licensor if you fail to comply with any material provision of or
act outside the scope of the licenses granted above.

7. Trademarks. No right, title, or interest in or to any trademarks,
service marks, or trade names of Licensor is granted hereunder. Java is
a registered trademark of Sun Microsystems, Inc. in the United States
and other countries.

8. Disclaimer of Warranties. The Specification is provided “AS IS”.
LICENSOR MAKES NO REPRESENTATIONS OR WARRANTIES, EITHER EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, NON-INFRINGEMENT (INCLUDING AS A
CONSEQUENCE OF ANY PRACTICE OR IMPLEMENTATION OF THE SPECIFICATION), OR
THAT THE CONTENTS OF THE SPECIFICATION ARE SUITABLE FOR ANY PURPOSE.
This document does not represent any commitment to release or implement
any portion of the Specification in any product.

The Specification could include technical inaccuracies or typographical
errors. Changes are periodically added to the information therein; these
changes will be incorporated into new versions of the Specification, if
any. Licensor may make improvements and/or changes to the product(s)
and/or the program(s) described in the Specification at any time. Any
use of such changes in the Specification will be governed by the
then-current license for the applicable version of the Specification.

9. Limitation of Liability. TO THE EXTENT NOT PROHIBITED BY LAW, IN NO
EVENT WILL LICENSOR BE LIABLE FOR ANY DAMAGES, INCLUDING WITHOUT
LIMITATION, LOST REVENUE, PROFITS OR DATA, OR FOR SPECIAL, INDIRECT,
CONSEQUENTIAL, INCIDENTAL OR PUNITIVE DAMAGES, HOWEVER CAUSED AND
REGARDLESS OF THE THEORY OF LIABILITY, ARISING OUT OF OR RELATED TO ANY
FURNISHING, PRACTICING, MODIFYING OR ANY USE OF THE SPECIFICATION, EVEN
IF LICENSOR HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

10. Report. If you provide Licensor with any comments or suggestions in
connection with your use of the Specification (“Feedback”), you hereby:
(i) agree that such Feedback is provided on a non-proprietary and
non-confidential basis, and (ii) grant Licensor a perpetual,
non-exclusive, worldwide, fully paid-up, irrevocable license, with the
right to sublicense through multiple levels of sublicensees, to
incorporate, disclose, and use without limitation the Feedback for any
purpose related to the Specification and future versions,
implementations, and test suites thereof.

1.6 Acknowledgements
--------------------

The following people and organizations have contributed to this
specification:

David Nuescheler (Specification Lead)

Peeter Piegaze (Principal Author)

| 

Razmik Abnous

Tim Anderson

Gordon Bell

Tobias Bocanegra

Al Brown

Dave Caruana

Geoffrey Clemm

David Choy

Jeff Collins

Cornelia Davis

Chenggang Duan

Roy Fielding

Xaver Fischer

Gary Gershon

Stefan Guggisberg

Florent Guillaume

Berry van Halderen

Rich Howarth

Jens Huebel

Volker John

Alison Macmillan

Ryan McVeigh

Stefano Mazzocchi

James Myers

John Newton

James Owen

Franz Pfeifroth

David Pitfield

Nicolas Pombourcq

Corprew Reed

Julian Reschke

Marcel Reutegger

Celso Rodriguez

Steve Roth

Angela Schreiber

Victor Spivak

Paul Taylor

David B. Victor

Dan Whelan

Kevin Wiggen

Jukka Zitting

| 

| 

Alfresco

Apache Software Foundation

BEA

Day Software

Documentum

EMC

FileNet

| 

| 

Fujitsu

Greenbytes

Hippo

Hummingbird

IBM

Imerge

Intalio

Mobius

Nuxeo

Opentext

Oracle

Pacific Northwest National Laboratory

Saperion

Vignette

Xythos

|
