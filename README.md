# 🏦 Desafio BB - Consulta de Extratos Bancários

Projeto completo de automação para consulta de extratos bancários via API do Banco do Brasil, implementado em **Python** e **UiPath RPA**.

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![UiPath](https://img.shields.io/badge/UiPath-Studio-orange.svg)](https://www.uipath.com/)
[![Status](https://img.shields.io/badge/Status-Completo-success.svg)]()

---

## 📋 Descrição

Sistema automatizado que:
- ✅ Lê planilha com múltiplas contas bancárias
- ✅ Autentica via OAuth2 na API do BB (Sandbox)
- ✅ Consulta extratos de cada conta
- ✅ Gera planilha Excel consolidada com abas por conta
- ✅ Registra log detalhado de execução
- ✅ Implementado em Python e UiPath (mesma lógica)

---

## 🚀 Tecnologias

### Python
- Python 3.x
- Pandas, Requests, OpenPyXL
- OAuth2 Client Credentials
- Dotenv para variáveis de ambiente

### UiPath
- UiPath Studio Community
- Excel Activities
- HTTP Request Activities
- DataTable manipulation

### Outros
- Postman (Collection para testes)
- API Banco do Brasil (Sandbox)
- Git/GitHub

---

## 📁 Estrutura do Projeto

```
desafio-bb-extrato/
├── python/
│   ├── src/
│   │   ├── auth.py          # Autenticação OAuth2
│   │   ├── extrato.py       # Consulta de extratos (com mock)
│   │   └── main.py          # Script principal
│   ├── data/
│   │   └── contas.xlsx      # Planilha de entrada
│   ├── output/
│   │   └── extrato.xlsx     # Planilha gerada (Python)
│   ├── .env                 # Credenciais (não versionado)
│   └── requirements.txt     # Dependências Python
│
├── uipath/
│   └── BB_Extrato_Final/
│       ├── Main.xaml        # Workflow principal
│       ├── project.json     # Config do projeto
│       └── README_UIPATH.md # Documentação UiPath
│
├── postman/
│   └── BB_Extratos.postman_collection.json
│
├── .gitignore
└── README.md
```

---

## ⚙️ Instalação e Configuração

### 1️⃣ Clonar o Repositório

```bash
git clone https://github.com/SEU_USUARIO/desafio-bb-extrato.git
cd desafio-bb-extrato
```

---

### 2️⃣ Configuração Python

#### a) Criar ambiente virtual

```bash
cd python
python -m venv venv
venv\Scripts\activate  # Windows
```

#### b) Instalar dependências

```bash
pip install -r requirements.txt
```

#### c) Configurar credenciais

Crie arquivo `.env` na pasta `python/`:

```env
BB_CLIENT_ID=seu_client_id
BB_CLIENT_SECRET=seu_client_secret
BB_DEV_APP_KEY=seu_dev_app_key
BB_TOKEN_URL=https://oauth.sandbox.bb.com.br/oauth/token
```

#### d) Preparar planilha de contas

Edite `python/data/contas.xlsx`:

| agencia | conta |
|---------|-------|
| 0001 | 123456 |
| 1010 | 987654 |

---

### 3️⃣ Configuração UiPath

1. Abra **UiPath Studio**
2. **File** → **Open** → `uipath/BB_Extrato_Final/project.json`
3. Verifique se os pacotes estão instalados:
   - UiPath.Excel.Activities
   - UiPath.System.Activities

---

## ▶️ Como Executar

### Python

```bash
cd python
python src/main.py
```

**Saída:**
- Arquivo: `python/output/extrato.xlsx`
- Abas: uma por conta + `Log_Execucao`

---

### UiPath

1. Abra o projeto no UiPath Studio
2. Pressione **F5** ou clique em **Run**
3. Verifique o arquivo: `python/output/extrato_final.xlsx`

---

### Postman

1. Importe `postman/BB_Extratos.postman_collection.json`
2. Execute "1. Autenticação - Obter Token"
3. Execute "2. Consultar Extrato"

---

## 📊 Estrutura das Planilhas

### Entrada: `contas.xlsx`

| agencia | conta |
|---------|-------|
| 0001 | 123456 |
| 1010 | 987654 |

### Saída Python: `extrato.xlsx`

**Aba por conta** (ex: `0001-123456`):

| dataLancamento | numeroDocumento | valorLancamento | textoDescricaoHistorico |
|----------------|-----------------|-----------------|-------------------------|
| 01/11/2024 | DOC1001 | -150.00 | PAGAMENTO CONTA |
| 03/11/2024 | DOC1002 | 2500.00 | SALARIO |

**Aba `Log_Execucao`**:

| agencia | conta | status | qtd_lancamentos |
|---------|-------|--------|-----------------|
| 0001 | 123456 | OK | 14 |
| 1010 | 987654 | OK | 11 |

### Saída UiPath: `extrato_final.xlsx`

**Aba `Log_Execucao`**:

| agencia | conta | status |
|---------|-------|--------|
| 1 | 123456 | OK |
| 1010 | 987654 | OK |

---

## 🔧 Modo de Desenvolvimento (Mock)

### Python

Por padrão usa dados fictícios. Para usar API real:

Em `main.py`, linha 35:
```python
resultado = consultar_extrato(agencia, conta, token, usar_mock=False)
```

### UiPath

Atualmente apenas registra log. Para integrar com API:
- Adicionar HTTP Request para autenticação
- Adicionar HTTP Request para consulta
- Adicionar Deserialize JSON
- Ver `uipath/README_UIPATH.md` para detalhes

---

## 🧪 Testes

### Testar autenticação

```bash
cd python
python src/auth.py
```

### Testar consulta de extrato

```bash
python src/extrato.py
```

---

## 📝 Notas Importantes

- ⚠️ **Ambiente:** Sandbox/Homologação (não produção)
- ⚠️ **API BB:** Pode estar temporariamente indisponível
- ⚠️ **Credenciais:** Nunca versionar arquivos `.env`
- ✅ **Mock:** Projeto funciona com dados fictícios para desenvolvimento
- ✅ **Escalável:** Fácil trocar mock por API real quando disponível

---

## 🎯 Status do Projeto

- [x] Estrutura Python completa
- [x] Autenticação OAuth2 implementada
- [x] Consulta de extratos (modo mock)
- [x] Geração de Excel com múltiplas abas
- [x] Log de execução detalhado
- [x] Postman Collection criada
- [x] UiPath workflow completo
- [x] Documentação completa
- [x] GitHub publicado
- [ ] Testes com API real (aguardando estabilidade do sandbox BB)
- [ ] Implementar retry logic
- [ ] Adicionar testes unitários

---

## 🤝 Como Contribuir

1. Fork o projeto
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`
3. Commit: `git commit -m 'Adiciona nova funcionalidade'`
4. Push: `git push origin feature/nova-funcionalidade`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto é para fins educacionais/demonstração técnica.

---

## 👤 Autor

**Rodrigo Moreira Alves**

- GitHub: [@itxtodrigo](https://github.com/itxrodrigo)


---

## 🙏 Agradecimentos

- Banco do Brasil por disponibilizar API Sandbox
- Comunidade UiPath
- Documentação Python

---

## 📞 Suporte

Para dúvidas ou problemas:
1. Abra uma [Issue](https://github.com/SEU_USUARIO/desafio-bb-extrato/issues)
2. Consulte a documentação em cada pasta
3. Verifique os logs de execução

---

**⭐ Se este projeto foi útil, deixe uma estrela no repositório!**