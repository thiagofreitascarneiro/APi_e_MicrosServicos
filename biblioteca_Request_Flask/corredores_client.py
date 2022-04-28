import requests 

 
# faça uma função usando a biblioteca requests
# que acessa a URL /corredores do servidor de corredoes
# via GET, e devolve uma lista de todos os corredores
 
def todos_corredores():
    url= "http://localhost:5000/corredores"
    r = requests.get(url)
    lista = r.json()
    return lista
 
# faça uma função usando a biblioteca requests
# que acessa a URL /corredores do servidor de corredoes
# via POST, enviando um dicionário de um novo corredor.
# Um corredor tem os campos "nome", "tempo" e "id"
 
def adiciona_corredores(nome, tempo, id):
    url= "http://localhost:5000/corredores"
    dici_corredor = {"nome": nome, "tempo": tempo, "id": id}
    r = requests.post(url, json=dici_corredor)
    return True

 
# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/maior_tempo do servidor
# de corredoes
# via GET, e retorne o nome do corredor
# mais lento
def mais_lento():
    url= "http://localhost:5000/corredores/maior_tempo"
    r = requests.get(url)
    dici_corredor = r.json()
    return dici_corredor['nome']

 
# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/maior_tempo do servidor
# de corredoes
# via DELETE, causando a remoção dos dados do corredor
# mais lento.
# Infelizmente o servidor tem um bug no caso em que a lista
# de corredores está vazia, mas vamos tratar esse bug
# no nosso cliente


 
# porque a funcionalidade anterior consiste em um erro
# de design no servidor corredores?


def deleta_mais_lento(i):
    url= f"http://localhost:5000/corredores/maior_tempo{}"
    r = requests.delete(url)
    if r.status_code == 500:
        return 'Não é possivel remover de uma lista vazia.'
    else:
        return 'ok'


 
 
# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via GET,
# sua função deve retornar o nome do corredor em questão
# o o seu melhor tempo, em uma tupla

def corredor_por_id(id):
    url= f"http://localhost:5000/corredores/maior_tempo{id}"
    r = requests.get(url)
    dic_retornado = r.json()
    if r.status_code == 404:
        return "corredor não existe"
    nome = (dic_retornado['corredor'])['nome']
    tempo = (dic_retornado['corredor'])['tempo']
    return (nome, tempo)
 
#como eu trataria o erro 404 e informaria o meu usuário?
 
# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via DELETE,
# causando a remoção dos dados do corredor
# mais lento
def deletar_por_id(id):
    url= f"http://localhost:5000/corredores/maior_tempo{id}"
    r = requests.delete(url)
    dic_retornado = r.json()
    if r.status_code == 404:
        return "corredor não existe"
    return 'ok'

 
 
# faça uma função usando a biblioteca requests
# que acessa a URL /corredores/ID do servidor
# de corredores, onde ID é um código numérico.
# O acesso ocorrerá via PUT,
# e você deverá enviar um dicionário com o novo tempo,
def novo_tempo(id, tempo_enviado):
    url= f"http://localhost:5000/corredores/maior_tempo{id}"
    r = requests.put(url, json={tempo_enviado})
    if r.status_code == 400:
        return "tempo não atualizado por ser maior que o record."
    if r.status_code == 404:
        return "verificador não encontrado."
    return 'ok'