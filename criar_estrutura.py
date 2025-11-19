import os

# Estrutura de pastas
pastas = [
    'src',
    'data',
    'output'
]

# Criar pastas
for pasta in pastas:
    os.makedirs(pasta, exist_ok=True)
    print(f"✅ Pasta '{pasta}' criada")

# Criar arquivos vazios
arquivos = [
    'src/auth.py',
    'src/extrato.py',
    'src/main.py',
    '.env',
    'README.md'
]

for arquivo in arquivos:
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write('')
    print(f"✅ Arquivo '{arquivo}' criado")

print("\n🎉 Estrutura do projeto criada com sucesso!")
print("\nEstrutura final:")
print("""
bb_extrato_python/
├── src/
│   ├── auth.py
│   ├── extrato.py
│   └── main.py
├── data/
├── output/
├── .env
├── requirements.txt
└── README.md
""")