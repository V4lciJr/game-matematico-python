from models.calc import Calc


def main() -> None:  # função principal onde começa o jogo
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 e 4]: '))

    calc: Calc = Calc(dificuldade)  # instancia um objeto Calc de acordo com a dificuldade escolhida pelo usuário

    print('Informe o resultado, para a seguinte operação: ')
    calc.mostrar_operacao()  # mostra a operaçao a ser feita

    resultado: int = int(input())  # recebe a respota da usuario

    if calc.checar_resultado(resultado):  # checa se a resposta esta correta e imprime o resultado e seus respectivos pontos
        pontos += 1  # increment a variavel pontos caso a resposta esteja correta
        print(f'Você tem {pontos} ponto(s).')

    continuar: int = int(input('Deseja continuar no jogo [1 - sim, 0 - não] ?'))

    if continuar:
        jogar(pontos)  # chamada recursiva da funcao, dessa forma não precisamos usar loops
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até mais!!!')


if __name__ == '__main__':
    main()
