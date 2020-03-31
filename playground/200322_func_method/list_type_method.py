L= [1, 2, 3]
L_2= [4, 5, 6]
print("List_1 :", L)
print("List_2 :", L_2)

print("List_1 * 3 :", L*3)
print("List_1 + List_2 :", L+L_2)
print("list comprehension: ", [i for i in range(1, 7)])

L.append(4)
print("List_1 append(4):", L)
L.insert(4, 5)
print("List insert(index: 4, element: 5) :", L)
L.extend([6, 7, 8])
print("List extend([6, 7, 8]):", L)
L_3= L.copy()
print("List copy and save to List_3 :", L_3)
L.remove(8)
print("List remove(8) :", L)
L.pop(6)
print("List pop(index: 6) ", L)

