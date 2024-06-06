from teoremamestre import Teorema

if __name__ == '__main__':
    teorema_instance = Teorema()
    while True:
        print()
        print("________________________________________________________________________________")
        print("Digite a expressão que deseja analisar ou 'sair' para encerrar o programa.")
        print("T(n) = aT(n /b)+f(n). O f(n) será estabelecido da seguinte forma: n^k log^p n")
        
        expression = input()
        if expression == 'sair':
            break 
        else:
            teorema_instance.metodo_mestre(expression)
        
