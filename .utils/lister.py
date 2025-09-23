import os

IGNORAR_PASTAS = {".git", "__pycache__", "venv", "node_modules", "scripts", '.utils'}

def listar_pastas(caminho, prefixo="", ultimo=True, arquivo=None):
    nome = os.path.basename(caminho)
    if os.path.isdir(caminho):
        icone = "📂"
    else:
        icone = "📄"
    
    conector = "└── " if ultimo else "├── "
    if arquivo:
        arquivo.write(f"{prefixo}{conector}{icone} {nome}\n")
    
    if os.path.isdir(caminho) and nome not in IGNORAR_PASTAS:
        itens = sorted(os.listdir(caminho))
        for i, item in enumerate(itens):
            caminho_completo = os.path.join(caminho, item)
            ultimo_item = i == len(itens) - 1
            listar_pastas(caminho_completo, prefixo + ("    " if ultimo else "│   "), ultimo_item, arquivo)

if __name__ == "__main__":
    saida = ".utils/estrutura_projeto.txt"
    with open(saida, "w", encoding="utf-8") as f:
        listar_pastas(".", arquivo=f)
    print(f"Estrutura salva em {saida}")
