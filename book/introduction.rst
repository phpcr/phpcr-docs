Introduction
============

In the following chapters, we will show how to use the API. But first, you
need a very brief overview of the core elements of PHPCR. After reading this
guide, you should browse through the API documentation to get an idea what
operations you can do on each of those elements. See the conclusions for links
if you want to have more background.

It is important to know about the following concepts:

* **Node, Property**: An object model for data structured similar to XML. A
  node is like the xml element, the property like the xml attribute.
  Properties are acquired from their nodes or directly from the session by
  their path. Nodes are acquired from parent nodes or from the session by
  their path. Both are Item, sharing the methods of that base interface. Names
  can be namespaced as in xml, and additionally may contain whitespaces or
  other not xml-legal characters.
* **Session**: The authenticated connection to one workspace in the
  repository. Repository and workspace are immutable inside the Session. The
  session is the main interface to interact with the actual data. Sessions are
  acquired from a repository
* **Repository**: Linking to one storage location with possibly many
  workspaces. Repositories are created with the help of the repository
  factory.
* **RepositoryFactory**: Create repository instances for your implementation
  with implementation specific parameters.
* **Workspace**: Provides general operations on the workspace of the Session it is acquired from.

Note on Implementation PHPCR Support
------------------------------------

PHPCR is a modular standard and has a built-in way to discover the
capabilities of your implementation. Therefore implementations do not
have to support all sections of the specification.

TODO: Add a section about capability testing to show how to write portable code.
