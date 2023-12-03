# O projeto Bytebank
Classe Funcionario no arquivo `bytebank.py`:
```python
from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        ano_atual = date.today().year
        return ano_atual - int(self._data_nascimento)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self) -> str:
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
```

Execução (falha) da classe no arquivo `main.py`:
```python
from bytebank import Funcionario

lucas = Funcionario('Lucas Carvalho', '13/03/2000', 1000)
print(lucas.idade())
```

# Criando o primeiro teste
Vamos migrar o código do teste em `main.py` para o método `teste_idade()` e executar esse método:
```python
from bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

teste_idade()
```

Fazendo a correção do método `idade()` na classe `Funcionario`:
```python
from datetime import date

class Funcionario:
    # Resto do código
    def idade(self):
        ano_atual = date.today().year
        data_nascimento_quebrada = self._data_nascimento.split('/')
        # O ano de nascimento é o último elemento (-1).
        ano_nascimento = data_nascimento_quebrada[-1]
        return ano_atual - int(ano_nascimento)
    # Resto do código
```
# O que são testes?
Teste manual:
1. Mais lento;
2. Sujeito a falhas (fator humano);
3. Inconveniente.

Teste automatizado:
1. Ele é... automatizado;
2. Feedback rápido;
3. Segurança em alteração do código.
4. Apoia o processo de refactoring.

# Tipos de teste
1. Teste unitário: testa apenas uma pequena parte da aplicação.
2. Teste de integração: testa a comunicação entre as partes menores.
3. Teste de ponta a ponta (E2E): simula o usuário da aplicação, ele é mais abrangente.

O foco do curso será testes unitários.

Mas veja o exemplo da função `teste_idade`:
```python
from bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste1 = Funcionario('Teste', '13/03/1999', 1111)
    print(f'Teste = {funcionario_teste1.idade()}')

    funcionario_teste2 = Funcionario('Teste', '01/12/1999', 1111)
    print(f'Teste = {funcionario_teste2.idade()}')

teste_idade()
```
Repare que o número de cenários aumentou. Se houver a criação de muitos cenários diferentes, pode ser difícil perceber o que funcionou e o que falhou.

# Instalação do Pytest
Vantagens do Pytest:
1. Múltiplos plugins;
2. Altamente escalável (dá conta do crescimento da base de código);
3. Utilização simples.

Para instalar o Pytest, use o comando abaixo (após entrar no ambiente virtual):

```shell
.\venv\Scripts\activate
pip install pytest==7.1.2
```

Depois de instalar os pacotes, pode ser interessante gerar o arquivo `requirements.txt` para conter as dependências usadas no seu ambiente e poder replicar esse ambiente em outor momento:
```shell
pip freeze > requirements.txt
```

Para usar o Pytest, insira as classes de teste no diretório `tests` (nome no plural). Esse diretório precisa ser tratado como um módulo do Python, portanto precisamos inserir o arquivo `__init__.py` dentro do diretório `tests`.

# Teste automatizado com Pytest
Qualquer método testável pelo Pytest deve ser prefixado com `test_`, no singular, em caixa baixa e com o underline.

Uma boa prática para testes é colocar nomes verbosos nos métodos/funções dos testes.

Metodologia Given-When-Then:
1. Dado (contexto), por exemplo "dinheiro guardado";
2. Quando (ação), por exemplo "comprar blusa";
3. Então (desfecho), por exemplo "blusa comprada".

A invocação dos testes com Pytest pode ser verbosa (basta inserir o parâmetro `-v` ou `--verbose`):
```
pytest --verbose
```

Definição da classe de teste `TestClase` no arquivo `tests/test_bytebank.py`:
```python
from bytebank import Funcionario
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given-Contexto
        entrada = '13/03/2000' # Given-Entrada
        esperado = 23
        funcionario_teste = Funcionario('Teste', entrada, 1111)

        # When-Quando
        resultado = funcionario_teste.idade() # When-idade()

        # Then-Desfecho
        assert resultado == esperado #Then resultado == esperado
```
> Se o arquivo estivesse nomeado como `tests_...` ao invés de `test_...`, o Pytest não vai reconhecer o arquivo e portanto o teste não será realizado.
