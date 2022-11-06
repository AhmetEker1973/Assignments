<<<<<<< HEAD
fibonacci = [1]  # adds the first “1” manually.

liste = list(range(1, 2))

while True  :
    i = liste[len(liste)-2] + liste[len(liste)-1]
    liste.append(i)
        
    if liste[len(liste) - 1] == 55 :
        break

fibonacci = fibonacci + liste
print(f"fibonacci -> ", fibonacci)

=======
fibonacci = [1]  # adds the first â€œ1â€ manually.

liste = list(range(1, 2))

while True  :
    i = liste[len(liste)-2] + liste[len(liste)-1]
    liste.append(i)
        
    if liste[len(liste) - 1] == 55 :
        break

fibonacci = fibonacci + liste
print(f"fibonacci -> ", fibonacci)

Output:
>>>>>>> 2af2fc321fb480b7b77fb02091e16fdfdf7bd654
fibonacci ->  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
