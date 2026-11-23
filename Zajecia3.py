# zad1 for i while

# MX = int(input())
# print("zaczynam liczyc")
# for LB in range(1, MX):
#     print(LB)

# LB = 1
# n = int(input())
# print("zaczynam liczyc")
# while LB < n:
#     print(LB)
#     LB = LB + 1

#zad2

# n = int(input())
# LB = n
# print("zaczynam liczyc")
# while LB >= 0:
#     print(LB)
#     LB = LB - 1
# print("Start!")    

# zad3
# LB = 2
# n = int(input())
# if n >= LB:
#     if n % 2 == 1:
#         while LB < n:
#             print(LB)
#             LB = LB + 2
#     else:
#         while LB <= n:
#             print(LB)
#             LB = LB + 2        

#zad4
# n = int(input())
# for LB in range(1, n+1):
#     print(LB*"#")

#nie udane
# n = int(input())
# print("--------------")
# for LB in range(1, n+1):
#     for LB in range(1, n):
#         print((n-1)*"#", end="")
#         print("#")

# zad5
# n = int(input())
# suma = 0
# for lb in range(1,n+1):
#     suma = suma + lb
# print(suma)

#zad6
# n = int(input())
# suma = 0
# lw = 0
# while n != 0:
#     suma = suma + n
#     lw = lw + 1
#     n = int(input())
# print(f"Suma: {suma}")
# print(f"Liczba wartości: {lw}")


#zad7
LS = int(input("Wprowadź liczbę studentów: "))
print(f"Liczba studentów: {LS}")
suma = 0
n=1
for n in (1, LS):
    WK = int(input("Wprowadź wynik studenta: "))
    if WK in range (0, 101):
        WK = int(input("Wprowadź wynik studenta: "))
        suma = suma + WK
        n = n+1
        
    else: print("Niepoprawny wynik")

print(f"Suma: {suma}")


# LS = int(input("Wprowadź liczbę studentów: "))
# print(f"Liczba studentów: {LS}")
# suma = 0
# WK = int(input("Wprowadź wynik studenta: "))
# while WK in range (0, 101):
#     for n in range (1, LS+1):

