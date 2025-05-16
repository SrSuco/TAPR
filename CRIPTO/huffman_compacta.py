import heapq
import os
from collections import defaultdict

class Node:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [Node(char, freq) for char, freq in freq_dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq, node1, node2)
        heapq.heappush(heap, merged)
    return heap[0]

def build_codes(root):
    codes = {}
    def _build_codes(node, current_code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = current_code
            return
        _build_codes(node.left, current_code + "0")
        _build_codes(node.right, current_code + "1")
    _build_codes(root, "")
    return codes

def huffman_encode(data):
    freq_dict = defaultdict(int)
    for ch in data:
        freq_dict[ch] += 1
    root = build_huffman_tree(freq_dict)
    codes = build_codes(root)
    encoded = ''.join(codes[ch] for ch in data)
    padding = 8 - len(encoded) % 8 if len(encoded) % 8 != 0 else 0
    encoded += "0" * padding
    return codes, encoded, padding

def save_compressed(codes, encoded, padding, output_path):
    with open(output_path, 'wb') as f:
        f.write(len(codes).to_bytes(2, 'big'))
        for ch, code in codes.items():
            f.write(bytes([ord(ch)]))
            f.write(bytes([len(code)]))
            code_int = int(code, 2)
            n_bytes = (len(code) + 7) // 8
            f.write(code_int.to_bytes(n_bytes, 'big'))
        f.write(bytes([padding]))
        for i in range(0, len(encoded), 8):
            byte = encoded[i:i+8]
            f.write(int(byte, 2).to_bytes(1, 'big'))

def compactar_arquivos_txt():
    # Diretório do próprio script (não do terminal!)
    pasta = os.path.dirname(os.path.realpath(__file__))
    arquivos = [arq for arq in os.listdir(pasta) if arq.lower().endswith('.txt')]
    if not arquivos:
        print('Nenhum arquivo .txt encontrado na pasta:', pasta)
        return
    for arquivo in arquivos:
        print(f"Compactando: {arquivo}")
        with open(os.path.join(pasta, arquivo), 'r', encoding='utf-8') as f:
            data = f.read()
        codes, encoded, padding = huffman_encode(data)
        saida = os.path.splitext(arquivo)[0] + '.huff'
        save_compressed(codes, encoded, padding, os.path.join(pasta,saida))
        print(f"Compactado: {arquivo} -> {saida}")

if __name__ == "__main__":
    compactar_arquivos_txt()