# Estruturas de Repetição em Python

## Ponto de Partida

Nesta aula, vamos explorar estruturas de repetição e controle essenciais para a implementação de algoritmos em Python:

1. **for**: Uma estrutura de repetição para percorrer sequências de elementos.
2. **while**: Uma estrutura para controlar repetições baseadas em condições.
3. **range**, **break**, e **continue**: Funções para controle adicional de repetições.

> **Estudo de Caso**: Imagine que você precisa criar um algoritmo para classificar cinco filmes exibidos no cinema, atribuindo de 1 a 5 estrelas para cada um.

## Vamos Começar!

### Estrutura de Repetição for

O `for` é uma ferramenta poderosa para realizar ações repetitivas de maneira controlada.

**Exemplo:**

```python
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    print(numero)
```

**Saída:**
```
1
2
3
4
5
```

### Estrutura de Repetição while

O `while` é usado para criar estruturas de repetição quando o número de repetições não é conhecido antecipadamente.

**Exemplo:**

```python
numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é ímpar")
    numero = int(input("Digite outro número (0 para sair): "))
```

## Siga em Frente...

### Controle de Repetição: range, break e continue

#### Função range()

A função `range()` cria sequências numéricas para uso em estruturas de repetição.

1. **Repetição por quantidade:**
   ```python
   for x in range(5):
       print(x)
   ```

2. **Limites inicial e superior:**
   ```python
   for y in range(2, 7):
       print(y)
   ```

3. **Com incremento:**
   ```python
   for z in range(1, 11, 2):
       print(z)
   ```

#### Comandos break e continue

- **break**: Interrompe a execução de uma estrutura de repetição.
- **continue**: Pula a iteração atual e continua com a próxima.

**Exemplo com break:**

```python
for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"O primeiro número par encontrado é: {numero}")
        break
```

**Exemplo com continue:**

```python
for numero in range(1, 11):
    if numero == 5:
        continue
    print(numero)
```

## Vamos Exercitar?

Vamos criar um programa para classificar cinco filmes com notas de 1 a 5 estrelas:

```python
filmes = ["Filme 1", "Filme 2", "Filme 3", "Filme 4", "Filme 5"]

print("Bem-vindo ao sistema de classificação de filmes!")
print("Por favor, classifique cada filme de 1 a 5 estrelas.")
print("Digite 0 a qualquer momento para encerrar o programa.\n")

for filme in filmes:
    while True:
        classificacao = input(f"Classifique '{filme}' de 1 a 5? (ou 0 para parar): ")
        if classificacao == '0':
            print(f"Classificação de '{filme}' interrompida.")
            break
        classificacao = int(classificacao)
        if classificacao < 1 or classificacao > 5:
            print("Por favor, insira um número entre 1 e 5.")
        else:
            print(f"Você classificou '{filme}' com {classificacao} estrelas.\n")
            break

print("Obrigado por usar nosso sistema de classificação!")
```

> Rode esse código no Google Colab, faça modificações e experimente com ele. Lembre-se de que a prática é extremamente importante para melhorar suas habilidades!

## Saiba Mais

Para aprofundar seus conhecimentos, recomendamos:

1. Dissertação: "Robotic process automation e a auditoria financeira: modern framework" de Luís Inácio Soares Calçada
2. Livro: "Começando a programar em Python para leigos" de John Paul Mueller
3. Livro: "Use a cabeça! Python" de Paul Barry

---

Esta aula introduziu conceitos fundamentais de estruturas de repetição em Python. Continue praticando e explorando essas ferramentas para criar algoritmos cada vez mais sofisticados!