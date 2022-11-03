fibonacci = [1]  # adds the first “1” manually.

liste = list(range(1, 2))

while True  :
    i = liste[len(liste)-2] + liste[len(liste)-1]
    liste.append(i)
        
    if liste[len(liste) - 1] == 55 :
        break

fibonacci = fibonacci + liste
print(f"fibonacci -> ", fibonacci)

Output:
fibonacci ->  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
