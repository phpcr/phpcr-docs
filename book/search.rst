Search
======

TODO: intelligent filtering criteria to do as little in-memory operations to apply criteria.

If you do not need the node objects but just some value, query for that value and use the result Row to avoid instantiating Node objects alltogether. If you need the Node objects, help PHPCR to optimize by using QueryResult::getNodes and iterating over the nodes instead of getting the rows, iterating over them and calling getNode on each row. (Actually, if you first do the getNodes(), you can then iterate over the rows and get the individual nodes and still use the special row methods as the implementation should have prefetched data on the getNodes.)

