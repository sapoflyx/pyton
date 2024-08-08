# Variáveis
senhas_gravadas = []
candidato = 22
votos = 0

# Escolher a senha
def registrar_senha():
    while True:
        senha = int(input("Escolha a sua senha! (Máx 5 números): "))
        confirm_senha = int(input("Confirme a sua senha: "))

        if senha > 99999:
            print("A sua senha deve conter no máximo 5 dígitos.")
        elif senha != confirm_senha:
            print("As senhas não são iguais!")
        else:
            print("Senha gravada.")
            senhas_gravadas.append(senha)
            break  

# Tentativa de senha
def tentar_acesso():
    while True:
        senha_dig = int(input("Digite a sua senha: "))

        if senha_dig not in senhas_gravadas:
            print("A senha está incorreta!")
        elif senha_dig > 99999:
            print("A tentativa deve conter no máximo 5 dígitos.")
        else:
            print("Acesso aceito!")
            break  

# Votar
def votar():
    global votos
    while True:
        voto = int(input("Escolha algum candidato: "))

        if voto > 99 or voto < 10:
            print("Só é aceito números de 2 dígitos.")
        elif voto != candidato:
            print("Não há candidatos com esse número.")
        else:
            votos += 1
            print("Voto computado!")
            print(f"O candidato contém a seguinte quantidade de votos: {votos}")
        break

# Executar 
registrar_senha()
tentar_acesso()
print("Lista de senhas gravadas:", senhas_gravadas)
votar()
