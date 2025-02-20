##ex 10

user = input('digite seu nome: ')

password = input('digite sua senha: ')

while True:

    test_user = input('digite seu nome: ')

    test_password = input('digite sua senha: ')

    if test_user == user and test_password == password:
        print('acesso pertido')
        break
    else:
        print('acesso negado')