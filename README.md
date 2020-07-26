# session3-Anil Bhatt
session3-Anil Bhatt created by GitHub Classroom

# Variables and Memory References
  Usually stored in RAM and this can be integer,float16/32 memory
	Memory address are stored in hex format. (any format can be stored)
	when you declare a varibale with int and try to change on fly throwerror
	when we store a value into a varibale we store the value to memory location
	and we assigning this memory location to the variable
	whole python works on references
# Reference Counting
  when we declare a variable "var1" it stored in a memory location and
	variable get the memory location. when we assign create varible "var1"
	to new varibale "var2" i.e. var1=var2 then these two variables uses same
	memory and a references count get increases.
  
# Garbage Collection
  As we create objects in memory, Python keeps track of the number of references we have on that object. As soon as the reference count hits 0, Python Memory Manager then reclaims, destroys that object, and reclaims that memory. But sometimes that doesn't work as expected. And in particular, we have to look at a situation called Circular References

# Dynamic vs Static Typing
 Some programming languages are statically types which means that for a example
	a variable declared as string cant be assinged int value to it.
	Python is dynamically typed, which mean that when you declare a varibale "var"
	as string i.e var="Happiness" which can be reused and stored int/float values.
	i.e var=20. Now String address references point to integer address. Only references changes.
	
# Variable Re-Assignment
  As said above in the references section, we can declare a variable of same type and do some operation such as
	addition,concatenation etc. and store the result back to same varible. It changes references pointing to.
	Python evaluates from right side first.
# Object Mutability
 An object whose internal state can be changes is `mutable`.	
 An object whose internal state cannot be changes is `Immutable`.
 
 Immutable are: 
	1. Numbers
	2. Strings
	3 Tuples
	4 Frozen Sets
	5 User-Defined Classes
	
 Mutable are:
	1. Lists
	2. Sets
	3. Dictinaries
	4. User-Defined Classes
	
	
	
# Function Arguments & Mutability

# Shared References & Mutability
 * The term shared reference is the concept of two variables referencing the same object in the memory (i.e. having the same memory address)
 	* a = 10, then when we write b = a, what we are actually saying is, set the memory reference of b equal to the memory reference of a. 
 	* It is not copying "values", it is copying memory references. 
 * Same thing with a function too. When you pass an argument to a function, what you are actually passing is the memory reference. 
 * Shared references happen all the time in our code, and we need to be careful with whether the reference address belongs to a mutable or immutable object. 
 * In some cases, even if you declare two separate variables separately, Python's memory manager might decide to automatically re-use the memory references! e.g.:
 	* a = 10 and b = 10; a and b will have same memory addresses
 	* s1 = "hello" and s2 = "hello"; s1 and s2 will have same memory addresses
 * How is that last thing safe?
 	* Well YES, that happens only for immutable objects, so you can't change what's stored on those addresses anyways. Python is doing this for optimizations (we'll cover this when we cover python optimizations). 
 * With Mutable objects, Python Memory Manager will never create shared references. 
 	* a = [1, 2, 3] and b = [1, 2, 3] will be stored at different memory addresses. 


# Variable Equality

# Everything is an Object

# Python Optimizations: Interning

# Python Optimizations: String Interning

# Python Optimizations: Peephole


int
encoded_from_base10
digit_map
ValueError
math
isclose
absolute
relative
tolerance
bin(
hex(
round
truncation
error
equality
zero
away'
