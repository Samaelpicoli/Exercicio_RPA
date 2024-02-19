import requests

def solicitar_csv():
    #faz a requisição do arquivo csv e escrevo ele na minha máquina
    url = 'https://docs.google.com/uc?export=download&id=1tEHImtjYPP2PPeeelD3nIPcaKFmfSJF8'
    r = requests.get(url, allow_redirects=True)
    nome = 'database.csv'
    with open(nome, 'wb') as arquivo:
        arquivo.write(r.content)
    return nome