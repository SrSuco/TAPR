# Classe compactador faz a contagem dos caracteres e salva o conteúdo baseado no número de repetições
# de caracteres repetidos, fazendo com que sejam salvos da seguinte forma: cN (sendo c o caractere testado e N o número de vezes que se repete)
def compactador(conteudo):
    compactado = []  # Lista para armazenar o resultado compactado
    i = 0
    while i < len(conteudo):
        contagem = 1  # Inicializa a contagem para o caractere atual
        # Conta o número de repetições consecutivas do caractere atual
        while i + 1 < len(conteudo) and conteudo[i] == conteudo[i + 1]:
            contagem += 1
            i += 1
        # Adiciona o caractere e sua contagem ao resultado
        if contagem > 1:
            compactado.append(f"{conteudo[i]}{contagem}")
        else:
            compactado.append(conteudo[i])
        i += 1  # Avança para o próximo caractere
    return ''.join(compactado)  # Retorna o resultado como uma string

# Abre o arquivo no modo de leitura
with open('arquivo1.txt', 'r') as arquivo:
    original = arquivo.read()

# Compacta o conteúdo usando a função compactador
compactado = compactador(original)

# Sobrescreve o arquivo com o conteúdo compactado
with open('arquivo1.txt.squeezed', 'w') as arquivo:
    arquivo.write(compactado)

# Abre o arquivo no modo de leitura
with open('arquivo2.txt', 'r') as arquivo:
    original = arquivo.read()

compactado = compactador(original)

with open('arquivo2.txt.squeezed', 'w') as arquivo:
    arquivo.write(compactado)