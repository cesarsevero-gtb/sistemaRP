
import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor

)

autentico = False

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha ['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True

            else:
                autenticado = False

while not autentico:
    decisao = int(input('digite 1 para logar e 2 para se cadastrar'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()
            print(resultado)

    except:
      print('erro ao se conectar ao banco de dados')