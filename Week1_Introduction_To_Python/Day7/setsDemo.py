# Sets are
#    1) Unordered - Hence can't iterate/slice using index
#    2) Unique
#    3) Mutable (can add/remove)
#    4) Defined with curly braces {}\
#    5) Also support set specific operations like union, intersection and difference
sample = {1,2,3,4,5,6}
print("#"*100,
   "\tSet - Adding Elements",
   "#"*100,'', sep='\n')
print(f"Type of set - sample: {type(sample)}")
print("sample (before adding):", sample)
sample.add(6)
print("sample (after adding '6'):", sample)
print(sample.add(6))#   No impact, for first time adding or repeated addition, returns None
print("sample (retrying adding '6'):", sample)


print("\n","#"*100,
   "\tSet - Updating Elements",
   "#"*100,'', sep='\n')
print("Sets can be added from a data structure like list, tuple etc. using .update(<ds>)")
print("Before update sample:",sample)
sample.update([100,200,300])
print("After update with [100,200,300], sample:",sample)


print("\n","#"*100,
   "\tSet - Removing Elements",
   "#"*100,'', sep='\n')
print("Element(s) can be removed in 3 ways as below:",
      "\t1) .remove(<element>) - Removes specified element. Raises KeyError if element is not present",
      "\t2) .discard(<element>) - Removes provided element. Doesn't raise any error if element not present",
      "\t3) .pop() - Removes and returns any element in random. Raises KeyError if set is already empty", sep='\n')
print("Removing 6 from sample:", sample.remove(6))
print("After removing 6 from sample:", sample)
print("Popping any element from sample:", sample.pop())
print("After popping from sample:", sample)

print("\n","#"*100,
   "\tSet - Iterating",
   "#"*100,'', sep='\n')
for i in sample:
    print(i, end=' ')
print()
print("\n","#"*100,
   "\tSet - Union, Intersection, Difference and Symmetric Difference",
   "#"*100,'', sep='\n')
print("Set union can be performed by '|' operator which provides uniques elements of both sets")
set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}
print("set1:", set1)
print("set2:", set2)
print("Union of set1 and set2 = set1 | set2:",set1 | set2)
print("\nSet Intersection can be performed by '&' operator which provides uniques elements of both sets")
print("Intersection of set1 and set2 = set1 & set2:",set1 & set2)
print("\nSet Difference can be performed by '-' operator which provides a new set with elements in the first set but not in the second")
print("Case1 -> set1 - set2:", set1 - set2)
print("Case2 -> set2 - set1:", set2 - set1)
print("\n Set symmetric-difference can be performed by '^' which provides a new set with elements in either set, but not in the both")
print("set1 ^ set2:", set1 ^ set2)


print("\n","#"*100,
   "\tSet - Length of a set",
   "#"*100,'', sep='\n')
print("Length of a given set can be calculated using len(<set_var>) function")
print("sample:",sample)
print("Number of elements in sample is = len(sample):", len(sample))

print("\n","#"*100,
   "\tSet - (Shallow) Copying elements",
   "#"*100,'', sep='\n')
print("Shallow copy of elements can be performed by <set_var>.copy()")
copy_sample = sample.copy()
print("copy_sample:", copy_sample)

print("\n","#"*100,
   "\tSet - Clearing elements",
   "#"*100,'', sep='\n')
print("All elements in a set can be cleared by <set_var>.clear() function")
copy_sample.clear()
print("copy_sample:", copy_sample)
print("sample:", sample)
