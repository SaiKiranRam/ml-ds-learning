# Tuples have following:
#     1) Immutable <-> can't modify after creation
#     2) Ordered - Insertion order is preserved
#     3) Dynamic
#     4) Index is available
#     5) Duplicates are allowed
#     6) Can be initialized by comma separated elements within '()'
print("#"*100,
   "\tTuples - Initializing",
   "#"*100,'', sep='\n')
print("Tuples can be initialized by comma separated elements within '()'")
sample_tuple = (1,2,3,4.0,5,1)
print("sample_tuple:", sample_tuple)

print("\n","#"*100,
   "\tTuples - Accessing Elements",
   "#"*100,'', sep='\n')
print("Elements can be accessed similar to list with index. For example, sample_tuple[2]:", sample_tuple[2])
print("\n","#"*100,
   "\tTuples - Slicing",
   "#"*100,'', sep='\n')
print("Similar to list, slicing can be done on Tuples with index/indices. For example, sample_tuple[0:2]:", sample_tuple[0:2])

print("\n","#"*100,
   "\tTuples - Concatenation",
   "#"*100,'', sep='\n')
sample_tuple2 = (True, False, 'abc')
print("sample_tuple:", sample_tuple)
print("sample_tuple2:", sample_tuple2)
print(f"Similar to list, concatenation can be done on Tuples by sample_tuple + sample_tuple2: {sample_tuple + sample_tuple2}")

print("\n","#"*100,
   "\tTuples - Multiplying/Repetition",
   "#"*100,'', sep='\n')
print("\nSimilar to list, concatenation can be done on Tuples by '*' followed by a number.",
      f"\nExample, sample_tuple2 * 3:", sample_tuple2 * 3)

print("\n","#"*100,
   "\tTuples - Iteration",
   "#"*100,'', sep='\n')
for var in sample_tuple2:
    print("var:", var, sep=' ')

print()
print("\n","#"*100,
   "\tTuple - Checking for an element",
   "#"*100,'', sep='\n')
print("sample_tuple:", sample_tuple)
print("4.00 in sample_tuple:", 4.00 in sample_tuple)
print("1000 in sample_tuple:", 1000 in sample_tuple)


print("\n","#"*100,
   "\tTuple - Counting occurrences of an element",
   "#"*100,'', sep='\n')
print(sample_tuple)
print("Occurrence of an element can be performed by <tuple_var>.count(<element>) function",
      "\nExample, sample_tuple.count(1):", sample_tuple.count(1))


print("\n","#"*100,
   "\tTuple - Finding index of an element",
   "#"*100,'', sep='\n')
print("sample_tuple:", sample_tuple)
print("Index of an element can be found by <tuple>.index(<element>)",
      "If present, provides the first occurrence of the element",
      "If absent, throws ValueError",
      "Example, sample_tuple.index(1):", sample_tuple.index(1), sep='\n')