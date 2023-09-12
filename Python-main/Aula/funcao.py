def mensagem1():
    print("olá!")
    
def mensagem2(nome, idade):
    print(f'Ola! {nome}, você tem {idade} anos')
    
def mensagem3():
    return "ola", 2

'''
def main():
    i=1
    while i <= 3:
        entradaNome=input('digite seu nome: ')
        entradaIdade=int(input('digite a sua idade: '))
        mensagem2(entradaNome,entradaIdade)
        i+=1
'''

def mensagem4(nome):
    return 'Olá, ' + nome + '!'

def main():
    m = mensagem4('Pedro')
    print(m)
    print(mensagem4('Eduardo'))
    
main()