
import os
import subprocess
import time

print('_____   ___    __  ____     ___ ______      ___ ___    ___  ____   __ __')
print('/ ___/  /  _]  /  ]|    \   /  _]      |    |   |   |  /  _]|    \ |  |  |')
print('   \_  /  [_  /  / |  D  ) /  [_|      |    | _   _ | /  [_ |  _  ||  |  |')
print('\__  ||    _]/  /  |    / |    _]_|  |_|    |  \_/  ||    _]|  |  ||  |  |')
print('/  \ ||   [_/   \_ |    \ |   [_  |  |      |   |   ||   [_ |  |  ||  :  |')
print('\    ||     \     ||  .  \|     | |  |      |   |   ||     ||  |  ||     |')
print(' \___||_____|\____||__|\_||_____| |__|      |___|___||_____||__|__| \__,_|')

print('SCRIPT CREATED BY IG')
print('DISCORD SECRET: https://discord.gg/ybDH9ppK7c ')
time.sleep(2)

print('1- BYPASS LOGS JOURNAL TRACE')
print('2- LIMPAR TODAS AS LOGS')
print('3- LIMPAR CACHE)')
print('4- REMOVER ARQUIVO (SELECIONE O ARQUIVO QUE DESEJA REMOVER EX: C:/Users/ig/Downloads/arq/arq)')
print('5- CREDITOS')
print('FODASE A ANTXITER KKKKKKKKKKKKK')

escolha = int(input('Selecione a opçao que voce deseja: '))

if escolha == 1:
    subprocess.run(['fsutil', 'usn', 'deleteJournal', '/d', 'c:'])
    subprocess.run(['timeout', '/t', '0'])
    subprocess.run(['fsutil', 'usn', 'createJournal', 'c:'])
    subprocess.run(['timeout', '/t', '0'])
    subprocess.run(['fsutil', 'usn', 'enablerangetracking', 'c:'])
    subprocess.run(['timeout', '/t', '0'])
    print('JournalTrace Limpo!')

elif escolha == 2:
    subprocess.run(["cmd", "cd/", "/c", "del", "*.log", "/a", "/s", "/q", "/f"])
    print('Logs Limpas!')

elif escolha == 3:
    subprocess.run(['cmd', '/c', 'deltree', '/y', 'c:\\windows\\tmp'])
    subprocess.run(['cmd', '/c', 'deltree', '/y', 'c:\\windows\\ff*.tmp'])
    subprocess.run(['cmd', '/c', 'deltree', '/y', 'c:\\windows\\history'])
    subprocess.run(['cmd', '/c', 'deltree', '/y', 'c:\\windows\\cookies'])
    subprocess.run(['cmd', '/c', 'deltree', '/y', 'c:\\windows\\recent'])
    subprocess.run(
        ['cmd', '/c', 'deltree', '/y', 'c:\\windows\\spool\\printers'])
    subprocess.run(['cmd', '/c', 'del', 'c:\\WIN386.SWP'])

elif escolha == 4:
    ose = str(input('Informe o diretorio do arquivo que deseja deletar!'))
    os.remove(ose)

elif escolha == 5:
    print('DESENVOLVIDO DO 0 POR IG')
    time.sleep(10)
else:
    print('OPÇAO INCORRETA')