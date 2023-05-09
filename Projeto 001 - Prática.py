# Senha de acesso ao sistema do caixa
senhacerta= "1234"
senha=str(input("Insira a senha: "))
while senha!= senhacerta:
    print("Senha incorreta! Tente novamente.")
    senha=str(input("Insira a senha: "))
print("Senha correta!")

# Registrar saldo inicial do caixa
saldo = -1
while saldo < 0:
    saldo=float(input("Informe o saldo inicial do caixa: "))
    if saldo < 0:
        print("Valor inválido, insira um valor maior ou igual a zero!")

# Número total de vendas realizadas
    nvendas = 0
    nprodutos = 0
    totalvendas = 0

#Iniciar nova venda
novavenda = str(input("Digite ""i"" para iniciar: " ))
if novavenda != "i":
    print("Opção indisponível, tente novamente! Fique atento aos caracteres minúsculos.")
    novavenda = str(input("Digite ""i"" para iniciar: " ))
while novavenda == "i":

    # Registrar venda
    total = 0
    somaprod=0
    while True:
        produto = ""
        while produto == "":
            produto= str(input("Digite o nome do produto: "))
            if produto == "":
                print("Esse campo é de preenchimento obrigatório")
        quantidade = -1
        while quantidade < 0:
            quantidade= int(input("Digite a quantidade: "))
            if quantidade < 0:
                print("A quantidade deve ser maior ou igual a zero!")
        valoruni = -1
        while valoruni < 0:
            valoruni= float(input("Digite o valor unitário: "))
            if valoruni < 0: 
                print("O valor unitário deve ser maior ou igual a zero!")
        total += (quantidade*valoruni)
        somaprod+=1
        continua = input("Inserir outro produto? (s/n): ")
        if continua == "n":
            print(f"Total da compra: {total}")
            break

    # Forma de pagamento, valor recebido e troco
    pagamento = 0
    while pagamento < 1 or pagamento > 4:
        pagamento = int(input("Opções:\n 1 - Dinheiro\n 2 - Pix\n 3 - Cartão\n 4 - Cancelar\n Qual a forma de pagamento? "))
        if pagamento == 1:
            dinheiro = -1
            while dinheiro < 0 or dinheiro < total:
                dinheiro = float(input("Valor recebido: "))
                if dinheiro < total:
                    print("O valor recebido é menor que o valor da venda. Por favor insira um novo valor maior ou igual o valor da venda!")
            troco = dinheiro - total
            print(f"O troco é de {troco}")
            # Calcular novo saldo do caixa
            saldo+=total
            nvendas+=1
            nprodutos+=somaprod
            totalvendas += total
        if pagamento > 4 or pagamento < 1:
            print("Forma de pagamento inválida! Tente novamente.")
        if pagamento == 2 or pagamento == 3:
            print("Pagamento registrado com sucesso!")
            nvendas+=1
            nprodutos+=somaprod
            totalvendas += total
        if pagamento == 4:
            print("Venda cancelada com sucesso!")

# Iniciar nova venda
    novavenda = str(input(f"O saldo do caixa é de ${saldo}\n Digite 'i' para iniciar uma nova venda ou 'f' para finalizar as operações do dia!\n Opção: "))
    if novavenda != "i" and novavenda != "f":
        print("Opção indisponível, tente novamente! Fique atento aos caracteres minúsculos.")
        novavenda = str(input(f"O saldo do caixa é de ${saldo}\n Digite 'i' para iniciar uma nova venda ou 'f' para finalizar as operações do dia!\n Opção: "))
    # Finalizar operações do dia
    if novavenda == "f":
        # Número total de vendas realizadas
        print(f"O número de vendas do dia foi de {nvendas}")
        # Número de itens comercializados
        print(f"O número total de itens comercializados hoje foi de {nprodutos}")
        # Valor total de vendas arrecadado
        print(f"O total arrecadado nas vendas foi de {totalvendas}")
        # Saldo final em dinheiro do caixa
        print(f"O saldo final registrado no caixa foi de {saldo}")
        break
