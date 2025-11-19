# 🏦 Desafio BB - Consulta de Extratos Bancários

Projeto de automação para consulta de extratos bancários via API do Banco do Brasil, implementado em **Python** e **UiPath**.

---

## 📋 Descrição

Sistema que:
- Lê planilha com múltiplas contas bancárias
- Autentica via OAuth2 na API do BB
- Consulta extratos de cada conta
- Gera planilha Excel consolidada com abas por conta
- Registra log de execução

---

## 🚀 Tecnologias

- Python 3.x
- Pandas, Requests, OpenPyXL
- API Banco do Brasil (Sandbox)
- Postman
- UiPath (em desenvolvimento)

---

## 📁 Estrutura do Projeto

```
bb_extrato_python/
├── src/
│   ├── auth.py          # Autenticação OAuth2
│   ├── extrato.py       # Consulta de extratos
│   └── main.py          # Script principal
├── data/
│   └── contas.xlsx      # Planilha de entrada
├── output/
│   └── extrato.xlsx     # Planilha gerada
├── postman/
│   └── collection.json  # Postman Collection
├── .env                 # Credenciais (não versionado)
├── requirements.txt     # Dependências Python
└── README.md
```

---

## ⚙️ Instalação e Configuração

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/desafio-bb-extrato.git
cd desafio-bb-extrato
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar credenciais

Crie arquivo `.env` na raiz:

```env
BB_CLIENT_ID=seu_client_id
BB_CLIENT_SECRET=seu_client_secret
BB_DEV_APP_KEY=seu_dev_app_key
BB_TOKEN_URL=https://oauth.sandbox.bb.com.br/oauth/token
```

### 5. Preparar planilha de contas

Edite `data/contas.xlsx` com as contas desejadas:

| agencia | conta    |
|---------|----------|
| 0001    | 123456   |
| 1010    | 987654   |

---

## ▶️ Como Executar

### Python

```bash
python src/main.py
```

**Saída:**
- Arquivo gerado em: `output/extrato.xlsx`
- Abas: uma por conta + `Log_Execucao`

### Postman

1. Importe `postman/collection.json`
2. Execute "1. Autenticação - Obter Token"
3. Execute "2. Consultar Extrato"

---

## 📊 Estrutura da Planilha de Saída

### Abas por conta (ex: `0001-123456`)

| dataLancamento | numeroDocumento | valorLancamento | textoDescricaoHistorico |
|----------------|-----------------|-----------------|-------------------------|
| 01/11/2024     | DOC1001         | -150.00         | PAGAMENTO CONTA         |
| 03/11/2024     | DOC1002         | 2500.00         | SALARIO                 |

### Aba `Log_Execucao`

| agencia | conta  | status | qtd_lancamentos |
|---------|--------|--------|-----------------|
| 0001    | 123456 | OK     | 14              |
| 1010    | 987654 | OK     | 11              |

---

## 🔧 Modo de Desenvolvimento (Mock)

Por padrão, o sistema usa dados fictícios. Para usar a API real:

Em `extrato.py`, altere:
```python
consultar_extrato(agencia, conta, token, usar_mock=False)
```

---

## 📝 Notas Importantes

- **Ambiente:** Sandbox/Homologação (não produção)
- **API BB:** Pode estar temporariamente indisponível
- **Credenciais:** Nunca versionar o arquivo `.env`

---

## 🎯 Roadmap

- [x] Estrutura Python
- [x] Autenticação OAuth2
- [x] Consulta de extratos
- [x] Geração de Excel
- [x] Postman Collection
- [ ] Implementação UiPath
- [ ] Testes com API real
- [ ] Deploy

---

## 👤 Autor

[GitHub](https://github.com/itxrodrigo)

---

## 📄 Licença

Este projeto é para fins educacionais/teste.