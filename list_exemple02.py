for idx in range(5):
    print("index is equal to ", idx)


liste = [12, 13, 42, 76, 89]


s = liste[0]
print(s)  # 12

s = liste[1]
print(s)  # 13


s = liste[2]
print(s)  # 42

s = liste[3]
print(s)  # 76

s = liste[4]
print(s)  # 89

print("---------------------------\n")


print(range(5))
# print(list(range(5)))
print(liste)



# =============================================
#  Exemple: for idx in range(N)
# =============================================

print("---------------------------\n")
print("Exemple for idx in range(N): \n")


liste = [12, 13, 42, 76, 89]

for idx in range(5):
    print(idx)

print("---\n")

for idx in range(5):
    s = liste[idx]
    print(s)

print("---\n")

s = 0
for idx in range(5):
    s += liste[idx]
    print(s)


# =============================================
#  Exemple: for idx in range(N)
# =============================================

print("---------------------------\n")
print("Exemple for x in liste: \n")


liste = [12, 13, 42, 76, 89]
s = 0
for elem in liste:
    s += elem
    print(s)
