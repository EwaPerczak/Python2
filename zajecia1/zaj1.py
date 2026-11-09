# #zad1

# print(int(6-2))
# print(type(6 - 2).__name__)
# print(int(6*2))
# print(type(6 * 2).__name__)
# print(int(6/2))
# print(type(6 / 2).__name__)

# print(int(6)-float(2))
# print(type(int(6)-float(2)).__name__)
# print(int(6)+float(2)) 
# print(type(int(6)+float(2)).__name__)
# print(int(6)*float(2))
# print(type(int(6)*float(2)).__name__)
# print(int(6)/float(2))
# print(type(int(6)/float(2)).__name__)


# #zad2

# print("6" + "2")
# print("6" * 3)
# #print("6" + 2) blad bo 1 to string a 1 to int i to jakby dodawac tekst do liczb
# print(6 + 2)
# print(6 - 2)

# #zad3

# #moje liczby 4 i 5.3
# calk = 4
# wym = 5.3
# print(calk == wym)
# print(int(calk) == float(wym))
# print(calk < wym)

 #zad4

# liczba = int(input())
# print("Start")
# if liczba > 0:
#     print("Liczba dodatnia")
#     print("Koniec")

# liczba = int(input())
# print("Start")
# if liczba > 0:
#     print("Liczba dodatnia")
# print("Koniec")

#zad5

# calk = -4
# calk = -3
# calk = 3
# if calk > 0:
#     print("dodatnia")
# if calk%2 == 0:
#     print("parzysta")

lb1 = float(1)
opr = str("/")
lb2 = float(5.3)

if opr == "+":
    print(lb1 + lb2)

if opr == "-":
    print(lb1 - lb2)    

if opr == "*":
    print(lb1 * lb2)

if opr == "/":
     if lb2 == 0:
         print("nie dziel przez 0")
     else:
         print(lb1 / lb2)    