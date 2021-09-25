class usuario:
    nome: None
    sobrenome: None
    genero: None
    sentenca: None
    cpf: None
    senha: None
    email: None
    divida: None
    compras: None
    limite_credito: None
class produto:
    codigo: None
    nome: None
    preco: None
#cadastro usuario

def menu_inicial ():
    print()
    print("   ___     ___    ___     ___    _____    _____    ___   _")
    print("  / _ \   |   \  /   |   / _ \   |_  /   /  __ \  |   \ | |    __   __")
    print(" / /_\ \  | |\ \/ /| |  / /_\ \   / /_  |  |_|  | | |\ \| |   / /  / /")
    print("/_/   \_\ |_| \__/ |_| /_/   \_\ /____|  \_____/  |_| \___|  | |  | |")
    print("                                                              \_\  \_\ ")
    per_cadatro=int(input("Você já possui cadastro?\n1-Sim\n2-Criar Agora\n→"))
    while True:
        if per_cadatro==1:
            login()
            break
        if per_cadatro==2:
            cadastroUser()
            break

def login():
    while True:
        print("Se deseja voltar preencha com apenas 0")
        mensage_erro = "Os dados não conferem ou são inválidos!"
        ok=0
        inp_email=str(input("Insira seu e-mail: "))
        if inp_email=="0":
            menu_inicial()
        inp_senha=str(input("Insira a senha: "))
        if inp_senha=="0":
            menu_inicial()
        with open("userData.txt", "r") as check_info:
            for line in check_info:#readline qundo usado 2 veses ele divide ex:frase:algo readline(3)=alg readline(1)=o
                atual_line=check_info.readline(3)#le so um pouco por linha para filtrar e ficar leve
                if atual_line=="ema":
                    resto_email=check_info.readline(3)#serve para 2 coisas: deixar so email em si e verificar se e' email:
                    if resto_email=="il:":
                        email_inteiro=list(check_info.readline())
                        email_inteiro.pop(-1)
                        email_pronto="".join(email_inteiro)#transforma em lista, remove quebra de linha e junta novamente
                        if inp_email==email_pronto:
                            ok+=1
                            incio_senha=check_info.readline(6)
                            if incio_senha=="senha:":
                                senha_inteira=list(check_info.readline())
                                senha_inteira.pop(-1)# transforma em lista, remove quebra de linha e junta novamente
                                senha_pronta="".join(senha_inteira)
                                if inp_senha==senha_pronta:
                                    ok+=1
                                    # carrega dados
                                    usuario.senha=senha_pronta #carreguei a senha
                                    usuario.email=email_pronto #carreguei o email

                                    linha_nome=check_info.readline(5)
                                    if linha_nome=="nome:":
                                        nome_bruto=list(check_info.readline())
                                        nome_bruto.pop(-1)
                                        nome_pronto="".join(nome_bruto)
                                        usuario.nome=nome_pronto #carreguei o nome

                                    linha_sobrenome=check_info.readline(10)
                                    if linha_sobrenome=="sobrenome:":
                                        sobrenome_bruto=list(check_info.readline())
                                        sobrenome_bruto.pop(-1)
                                        sobrenome_pronto="".join(sobrenome_bruto)
                                        usuario.sobrenome=sobrenome_pronto #carreguei o sobrenome

                                    linha_genero=check_info.readline(7)
                                    if linha_genero=="genero:":
                                        genero_bruto=list(check_info.readline())
                                        genero_bruto.pop(-1)
                                        genero_pronto="".join(genero_bruto)
                                        usuario.genero=genero_pronto #carreguei o genero
                                        if genero_pronto == "Masculino":
                                            user_sentenca = "o"
                                        elif genero_pronto == "Femenino":
                                            user_sentenca = "a"
                                        elif genero_pronto == "Outros":
                                            user_sentenca = "o(a)"
                                        usuario.sentenca=user_sentenca #carreguei a senteca. E' como chamarei o user

                                    linha_cpf=check_info.readline(4)
                                    if linha_cpf=="cpf:":
                                        cpf_bruto=list(check_info.readline())
                                        cpf_bruto.pop(-1)
                                        cpf_pronto="".join(cpf_bruto)
                                        usuario.cpf=cpf_pronto #carreguei o cpf

                                    linha_limite=check_info.readline(18)
                                    if linha_limite=="limite de credito:":
                                        limite_bruto=list(check_info.readline())
                                        limite_bruto.pop(-1)
                                        limite_pronto="".join(limite_bruto)
                                        limite_pronto=float(limite_pronto)
                                        usuario.limite_credito=limite_pronto #carreguei o limite

                                    linha_divida=check_info.readline(7)
                                    if linha_divida=="divida:":
                                        divida_bruta=list(check_info.readline())
                                        divida_bruta.pop(-1)
                                        formula=[]
                                        numero=[]
                                        i=0
                                        while True:
                                            i+=1
                                            if i==len(divida_bruta):
                                                break
                                            if divida_bruta[i]=="-" or divida_bruta[i]=="+":
                                                numero_junto="".join(numero)
                                                numero_numero=float(numero_junto)
                                                if divida_bruta[i] == "-":
                                                    numero_numero*=-1
                                                elif divida_bruta[i]=="+":
                                                    numero_numero*=+1
                                                formula.append(numero_numero)
                                                numero = []
                                            if divida_bruta[i]=="." or divida_bruta[i]=="0" or divida_bruta[i]=="1" or divida_bruta[i]=="2" or divida_bruta[i]=="3" or divida_bruta[i]=="4" or divida_bruta[i]=="5" or divida_bruta[i]=="6" or divida_bruta[i]=="7" or divida_bruta[i]=="8" or divida_bruta[i]=="9":
                                                numero.append(divida_bruta[i])
                                        divida_pronta=sum(formula)
                                        usuario.divida=divida_pronta

                                    linha_compras=check_info.readline(8)
                                    if linha_compras=="Compras:":
                                        compra_bruta = list(check_info.readline())
                                        compra_bruta.pop(-1)
                                        if compra_bruta!="":#formula para calcular valor do carrinho
                                            list_saldo=[]
                                            numero=0
                                            for i in range(len(compra_bruta)):
                                                if i==len(compra_bruta):
                                                    continue
                                                if compra_bruta[i]=="-" and numero==0:
                                                    list_saldo.append(",")
                                                    numero-=1
                                                if compra_bruta[i]=="=":
                                                    numero+=1
                                                elif numero==0:
                                                    list_saldo.append(compra_bruta[i])
                                            lista_valor = []
                                            lista_valores=[]
                                            if len(list_saldo)!=0:
                                                list_saldo.pop(0)
                                            for n in range(len(list_saldo)):
                                                if n == len(list_saldo):
                                                    continue
                                                if list_saldo[n]==",":
                                                    valor="".join(lista_valor)
                                                    valor_fl=float(valor)
                                                    lista_valores.append(valor_fl)
                                                    lista_valor=[]
                                                else:
                                                    lista_valor.append(list_saldo[n])
                                            valor="".join(lista_valor)
                                            if valor=="":
                                                valor_fl = float(0.0)
                                            else:
                                                valor_fl = float(valor)
                                            lista_valores.append(valor_fl)
                                        usuario.compras = sum(lista_valores)

                                    menu_do_usuario(usuario.sentenca, usuario.nome)
                                    break
            if ok != 2:
                print(mensage_erro)
        continue#quando a senha errada ele fecha o check_ifo e le tudo novamente

def cadastroUser():
    usuario.nome,*sobren = map(str, input("Insira seu nome completo: ").split())
    usuario.sobrenome = " ".join(sobren)
    while True:
        genero_inp=int(input("Qual o seu genero?\n1-Masculino\n2-Femenino\n3-Outros\n→"))
        if genero_inp==1 or genero_inp==2 or genero_inp==3:
            if genero_inp==1:
                usuario.sentenca="o"
                usuario.genero="Masculino"
            elif genero_inp==2:
                usuario.sentenca="a"
                usuario.genero="Femenino"
            elif genero_inp==3:
                usuario.sentenca="o(a)"
                usuario.genero="Outros"
            break
    # CPF
    while True:
        mensagem_erro_cpf = "O CPF não é válido!"
        cpf = list(input("Insira seu cpf:\nExemplo:XXX.XXX.XXX-XX\n→"))
        for posicao in range(len(cpf)):  # retira todos os . ou - se tiver na entrada
            if len(cpf) == posicao:
                break
            if cpf[posicao] == "." or cpf[posicao] == "-" or cpf[posicao]==",":
                cpf.pop(posicao)

        for contagem in range(len(cpf)):  # os valores sao como str aqui sao convertidos em int para as formulas de validacao
            cpf[contagem] = int(cpf[contagem])
        if len(cpf) != 11:  # verifica se foi digitado a mais ou a menos
            print(mensagem_erro_cpf)
            continue
        else:
            # os cpf que passam na formula porem nao existem eles sao: 111.111.111-11 ou 222.222.222-22
            if cpf[0] == cpf[1] and cpf[1] == cpf[2] and cpf[2] == cpf[3] and cpf[3] == cpf[4] and cpf[4] == cpf[5] and cpf[5] == cpf[6] and cpf[6] == cpf[7] and cpf[7] == cpf[8] and cpf[8] == cpf[9] and cpf[9] == cpf[10]:
                print(mensagem_erro_cpf)
            else:
                # verifica se o resto da conta1 resuta em um numero igual o primeiro digito depois do traco
                conta1 = cpf[0] * 10 + cpf[1] * 9 + cpf[2] * 8 + cpf[3] * 7 + cpf[4] * 6 + cpf[5] * 5 + cpf[6] * 4 + cpf[7] * 3 + cpf[8] * 2
                conta2 = (conta1 * 10) % 11
                if conta2 == 10:
                    conta2 = 0
                primeiro_digito_final = conta2
                # como o primeiro numero depois do traco esta na penultima posicao usei o [-2]
                if primeiro_digito_final != cpf[-2]:
                    print(mensagem_erro_cpf)
                else:
                    # verifica o segundo digito
                    conta1 = cpf[0] * 11 + cpf[1] * 10 + cpf[2] * 9 + cpf[3] * 8 + cpf[4] * 7 + cpf[5] * 6 + cpf[6] * 5 + cpf[7] * 4 + cpf[8] * 3 + cpf[9] * 2
                    conta2 = (conta1 * 10) % 11
                    if conta2 == 10:
                        conta2 = 0
                    segundo_digito_final = conta2
                    if segundo_digito_final != cpf[-1]:
                        print(mensagem_erro_cpf)
                    else:
                        break
    usuario.cpf = cpf
    #SENHA
    while True:
        senha = list(input("Insira uma senha: "))# separa as letras para contagem, em melhoria seria possivel verificar a complexidade dela
        if len(senha) > 5:
            senha_inteira = "".join(senha)#juntar novamente as letras
            senha_cofirma = str(input("Confirme sua senha: "))
            if senha_cofirma == senha_inteira:
                break
            else:
                print("As senhas não coincidem!")
        else:
            print("A senha deve conter no mínimo 6 caracteres")
    usuario.senha = senha_inteira

    # E-MAIL
    #verificar se tem e-mail igual
    while True:
        t_email=list(input("Insira seu email "))
        qtd=0
        for i in range(len(t_email)):
            if t_email[i]=="@":
                qtd+=1
        if qtd==1:
            email_fin = "".join(t_email)
            break
        else:
            print("E-mail invalido!")
    usuario.email = email_fin
    #limite de credito
    while True:
        limite = float(input("Insira o limite de crédito desejado para sua conta (valor máximo 1000 reais):"))
        if limite>1000:
            print("O limite máximo são R$ 1000!")
        else:
            break
    usuario.limite_credito=limite
    usuario.compras=0
    usuario.divida=0
    adicao_user(usuario.nome,usuario.sobrenome,usuario.genero,usuario.cpf,usuario.email,usuario.senha,usuario.limite_credito)
    menu_do_usuario(usuario.sentenca, usuario.nome)
#ler mais casas
def adicao_user(nome,sobrenome,genero,cpf,email,senha,limite_credito):
    codigo_cliente:None
    with open("userData.txt","r") as ler_cod_cliente:
        primeiro_carater=ler_cod_cliente.readline(1)
        if primeiro_carater=="":
            codigo_cliente=1
        else:
            for line in ler_cod_cliente:
                if primeiro_carater=="1" or primeiro_carater=="2" or primeiro_carater=="3" or primeiro_carater=="4" or primeiro_carater=="5" or primeiro_carater=="6" or primeiro_carater=="7" or primeiro_carater=="8" or primeiro_carater=="9" or primeiro_carater==1 or primeiro_carater==2 or primeiro_carater==3 or primeiro_carater==4 or primeiro_carater==5 or primeiro_carater==6 or primeiro_carater==7 or primeiro_carater==8 or primeiro_carater==9:
                    numero = int(primeiro_carater)
            codigo_cliente=numero+1
    texto_de_cadastro=f"{codigo_cliente}\nemail:{email}\nsenha:{senha}\nnome:{nome}\nsobrenome:{sobrenome}\ngenero:{genero}\ncpf:{cpf}\nlimite de credito:{limite_credito}\ndivida:0\nCompras:\n---------------------------------------------------------------------------\n"
    with open("userData.txt", "a") as adiciona_arquivo:#havia colocado como: adiciona_arquivo = open("userData.txt","a"), mas descobri que com with ele da .close() sozinho
        adiciona_arquivo.write(texto_de_cadastro)


def menu_do_usuario(genero,nome):
    print(f"Seja bem vind{genero} {nome}!")
    numero=10
    while numero!=2 and numero!=3 and numero!=4 and numero!=0:
        print("2-Produtos")
        print("3-Meu carrinho")
        print("4-Pagar fatura")
        print("0-Sair")
        numero=int(input("→"))
        if numero == 2:
            comprar()
        elif numero == 3:
            carrinho()
        elif numero == 4:
            fatura()
        elif numero == 0:
            exit()

def comprar():
    with open("productData.txt","r") as lista_produtos:
        line_int=lista_produtos.readlines()
        line_str="".join(line_int)
        print(line_str)
    inp_compra=int(input("Deseja comprar algo?\n1-Sim\n0-Voltar\n→"))
    if inp_compra == 0:
        menu_do_usuario(usuario.sentenca,usuario.nome)
    elif inp_compra == 1:
        while True:
            print("Para voltar digite 0")
            id=str(input("Qual o ID do produto?"))
            if id=="0":
                menu_do_usuario(usuario.sentenca,usuario.nome)
            else:
                id_pronto="ID:"+id+"\n"#deixei igual o txt
            qtd=int(input("Qual a quantidade?"))
            if qtd=="0":
                menu_do_usuario(usuario.sentenca,usuario.nome)
            with open("productData.txt","r") as busca_id:
                for line in busca_id:
                    if line==id_pronto:#comparei pra ele procura ate achar igual
                        produto.codigo=id

                        product_nome=busca_id.readline(16)
                        if product_nome=="Nome do produto:":
                            nome_list=list(busca_id.readline())
                            nome_list.pop(-1)
                            nome_prod_ok="".join(nome_list)
                            produto.nome=nome_prod_ok
                            valor=busca_id.readline(9)
                            if valor=="Valor: R$":
                                preco_list = list(busca_id.readline())
                                preco_list.pop(-1)
                                preco_prod_ok = "".join(preco_list)
                                preco_prod_ok= float(preco_prod_ok)
                                produto.preco = preco_prod_ok


                                valor_tt=produto.preco*qtd
                                if usuario.compras+usuario.divida+valor_tt>usuario.limite_credito:
                                    print("O limite foi atingido. Para comprar mais emita/pague sua fatura")
                                    continue
                                add_carrinho(qtd)
                                usuario.compras+=valor_tt
                                print("Adicionado✔")
                            pos_compra=int(input("Adicionar mais itens ao carrinho?\n1-Sim\n2-Emitir fatura\n0-Voltar ao menu\n→"))
                            if pos_compra == 1:
                                continue
                            if pos_compra == 2:
                                add_fatura(valor_tt)
                            if pos_compra == 0:
                                menu_do_usuario(usuario.genero,usuario.nome)
def add_carrinho(qtd):
    texto_compra=f"---id:{produto.codigo} X {qtd}={produto.preco*qtd}\n"
    with open("userData.txt","r") as dados_user:
        email="email:"+usuario.email+"\n"
        tudo_antes=[]
        for line_atual in dados_user:
            tudo_antes.append(line_atual)
            if line_atual==email:
                ler1=dados_user.readline()
                tudo_antes.append(ler1)
                ler2 = dados_user.readline()
                tudo_antes.append(ler2)
                ler3 = dados_user.readline()
                tudo_antes.append(ler3)
                ler4 = dados_user.readline()
                tudo_antes.append(ler4)
                ler5 = dados_user.readline()
                tudo_antes.append(ler5)
                ler6 = dados_user.readline()
                tudo_antes.append(ler6)
                ler7 = dados_user.readline()
                tudo_antes.append(ler7)
                ler8=dados_user.readline(8)
                tudo_antes.append(ler8)
                if ler8=="Compras:":
                    linha_dado=list(dados_user.readline())
                    linha_dado.pop(-1)
                    linha_ok="".join(linha_dado)
                    tudo_antes.append(linha_ok)
                    tudo_antes.append(texto_compra)
    with open("userData.txt","w") as escrevendo_novamente:
        nada_aqui="".join(tudo_antes)
        escrevendo_novamente.write(nada_aqui)

def carrinho():
    emailuser="email:"+usuario.email+"\n"
    print("Este é seu carrinho:")
    with open("userData.txt", "r") as compras:
        for line in compras:
            if line==emailuser:
                l1=compras.readline()
                l2=compras.readline()
                l3=compras.readline()
                l4=compras.readline()
                l5=compras.readline()
                l6=compras.readline()
                l7=compras.readline()
                compra=compras.readline(8)
                if compra=="Compras:":
                    linha=compras.readline(3)
                    if linha=="\n--":
                        print("Você não tem nada adicionado ao carrinho!")
                        menu_do_usuario(usuario.sentenca,usuario.nome)
                    elif linha=="---":
                        lista_valores = []
                        while True:
                            numero_id=[]
                            while True:
                                id = str(compras.readline(1))
                                if id=="X":
                                    break
                                elif id=="0" or id=="1" or id=="2" or id=="3" or id=="4" or id=="5" or id=="6" or id=="7" or id=="8" or id=="9":
                                    numero_id.append(id)
                            codigo_p="".join(numero_id)
                            numero_qtd=[]
                            while True:
                                qtd = str(compras.readline(1))
                                if qtd!="=":
                                    numero_qtd.append(qtd)
                                else:
                                    break
                            numero_qtd.pop(0)
                            qtd="".join(numero_qtd)
                            valor_total=[]
                            while True:
                                valor = str(compras.readline(1))
                                if valor!="-":
                                    valor_total.append(valor)
                                else:
                                    break
                            terminou=0
                            if valor_total[-1]=="\n":
                                valor_total.pop(-1)
                                terminou=1
                            valor_tt=float("".join(valor_total))
                            lista_valores.append(valor_tt)

                            id_no_cadastro=f"ID:{codigo_p}\n"
                            with open("productData.txt","r") as busca_produto:
                                for line in busca_produto:
                                    if id_no_cadastro==line:
                                        nome = busca_produto.readline()
                                        print(f"{nome}Quantidade:{qtd}\nValor Total:{valor_tt}\n")
                            id_n = compras.readline(1)
                            usuario.compras+=valor_tt
                            if terminou==1:
                                valor_total_carrinho = 0
                                for contagem in range(len(lista_valores)):
                                    valor_total_carrinho+=lista_valores[contagem]
                                inp_fatura=int(input(f"O valor total do carrinho é : {valor_total_carrinho}\nVocê deseja emitir a fatura?\n1-Sim\n0-Voltar ao menu\n→"))
                                if inp_fatura==0:
                                    menu_do_usuario(usuario.sentenca,usuario.nome)
                                if inp_fatura==1:
                                    add_fatura(valor_total_carrinho)
                                    menu_do_usuario(usuario.sentenca, usuario.nome)
                                break

def add_fatura(valor):
    usuario.divida+=valor
    emailuser="email:"+usuario.email+"\n"
    with open("userData.txt", "r") as divida:
        todo_o_txt=[]
        for line in divida:
            todo_o_txt.append(line)
            if line==emailuser:
                l1 = divida.readline()
                todo_o_txt.append(l1)
                l2 = divida.readline()
                todo_o_txt.append(l2)
                l3 = divida.readline()
                todo_o_txt.append(l3)
                l4 = divida.readline()
                todo_o_txt.append(l4)
                l5 = divida.readline()
                todo_o_txt.append(l5)
                l6 = divida.readline()
                todo_o_txt.append(l6)
                linha_divida=divida.readline(7)
                todo_o_txt.append(linha_divida)
                if linha_divida=="divida:":
                    valores=list(divida.readline())
                    valores.pop(-1)
                    valor_str=str(valor)
                    valores.append(str(valor_str+"+"+"\n"))
                    ok="".join(valores)
                    todo_o_txt.append(ok)

                    linha_compras=divida.readline(8)
                    todo_o_txt.append(linha_compras)
                    if linha_compras=="Compras:":
                        vendidos=divida.readline()
                        with open("log.txt","a") as registro:
                            registro.write(vendidos)
                        todo_o_txt.append("\n")

        with open("userData.txt","w") as reescrevendo:
            escrevendo="".join(todo_o_txt)
            reescrevendo.write(escrevendo)
        print("Fatura emitida✔")
        print("Carrinho esvaziado!")
        menu_do_usuario(usuario.sentenca, usuario.nome)
def fatura():
    while True:
        inp_inicio=int(input(f"O valor da sua divida é R${usuario.divida:.2f} deseja paga-la?\n1-Sim\n0-Voltar\n→"))
        if inp_inicio==0:
            menu_do_usuario(usuario.sentenca,usuario.nome)
            break
        elif inp_inicio==1:
            break
    emailuser="email:"+usuario.email+"\n"
    with open("userData.txt", "r") as pagar:
        todo_o_txt=[]
        for line in pagar:
            todo_o_txt.append(line)
            if line==emailuser:
                l1 = pagar.readline()
                todo_o_txt.append(l1)
                l2 = pagar.readline()
                todo_o_txt.append(l2)
                l3 = pagar.readline()
                todo_o_txt.append(l3)
                l4 = pagar.readline()
                todo_o_txt.append(l4)
                l5 = pagar.readline()
                todo_o_txt.append(l5)
                l6 = pagar.readline()
                todo_o_txt.append(l6)
                linha_divida=pagar.readline(7)
                todo_o_txt.append(linha_divida)
                if linha_divida=="divida:":
                    valores=list(pagar.readline())
                    valores.pop(-1)
                    valor_str=str(usuario.divida)
                    valores.append(str(valor_str+"-"+"\n"))
                    ok="".join(valores)
                    todo_o_txt.append(ok)
                    print(todo_o_txt)

        with open("userData.txt", "w") as escrevendo_novamente:
            txt="".join(todo_o_txt)
            escrevendo_novamente.write(txt)

        with open("log.txt","a") as registrar:
            registrar.write(str(usuario.divida)+"\n")
            todo_o_txt.append("\n")
        usuario.divida-=usuario.divida
        print("Pago✔")
        menu_do_usuario(usuario.sentenca,usuario.nome)
menu_inicial()