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
