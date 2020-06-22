#Tuples are similar to lists, but you can't change them after you create them
#Instead of square brackets, we use parenthesis for tuples
fibonacci_seq = (0,1,1,2,3,5,8,13,21)
print(fibonacci_seq)

#You can get items in your tuple just like you can for lists
#Note that although you use parenthesis to create the tuple, you use square brackets to refer to an item in the tuple, the same as for lists
print("The 4th number in the Fibonacci sequence is %s" % fibonacci_seq[3])

#But you cannot edit the tupple
#The following line will give you an error if you try to run it 
#fibonacci_seq[1] = 8

#Just like with lists, you can get the number of items in the tuple by using the len command
print("Our tuple contains %s items" %len(fibonacci_seq))