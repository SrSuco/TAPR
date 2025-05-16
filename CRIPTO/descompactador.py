def descompactador(conteudo):
    descompactado = []  # Lista para armazenar o resultado descompactado
    i = 0  # Índice inicial para percorrer o conteúdo

    while i < len(conteudo):
        caractere = conteudo[i]  # Pega o caractere atual
        i += 1  # Avança para o próximo índice

        # Verifica se o próximo trecho é um número (representando a contagem)
        contagem = ""
        while i < len(conteudo) and conteudo[i].isdigit():
            contagem += conteudo[i]
            i += 1
        
        # Se uma contagem foi encontrada, multiplica o caractere por ela
        if contagem:
            descompactado.append(caractere * int(contagem))
        else:
            # Caso contrário, apenas adiciona o caractere (sem repetição)
            descompactado.append(caractere)

    return ''.join(descompactado)  # Retorna o resultado como uma única string


# Lógica para abrir, descompactar e sobrescrever os arquivos
with open('arquivo1.txt.squeezed', 'r') as arquivo:
    compactado = arquivo.read()
descompactado = descompactador(compactado)
with open('arquivo1New.txt', 'w') as arquivo:
    arquivo.write(descompactado)

with open('arquivo2.txt.squeezed', 'r') as arquivo:
    compactado = arquivo.read()
descompactado = descompactador(compactado)
with open('arquivo2New.txt', 'w') as arquivo:
    arquivo.write(descompactado)