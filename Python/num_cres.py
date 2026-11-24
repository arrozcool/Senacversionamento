i = 1
soma = 0
numS = 0
print ("faça uma ordem crescente, se não for o progama irá somar todos os valores postos e parara de funcionar")
while i > 0:
    num = int(input("diga um numero: "))
    
    if num > 0:
        if numS < num:
            numS = num
            soma = soma+num
        else:
            print ("o número informado não é crescente")

    R = int(input(f"Você quer para agr \n 1 = sim \n 2 = Não \n"))

    if R == 1:
        print (soma, "o progama está parando")
        break




        
            
            
        





