n=str(input("Digite o número que deseja adicionar os bits de paridade: "))

for i in list(n):
    if i!='1' and i!='0':
        print("Valor inválido! O número digitado deve ser binário")
        exit()

l1= (list(n)) 
nletters=len(l1) #ler a quantidade de dígitos

if nletters >57:
    print("Limite de dígitos atingido")
    exit()
elif nletters<2:
    bp=2
elif nletters<5:
    bp=3
elif nletters<12:
    bp=4
elif nletters<27:
    bp=5
elif nletters<58:
    bp=6

l1.insert(0,'0')
c=1
while c<bp:
    l1.insert((2**c)-1,'0')
    c+=1

#processando os bits de cada vez
#bit 1
ax,soma,varredura = 0,0,0
while(varredura<len(l1)):
    while(ax<1 and varredura<len(l1)):
        soma+=int(l1[varredura])
        ax+=1
        if ax<1:
            varredura+=1
    varredura+=2
    ax=0
if soma%2==0:
    l1[0]='0'
else:
    l1[0]='1'

#bit 2 
ax,soma,varredura = 0,0,1
while(varredura<len(l1)):
    while(ax<2 and varredura<len(l1)):
        soma+=int(l1[varredura])
        ax+=1
        if ax<2:
            varredura+=1
    varredura+=3
    ax=0
if soma%2==0:
    l1[1]='0'
else:
    l1[1]='1'

#bit 4
if bp>2:
    ax,soma,varredura = 0,0,3
    while(varredura<len(l1)):
        while(ax<4 and varredura<len(l1)):
            soma+=int(l1[varredura])
            ax+=1
            if ax<4:
                varredura+=1
        varredura+=5
        ax=0
    if soma%2==0:
        l1[3]='0'
    else:
        l1[3]='1'

#bit 8
if bp>3:
    ax,soma,varredura = 0,0,7
    while(varredura<len(l1)):
        while(ax<8 and varredura<len(l1)):
            soma+=int(l1[varredura])
            ax+=1
            if ax<8:
                varredura+=1
        varredura+=9
        ax=0
    if soma%2==0:
        l1[7]='0'
    else:
        l1[7]='1'

#bit 16
if bp>4:
    ax,soma,varredura = 0,0,15
    while(varredura<len(l1)):
        while(ax<16 and varredura<len(l1)):
            soma+=int(l1[varredura])
            ax+=1
            if ax<16:
                varredura+=1
        varredura+=17
        ax=0
    if soma%2==0:
        l1[15]='0'
    else:
        l1[15]='1'

#bit 32
elif bp>5:
    ax,soma,varredura = 0,0,31
    while(varredura<len(l1)):
        while(ax<32 and varredura<len(l1)):
            soma+=int(l1[varredura])
            ax+=1
            if ax<32:
                varredura+=1
        varredura+=33
        ax=0
    if soma%2==0:
        l1[31]='0'
    else:
        l1[31]='1'

nstring="".join(l1)

print("Número processado com os bits de Paridade: {}".format(nstring))