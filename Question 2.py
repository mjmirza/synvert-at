#Given 2 lists, create a new list by taking alternate items from the lists.
#Example Input:
#A = [1,2,3,4,5]
#B = [6,7,8,9,10,11,12]
#Output:
#[1,6,2,7,3,8,4,9,5,10,11,12]

A = [1,2,3,4,5]
B = [6,7,8,9,10,11,12]
C = []


for i in range(len(A)):
    C = C + [A[i], B[i]]

print(C)

#easily and alternatively we could also use append function here aswell to append the values in the list C, but it will use append default function and i wanted to avoid that