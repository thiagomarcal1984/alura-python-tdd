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
