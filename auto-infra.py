import os
import requests
import json
import socket

def verificar():
    ip_maquina = socket.gethostbyname(socket.gethostname())
    if ip_maquina.split('.')[0] == '127':
        print('-'*70)
        problem = input('Infelizmente o Script capturou o IP de "localhost". Precisa-se do seu IP da rede LAN.\n'
        'Por favor digite seu IP na rede em que se encontra > ')
        provisionamento(ip_maquina=problem)
    else:
        provisionamento(ip_maquina)

def init():
    try:
        rede = int(input('DNS será Provisionado a partir de:\n1 - WAN\n2 - LAN\n'))
        if rede == 1:
            wan_information = requests.get("https://ipinfo.io/json")
            if(wan_information.status_code == 200):
                ip_maquina = json.loads(wan_information.text)["ip"]
                provisionamento(ip_maquina)
            else:
                verificar()
        elif rede == 2:
            verificar()
        else:
            print('Opção Inválida, tente novamente.')
    except Exception as stdrr:
        print(f'Ops! Ocorreu algum erro na execução do Init\n\nEste foi o erro Capturado: {stdrr}')

def provisionamento(ip_maquina):
    try:
        octeto1 = ip_maquina.split('.')[0]
        octeto2 = ip_maquina.split('.')[1]
        octeto3 = ip_maquina.split('.')[2]
        octeto4 = ip_maquina.split('.')[3]
        print('-'*70)
        confirma = input(f'\nIP da Máquina:            {ip_maquina}\nIP Reverso:               {octeto4}.{octeto3}.{octeto2}.{octeto1}\n'
        f'Último Bloco do IP:       {octeto4}\n\nTudo Certo? [y/n]: ')
        print()
        if confirma.lower() == 'y':
            try:
                with open('./configs/dns/db.infra.code.br', 'r') as arq1:
                    conteudo = arq1.read()
                    subs = conteudo.replace('IPDIRETO', ip_maquina)
                    with open('./configs/dns/db.infra.code.br', 'w') as arq1_2:
                        arq1_2.write(subs)

                with open('./configs/dns/db.infra.code.br.reverse', 'r') as arq2:
                    conteudo2 = arq2.read()
                    subs2 = conteudo2.replace('IPFINAL', octeto4)
                    with open('./configs/dns/db.infra.code.br.reverse', 'w') as arq2_2:
                        arq2_2.write(subs2)

                with open('./configs/dns/named.conf.infra.code.br', 'r') as arq3:
                    conteudo3 = arq3.read()
                    subs3 = conteudo3.replace('IPREVERSO', f'{octeto3}.{octeto2}.{octeto1}')
                    with open('./configs/dns/named.conf.infra.code.br', 'w') as arq3_2:
                        arq3_2.write(subs3)
                os.system('cls' if os.name == 'nt' else 'clear')
                os.system('docker compose up')

            except Exception as erro_ar1:
                print(f'Ocorreu algum Erro ao Abrir os arquivos do DNS.\n\nERRO: {erro_ar1}')

        elif confirma.lower() == 'n':
            print('Não? Por favor, Reinicie os Procedimentos...\n')

        else:
            print('Opção Inválida! Confirme por favor.\n')
    except Exception as stdrr:
        print(f'Ops! Ocorreu algum erro na execução do Provisionamento\n\nEste foi o erro Capturado: {stdrr}')

init()
