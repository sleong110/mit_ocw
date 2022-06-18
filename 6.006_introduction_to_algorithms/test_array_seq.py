from array_seq import Array_Seq

seq = Array_Seq()

iterables = 'ABCDEFGHIJK'
print('iterables length:' + str(len(iterables)))
seq.build(iterables)

print(seq.A)
print(seq.size)

for item in seq.A:
    print(item)

# Get 4th item
print(seq.get_at(3))
print(seq.set_at(3, 'N'))
print(seq.get_at(3))

print(seq.A)

print(seq.insert_at(4, 'P'))
print(seq.A)
print(seq.size)

print(seq.delete_at(5))
print(seq.A)
print(seq.size)

print(seq.insert_first('Z'))
print(seq.insert_last('P'))

print(seq.A)
print(seq.delete_first())
print(seq.delete_last())
print(seq.A)