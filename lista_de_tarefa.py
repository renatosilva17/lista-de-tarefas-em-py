#lista de tarefas#
#1- mostrar todas as tarefas
#2- mostrar tarefas concluidas
#3- mostrar tarefas pendentes 
#4- mostrar tarefas por prioridades 
#5- cadastrar tarefa nova 
#6- finalizar tarefa
#7- remover tarefa
#0- sair

#tarefas = ["matematica", "portugues","ciencias","progrmacao","ingles"]

tarefas = [
    {"titulo":"matematica","concluida":"nao","prioridade": "alta" },
    {"titulo":"ingles","concluida":"sim","prioridade": "baixa" },
    {"titulo":"portugues","concluida":"sim","prioridade": "baixa" },
    {"titulo":"ciencias","concluida":"nao","prioridade": "alta" },
    {"titulo":"programacao","concluida":"nao","prioridade": "alta" }
]



while True:
    print("--->Veja suas tarefas<---")
    print("1- todas as tarefas")
    print("2- tarefas concluidas")
    print("3- tarefas pendentes")
    print("4- tarefas de prioridade")
    print("5- cadastrar nova tarefa")
    print("6- finalizar tarefa")
    print("0- sair")

    opcao = input("digite um numero: ")

    if opcao == "1":
        print(tarefas)

    elif opcao == "2":
        print("--->tarefas concluidas<---")
        for tarefa in tarefas:
            if tarefa ["concluida"] == "sim":
                print (tarefa)

    elif opcao == "3":
        print("--->tarefas pendentes<---")
        for tarefa in tarefas:
            if tarefa ["concluidas"] == "nao":
                print (tarefa)