# Fundamentos da Programacao
#
# Projeto - Numeros de cartoes de credito
#
# Nome - Andre Mendonca 
# Numero - 82304


""" O objetivo a funcao calc_soma (que e fundamental para a verificacao do algortimo de luhn) 
e fazer a soma ponderada da cadeia de caracteres que a funcao calc_soma recebe, 
em que para fazer a soma ponderada e necessario inverter o numero que a funcao 
recebe (ja sem o ultimo digito), multiplicar os digitos que estao em posicoes 
impares na cadeia de caracteres recebida por 2 subtraindo por 9 caso o resultado 
da multiplicacao seja maior do que 9
e por fim somar todos os numeros incluindo o numero de verificacao, sendo que 
o resto da divisao dessa soma tem de ser 0, retornando assim a soma ponderada"""

def calc_soma(numero_cartao_inserido):
    i=0
    j=0
    numero_invertido = ''
    comprimento_numero_cartao_inserido = len(numero_cartao_inserido)
    soma_ponderada = 0 
    
    #Ciclo while que percorre o comprimento da cadeia de caracteres recebida na 
    #funcao ate a ultima posicao e verifica se o valor contido na posicao esta 
    #entre 0 e 9, invertendo assim o numero do cartao recebido
  
    while j < comprimento_numero_cartao_inserido:
        if numero_cartao_inserido[j]<='9' and numero_cartao_inserido[j]>='0':
            numero_invertido = numero_cartao_inserido[j] + numero_invertido
        else:
            raise ValueError("O caracter a ser inserido deve ser um numero entre 0 e 9")
        j = j +1
        
    # Ciclo while que percorre o comprimento da cadeia de caracteres recebida na 
    # funcao ate a ultima posicao (em que o numero ja esta invertido) e verifica 
    # se as posicoes da cadeia de caracteres sao pares (pois a primeira posicao 
    # da cadeia de caracteres e 0) e caso sejam pares multiplica o valor da posicao 
    # par por 2 
    
    while i < comprimento_numero_cartao_inserido:
        if i%2==0:
            eval(numero_invertido[i])*2
            
            if eval(numero_invertido[i])*2 > 9:
                soma_ponderada = soma_ponderada + eval(numero_invertido[i])*2 - 9
            else:
                soma_ponderada = soma_ponderada + eval(numero_invertido[i])*2
        else:
            soma_ponderada = soma_ponderada + eval(numero_invertido[i])
            
        i = i + 1        
    
    return soma_ponderada
    
    
""" O objetivo da funcao luhn_verifica e verificar se a cadeia de caracteres do 
numero de cartao recebido passa ao algoritmo de luhn, retornando apenas true ou 
false, nesta funcao e chamada a funcao calc_soma que realiza a soma ponderada do 
numero recebido na funcao luhn_verifica, apos a passagem desse numero pela calc_soma 
a funcao luhn_verifica retorna true caso essa soma ponderada seja 0 e false caso contrario """

def luhn_verifica(numero_cartao_inserido):
    
    numero_cartao_inserido= eval(numero_cartao_inserido)
    
    # A variavel ultimo_numero contem o ultimo digito (digito de verificacao)
    # Apos retirar o ultimo digito a variavel numero_cartao_inserido contem o numero inserido sem o ultimo digito
    
    ultimo_numero = numero_cartao_inserido%10
    numero_cartao_inserido = numero_cartao_inserido//10 
    
    resto = (calc_soma(str(numero_cartao_inserido))+ultimo_numero)%10
    
    if resto == 0:
        return True
    else:
        return False

""" A funcao comeca_por recebe duas cadeias de carateres, cad1 e cad2 e verifica
se cad1 tem os mesmo numeros iniciais do que cad2 e vice-versa, caso sejam iguais
a funcao devolve true, caso contrario a funcao devolve falso """
    
def comeca_por(cad1,cad2):
    
    # A variavel comprimento_cad2 contem o comprimento da cadeia de caracteres de
    # cad2 (recebida inicialmente na funcao como parametro), sendo que o comprimento
    # de cad2 foi utilizado para a realizacao de uma nova cadeia de caracteres (substituindo
    # a cadeia de caracteres de cad1), conseguindo assim verificar se cad1 e cad2 sao iguais
    
    comprimento_cad2 = len(cad2)
    cad1 = cad1[:comprimento_cad2]
    
    if cad1 == cad2:
        return True
    else:
        return False
    
""" A funcao comeca_por_um recebe dois parametros, uma cadeia de carateres (cad) 
e um tuplo que contem cadeias de caracteres (t_cads), esta funcao tem como objetivo
comparar cad com t_cads e se cad comecar por um dos elementos do tuplo t_cads
nesse caso devolve true, caso contrario devolve false""" 

def comeca_por_um(cad,t_cads):
    
    comprimento_tuplo=len(t_cads)
    i=0 
    
    # Ciclo while que percorre tuplo (t_cads) desde a posicao 0 ate ao comprimento
    # do tuplo, utilizando e chamando a funcao comeca_por (inserindo os valores de cad
    # e t_cads) este ciclo realiza a verificacao em que caso a funcao comeca_por retorne
    # o valor true, quer dizer que cad e t_cads sao iguais e nesse caso este ciclo 
    #devolve true    
    
    while i < comprimento_tuplo:
        if comeca_por(cad,t_cads[i]):
            return True
        i = i + 1
    return False
    
""" A funcao valida_iin recebe uma cadeia de carateres em que o objetivo e da funcao
e verificar se os valores da cadeia de caracteres inserida no parametro da funcao
correspondem a uma rede emissora (iin), caso corresponda a uma rede emissora a funcao devolve
a cadeia de caracteres cujo o valor e o nome dessa rede emissora, caso contrario
a funcao devolve uma cadeia de caracteres vazia"""

iin = (("American Express", "AE", ("34","37"), ("15",)),
       ("Diners Club International", "DCI", ("309", "36", "38", "39"), ("14",))
       ,("Discover Card", "DC", ("65",), ("16",)),
       ("Maestro", "M", ("5018", "5020", "5038"), ("13", "19")),
       ("Master Card", "MC", ("50", "51", "52", "53", "54", "19"), ("16",)),
       ("Visa Electron", "VE", ("4026", "426", "4405", "4508"), ("16",)),
       ("Visa", "V", ("4024", "4532", "4556"), ("13", "16")))

def valida_iin(numero_cartao_inserido):
    
    # Passagem da cadeia de caracteres de string para um numero para retirar o ultimo numero
    # em seguida volta-se a passar de numero para string para ser
    # possivel percorrer a cadeia de caracteres
    
    comprimento_cartao_inserido = len(numero_cartao_inserido)
    
    numero_cartao_inserido = eval(numero_cartao_inserido)
    ultimo_numero = numero_cartao_inserido%10
    numero_cartao_inserido = numero_cartao_inserido//10
    
    numero_cartao_inserido = str(numero_cartao_inserido)
    
    # O primeiro ciclo for percorre todos os elementos que estao no tuplo iin
    # que foi criado anteriormente, o segundo ciclo for percorre os elementos que
    # estao contidos na posicao 3 do tuplo iin e se for encontrado um comprimento igual
    # ao comprimento do numero inserido no parametro da funcao e se consequentemente os numeros
    # prefixos desse mesmo numero recebido como parametro nesta funcao for equivalente
    # a uma das redes emissoras, entao devolve a cadeia de caracteres que representa
    # a rede emissora desse mesmo numero inserido, caso contrario devolve vazio
    
    for elemento in iin:
        for comprimento in elemento[3]: 
                if comprimento == str(comprimento_cartao_inserido): 
                    if comeca_por_um(numero_cartao_inserido, elemento[2]): 
                        return elemento[0]
    return '' 

"""A funcao categoria recebe uma cadeia de carateres, e devolve uma cadeia correspondente 
a categoria do iin correspondente ao primeiro caracter da cadeia"""

categorias_emissor = ('Companhias aereas',
                      'Companhias aereas e outras tarefas futuras da industria',
                      'Viagens e entretenimento e bancario / financeiro',
                      'Servicos bancarios e financeiros',
                      'Servicos bancarios e financeiros',
                      'Merchandising e bancario / financeiro',
                      'Petroleo e outras atribuicoes futuras da industria',
                      'Saude, telecomunicacoes e outras atribuicoes futuras da industria',
                      'Atribuicao nacional')

def categoria(numero_mii):
    numero_mii = str(numero_mii)
    if numero_mii[0]>='1' and numero_mii[0]<='9': 
        return categorias_emissor[eval(numero_mii[0])-1]  
    else:
        raise ValueError("Na sequencia de numeros do numero_mii, o primeiro digito a inserir deve ser um digito entre 1 e 9")

"""A funcao verifica_cc recebe um inteiro que representa um numero de cartao de credito 
e permite verificar se e valido atraves da implementacao de outras funcoes auxiliares""" 
    
def verifica_cc(numero_cartao_inserido):
    
    numero_cartao_inserido = str(numero_cartao_inserido)
    rede_cartao = valida_iin(numero_cartao_inserido)
    luhn = luhn_verifica(numero_cartao_inserido)
    categoria_entidade = categoria(numero_cartao_inserido)
    
    if rede_cartao and luhn:
        return (categoria_entidade,rede_cartao)
    else:
        return 'cartao invalido'   
    
"""A funcao digito_verificacao recebe um numero inteiro e devolve um digito de 
verificacao de luhn valido para o numero 
de cartao de credito recebido por parametro, para a verificacao se o numero
corresponde ao algoritmo de luhn e necessario a implementacao da funcao auxiliar
calc_soma que realiza a soma ponderada desse mesmo numero"""

def digito_verificacao(numero_cartao_inserido):
    
    resto = calc_soma(numero_cartao_inserido)%10 
    conta_verifica = str(10-resto)
    if resto == 0:
        digito_verificacao = '0'
    elif resto > 0:
        digito_verificacao = conta_verifica
        
    return digito_verificacao  

"""A funcao gera_num_cc gera um numero de cartao e credito valido, baseado na abreviatura  
 que pertence a um dos tuplos do iin e devolve um numero gerado aleatoriamente"""

from random import *

def gera_num_cc(abreviatura):
    
    j = 0
    i = 0
    comprimento_tuplo = len(iin)
    
    # Tal como e dito no enunciado, e necessario utilizar a funcao random que esta 
    #localizada na biblioteca random do python para gerar um numero aleatorio 
    #(nos intervalos entre 0 e 1), como nao era possivel utilizar o randint nem 
    #o choice, a alternativa foi utilizar a funcao random para gerar um numero 
    #aleatorio e multiplicar esse mesmo numero aleatorio pelo tamanho do tuplo (comprimento_aleatorio) 
    #e tambem no caso dos prefixos (numeros_aleatorios), que consequentemente vai 
    #gerar uma das posicoes possiveis (0,1 ou 2) ate chegar ao fim do comprimento do tuplo
    
    while j < comprimento_tuplo:
        if iin[j][1] == abreviatura:
            comprimento_aleatorio = iin[j][3][int(random() * len(iin[j][3]))]
            numeros_aleatorios = iin[j][2][int(random() * len(iin[j][2]))]
        j = j+1
    
    numero_gerado = str(numeros_aleatorios)
    comprimento_numero_gerado = len(numero_gerado)
    limite = int(comprimento_aleatorio)-int(comprimento_numero_gerado)-1
    
    while i < limite:
        numero_gerado = numero_gerado + str(int(random()*10))
        i = i + 1
        
    dig_verificacao = digito_verificacao(numero_gerado)
        
    numero_gerado = int(numero_gerado + dig_verificacao)
                
    return numero_gerado

