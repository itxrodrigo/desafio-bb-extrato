import requests
from datetime import datetime, timedelta
import random

def consultar_extrato(agencia, conta, token, usar_mock=True):
    """
    Consulta o extrato de uma conta bancária
    
    Args:
        agencia: número da agência
        conta: número da conta
        token: token de acesso OAuth2
        usar_mock: se True, retorna dados fictícios (para desenvolvimento)
    
    Returns:
        dict com 'sucesso', 'dados' ou 'erro'
    """
    
    if usar_mock:
        # MOCK: Dados fictícios para desenvolvimento
        print(f"[MOCK] Consultando extrato: Ag {agencia} / Conta {conta}")
        
        # Simular 30% de chance de erro para testar tratamento
        if random.random() < 0.3:
            erros_possiveis = [
                "Conta nao encontrada",
                "Agencia invalida",
                "Sem movimentacao no periodo"
            ]
            return {
                'sucesso': False,
                'erro': random.choice(erros_possiveis)
            }
        
        # Gerar dados fictícios de extrato
        lancamentos = []
        data_inicial = datetime.now() - timedelta(days=30)
        
        for i in range(random.randint(5, 15)):
            data_lancamento = data_inicial + timedelta(days=i*2)
            lancamentos.append({
                'dataLancamento': data_lancamento.strftime('%d/%m/%Y'),
                'numeroDocumento': f'DOC{1000 + i}',
                'valorLancamento': round(random.uniform(-500, 1000), 2),
                'textoDescricaoHistorico': random.choice([
                    'PIX RECEBIDO',
                    'PAGAMENTO CONTA',
                    'TRANSFERENCIA',
                    'SALARIO',
                    'COMPRA CARTAO'
                ])
            })
        
        return {
            'sucesso': True,
            'dados': lancamentos
        }
    
    else:
        # CÓDIGO REAL: Consulta na API do BB
        url = f"https://api.hm.bb.com.br/extratos/v1/agencia/{agencia}/conta/{conta}"
        
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        
        try:
            print(f"Consultando extrato: Ag {agencia} / Conta {conta}")
            
            response = requests.get(url, headers=headers, timeout=30)
            
            if response.status_code == 200:
                dados = response.json()
                lancamentos = dados.get('lancamentos', [])
                
                return {
                    'sucesso': True,
                    'dados': lancamentos
                }
            else:
                return {
                    'sucesso': False,
                    'erro': f"HTTP {response.status_code}: {response.text}"
                }
                
        except requests.exceptions.Timeout:
            return {
                'sucesso': False,
                'erro': "Timeout na requisicao"
            }
        except Exception as e:
            return {
                'sucesso': False,
                'erro': str(e)
            }

# Teste
if __name__ == "__main__":
    # Teste com mock
    resultado = consultar_extrato("0001", "12345-6", "token_fake", usar_mock=True)
    
    if resultado['sucesso']:
        print("\n[OK] Extrato obtido:")
        for lanc in resultado['dados'][:3]:  # Mostra só os 3 primeiros
            print(f"  {lanc['dataLancamento']} | {lanc['numeroDocumento']} | R$ {lanc['valorLancamento']}")
    else:
        print(f"\n[ERRO] {resultado['erro']}")