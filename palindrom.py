def Czy_palindrom(x):
    n=len(x)
    for i in range(n-1):
        if x[i] != x[n-1-i]:
            return False
    return True
print("Program do spradszania czy słowo jest palondromem")
print("Podaj słowo: ")
s1 = input()
print("Podane słowo " + ("jest" if(Czy_palindrom(s1)) else "nie jest") + " palindromem")