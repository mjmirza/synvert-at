#QUESTION 1
#Given 2 strings, find the starting position of string 1 inside string 2. Please implement the
#logic by yourself without using built-in functions or methods.


string1 = "dummy"
string2 = "my test you an find insides this dummy example"

count = 0
for i in range(len(string2)):
    if string2[i] == string1[0]:
        for j in range(len(string1)):
            if string2[i+j] == string1[j]:
                count += 1
            else:
                count = 0
                break
        if count == len(string1):
            print(i)
            break
    else:
        continue
    
print("Not found") if count == 0 else None

#btw find string in string is a built-in function that can be use from python default library

#reference url : https://stackoverflow.com/questions/33217326/finding-a-substring-of-a-string-in-python-without-inbuilt-functions