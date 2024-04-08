#A = int(input("А5 ны енгіз "))
#B = int(input("Б ны енгіз "))
# 
#i = 1
#for num in range(A, B + 1):
#    i *= num

#print(i)


def find_product(A, B):
    num = 1
    for i in range(A, B + 1):
        num *= i
    return num

A = int(input("А га ман берыныз "))
B = int(input("Б ға мән беріңіз(B А дан үлкен болу керек ): "))

if B <= A:
    print("Қате. B А дан үлкен болу керек")
else:
    C = find_product(A, B)
    print(C)