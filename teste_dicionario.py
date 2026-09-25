aluno = {"nome": "ana", "nota": 8, "cel": "11989891919"}

clientes = [
    {"nome": "ana","cel": "119898891919", "empresa": "fiat"},
    {"nome": "pedro", "cel": "11977979712", "empresa": "honda"},
    {"nome": "maria", "cel": "1106695719", "empresa": "mercedes"},
    {"nome": "carlos", "cel": "119283901", "empresa": "ferrari"}
]

#pesquisa de um cliente pela empresa
empresa_digitada = input("digite o nome da empresa: ")   
for cliente in clientes:
 if cliente["empresa"] == empresa_digitada:
     print(cliente["nome"])

#cadastrar um novo cliente
     
     print("---> cadastrando um novo cliente<---")
     nome = input("digite o nome do cliente: ")
     celular = input("digite o numero de telefone: ")
     empresa = input("digite a empresa do cliente: ")

novo_cliente = {
   "nome": nome,
   "cel": celular,
   "empresa": empresa
}
clientes.append(novo_cliente)
print (clientes)

#remover cliente
print("--->remover cliente<---")
nome_cliente = input ("nome do cliente para removelo: ")
for cliente in clientes:
   if cliente["nome"] == nome_cliente:
      clientes.remove (cliente)
      break
   
print(clientes)
   #celular = input ("digite o celular do cliente para removelo")
#empresa = input( "digite a empresa do cliente para removelo")

#remover_cliente = {
 #  "nome": nome,
  # "celular": celular,
  # "empresa": empresa
#}

#clientes.pop(remover_cliente)
#print(cliente)



#for cliente in clientes:
 #   if cliente["empresa"] == "ferrari":
 #       print(cliente["nome"])


# pedir pro usuario digitar qual empresa ele quer
