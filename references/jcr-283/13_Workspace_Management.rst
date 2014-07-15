==================================================================================
JCR 2.0: 13 Workspace Management (Content Repository for Java Technology API v2.0)
==================================================================================

13 Workspace Management
=======================

A repository may support *workspace management*, which enables the
creation and deletion of workspaces through the JCR API. A repository
that supports this feature must support the semantics of multiple
workspaces (see §3.10 *Multiple Workspaces*) and support cross-workspace
operations (see §10.7.2 *Copying Across Workspaces* and §10.8 *Cloning
and Updating Nodes*).

Whether an implementation supports workspace management can be
determined by querying the repository descriptor table with

Repository.OPTION\_WORKSPACE\_MANAGMENT\_SUPPORTED.

A return value of true indicates support (see §24.2 *Repository
Descriptors*).

13.1 Creation and Deletion of Workspaces
----------------------------------------

The method

void Workspace.createWorkspace(String name)

creates a new workspace with the specified name. The new workspace will
contain only a root node. The new workspace can be accessed through a
login specifying its name.

| void Workspace.createWorkspace(String name,
|  String srcWorkspace)

creates a new workspace with the specified name initialized with a clone
of the content of the workspace srcWorkspace (see §10.8.1 *Cloning Nodes
Across Workspaces*). Semantically, this method is equivalent to creating
a new workspace and manually cloning srcWorkspace to it. However, this
method may assist some implementations in optimizing subsequent
Node.update and Node.merge calls between the new workspace and its
source. The new workspace can be accessed through a login specifying its
name.

void Workspace.deleteWorkspace(String name)

Deletes the workspace with the specified name from the repository,
deleting all content within it.
