from db_utils import *


commands = {'help': 0, 
            'cadastrar': 1,
            'excluir': 2,
            'alterar': 3,
            'consultar': 4,
            'adc_estoque': 5}


def input_handler(entrada: str) -> list:
    lista_input = entrada.split()
    if lista_input[0] in commands.keys():
        comando = commands[lista_input[0]]
        return int(comando), lista_input[1:]
    else:
        comando = lista_input[0]
        return comando, lista_input[1:]

def command_handler(comando, entrada: list) -> str:
    if type(comando) == type('deu ruim'):
        message = f'{comando} não é um comando, tente novamente.'
        return message
    elif comando == 0:
        message ="Os comandos válidos são: 'cadastrar', 'excluir', 'alterar', 'consultar'.\nDigite 'help <comando>' para obter ajuda sobre um comando específico."
        return message
    elif comando == 1:
        cadastrar_produto(*entrada)
        message = 'Produto cadastrado com sucesso!'
        return message
    elif comando == 2:
        pass
    elif comando == 3:
        pass
    elif comando == 4:
        pass
    elif comando == 5:
        pass



def main_loop():
    print('\n\n\nPadaria-CLI')
    print('Digite "help" para obter ajuda.')
    print("Para sair, insira 'q'.")
    while True:
        entrada = input('> ')
        if entrada == 'q':
            print('Programa finalizado.\n\n')
            break
        
        print(command_handler(*input_handler(entrada)))