import requests


# verifica Interseção
def intersecao(ret_a, ret_b):
    if ret_a[1] < ret_b[3] or ret_a[0] < ret_b[2]:
        return "Não houve interseção."
    elif ret_a[2] > ret_b[0] or ret_a[3] > ret_b[1]:
        return "Não houve interseção."
    else:
        return "Houve interseção nos pontos: " + str(set(ret_a).intersection(ret_b))


# Verificando CNPJ válido com ou sem máscara
def validaCPF(cnpj):
    remove_items = "./-"
    for i in range(0, len(remove_items)):
        cnpj = cnpj.replace(remove_items[i], "")
    print("\nAplicando Mascara: " + '{}.{}.{}/{}-{}'.format(cnpj[:3], cnpj[3:6], cnpj[6:9], cnpj[9:12], cnpj[12:]))
    if len(cnpj) > 14:
        return "Quantidade de digitos inválida"
    elif len(cnpj) < 14:
        return "Quantidade de digitos inválida"
    elif not cnpj.isdigit():
        return "CNPJ não pode conter Letras"
    elif len(cnpj) == 14:
        return "CNPJ válido"


# Acessando URL e imprimindo informação desejada
def currentDateTime():
    x = []
    task = {}
    resp = requests.get('http://worldclockapi.com/api/json/utc/now', task)
    if resp:
        x.append(resp.json())
        dateTime = x[0]['currentDateTime']
        timeZone: object = x[0]['timeZoneName']
        return'\nRequisição realizada com sucesso!\nDia Atual: ' + dateTime[0:10] + '\nHora atual: ' + dateTime[11:16] \
              + '\nTime Zone: ' + timeZone + "\n\nRequisição completa: " + str(x)
    else:
        return'Falha ao realizar requisição.'


print(intersecao(ret_a=[25, 10, 10, 5], ret_b=[15, 10, 10, 5]))
print(validaCPF("479.674.138.064-tt"))
print(currentDateTime())