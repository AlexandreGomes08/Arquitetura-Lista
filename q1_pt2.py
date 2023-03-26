print("Distância de Hamming ")
n1= input(str("Digite o 1° número: "))
n2= input(str("Digite o 2° número: "))

if len(n1)!=len(n2):
    print("A quantidade de dígitos deve ser a mesma!")
    exit()

for i in list(n1):
    if i!= '1' and i!= '0':
        print("Valor inválido, a entrada deve ser números binários!")
        exit()
for i in list(n2):
    if i!= '1' and i!= '0':
        print("Valor inválido, a entrada deve ser números binários!")
        exit()
d=0    #distancia
l1=(list(n1))
l2=(list(n2))
c=0    #contador
while c<len(n1):
    if l1[c]!=l2[c]:
        d+=1
    c+=1
print("A distância de Hamming é: {}".format(d))