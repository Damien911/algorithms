
lista = []
i = 1

for x in range(10000):
    lista.append(i)
    i = i + 1

typ = int(input("Podaj liczbę 1- 10.000 do znalezienia: "))



def binary_search(list, item):
    low = 0
    high = len(list)-1
    i = 0
    while low <= high:
        mid = round((low + high)/2)
        guess = list[mid]
        i = i + 1
        if guess == item:
            return mid, i
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

start = binary_search(lista, typ)
print(start)
fstring = f"Poszukiwana liczba znajduje się na pozycji {start[0]}, znaleziono po wykonaniu {start[1]} operacji."
print(fstring)







    
