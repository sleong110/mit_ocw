# Recitation 2

## Sequence Interface

1.) Maintains a collection of items in an extrinsic order
2.) Each item stored has a rank in the sequence
3.) Extrinsic means the first item is 'first', not because of what the item is, but because some external party put it there.
4.) Sequences are generalization of stacks and queues, which support subset of sequence operations.

Container   | build(X)          | give an iterable X, build sequence from items in X
            | len()             | return the number of stored items
------------------------------------------------------------------------------------
Static      | iter_seq()        | return the stored items one-by-one in sequence order
            | get_at(i)         | return the ith item
            | set_at(i, x)      | replace the ith item with x
-------------------------------------------------------------------------------------
Dynamic     | insert_at(i, x)   | add x as the ith item
            | delete_at(i)      | remove and return the ith item
            | insert_first(x)   | add x as the first item
            | delete_first()    | remove andreturn the first item
            | insert_last(x)    | add x as the last item
            | delete_last()     | remove and return the last item
            