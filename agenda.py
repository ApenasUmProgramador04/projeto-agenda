def menu():
    while True:
        opção = input('{} agenda {}{}{}1) Cadastrar contato{}2) Listar contatos{}3) Buscar contato{}4) Sair{}{}{}{}Escolha uma opção: '.format('='*5,'='*5,'\n','\n','\n','\n','\n','\n','\n','='*20,'\n'))
        if opção == '1':
            cadastrar_contato()
        elif opção == '2':
            listar_contatos() 
        elif opção == '3':
            buscar_contato() 
        elif opção == '4':
            print('fechando a agenda !')
            exit()

        else:
            print('Opção inválida. Tente novamente.')
def cadastrar_contato():
    while True:
        opção = input('\ndeseja cadastrar um novo contato ? ')
        if opção in ['sim','s']:        
            nome = input('\ndigite o nome do contato: ')
            telefone = input('digite o telefone do contato: ')
            try:
                agenda = open('C:\\Users\\User\\Documents\\Coisa do Bruno\\python\\meus_projetos\\projeto_agenda\\agenda.txt','a')
                dado = f'{nome};{telefone}\n'
                agenda.write(dado)
                agenda.close()
                print('contato gravado com sucesso !!')
            except:
                print('erro na gravacão de contato !!!')
        elif opção in ['não','nao','n']:
            menu()
        else:
            print('opção invalida tente novamente !!')

def listar_contatos():
    print('{}Sua lista de contatos{}{}'.format('='*10,'='*10,'\n'))
    agenda = open('C:\\Users\\User\\Documents\\Coisa do Bruno\\python\\meus_projetos\\projeto_agenda\\agenda.txt','r')
    for contatos in agenda:
        print(contatos)
    agenda.close()
    print('='*15,'fim da lista','='*15)
    opção = input('deseja deletar algum contato ?')
    if opção.lower() in ['sim','s']:
        deletar_contato()
    else:
        menu()

def buscar_contato(): 
        nome = input('digite o nome do contato: ')
        agenda = open('C:\\Users\\User\\Documents\\Coisa do Bruno\\python\\meus_projetos\\projeto_agenda\\agenda.txt','r')
        for contato in agenda:
            if nome.lower() in contato.lower():
                print('='*10, '\n', contato, '\n', '='*10)
        agenda.close()

def deletar_contato():
    nomeDeletado =input('digite o nome do contato que deseja deletar: ')
    agenda = open('C:\\Users\\User\\Documents\\Coisa do Bruno\\python\\meus_projetos\\projeto_agenda\\agenda.txt','r')
    aux1 = []
    aux2 = []
    for i in agenda:
        aux1.append(i)
    for i in range(len(aux1)):
        if str(nomeDeletado).lower() not in str(aux1[i]).lower():
            aux2.append(aux1[i])
        agenda = open('C:\\Users\\User\\Documents\\Coisa do Bruno\\python\\meus_projetos\\projeto_agenda\\agenda.txt','w')
        for i in aux2:
            agenda.write(i)
        agenda.close()
    print('\ncontato deletado com sucesso !!\n')
    listar_contatos()
    


def main():
    menu()

    
main()