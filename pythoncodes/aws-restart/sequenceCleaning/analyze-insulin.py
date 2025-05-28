import re

# === 1. Ler e limpar a sequência ===
with open('preproinsulin-seq.txt', 'r') as file:
    raw_seq = file.read()

# Limpeza: remove tudo que não é letra e coloca em minúsculo
clean_seq = re.sub(r'[^a-zA-Z]', '', raw_seq).lower()

# Confirmar que ficou com 110 caracteres
print(f"Sequência limpa: {len(clean_seq)} caracteres")

# Salvar a sequência limpa
with open('preproinsulin-seq-clean.txt', 'w') as file:
    file.write(clean_seq)

# === 2. Cortar as partes ===
parts = {
    'lsinsulin-seq-clean.txt': clean_seq[0:24],    # 1-24
    'binsulin-seq-clean.txt': clean_seq[24:54],   # 25-54
    'cinsulin-seq-clean.txt': clean_seq[54:89],   # 55-89
    'ainsulin-seq-clean.txt': clean_seq[89:110]   # 90-110
}

# Salvar as partes
for filename, sequence in parts.items():
    with open(filename, 'w') as file:
        file.write(sequence)
    print(f"{filename} salvo com {len(sequence)} caracteres.")

# === 3. Validar todos os arquivos ===
# Arquivos + tamanhos esperados
files = {
    'preproinsulin-seq-clean.txt': 110,
    'lsinsulin-seq-clean.txt': 24,
    'binsulin-seq-clean.txt': 30,
    'cinsulin-seq-clean.txt': 35,
    'ainsulin-seq-clean.txt': 21
}

print("\n=== Validação ===")
for filename, expected_length in files.items():
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            length = len(content)
            if length == expected_length:
                print(f"✅ {filename}: OK! {length}/{expected_length} caracteres")
            else:
                print(f"❌ {filename}: ERRO! {length}/{expected_length} caracteres")
    except FileNotFoundError:
        print(f"❌ {filename}: Arquivo não encontrado!")