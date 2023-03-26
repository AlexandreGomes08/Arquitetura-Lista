b,d,bo,e,g = 1,0,-1,-2,-3

print("Execução de um pipeling de 5 estágios.")
n=int(input("Digite o número de instruções:"))

print("Processando...")
print("========================")
while g != n+1:
    if b<=n and b>0:
        print("Buscando l{}".format(b))
    b+=1
    if d<=n and d>0:
        print("Decodificando l{}".format(d))
    d+=1
    if bo<=n and bo>0:
        print("Buscando Operandos l{}".format(bo))
    bo+=1
    if e<=n and e>0:
        print("Executando l{}".format(e))
    e+=1
    if g<=n and g>0:
        print("Gravando l{}".format(g))
    g+=1
    print("========================")