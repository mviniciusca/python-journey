# Ponto de Partida: Introdução ao Python

## Por que Python?

Python é uma linguagem de programação de alto nível amplamente usada na indústria de tecnologia. Nesta aula, você começará a entender por que Python é tão popular e como pode ser utilizada em diversas aplicações.

Você aprenderá sobre:
- Ferramentas necessárias para iniciar a programação em Python
- Instalação do Python em seu computador
- Seleção de um ambiente de desenvolvimento adequado
- Criação de variáveis e tipos de dados em Python

> Como professor, preciso avaliar constantemente os estudantes. Sendo assim, quero automatizar a média de notas dos alunos. É possível fazer isso utilizando Python?

## Vamos Começar!

### Introdução à linguagem Python

```python
print("hello world!")
```

**Saída:**
```
hello world!
```

> Há uma lenda entre programadores segundo a qual se você não imprimir o "hello world" quando começar a aprender uma linguagem, não conseguirá assimilar nada sobre ela (Ciência da Computação, 2015).

Python é uma linguagem de programação **versátil e fácil de aprender**. Foi criada por Guido van Rossum e lançada em 1991. Desde então, tornou-se uma das linguagens mais populares do mundo por causa de sua legibilidade e sintaxe simples.

### Por que escolher Python?

Python é usado em várias áreas, incluindo:
- Desenvolvimento web
- Automação
- Aprendizado de máquina
- Análise de dados

De acordo com o guia de desenvolvimento para iniciantes Python (Python Wiki, 2022):

> Python é uma linguagem de programação orientada a objetos, clara e poderosa, comparável a Perl, Ruby, Scheme ou Java.

## Filosofia Python

Uma das principais filosofias de Guido van Rossum é que **o código deve ser facilmente legível**, uma vez que é lido com mais frequência do que é escrito. Isso é formalizado no **PEP 8**, o Guia de Estilo para Código Python.

### Código "Pythonic"

Seguir as diretrizes do PEP 8 resulta em um código que é considerado "pythonic" – ou seja, que adere aos princípios de:
- Formatação do código
- Definição e organização de funções
- Aplicação da indentação
- Outros aspectos relacionados à sintaxe do código Python

## Ferramentas e Interpretadores

Para escrever e executar código Python, você precisará de:

1. Um interpretador Python
2. Um ambiente de desenvolvimento (IDE)

### Instalação do Python

O passo a passo para a instalação do interpretador Python está disponível no site oficial, tanto para Windows quanto para outros sistemas operacionais.

### IDEs Recomendadas

- **PyCharm**
- **Visual Studio Code (VSCode)**
- **Python Anaconda** (inclui Jupyter Notebook)
- **Google Colab** (recomendado para esta disciplina)

> O Google Colab é uma plataforma que possibilita que qualquer pessoa escreva e execute código Python a partir do navegador, sem necessidade de instalação.

## Variáveis e Tipos de Dados

Em Python, as variáveis são espaços alocados na memória RAM para armazenar valores. O interpretador Python consegue estabelecer o tipo de dado da variável observando seu valor.

### Exemplos:

```python
x = 10
nome = 'aluno'
nota = 8.75
fez_inscricao = True

print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))
```

**Saída:**
```
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

### Capturando Input do Usuário

```python
nome = input("Digite um nome: ")
print(nome)
```

### Formatando Strings

Existem várias formas de imprimir textos e variáveis em Python. A mais recomendada é usando **f-strings**:

```python
print(f"Olá, {nome}, bem-vindo à disciplina de programação. Parabéns pelo seu primeiro hello world")
```

## Exercício Prático: Calculando Médias de Alunos

Vamos criar um programa para calcular a média de notas dos alunos:

```python
Nota_1 = int(input("Digite a primeira nota: "))
Nota_2 = int(input("Digite a segunda nota: "))
Nota_3 = int(input("Digite a terceira nota: "))
Nota_4 = int(input("Digite a quarta nota: "))

media = (Nota_1 + Nota_2 + Nota_3 + Nota_4) / 4

if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"Média final: {media}")
print(f"Situação: {situacao}")
```

## Saiba Mais

Para aprofundar seus conhecimentos em Python, recomendamos os seguintes recursos:

1. Livro: "Começando a programar em Python para leigos" de John Paul Mueller
2. Livro: "Use a cabeça! Python" de Paul Barry
3. Livro: "Python e mercado financeiro: programação para estudantes, investidores e analistas" de Marco Aurélio Leonel Caetano
4. Sites oficiais: [Python](https://www.python.org/), [Jupyter](https://jupyter.org/), e [Google Colab](https://colab.research.google.com/)

---

Este material é uma introdução básica ao Python, suas ferramentas e alguns exemplos de uso. Esperamos que isso tenha despertado sua curiosidade para aprender mais sobre esta poderosa linguagem de programação!