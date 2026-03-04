#Você faz parte da equipe de desenvolvimento da agência espacial fictícia OrbitalTech.
#A agência é responsável por planejar, executar e monitorar missões espaciais tripuladas.

import validacoes

def cadastrar_missao(missao, d, astronautas, p, dias, orcamento):
    while True:
        #missao.append(str(input("Nome da missão: ")))
        #d.append(int(input("Informe o destino: 1 - Satélite | 2 - Lua | 3 - Marte ")))
        validacoes.validar_se_negativo(astronautas.append(int(input("Informe o número de astronautas: "))))
        #p.append(int(input("Digite a prioridade (1 - Alta | 5 - Baixa)")))
        #dias.append(int(input("Quantos dias de previsão da missão? ")))
        #orcamento.append(float(input("Orçamento liberado: ")))

        cadastro = int(input("Quer cadastrar nova missão? 0 - Sim | 1 - Não "))
        if cadastro == 1:
            break

#são informados no cadastro
nome_missao = []
destino = []
num_astronautas = []
prioridade = []
previsao_dias = []

status = [] #não precisa informar no cadastro, status já inicia em "Planejado"
combustivel = [] #será calculado

#fornecer posteriormente se o orçamento foi suficiente ou não
orcamento_liberado = []
orcamento_final = []

cadastrar_missao(nome_missao, destino, num_astronautas, prioridade, previsao_dias, orcamento_liberado)
print(nome_missao)
