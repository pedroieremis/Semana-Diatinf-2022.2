import os, socket

def init():
    try:
        ip_maquina = socket.gethostbyname(socket.gethostname())
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
            print('Opção Inválida! Preciso de sua Confirmação.\n')
    except Exception as stdrr:
        print(f'Ops! Ocorreu algum erro na execução do Programa!\n\nEste foi o erro Capturado: {stdrr}')

init()