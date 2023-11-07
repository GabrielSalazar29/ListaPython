while True:
    print("Menu de opções:")
    print("1. Média aritmética")
    print("2. Média ponderada")
    print("3. Sair")
    
    opcao = input("Digite a opção desejada: ")
    
    if opcao == '1':
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media_aritmetica = (nota1 + nota2) / 2
        print(f"Média aritmética: {media_aritmetica:.2f}")
    elif opcao == '2':
        nota1 = float(input("Digite a primeira nota: "))
        peso1 = float(input("Digite o peso da primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        peso2 = float(input("Digite o peso da segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        peso3 = float(input("Digite o peso da terceira nota: "))
        media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
        print(f"Média ponderada: {media_ponderada:.2f}")
    elif opcao == '3':
        break
    else:
        print("Opção inválida. Por favor, digite 1, 2 ou 3.")