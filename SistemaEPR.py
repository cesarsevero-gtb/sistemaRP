import matplotlib.pyplot as plt
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
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            print('E-mail ou senha incorreto')
    elif decisao == 2:
        print('Faça seu cadastro')
        nome = input('Digite seu nome: ')
        senha = input('Digite sua senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                usuarioExistente = 1

        if usuarioExistente == 1:
            print('Usuario já cadastrado tente um nome ou senha diferente')
        elif usuarioExistente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute('insert into cadastros (nome, senha, nivel) values (%s, %s, %s)', (nome, senha, 1))
                    conexao.commit()
                print('usuario cadastrado com sucesso')
            except:
                print('Erro ao inserir os dados no banco de dados')

    return autenticado, usuarioMaster


def cadastrarProduto():
    nome = input('Digite o nome do produto')
    ingrediente = input('Digite o nome dos ingredientes')
    grupo = input('Categoria do produto')
    preco = float(input('Digite o valor do produto'))
    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos (nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)',
                           (nome, ingrediente, grupo, preco))
            conexao.commit()
            print('Produto cadastrado com sucesso')
    except:
        print('Erro ao cadastrar produto')


def listarProduto():
    produto = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtosCadastrado = cursor.fetchall()

    except:
        print('Erro ao se conectar ao banco de dados')

    for i in produtosCadastrado:
        produto.append(i)

    if len(produto) != 0:
        for i in range(0, len(produto)):
            print(produto[i])
    else:
        print('Nenhum produto cadastrado')


def excluirProduto():
    idDeletar = int(input('Digite o ID do produtos que deseja deletar'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {}'.format(idDeletar))
    except:
        print('erro ao excluir o produto')


def listarPedidos():
    pedidos = []
    decision = 0

    while decision != 2:
        pedidos.clear()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos')
                listarPedidos = cursor.fetchall()

        except:
            print('Erro no Banco de dados')

        for i in listarPedidos:
            pedidos.append(i)

        if len(pedidos) != 0:
            for i in range(0, len(pedidos)):
                print(pedidos[i])
        else:
            print('Nenhum pedido encontrado')

        decision = int(input('Digite 1 para produto entregue ou 2 para voltar'))

        if decision == 1:
            idDeletar = int(input('Digite o id do pedido entregue'))

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                    print('Pedido dado como entregue')
            except:
                print('Erro ao deletar pedido')


def gerarEstatistica():
    nomeProdutos = []
    nomeProdutos.clear()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos')
            produtos = cursor.fetchall()

    except:
        print('Erro ao Gerar Estatisticas')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatisticaVendido')
            vendido = cursor.fetchall()
    except:
        print('Erro ao cconsultar ao banco de dados')

    estado = int(input('digite 0 para sair, 1 para pesquisar por nome; 2 para pesquisar por grupo'))

    if estado == 1:
        decisao3 = int(input('digite 1 para pesquisar por dinheiro e 2 por quantidade unitaria'))
        if decisao3 == 1:

            for i in produtos:
                nomeProdutos.append(i['nome'])
            valores = []
            valores.clear()

            for h in range(0, len(nomeProdutos)):
                somaValor = -1
                for i in vendido:
                    if i['nome'] == nomeProdutos[h]:
                        somaValor += i['preco']
                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor + 1)

            plt.plot(nomeProdutos, valores)
            plt.ylabel('Quantidade vendida em reais')
            plt.xlabel('Produtos')
            plt.show()
        if decisao3 == 2:
            grupoUnico = []
            grupoUnico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    grupo = cursor.fetchall()

            except:
                print('Erro na consulta')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from statisticaVendido')
                    vendidoGrupo = cursor.fetchall()

            except:
                print('Erro ao consultar estatisticas')

            for i in grupo:
                grupoUnico.append(i['nome'])

            grupoUnico = sorted(set(grupoUnico))

            qntFinal = []
            qntFinal.clear()

            for h in range(0, len(grupoUnico)):
                qntUnitaria = 0
                for i in vendidoGrupo:
                    if grupoUnico[h] == i['nome']:
                        qntUnitaria += 1
                qntFinal.append(qntUnitaria)

            plt.plot(grupoUnico, qntFinal)
            plt.ylabel('quantidade unitaria vendida')
            plt.xlabel('produtos')
            plt.show()

    elif estado == 2:
        decisao3 = int(input('digite 1 para pesquisar por dinheiro e 2 por quantidade unitaria'))
        if decisao3 == 1:

            for i in produtos:
                nomeProdutos.append(i['grupo'])
            valores = []
            valores.clear()

            for h in range(0, len(nomeProdutos)):
                somaValor = -1
                for i in vendido:
                    if i['grupo'] == nomeProdutos[h]:
                        somaValor += i['preco']
                if somaValor == -1:
                    valores.append(0)
                elif somaValor > 0:
                    valores.append(somaValor + 1)

            plt.plot(nomeProdutos, valores)
            plt.ylabel('Quantidade vendida em reais')
            plt.xlabel('Produtos')
            plt.show()

        if decisao3 == 2:
            grupoUnico = []
            grupoUnico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos')
                    grupo = cursor.fetchall()

            except:
                print('Erro na consulta')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from statisticaVendido')
                    vendidoGrupo = cursor.fetchall()

            except:
                print('Erro ao consultar estatisticas')

            for i in grupo:
                grupoUnico.append(i['grupo'])

            grupoUnico = sorted(set(grupoUnico))

            qntFinal = []
            qntFinal.clear()

            for h in range(0, len(grupoUnico)):
                qntUnitaria = 0
                for i in vendidoGrupo:
                    if grupoUnico[h] == i['grupo']:
                        qntUnitaria += 1
                qntFinal.append(qntUnitaria)

            plt.plot(grupoUnico, qntFinal)
            plt.ylabel('quantidade unitaria vendida')
            plt.xlabel('produtos')
            plt.show()


while not autentico:
    decisao = int(input('digite 1 para logar e 2 para se cadastrar'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()


    except:
        print('erro ao se conectar ao banco de dados')

    autentico, usuarioSupremo = logarCadastrar()

if autentico:
    print('autenticado')

    if usuarioSupremo == True:
        decisaoUsuario = 1

        while decisaoUsuario != 0:
            decisaoUsuario = int(input(
                'Digite 0 para sair e 1 para dadastrar produto, 2 para ver produtos cadastrado, 3 para listar pedidos e 4 para visualizar as estatísticas'))

            if decisaoUsuario == 1:
                cadastrarProduto()
            elif decisaoUsuario == 2:
                listarProduto()

                delete = int(input('digite 1 para deletar ou 2 para sair'))

                if delete == 1:
                    excluirProduto()
            elif decisaoUsuario == 3:
                listarPedidos()
            elif decisaoUsuario == 4:
                gerarEstatistica()


    elif usuarioSupremo == False:
        decisaoMembro = 1

        while decisaoMembro != 0:
            decisaoMembro = int(input('Digite 0 para sair ou digite 1 para ver produtos listado'))

            if decisaoMembro == 1:
                listarProduto()
