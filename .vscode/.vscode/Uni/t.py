# m, n = list(map(int, input().split()))
# matrix = []
# for i in range(m):
#     a = list(map(int, input().split()))
#     matrix.append(a)
# print()

# for j in range(m):
#     for k in range(n):
#         print(matrix[j][k], end=" ")
#     print()
# print()
class person:
    def __init__(a, name, age):
        a.name = name
        a.age = age
    def __str__(a):
        return f"{a.name} is {a.age} years old"
        print("hello my name is "+ a.name+" and i am "+str(a.age)+"years old")
        
p1 = person("Anvi", 21)
p2 = person("Daksh shop", 684)
print(p1)