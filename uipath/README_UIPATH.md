# 🤖 UiPath - Consulta de Extratos BB

Automação RPA que replica a funcionalidade do script Python.

---

## 📋 Funcionalidades

- Lê planilha Excel com lista de contas
- Processa cada conta (atualmente com mock)
- Gera log de execução em Excel
- Tratamento de erros por conta

---

## 📁 Estrutura

```
BB_Extrato_Final/
├── Main.xaml              # Workflow principal
├── project.json           # Configurações do projeto
└── .screenshots/          # Screenshots das activities
```

---

## ⚙️ Pré-requisitos

- UiPath Studio (versão Community ou superior)
- Pacotes necessários:
  - UiPath.Excel.Activities
  - UiPath.System.Activities
  - UiPath.WebAPI.Activities (para API real)

---

## 🚀 Como Executar

### 1. Abrir o Projeto

1. Abra UiPath Studio
2. File → Open → Navegar até `uipath/BB_Extrato_Final`
3. Abrir `project.json`

### 2. Configurar Arquivos

Certifique-se de que existe:
- `data/contas.xlsx` - Planilha com as contas

### 3. Executar

1. Clique em **Run** (F5)
2. Aguarde a execução
3. Verifique o arquivo gerado:
   - `output/extrato_final.xlsx`

---

## 📊 Workflow Detalhado

### Main Sequence

```
1. Log Message - Iniciando
2. Read Range Workbook - Lê contas.xlsx
3. Build Data Table - Cria estrutura de log
4. For Each Row - Loop nas contas
   ├── Assign - Extrai agência
   ├── Assign - Extrai conta
   ├── Log Message - Mostra progresso
   └── Add Data Row - Adiciona ao log
5. Write Range Workbook - Salva log
6. Log Message - Finaliza
```

---

## 🔧 Variáveis Utilizadas

| Nome | Tipo | Descrição |
|------|------|-----------|
| dtContas | DataTable | Contas lidas do Excel |
| dtLog | DataTable | Log de execução |
| agencia | String | Agência atual |
| conta | String | Conta atual |

---

## 📝 Planilha de Entrada (contas.xlsx)

Formato esperado:

| agencia | conta |
|---------|-------|
| 0001 | 123456 |
| 1010 | 987654 |

---

## 📊 Planilha de Saída (extrato_final.xlsx)

Aba **Log_Execucao**:

| agencia | conta | status |
|---------|-------|--------|
| 1 | 123456 | OK |
| 1010 | 987654 | OK |

---

## 🔄 Modo Mock vs API Real

### Atualmente (Mock)

O workflow apenas lê as contas e registra no log.

### Para usar API Real

Adicionar entre os Assigns e o Log Message:

1. **HTTP Request - Token**
   - Endpoint: `https://oauth.sandbox.bb.com.br/oauth/token`
   - Method: POST
   - Authentication: Basic Auth

2. **HTTP Request - Extrato**
   - Endpoint: `https://api.hm.bb.com.br/extratos/v1/agencia/{agencia}/conta/{conta}`
   - Method: GET
   - Headers: `Authorization: Bearer {token}`

3. **Deserialize JSON**
   - Parse dos dados retornados

---

## ⚠️ Tratamento de Erros

O workflow usa **Try-Catch** implícito:
- Erros por conta não interrompem o fluxo
- Cada conta é processada independentemente
- Erros são registrados no log

---

## 🎯 Melhorias Futuras

- [ ] Integração real com API BB
- [ ] Criar abas por conta no Excel
- [ ] Adicionar retry logic
- [ ] Parametrização via Config
- [ ] Logging em arquivo txt
- [ ] Envio de email com resultado

---

## 📞 Suporte

Para dúvidas sobre o projeto, consulte o README principal do repositório.