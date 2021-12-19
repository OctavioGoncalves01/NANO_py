nome = input("Digite um funcionario: ")
empresa = input("Digite a instituição: ")
quantidade_funcionario = int(input("Digite a quantidade de funcionarios: "))
mediaMensalidade = float(input("Digite a méda de mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", quantidade_funcionario, " funcionarios.")
print("A média da mensalidade é de: " + str(mediaMensalidade))

print('================ Verifique os tipos de dados abaixo: ==============================')
print("O tipo de dado da ariavel [nome] é: ", type(nome))
print("O tipo de dado da variavel é [empresa] é", type(empresa))
print("O tipo de dado da variavel é [quantidade_funcionarios] é", type(quantidade_funcionario))
print("O tipo de dado da variavel é [mediaMensalidade] é", type(mediaMensalidade))