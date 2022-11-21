def count(s1, s2):
    last = s2[len(s2)-1]
    res = 0
    for i in s1:
        if i == last:
            res +=1
    return res
s1= input("enter first string")
s2= input("enter second string")
print(count(s1,s2))