from linked_list_seq import Linked_List_Node, Linked_List_Seq

iterables = (1, 2, 3, 4, 5,)

llist = Linked_List_Seq()
llist.build(iterables)

# Build Link List
print("iterate through the linked list sequence built from iterables (1, 2, 3, 4, 5,)")
for item in llist:
    print(item)

print("get item at index 2 that has a value 3")
print(llist.get_at(2)) # 3

print("set item at index 1 as 15")
llist.set_at(1, 15)
print(llist.get_at(1))




