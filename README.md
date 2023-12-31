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

# Configurando ferramenta de cobertura
A extensão `pytest-cov` permite analisar a cobertura dos testes escritos com Pytest. Para invocar essa extensão, use o parâmetro `--cov` (coverage, cobertura) do comando `pytest`.

```
(venv) PS D:\alura\python-tdd> pytest --cov
=========================== test session starts ============================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0
rootdir: D:\alura\python-tdd, configfile: pytest.ini
plugins: cov-4.1.0
collected 5 items

test\test_bytebank.py ....X                                           [100%]

---------- coverage: platform win32, python 3.11.0-final-0 -----------       
Name                    Stmts   Miss  Cover
-------------------------------------------
bytebank.py                35      1    97%
test\__init__.py            0      0   100%
test\test_bytebank.py      38      0   100%
-------------------------------------------
TOTAL                      73      1    99%


======================= 4 passed, 1 xpassed in 0.11s ======================= 
(venv) PS D:\alura\python-tdd> 
```

O relatório tem 3 colunas: 
1. Statements (Stmts) é o número de linhas de código declaradas.
2. Miss é o número de linhas de código não testadas.
3. Cover é a razão entre as declarações cobertas e o número de todas as declarações (resultando o percentual de cobertura).

Repare que o relatório analisa a cobertura de outros arquivos que não necessariamente precisam ser testados (os dois arquivos de dentro do diretório test).

Para evitar essa poluição no relatório, forneça para o parâmetro `--cov` o valor correspondente ao módulo que será testado, e em seguida o valor que corresponde ao diretório onde estão os testes que serão executados (no caso, o diretório `test`):

```
(venv) PS D:\alura\python-tdd> pytest --cov=bytebank test/
=========================== test session starts ============================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0
rootdir: D:\alura\python-tdd, configfile: pytest.ini
plugins: cov-4.1.0
collected 5 items

test\test_bytebank.py ....X                                           [100%]

---------- coverage: platform win32, python 3.11.0-final-0 -----------       
Name          Stmts   Miss  Cover
---------------------------------
bytebank.py      35      1    97%
---------------------------------
TOTAL            35      1    97%


======================= 4 passed, 1 xpassed in 0.06s ======================= 
(venv) PS D:\alura\python-tdd> pytest --cov=bytebank test
```

# Garantindo cobertura total
Podemos passar o parâmetro `--cov-report term-missing` para o Pytest, de forma a exibir as linhas de código que não tem teste associado:

```
(venv) PS D:\alura\python-tdd> pytest --cov=bytebank test/ --cov-report term-missing
=========================== test session starts ============================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0
rootdir: D:\alura\python-tdd, configfile: pytest.ini
plugins: cov-4.1.0
collected 5 items

test\test_bytebank.py ....X                                           [100%]

---------- coverage: platform win32, python 3.11.0-final-0 -----------       
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
bytebank.py      35      1    97%   46
-------------------------------------------
TOTAL            35      1    97%


======================= 4 passed, 1 xpassed in 0.09s ======================= 
(venv) PS D:\alura\python-tdd>
```
> Repare na coluna `Missing`, que contém o número 46. Esse número é o da linha de código sem teste.


Mudança no teste para aumentar a cobertura do código:
```python
from bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    # Resto do código
    def test_retorno_str(self):
        # Given
        nome, data_nascimento, salario =  'Teste', '11/11/2000', 2000
        esperado = "Funcionario(Teste, 11/11/2000, 2000)"

        # When
        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__()
        
        # Then
        assert resultado == esperado
```

Usando novamente o `pytest-cov` para ver o percentual de cobertura:
```
(venv) PS D:\alura\python-tdd> pytest --cov=bytebank --cov-report term-missing
=========================== test session starts ============================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0
rootdir: D:\alura\python-tdd, configfile: pytest.ini
plugins: cov-4.1.0
collected 6 items

test\test_bytebank.py ....X.                                          [100%]

---------- coverage: platform win32, python 3.11.0-final-0 -----------       
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
bytebank.py      35      0   100%
-------------------------------------------
TOTAL            35      0   100%


======================= 5 passed, 1 xpassed in 0.12s ======================= 
(venv) PS D:\alura\python-tdd> 
```
# Excluindo código para a cobertura

## Relatórios em HTML
Para criar um relatório de testes e mformato HTML, insira no parâmetro `--cov-report` o valor `html` (`pytest --cov=bytebank --cov-report html`):
```
(venv) PS D:\alura\python-tdd> pytest --cov=bytebank --cov-report html
=========================== test session starts ============================
platform win32 -- Python 3.11.0, pytest-7.1.2, pluggy-1.3.0
rootdir: D:\alura\python-tdd, configfile: pytest.ini
plugins: cov-4.1.0
collected 5 items

test\test_bytebank.py ....X                                           [100%]

---------- coverage: platform win32, python 3.11.0-final-0 -----------       
Coverage HTML written to dir htmlcov


======================= 4 passed, 1 xpassed in 0.26s ======================= 
(venv) PS D:\alura\python-tdd> pytest --cov=bytebank --cov-report html
```

> Após a execução do comando, o diretório `htmlcov` será criado, com vários arquivos HTML vinculados a cada módulo Python testado. ***O diretório htmlcov foi renomeado para #htmlcov porque o .gitignore não consegue remover a exceção para o diretório com a cobertura dos teste***.
>
> Esses relatórios HTML permitem destacar:
> 1.  o que está coberto por testes;
> 2.  o que não está coberto por testes; e 
> 3. os testes que foram ignorados.

## Excluindo testes com o arquivo `.coveragerc`
O arquivo `.coveragerc` (que fica na raiz do projeto) contém algumas configurações para a extensão `pytest-cov`, semelhantes às de um arquivo `.ini`:

```ini
[run]

[report]
exclude_lines = 
    def __str__
```
Abaixo do parâmetro `[report]exclude_lines` colocamos os prefixos dos métodos que desejamos excluir da cobertura de testes.

Para refazer o relatório com as exclusões, basta repetir o código `pytest --cov --cov-report html`.

# Gerando relatórios
Uma forma de resumir o código para gerar os relatórios de cobertura de testes é inserir mais alguns parâmetros no arquivo `.coveragerc`:

```ini
[run]
# É necessário informar o `diretório` que 
# será acessado, não o módulo Python.
# Por isso, o arquivo `bytebank.py` foi movido 
# para o diretório `codigo`, e as referências a 
# esse arquivo foram atualizadas.
source = ./codigo

[report]
exclude_lines = 
    def __str__

[html]
directory = coverage_relatorio_html
```

> O arquivo `.coveragerc` tem esse nome porque a extensão `.rc` é comumente utilizada para indicar que é um arquivo de configuração. A sigla "rc" significa "run commands" ou "runtime configuration", indicando que o arquivo contém configurações para serem utilizadas durante a execução do programa.


É possível "enxugar" o comando do Pytest, sem fornecer os parâmetros. Basta configurar o arquivo `pytest.ini`, acrescentando o parâmetro `addopts` dentro do grupo `[pytest]`:
```ini
[pytest]
; Add Options
addopts = -v --cov=codigo test/ --cov-report term-missing
markers = 
    calcular_bonus: Teste para o método calcular_bonus.
```
> Repare que `addopts` recebe os 3 parâmetros que usamos até agora: 
> 1. `-v`: saída verbosa;
> 2. `cov=*diretório*`: indica o diretório que conterá os **códigos das funcionalidades** que serão testados;
> 3. `cov-report *tipo_de_relatório*`: indica o tipo de relatório de cobertura; e
> 4. o diretório que conterá os **códigos dos testes**.

Para exportar os relatórios de teste para XML, use o parâmetro `--junitxml *nome_do_arquivo_de_saida*` para o comando `pytest`:
```
pytest --junitxml report.xml
```
Arquivo resultante (mostra as classes de testes, métodos de teste e tempo gasto com os testes): 
```XML
<?xml version="1.0" encoding="utf-8"?>
<testsuites>
    <testsuite name="pytest" errors="0" failures="0" skipped="0" tests="5" time="0.205" timestamp="2023-12-07T20:55:27.742043" hostname="DESKTOP-AJ7MRN7">
        <testcase classname="test.test_bytebank.TestClass" name="test_quando_idade_recebe_13_03_2000_deve_retornar_22" time="0.005" />
        <testcase classname="test.test_bytebank.TestClass" name="test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho" time="0.003" />
        <testcase classname="test.test_bytebank.TestClass" name="test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000" time="0.002" />
        <testcase classname="test.test_bytebank.TestClass" name="test_quando_calcular_bonus_recebe_1000_deve_retorna_100" time="0.002" />
        <testcase classname="test.test_bytebank.TestClass" name="test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception" time="0.005" />
    </testsuite>
</testsuites>
```

Para gerar o relatório de *cobertura* dos testes, você pode usar o valor `xml` para o parâmetro `cov-report` do `pytest`:

```
pytest --cov-report xml
```
> O arquivo `coverage.xml` também está no arquivo `.gitignore`.
>
> Conteúdo do arquivo `coverage.xml`:
> ```XML
> <?xml version="1.0" ?>
> <coverage version="7.3.2" timestamp="1701993527626" lines-valid="33" lines-covered="33" line-rate="1" branches-covered="0" branches-valid="0" branch-rate="0" complexity="0">
> 	<!-- Generated by coverage.py: https://coverage.readthedocs.io/en/7.3.2 -->
> 	<!-- Based on https://raw.githubusercontent.com/cobertura/web/master/htdocs/xml/coverage-04.dtd -->
> 	<sources>
> 		<source>D:\alura\python-tdd\codigo</source>
> 	</sources>
> 	<packages>
> 		<package name="." line-rate="1" branch-rate="0" complexity="0">
> 			<classes>
> 				<class name="bytebank.py" filename="bytebank.py" complexity="0" line-rate="1" branch-rate="0">
> 					<methods/>
> 					<lines>
> 						<line number="1" hits="1"/>
> 						<line number="3" hits="1"/>
> 						<line number="4" hits="1"/>
> 						<line number="5" hits="1"/>
> 						<line number="6" hits="1"/>
> 						<line number="7" hits="1"/>
> 						<line number="9" hits="1"/>
> 						<line number="10" hits="1"/>
> 						<line number="11" hits="1"/>
> 						<line number="13" hits="1"/>
> 						<line number="14" hits="1"/>
> 						<line number="15" hits="1"/>
> 						<line number="17" hits="1"/>
> 						<line number="18" hits="1"/>
> 						<line number="19" hits="1"/>
> 						<line number="21" hits="1"/>
> 						<line number="22" hits="1"/>
> 						<line number="24" hits="1"/>
> 						<line number="26" hits="1"/>
> 						<line number="27" hits="1"/>
> 						<line number="28" hits="1"/>
> 						<line number="30" hits="1"/>
> 						<line number="31" hits="1"/>
> 						<line number="32" hits="1"/>
> 						<line number="33" hits="1"/>
> 						<line number="35" hits="1"/>
> 						<line number="36" hits="1"/>
> 						<line number="37" hits="1"/>
> 						<line number="39" hits="1"/>
> 						<line number="40" hits="1"/>
> 						<line number="41" hits="1"/>
> 						<line number="42" hits="1"/>
> 						<line number="43" hits="1"/>
> 					</lines>
> 				</class>
> 			</classes>
> 		</package>
> 	</packages>
> </coverage>
> ```
