print("|CIRCUITOS LÓGICOS|")
n=int(input("Digite o circuito que você deseja simular[1/2]: "))
print("\nDigite os seguintes valores: ")
a=int(input("valor de a: "))
b=int(input("valor de b: "))
c=int(input("valor de c: "))
d=int(input("valor de d: "))

if a!=1 and a!=0:
    print("Valor inválido!São permitidos apenas valores 1 e 0")
    exit()
if b!=1 and b!=0:
    print("Valor inválido!São permitidos apenas valores 1 e 0")
    exit()
if c!=1 and c!=0:
    print("Valor inválido!São permitidos apenas valores 1 e 0")
    exit()
if d!=1 and d!=0:
    print("Valor inválido!São permitidos apenas valores 1 e 0")
    exit()

if a==1:
    na=0
else:
    na=1
if b==1:
    nb=0
else:
    nb=1
if c==1:
    nc=0
else:
    nc=1
if d==1:
    nd=0
else:
    nd=1

#funções para as portas lógicas
def AND (a,b):
    if a == 1 and b == 1: 
        return 1
    else: 
        return 0
def NAND (a,b):
    if a == 0 or b == 0: 
        return 1
    else: 
        return 0
def OR (a,b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0
def NOR (a,b):
    if a == 0 and b == 0:
        return 1
    else:
        return 0

#circuito 1
if n==1:
    p1=NAND(na,b)
    p2=NAND(a,nb)
    p3=OR(c,d)
    p4=NOR(NOR(p1,p2),nc)
    p5=AND(p4,p3)
    saida=p5
    print("Valor de Saída do circuito: {}".format(saida))

#circuito 2
if n==2:
    p1=AND(b,nd)
    p2=AND(nb,d)
    p3=AND(c,d)
    p4=OR(na,c)
    p5=NAND(b,d)
    p6=NOR(p1,a)
    p7=OR(p2,p3)
    p8=AND(p4,p5)
    p9=NAND(p6,p7)
    p10=NOR(c,p8)
    p11=AND(p9,p10)
    saida=p11
    print("Valor da Saída do circuito: {}".format(saida))
