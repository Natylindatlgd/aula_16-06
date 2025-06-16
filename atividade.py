import urllib.parse

def extrair_nome_usuario(url):
    parsed_url = urllib.parse.urlparse(url)
    caminho = parsed_url.path
    partes = caminho.split('/')
    if len(partes) > 1 and partes[1]:
        return partes[1]
    else:
        return None

url_usuario = input("Digite uma URL: ")

nome_usuario = extrair_nome_usuario(url_usuario)

if nome_usuario:
    print(f"O nome de usuário extraído é: {nome_usuario}")
else:
    print("Nenhum nome de usuário encontrado na URL.")
