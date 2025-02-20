password = input('digite sua senha\n')

test_password = input('digite sua senha\n')

while password != test_password:
    test_password = input('digite sua senha\n')
else:
    print('acesso liberado')