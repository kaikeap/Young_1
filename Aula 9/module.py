import calculadora

def menu() :
    while True:
        print('*******************')
        print('        menu       ')
        print('*******************')
        print('*[1] - somar      *')
        print('*[2] - subtrair   *')
        print('*[3] - multiplicar*')
        print('*[4] - dividir    *')
        print('*[5] - sair       *')
        print('*******************')
        opt = int(input('Opção desejada \n'))
        num1 = int(input('Digite nº 1 \n'))
        num2 = int(input('Digite nº 2 \n'))
        if opt == 1:
            print(calculadora.somar(num1 , num2))
            pause =  input('')
        elif opt == 2:
            print(calculadora.subtrair(num1 , num2))
            pause =  input('')
        elif opt == 3:
            print(calculadora.mutiplicar(num1 , num2))
            pause =  input('')
        elif opt == 4:
            print(calculadora.divisão(num1 , num2))
            pause =  input('')
        elif opt == 5:
            break
        else:
            menu()

menu()