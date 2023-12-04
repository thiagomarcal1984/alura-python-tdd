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

# Para saber mais: Arrange-Act-Assert

Existe uma outra metodologia muito utilizada para a construção do raciocínio de funcionamento de testes chamada **Arrange-Act-Assert** ou simplesmente **AAA**. Essa metodologia também consiste em 3 etapas para a construção de um teste, análogas às etapas do **Given-When-Then**.

- **Arrange:** A tradução não literal seria algo como organizar. A organização, nesse caso, seria focada nos passos preliminares necessários para montar o contexto inicial do teste;
- **Act:** A tradução não literal seria algo como agir. Nesse caso seria a ação que parte dos passos organizados na primeira etapa e leva ao que vamos averiguar no final;
- **Assert:** A tradução não literal seria algo como averiguar. Nesse caso, averiguarmos que o desfecho trazido pela ação é realmente aquele que esperamos.

# Outro cenário para testar
Uma nova funcionalidade (retornar o sobrenome) será criada. Após a sua criação, foi criado um novo cenário de teste.

Nova definição da classe `Funcionario`:
```python
class Funcionario:
    # Resto do código
    def sobrenome(self):
        # Remover caracteres em branco do início e do fim da string.
        nome_completo = self.nome.strip() 
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]
    # Resto do código
```

```python
class TestClass:
    # Resto do código
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        # Given
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'
        lucas = Funcionario(entrada, '11/11/2000', 1111)

        # When
        resultado = lucas.sobrenome()

        # Then
        assert resultado == esperado
```
Existe uma forma de desenvolver inversa: primeiro desenvolvemos o teste e depois desenvolvemos a funcionalidade. Essa é a premissao do TDD (Test Driven Development).

# TDD - Test Driven Development
O TDD tem um ciclo de 3 fases:
1. Criar/adaptar o teste (que vão falhar num primeiro momento);
2. Criar/adaptar a funcionalidade (para passar no teste);
3. Refatorar a funcionalidade (para fazer o código se conformar a boas práticas, padrões de projeto etc.).

# Implementando uma funcionalidade
Primeira etapa: criar o teste:
```python
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # Given
        entrada_salario  = 100000
        entrada_nome = 'Paulo Bragança'
        esperado =  90000

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)

        # When
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        # Then
        assert resultado == esperado
```
> Depois de rodar o `pytest -v`, o código vai apresentar o seguinte erro, já que o método não existe na classe `Funcionario`: 
> ```
> >       funcionario_teste.decrescimo_salario()
> E       AttributeError: 'Funcionario' object has no attribute 'decrescimo_salario'
> 
> test\test_bytebank.py:36: AttributeError
> ========================= short test summary info ==========================
> FAILED test/test_bytebank.py::TestClass::test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000
> ======================= 1 failed, 2 passed in 0.21s ========================
> ```

Segunda etapa: criar uma funcionalidade para que o teste passe.
```python
class Funcionario:
    # Resto do código
    def decrescimo_salario(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Ptolomeu']
        if self._salario >= 100000 and (self.sobrenome() in sobrenomes):
            decrescimo = self._salario * 0.1
            self._salario -= decrescimo
    # Resto do código
```
Após a criação da funcionalidade, verifique se os testes passaram
```
(venv) PS D:\alura\python-tdd> pytest -v
=========================== test session starts ============================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0 -- D:\alura\python-tdd\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\alura\python-tdd
collected 3 items

test/test_bytebank.py::TestClass::test_quando_idade_recebe_13_03_2000_deve_retornar_22 PASSED [ 33%]
test/test_bytebank.py::TestClass::test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho PASSED [ 66%]
test/test_bytebank.py::TestClass::test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000 PASSED [100%]

============================ 3 passed in 0.04s ============================= 
(venv) PS D:\alura\python-tdd>
```
Terceira etapa: refatorar o código.

No exemplo, o método `decrescimo_salario` faz duas coisas: checa se a pessoa tem um sobrnome e faz o decréscimo do salário. Isso fere o princípio da responsabilidade única do código.

Essa refatoração vai ser feita na próxima aula.

# Refatorando o código
A refatoração vai consistir em dividr o método `decrescimo_salario` em duas partes separadas:
```python
class Funcionario:
    # Resto do código
    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario -= decrescimo

    def _eh_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Ptolomeu']
        return self._salario >= 100000 and (self.sobrenome() in sobrenomes)
    # Resto do código
```
Depois de executar o `pytest -v`, os testes continuam passando e o código das funcionalidades está melhor estruturado.

# Um método com Exception
Criação do teste para o "caso feliz" do cálculo do bônus do salário:
```python
from bytebank import Funcionario
class TestClass:
    # Resto do código.
    def test_quando_calcular_bonus_recebe_1000_deve_retorna_100(self):
        # Given
        entrada  = 1000
        esperado =  100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)

        # When
        resultado = funcionario_teste.calcular_bonus()

        # Then
        assert resultado == esperado
```
O "caso infeliz" é quando o funcionário não faz jus ao bônus. O método foi reescrito para lançar uma exceção:
```python
class Funcionario:
    # Resto do código.
    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus.')
        return valor
```
O teste para capturar a exceção será escrito na próxima aula.

# Lidando com Exceptions no Pytest
Qualquer teste que precise confirmar o lançamento de uma exceção deve ser envolvido por `with pytest.raises(NomeDaException)`.

Veja a implementação do teste a seguir:
```python
from bytebank import Funcionario
import pytest

class TestClass:
    # Resto do código
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            # Given
            entrada  = 1000000

            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)

            # When
            resultado = funcionario_teste.calcular_bonus()

            # Then
            # Se a exceção não for lançada após a execução do teste, 
            # ele não passa (Failed: DID NOT RAISE <class 'Exception'>).
```
# Organizando testes com Markers
## Filtrando os testes pelo nome do método (parâmetro `-k` do pytest)
O parâmetro `-k <string_procurada>` no Pytest permite filtrar os nomes dos testes que serão executados. Veja o exemplo abaixo, procurando pela palavra `idade` nos métodos de teste:
```
(venv) PS D:\alura\python-tdd> pytest --verbose -k idade
====================================================================== test session starts ======================================================================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0 -- D:\alura\python-tdd\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\alura\python-tdd
collected 5 items / 4 deselected / 1 selected

test/test_bytebank.py::TestClass::test_quando_idade_recebe_13_03_2000_deve_retornar_22 PASSED                                                              [100%] 

================================================================ 1 passed, 4 deselected in 0.04s ================================================================ 
(venv) PS D:\alura\python-tdd> 
```

Mesma coisa, procurando pela palavra `calcular`:
```
(venv) PS D:\alura\python-tdd> pytest -v -k calcular
====================================================================== test session starts ======================================================================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0 -- D:\alura\python-tdd\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\alura\python-tdd
collected 5 items / 3 deselected / 2 selected

test/test_bytebank.py::TestClass::test_quando_calcular_bonus_recebe_1000_deve_retorna_100 PASSED                                                           [ 50%] 
test/test_bytebank.py::TestClass::test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception PASSED                                                 [100%]

================================================================ 2 passed, 3 deselected in 0.04s ================================================================ 
(venv) PS D:\alura\python-tdd> 
```
> Repare que há um número de testes não executados (deselected) nos resultados do teste.

## Controlando quais testes serão executados por meio dos markers
É possível "rotular" alguns testes com os chamados `markers`. O Pytest tem a anotação `pytest.mark`, que pode ser anteposta aos métodos de teste.

Depois que os métodos de teste forem anotados com um marker (por exemplo, `@pytest.mark.meu_marker`), você pode executar o comando `pytest -m nome_exato_do_marker` para executar apenas os testes que contenham esse marker personalizado.

Alguns markers tem funções específicas. Por exemplo, o marker `pytest.mark.skip` serve para pular o teste anotado.
Para ver quais os markers estão registrados, use o comando `pytest --markers`.

Vamos supor que queremos pular o teste `test_quando_idade_recebe_13_03_2000_deve_retornar_22`. Apenas anotamos ele com o marker `pytest.mark.skip`:
```python
from bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    @mark.skip
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Implementação do teste.
    # Resto do código.
```

Repare que, ao invocarmos `pytest -v`, o teste `test_quando_idade_recebe_13_03_2000_deve_retornar_22` não será executado (repare na palavra `SKIPPED`):
```
(venv) PS D:\alura\python-tdd> pytest -v
====================================================================== test session starts ======================================================================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0 -- D:\alura\python-tdd\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\alura\python-tdd, configfile: pytest.ini
collected 5 items

test/test_bytebank.py::TestClass::test_quando_idade_recebe_13_03_2000_deve_retornar_22 SKIPPED (unconditional skip)                                        [ 20%] 
test/test_bytebank.py::TestClass::test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho PASSED                                                [ 40%]
test/test_bytebank.py::TestClass::test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000 PASSED                                                  [ 60%]
test/test_bytebank.py::TestClass::test_quando_calcular_bonus_recebe_1000_deve_retorna_100 PASSED                                                           [ 80%] 
test/test_bytebank.py::TestClass::test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception PASSED                                                 [100%]

================================================================= 4 passed, 1 skipped in 0.09s ================================================================== 
(venv) PS D:\alura\python-tdd> 
```

# Usando markers personalizados.
Nova definição da classe `TestClass`, com os markers do Pytest:
```python
from bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    # Resto do código
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retorna_100(self):
        # Implementação do teste

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        # Implementação do teste
    # Resto do código
```

Ao executarmos o comando `pytest -v -m calcular_bonus`, recebemos alguns warnings porque o marker `calcular_bonus` não está registrado no Pytest:
> Note que precisamos usar o nome exato do marker para que ele funcione. Se quisermos usar o marker `calcular_bonus`, não basta escrevermos apenas `calcular`.
```
(venv) PS D:\alura\python-tdd> pytest -v -m calcular_bonus
====================================================================== test session starts ======================================================================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0 -- D:\alura\python-tdd\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\alura\python-tdd, configfile: pytest.ini
collected 5 items / 3 deselected / 2 selected

test/test_bytebank.py::TestClass::test_quando_calcular_bonus_recebe_1000_deve_retorna_100 PASSED                                                           [ 50%]
test/test_bytebank.py::TestClass::test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception PASSED                                                 [100%] 

======================================================================= warnings summary ======================================================================== 
test\test_bytebank.py:45
  D:\alura\python-tdd\test\test_bytebank.py:45: PytestUnknownMarkWarning: Unknown pytest.mark.calcular_bonus - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @mark.calcular_bonus

test\test_bytebank.py:59
  D:\alura\python-tdd\test\test_bytebank.py:59: PytestUnknownMarkWarning: Unknown pytest.mark.calcular_bonus - is this a typo?  You can register custom marks to avoid this warning - for details, see https://docs.pytest.org/en/stable/how-to/mark.html
    @mark.calcular_bonus

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
========================================================== 2 passed, 3 deselected, 2 warnings in 0.06s ========================================================== 
(venv) PS D:\alura\python-tdd> 
```

Para evitar esses warnings, temos que configurar o arquivo `pytest.ini` na raiz do projeto. Ele terá a seguinte configuração:
```ini
[pytest]
markers = 
    ; nome_do_marker: Descrição do marker.
    calcular_bonus: Teste para o método calcular_bonus.
```

Repetindo o comando após a inclusão do `pytest.ini`, os warnings não vão mais aparecer:
```
(venv) PS D:\alura\python-tdd> pytest -v -m calcular_bonus
====================================================================== test session starts ======================================================================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0 -- D:\alura\python-tdd\venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: D:\alura\python-tdd, configfile: pytest.ini
collected 5 items / 3 deselected / 2 selected

test/test_bytebank.py::TestClass::test_quando_calcular_bonus_recebe_1000_deve_retorna_100 PASSED                                                           [ 50%] 
test/test_bytebank.py::TestClass::test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception PASSED                                                 [100%] 

================================================================ 2 passed, 3 deselected in 0.04s ================================================================ 
(venv) PS D:\alura\python-tdd> 
```

Exibição dos markers registrados após a inclusão do arquivo `pytest.ini` e a execução do comando `pytest --markers`:
```
(venv) PS D:\alura\python-tdd> pytest --markers
@pytest.mark.calcular_bonus: Teste para o método calcular_bonus.

@pytest.mark.filterwarnings(warning): add a warning filter to the given test. see https://docs.pytest.org/en/stable/how-to/capture-warnings.html#pytest-mark-filterwarnings

# Resto da saída
```
# Para saber mais: Markers
Parte da razão pela qual o Pytest é conhecido como framework de testes, não uma simples biblioteca, está no fato do Pytest possuir uma vasta gama de ferramentas direcionadas a melhorar a eficiência e organização dos testes desenvolvidos.

Os markers ou marcadores são uma dessas ferramentas incríveis do Pytest e oferecem não somente uma forma de organizar melhor os testes com tags personalizadas, mas colaboram para definir como determinados testes irão funcionar ou ser executados.

## skip
```python
@pytest.mark.skip(reason="não quero executar isso agora")
def test_aleatorio():
    # Resto do código.
```
Através do uso do marker `skip` podemos pular um teste, caso a execução dele não seja necessária naquele instante.

## skipif
```python
import sys

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requer Python na versão 3.10 ou superior")
def test_funcao():
    # Resto do código.
```
Acima, o teste não é executado caso sys.version_info < (3, 10) seja verdadeiro, ou seja, caso a versão do Python esteja abaixo da versão 3.10.

Através do uso do marker `skipif` podemos pular um teste caso ele se encaixe em determinada situação definida por uma condicional.

## xfail
```python
@pytest.mark.xfail
def test_funcao():
    # Resto do código.
```
Através do uso do marker xfail especificamos que o teste deve retornar uma falha, em vez de passar.

Essas e muitas outras possibilidades de uso de markers para modificar a mecânica de uso dos testes podem ser vistas na documentação oficial do Pytest.

How to mark test functions with attributes: https://docs.pytest.org/en/7.1.x/how-to/mark.html#mark

## Testando o marker `xfail`
Mudei o código do método `test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception`:
```python
    @mark.calcular_bonus
    @pytest.mark.xfail
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        # with pytest.raises(Exception):
            # Resto do código
```
Após executar o `pytest`, o resultado mostra quais testes passaram e quais falharam porque deveriam falhar (o número de `xfailed`):
```
(venv) PS D:\alura\python-tdd> pytest
====================================================================== test session starts ======================================================================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0
rootdir: D:\alura\python-tdd, configfile: pytest.ini
collected 5 items

test\test_bytebank.py ....x                                                                                                                                [100%]

================================================================= 4 passed, 1 xfailed in 0.22s ================================================================== 
(venv) PS D:\alura\python-tdd> 
```
## E se o teste marcado com `xfail` passar?
Suponha um código que deveria lançar uma exceção, mas não lança:
```python
    @mark.calcular_bonus
    @pytest.mark.xfail
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            # Resto do código
```

Nesse caso, o relatório do Pytest exibe o parâmetro `xpassed` (que mostra testes que passaram, mas não deveriam):
```
(venv) PS D:\alura\python-tdd> pytest
====================================================================== test session starts ======================================================================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0
rootdir: D:\alura\python-tdd, configfile: pytest.ini
collected 5 items

test\test_bytebank.py ....X                                                                                                                                [100%]

================================================================= 4 passed, 1 xpassed in 0.05s ================================================================== 
(venv) PS D:\alura\python-tdd> 
```
