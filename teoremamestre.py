import math
import re

class Teorema:

    @staticmethod
    def removeSpaces(expressionVect):
        expressionVect = [char for char in expressionVect if char != ' ']
        return expressionVect

    @staticmethod
    def metodo_mestre(expression):
        expression = expression.upper()
        print(expression)
        expressionVect = expression.split("=")

        rightVect = list(expressionVect[1])
        rightVect = Teorema.removeSpaces(rightVect)
        print(rightVect)

        half = ''.join(rightVect)

        

    
        if any(char in expression for char in ['-']):
            print("Não é possível utilizar o método mestre, pois '-' está presente na expressão.")
            return

        # A--------------------------------------------
        index_t = half.find('T')
        if index_t != -1:
            term_before_t = half[:index_t].strip()
            term_before_t = re.sub(r'\(.*?\)', '', term_before_t)
            print(f"O termo antes de (T) é: {term_before_t}")
            try:
                A = float(term_before_t)
                print(f"A é: {A}")
            except ValueError:
                A = float(1)
        else:
            print("Não foi possível encontrar o termo antes de (T) na expressão.")

        # B d--------------------------------------------
        index_n = half.find('N')

        if index_n != -1:
            term_before_n = ""
            i = index_n - 1

            while i >= 0 and (half[i].isdigit() or half[i] == '.'):
                term_before_n = half[i] + term_before_n
                i -= 1

            if term_before_n:
                AntesDoPrimeiroN = float(term_before_n)
                print(f"O termo antes do primeiro (N) é: {AntesDoPrimeiroN}")
            else:
                print("Nenhum número encontrado antes do primeiro (N).")
                AntesDoPrimeiroN = 1
        else:
            print("Não foi possível encontrar o termo antes do primeiro (N) na expressão.")

        # B Normal --------------------------------------------
        index_bar = half.find('/')
        index_close_parenthesis = half.find(')')

        if index_bar != -1 and index_close_parenthesis != -1:
            term_after_bar = half[index_bar + 1: index_close_parenthesis].strip()
            print(f"O termo depois de (/) é: {term_after_bar}")
            term_after_bar = term_after_bar.strip(')')
            try:
                B = float(term_after_bar)
                B = B / AntesDoPrimeiroN
                print(f"B: {B}")
            except ValueError:
                print("O termo depois de (/) não é um número válido.")
        else:
            print("Não foi possível encontrar o termo depois de (/) na expressão.")




    # K---------------------------------------------------
        index_caret = half.find('^')
        index_log1 = half.find('LOG')
        if index_caret != -1 and half[index_caret - 1] == 'N':
            if index_log1 != -1:
                term_after_caret = half[index_caret + 1: index_log1].strip()
            else:
                term_after_caret = half[index_caret + 1:].strip()

            try:
                k = float(term_after_caret)
                print(f"k encontrado: {k}")
            except ValueError:
                print("O termo após '^' não é um número válido.")
        else:
            index_plus = half.find('+')
            if index_log1 != -1:
                if index_caret == -1 and half[index_plus+1:index_log1] == 'N':
                    k = float(1)
                else:
                    k = float(0)
            else:
                if index_caret == -1 and half[index_plus+1:] == 'N':
                    k = float(1)
                else:
                    k = float(0)

        # Sétimo passo - Verificar a presença do caractere 'log'
        index_log = half.find('LOG')
        if index_log != -1:
            term_after_log = half[index_log + 3:].strip()
            term_after_log = term_after_log.strip('N')

            index_caret = term_after_log.find('^')
            if index_caret != -1:
                term_after_log = term_after_log[1:].strip()
                try:
                    p = float(term_after_log)
                    print(f"p encontrado: {p}")
                except ValueError:
                    print("O termo após 'log^' não é um número válido.")
                half = half.replace(f'LOG^{term_after_log}', '')  # Remove 'log^p' da expressão
            else:
                p = float(1)  # Se '^' não for encontrado, define p como 1
                print("Nenhuma ocorrência de 'log^p' encontrada na expressão.")
        else:
            p = 0  # Se 'log' não for encontrado, define p como 0
            print("Nenhuma ocorrência de 'log' encontrada na expressão.")

        # Oitavo passo - Verificar se 'a' >= 1 e 'b' > 1
        if A < 1:
            print("Não é possível utilizar o método mestre, pois 'a' é menor que 1.")
            return
        elif B <= 1:
            print("Não é possível utilizar o método mestre, pois 'b' é menor ou igual a 1.")
            return
        else:
            print("É possível utilizar o método mestre")

        # Nono passo - Imprimir os valores obtidos
        print(f"a = {A}")
        print(f"b = {B}")
        print(f"f(n) = n^{k} log^{p} n")
        print(f"k = {k}")
        print(f"p = {p}")

        # Décimo passo - Calcular o logaritmo utilizando math.log()
        result_log = math.log(A, B)

        # Décimo primeiro passo - Identificar em qual caso está
        if result_log > k:
            print(f"Está no Caso 1: T(n) = Theta(n^{result_log})")
        elif result_log == k:
            if p > -1:
                print(f"Está no Caso 2 e p > -1: T(n) = Theta(n^{k} log^{p + 1} n)")
            elif p == -1:
                print(f"Está no Caso 2 e p = -1: T(n) = Theta(n^{k} log log n)")
            else:
                print(f"Está no Caso 2 e p < -1: T(n) = Theta(n^{k})")
        elif k > result_log:
            if p >= 0:
                print(f"Está no Caso 3 e p >= 0 : T(n) = Theta(n^{k} log^{p} n)")
            else:
                print(f"Está no Caso 3 e p < 0 : T(n) = Theta(n^{k})")

        


  



