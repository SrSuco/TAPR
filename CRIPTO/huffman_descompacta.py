import os

def read_codes(f):
    num_entries = int.from_bytes(f.read(2), 'big')
    codes = {}
    for _ in range(num_entries):
        ch = f.read(1).decode('utf-8')
        code_len = ord(f.read(1))
        n_bytes = (code_len + 7) // 8
        code_bytes = f.read(n_bytes)
        code_int = int.from_bytes(code_bytes, 'big')
        code_str = bin(code_int)[2:].zfill(code_len)
        codes[ch] = code_str
    return codes

def invert_codes(codes):
    return {v: k for k, v in codes.items()}

def huffman_decode(encoded_bits, codes):
    reverse_codes = invert_codes(codes)
    decoded = []
    current = ""
    for bit in encoded_bits:
        current += bit
        if current in reverse_codes:
            decoded.append(reverse_codes[current])
            current = ""
    return ''.join(decoded)

def descompactar_arquivos_huff():
    # Diretório do próprio script
    pasta = os.path.dirname(os.path.realpath(__file__))
    arquivos = [arq for arq in os.listdir(pasta) if arq.lower().endswith('.huff')]
    print(f"Procurando arquivos .huff na pasta: {pasta}")
    print("Arquivos encontrados:", arquivos)
    if not arquivos:
        print('Nenhum arquivo .huff encontrado na pasta:', pasta)
        return
    for arquivo in arquivos:
        print(f"Descompactando: {arquivo}")
        with open(os.path.join(pasta, arquivo), 'rb') as f:
            codes = read_codes(f)
            padding = ord(f.read(1))
            encoded_bytes = f.read()
            total_bits = ""
            for b in encoded_bytes:
                total_bits += bin(b)[2:].zfill(8)
            if padding:
                total_bits = total_bits[:-padding]
            decoded = huffman_decode(total_bits, codes)
        saida = os.path.splitext(arquivo)[0] + '.txt'
        with open(os.path.join(pasta, saida), 'w', encoding='utf-8') as f:
            f.write(decoded)
        print(f"Descompactado: {arquivo} -> {saida}")

if __name__ == "__main__":
    descompactar_arquivos_huff()