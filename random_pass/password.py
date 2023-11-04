import random
import time
import sys
import pyperclip
import hashlib

lower = "abcdefghijklmnopqrstuvxwyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVXWYZ"
numeros = "0123456789"
simbolos = "[]{}()*/;,\|.<>_-+"

print('''

██████╗  █████╗ ███╗   ██╗██████╗  ██████╗ ███╗   ███╗      ██████╗  █████╗ ███████╗███████╗
██╔══██╗██╔══██╗████╗  ██║██╔══██╗██╔═══██╗████╗ ████║      ██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝███████║██╔██╗ ██║██║  ██║██║   ██║██╔████╔██║█████╗██████╔╝███████║███████╗███████╗
██╔══██╗██╔══██║██║╚██╗██║██║  ██║██║   ██║██║╚██╔╝██║╚════╝██╔═══╝ ██╔══██║╚════██║╚════██║
██║  ██║██║  ██║██║ ╚████║██████╔╝╚██████╔╝██║ ╚═╝ ██║      ██║     ██║  ██║███████║███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝      ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝
                                                                                            
                                                                        [By: T0tsuK4 1.0]
''')

def barra_de_carregamento(tamanho, velocidade):
    for i in range(1, tamanho + 1):
        percentual = int((i / tamanho) * 100)
        barra = '=' * int(i * 50 / tamanho) + '>' + ' ' * (50 - int(i * 50 / tamanho))
        mensagem = f'\r[{percentual:3d}%] [{barra}]'
        sys.stdout.write(mensagem)
        sys.stdout.flush()
        time.sleep(velocidade)

def gerar_senha(tamanho, segura=True):
    tudo = lower + upper + numeros + simbolos
    if segura:
        tudo += upper + numeros + simbolos
    senha = "".join(random.choice(tudo) for _ in range(tamanho))
    barra_de_carregamento(tamanho, 0.02)
    print()
    return senha

def criptografar_senha(senha):
    sha256 = hashlib.sha256()
    sha256.update(senha.encode())
    return sha256.hexdigest()

def salvar_senha_em_arquivo(senha):
    with open("senha.txt", "w") as arquivo:
        arquivo.write(senha)
    print("Senha salva no arquivo 'senha.txt'")

def copiar_senha_para_area_de_transferencia(senha):
    pyperclip.copy(senha)
    print("Senha copiada para a área de transferência")

def main():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha (entre 8 e 36 caracteres): "))
            if 8 <= tamanho <= 36:
                break
            else:
                print("Tamanho da senha deve estar entre 8 e 36 caracteres.")
        except ValueError:
            print("Tamanho da senha deve ser um número inteiro válido")
    
    segura = input("Você deseja gerar uma senha segura? (S/n): ").lower()
    segura = segura != "n"

    print("Gerando a senha com tamanho", tamanho)

    print("Gerando a senha: ", end='', flush=True)
    senha_gerada = gerar_senha(tamanho, segura)
    print()
    print(f"Senha gerada: {senha_gerada}")

    opcao = input("O que você deseja fazer com a senha? (1 - Salvar em arquivo, 2 - Copiar para a área de transferência, 3 - Sair): ")
    
    if opcao == "1":
        salvar_senha_em_arquivo(senha_gerada)
    elif opcao == "2":
        copiar_senha_para_area_de_transferencia(senha_gerada)
    else:
        print("Programa encerrado.")

    # Criptografar a senha e exibir o hash
    senha_criptografada = criptografar_senha(senha_gerada)
    print()
    print(f"Senha criptografada (SHA-256): {senha_criptografada}")

if __name__ == "__main__":
    main()
