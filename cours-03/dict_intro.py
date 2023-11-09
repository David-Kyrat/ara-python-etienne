
a={"lu":"lundi","me":"mercredi","ma":"mardi"}
print(a)
print(a["lu"])
print("ve" in a)
print("ma" in a)


# A l'aide d'une boucle for et d'une liste, print toutes les valeurs de a.
# Hint: mets les clés de a dans une liste et fait une boucle for avec liste
# 
print("=================================")

b=["lu","ma","me"]
for elem in b:
    print(a[elem])

print("=================================")

f = range
g = len

# composition des fonctions f puis g en b => ? 
# ! => f(g(x))

for i in f(g(b)):
    print(i) 


for i in range(len(b)):
    clef= b[i]
    print(clef)
    print(a[clef])
