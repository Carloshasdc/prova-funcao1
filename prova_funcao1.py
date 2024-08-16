# Crie uma função chamada media que receberá três números como argumentos. 
# Esta função deve calcular a média aritmética desses três números. 
# Para fazer isso, some os três números e, em seguida, divida o resultado por três. Por fim, 
# a função deve retornar o valor da média aritmética calculada.

def  media(a,b,c):
     soma = a+b+c
     med = soma/3
     return med
 
 
a= int(input('Digite o primeiro numero:'))
b= int(input('Digite o segundo numero:'))
c= int(input('Digite o terceiro numero:'))


print(f'a media aritimetica é: {media(a,b,c)}')