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

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        # Given
        entrada = ' Lucas Carvalho '
        esperado = 'Carvalho'
        lucas = Funcionario(entrada, '11/11/2000', 1111)

        # When
        resultado = lucas.sobrenome()

        # Then
        assert resultado == esperado

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

    def test_quando_calcular_bonus_recebe_1000_deve_retorna_100(self):
        # Given
        entrada  = 1000
        esperado =  100

        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)

        # When
        resultado = funcionario_teste.calcular_bonus()

        # Then
        assert resultado == esperado
