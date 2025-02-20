# Aula 2
## comandos importantes

-PRINT = serve para mostrar algo, ou uma informação.

-INPUT = é basicamente uma entrada de informação, caso coloque no codigo ele vai aguardar uma informação para receber.

-OUTPUT = é o contrario de de INPUT ele manda informação.

-VARIAVEL = é um local onde guarda uma informação que você determinou.

# O que é uma condicionais
-é o "if else"
-condicionais é uma estrutura de de programação uqe se uma condição for verdadeira  eu faço uma determinada ação, do contrário se for falso faço outra. 

ex: 
```python
a = 4
b = 2

if a == b:
    print('oi')
else:
    print('tchau')
```
## Condicionais composto
-Estrutura com multiplas condições
 
 ### Condicionais composto
Estrutura com multiplas condições

ex: 
```python
a = 4
b = 2

if a > b:
    print('oi')
elif a < b:
    print('tchau')
else:
    print('saude')
```
# Aula 3
-while: significa enquanto

-\n: pode ser usado para pular uma linha

# Aula 4

## comandos de repetiçao python

-while true: o contrario do 'while' o 'while true' repete o codigo ate que seja verdadeiro enquanto for falso ele continua.

-for


## EXERCICIOS

# Lista de Exercícios de Python sobre Condicionais

## 1. Par ou Ímpar
**Enunciado**:  
- Peça ao usuário que digite um número inteiro.  
- Verifique se o número é par ou ímpar.  
- Mostre uma mensagem indicando o resultado.

---

## 2. Positivo, Negativo ou Zero
**Enunciado**:  
- Receba um número inteiro do usuário.  
- Verifique se esse número é positivo, negativo ou zero.  
- Exiba a mensagem correspondente.

---

## 3. Comparação de Dois Números
**Enunciado**:  
- Peça para o usuário inserir dois números.  
- Compare os números e mostre qual deles é maior, ou se são iguais.

---

## 4. Nota Aprovado/Reprovado
**Enunciado**:  
- Peça ao usuário que digite uma nota (0 a 10).  
- Se a nota for maior ou igual a 6, exiba "Aprovado". Caso contrário, exiba "Reprovado".  
- Caso a nota esteja fora do intervalo [0, 10], mostre uma mensagem de erro.

---

## 5. Dia da Semana
**Enunciado**:  
- Solicite um número de 1 a 7.  
- Cada número representa um dia da semana (1 = segunda-feira, 2 = terça-feira, etc.).  
- Exiba o nome do dia correspondente ou mostre "Dia inválido" se o número não estiver entre 1 e 7.

---

## 6. Maior de Três Números
**Enunciado**:  
- Leia três números do usuário.  
- Verifique qual deles é o maior e exiba na tela.  
- Se houver empate, exiba qual(is) número(s) está(ão) empatado(s) e que são os maiores.

---

## 7. Jogo de Adivinhação Simples
**Enunciado**:  
- Defina um número secreto em seu código, por exemplo, 7.  
- Peça ao usuário que tente adivinhar qual é o número secreto.  
- Se o palpite for maior que o número secreto, mostre "Muito alto!". Se for menor, "Muito baixo!". Se for igual, "Acertou!".

---

## 8. Verificação de Idade
**Enunciado**:  
- Receba do usuário sua idade.  
- Se a idade for menor que 18, exiba "Menor de idade".  
- Se a idade for entre 18 e 64, exiba "Adulto".  
- Se a idade for 65 ou mais, exiba "Idoso".

---

## 9. Classificação de Intervalos
**Enunciado**:  
- Peça ao usuário que digite um número.  
- Verifique e mostre em qual dos intervalos o número se encaixa:  
  - [0, 25]  
  - (25, 50]  
  - (50, 75]  
  - (75, 100]  
- Caso o número esteja fora de 0 a 100, exiba "Fora de intervalo".

---

## 10. Verificador de Login Simplificado
**Enunciado**:  
- Peça ao usuário que digite um nome de usuário e uma senha.  
- Compare com valores pré-definidos no código (por exemplo, usuário = "admin" e senha = "1234").  
- Se estiver correto, exiba "Acesso concedido". Caso contrário, "Acesso negado".

---

## 11. Desconto Progressivo
**Enunciado**:  
- Receba do usuário o valor de uma compra.  
- Se o valor for até R\$100, não conceda desconto.  
- Se estiver entre R\$101 e R\$200, conceda 10% de desconto.  
- Se for acima de R\$200, conceda 20% de desconto.  
- Mostre o valor final após o desconto.

---

## 12. Conversor de Notas para Conceitos
**Enunciado**:  
- Peça ao usuário que digite uma nota (0 a 10).  
- Converta a nota em conceito, seguindo alguma regra, por exemplo:  
  - 0 a 4: Conceito D  
  - 5 a 6: Conceito C  
  - 7 a 8: Conceito B  
  - 9 a 10: Conceito A  
- Exiba o conceito correspondente ou indique que a nota é inválida se não estiver no intervalo.

---

## 13. Identificação de Vogais e Consoantes
**Enunciado**:  
- Receba uma letra do usuário.  
- Verifique se a letra é uma vogal (a, e, i, o, u) ou consoante.  
- Considere apenas letras minúsculas para simplificar, ou trate as duas possibilidades (maiúsculas e minúsculas).

---

## 14. Verificar Divisibilidade
**Enunciado**:  
- Solicite um número inteiro.  
- Verifique se ele é divisível por 2, 3 e 5, mostrando mensagens diferentes para cada caso:  
  - "É divisível por 2" ou "Não é divisível por 2".  
  - "É divisível por 3" ou "Não é divisível por 3".  
  - "É divisível por 5" ou "Não é divisível por 5".

---

## 15. Triângulo Válido
**Enunciado**:  
- Receba três valores (comprimentos de lados).  
- Verifique se podem formar um triângulo (cada lado deve ser menor que a soma dos outros dois).  
- Se formarem um triângulo, verifique se é equilátero, isósceles ou escaleno.  
- Exiba o resultado.

---

## 16. Validação de Horário
**Enunciado**:  
- Peça ao usuário que informe um horário no formato "HH:MM".  
- Verifique se esse horário é válido (por exemplo, hora de 0 a 23 e minuto de 0 a 59).  
- Exiba "Horário válido" ou "Horário inválido".

---

## 17. Verificação de Aprovação em Duas Provas
**Enunciado**:  
- Solicite as notas de duas provas (0 a 10).  
- Verifique se o aluno foi aprovado:  
  - Se a média das notas for >= 6, "Aprovado".  
  - Senão, "Reprovado".  
- Se qualquer das notas estiver fora do intervalo, exiba "Nota inválida".

---

## 18. Sistema de Pagamento
**Enunciado**:  
- Peça o valor de uma compra e a forma de pagamento (1 = à vista, 2 = parcelado).  
- Se for à vista, conceda 5% de desconto.  
- Se for parcelado em 2x, o preço permanece igual.  
- Se for parcelado em mais vezes, acrescente 10% de juros.  
- Exiba o valor final.

---

## 19. Verificar se a Letra é Maiúscula ou Minúscula
**Enunciado**:  
- Peça ao usuário que informe uma letra.  
- Verifique se é maiúscula, minúscula ou se o caractere não é uma letra do alfabeto.  
- Exiba a mensagem correspondente.

---

## 20. Menu Interativo
**Enunciado**:  
- Mostre um menu com 3 opções:  
  1. Fazer algo (ex: "Exibir mensagem")  
  2. Fazer outra coisa (ex: "Calcular soma")  
  3. Sair  
- Peça ao usuário que selecione uma opção (1, 2 ou 3).  
- Use if/elif/else para executar a ação desejada.  
- Se for uma opção inválida, exiba uma mensagem de erro.  
- Continue pedindo a opção até o usuário escolher sair.
