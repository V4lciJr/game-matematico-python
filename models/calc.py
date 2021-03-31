from random import randint


# Classe responsável por executar toda a lógica do jogo
class Calc:

    def __init__(self: object, dificuldade: int) -> None:
        self.__dificuldade = dificuldade  # dificuldade esolhida pelo usuário
        self.__valor1: int = self._gerar_valor  # valores gerados aleatoriament de acordo com a dificuldade escolhida
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 4)  # 1 = somar, 2 = diminuir, 3 = multiplicar, 4 = dividir
        self.__resultado: float = self._gerar_resultado  # propriedade responsável por executar as operações apresentadas

    # propriedades criadas para facilitar a manipulacao dos atributos

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str: # sobrescrita do método builtin str, para impressão do objeto do tipo Calc
        opr: str = ''
        if self.operacao == 1:
            opr = 'Somar'
        elif self.operacao == 2:
            opr = 'Diminuir'
        elif self.operacao == 3:
            opr = 'Multiplicar'
        elif self.operacao == 4:
            opr = 'Dividir'
        else:
            opr = 'Operação Desconhecida'

        return f'Valor 1: {self.valor1}\nValor 2: {self.valor2}\nDificuldade: {self.dificuldade}\nOperação: {opr}'

    @property
    def _gerar_valor(self: object) -> int: # gera valores inteiros aleatorios de acordo com a dificuldade escolhida

        if self.dificuldade == 1: # caso seja 1 valores inteiros aleatorios entre 0 e 10
            return randint(0, 10)
        elif self.dificuldade == 2: # caso seja 2 valores inteiros aleatorios entre 0 e 100
            return randint(0, 100)
        elif self.dificuldade == 3: # caso seja 3 valores inteiros aleatorios entre 0 e 1000
            return randint(0, 1000)
        elif self.dificuldade == 4: # caso seja 4 valores inteiros aleatorios entre 0 e 10000
            return randint(0, 10000)
        else:                        # caso o usuario queira dar uma de esperto e não escolher nenhuma das opcoes listadas
            return randint(0, 100000) # gera valores inteiros aleatorios entre 0 e 100000

    @property
    def _gerar_resultado(self: object) -> float:  # retorna o resultado da operacao gerada no atributo self.__operacao

        if self.operacao == 1:  # caso 1, retorne a soma dos valores 1 e 2
            return self.valor1 + self.valor2
        elif self.operacao == 2:   # caso 2, retorne a subtracao dos valores 1 e 2
            return self.valor1 - self.valor2
        elif self.operacao == 3:   # caso 3, retorne a multiplicacao dos valores 1 e 2
            return self.valor1 * self.valor2
        else:
            return self.valor1 / self.valor2  # caso contrário, retorne a divisão dos valores 1 e 2, pois o atributo
                                              # self.__operacao, gera aleatoriamente inteiros entre 1 e 4

    @property
    def _simbolo_op(self: object) -> str: # propriedade criada para facilitar a impressao da operacao a ser feito pelo usuario
                                          # e para facilitar a impressao do resultado
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        elif self.operacao == 3:
            return '*'
        else:
            return '/'

    def checar_resultado(self: object, resposta: int) -> bool:  # checa se o resultado gerado em self.resultado é igual ao informado pelo usuario
        ok: bool = False

        if self.resultado == resposta:
            print('Resposta Correta! :)')
            ok = True
        else:
            print('Resposta Errada! :(')
        print(f'{self.valor1} {self._simbolo_op} {self.valor2} = {self.resultado}')

        return ok  # retorna true caso esteja correto e false caso a resposta esteja errada.

    def mostrar_operacao(self) -> None: # mostra a operacao cuja a qual o usuario terá que responder o resultado

        print(f'{self.valor1} {self._simbolo_op} {self.valor2} = ?')


