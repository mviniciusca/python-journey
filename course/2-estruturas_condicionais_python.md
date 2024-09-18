# Aula 2: Estruturas Condicionais em Python

## Ponto de Partida

Nesta aula, vamos explorar três conceitos fundamentais para a implementação de algoritmos em Python:

1. **Operadores relacionais**: Ferramentas de comparação que nos permitem avaliar relações entre valores.
2. **Estruturas lógicas**: Peças de quebra-cabeça que unem condições para criar critérios mais complexos.
3. **Estruturas condicionais**: Instruções que dizem ao programa como agir com base em condições específicas.

> **Estudo de Caso**: Imagine que você trabalhe em uma empresa que administra cinemas. A diretoria solicitou a implementação de um sistema de autoatendimento baseado na idade dos clientes e na disponibilidade de ingressos.

## Vamos Começar!

### Operadores Relacionais

Os operadores relacionais são essenciais para tomar decisões em programação. Eles nos permitem fazer comparações entre valores.

| Operação | Significado                     |
| -------- | ------------------------------- |
| <        | Estritamente menor que          |
| <=       | Menor ou igual que              |
| >        | Estritamente maior que          |
| >=       | Maior ou igual que              |
| ==       | Igual                           |
| !=       | Diferente                       |
| is       | Identidade do objeto            |
| is not   | Negação da identidade do objeto |

### Estruturas Lógicas

Além dos operadores relacionais, utilizamos operadores booleanos para construir decisões mais complexas:

1. **Operador "E" (and)**
   - Retorna "Verdadeiro" somente quando ambos os argumentos são verdadeiros.

2. **Operador "OU" (or)**
   - Retorna "Verdadeiro" se pelo menos um dos argumentos for verdadeiro.

3. **Operador "NÃO" (not)**
   - Inverte o valor do argumento.

> Esses operadores booleanos são essenciais para a criação de estruturas de decisão mais sofisticadas.

## Siga em Frente...

### Estruturas Condicionais: if, else e elif

As estruturas condicionais em Python são como bifurcações em uma estrada, orientando o fluxo do programa com base nas condições estabelecidas.

- **if**: Executa um bloco de código se a condição for verdadeira.
- **else**: Executa um bloco de código se a condição do if for falsa.
- **elif**: Abreviação de "else if", permite avaliar múltiplas condições em sequência.

**Exemplo:**

```python
idade = 25

if idade < 18:
    print("Menor de idade")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")
```

## Vamos Exercitar?

Vamos criar um algoritmo de recomendação para um cinema, baseado na idade do cliente e na disponibilidade de ingressos:

```python
# Bem-vindo à Máquina de Venda Automática de Ingressos de Cinema!

# Solicita a idade do cliente
idade = int(input("Por favor, digite sua idade: "))

# Verifica a idade para sugestão de filmes
if idade < 12:
    print("Recomendamos o filme infantil FILME 1.")
elif 12 <= idade < 18:
    print("Recomendamos o filme adolescente FILME 2.")
else:
    print("Recomendamos o emocionante FILME 3.")

# Verifica a disponibilidade de ingressos
quantidade_ingressos = 10  # Suponha que haja 10 ingressos disponíveis
if quantidade_ingressos > 0:
    print("Ingressos estão disponíveis. Divirta-se no cinema!")
else:
    print("Desculpe, todos os ingressos estão esgotados para hoje.")
```

> Rode esse código no seu Google Colab e faça testes, substitua a disponibilidade de ingresso, insira idades diferentes... Enfim, "brinque" com ele.

## Saiba Mais

Para aprofundar seus conhecimentos, recomendamos:

1. Artigo: "Arquitetura de sistemas de recomendação para apoio ao vendedor no uso de sistemas de força de vendas em empresa com grande portfólio de produtos" (OHASHI et al., 2021)
2. Livro: "Começando a programar em Python para leigos" de John Paul Mueller
3. Livro: "Use a cabeça! Python" de Paul Barry

---

Esta aula introduziu conceitos fundamentais de estruturas condicionais em Python. Continue praticando e explorando essas ferramentas para criar algoritmos cada vez mais sofisticados!