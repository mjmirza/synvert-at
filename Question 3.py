#QUESTION 3
#Given a string A and a list of shorter strings B, and the longest string in B that can be created by removing characters from string A (without rearranging characters).
#Example Input:
#A = "peanut butter jelly is the best!"
#B = ["bus","pets","bully","jester"]
#Output:
#"bully"

A = "peanut butter jelly is the best!"
B = ["bus","pets","bully","jester"]

def longest_string(A, B):
    longString = ""
    for b in B:
        i = 0
        j = 0
        while i < len(A) and j < len(b):
            if A[i] == b[j]:
                j += 1
            i += 1
        if j == len(b):
            if len(b) > len(longString):
                longString = b
    return longString


print(longest_string(A,B))

#this is a confusing question i must admit when it comes to  nonchanging orders