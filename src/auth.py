import requests
import os
import base64
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

def get_token():
    """
    Obtém o token de acesso OAuth2 da API do Banco do Brasil (Sandbox)
    """
    
    # URL do endpoint de autenticação (Sandbox)
    url = os.getenv('BB_TOKEN_URL', 'https://oauth.hm.bb.com.br/oauth/token')
    
    # Credenciais do .env
    client_id = os.getenv('BB_CLIENT_ID')
    client_secret = os.getenv('BB_CLIENT_SECRET')
    dev_app_key = os.getenv('BB_DEV_APP_KEY')
    
    # Validar se as credenciais existem
    if not client_id or not client_secret:
        raise ValueError("Erro: BB_CLIENT_ID ou BB_CLIENT_SECRET não encontrados no arquivo .env")
    
    # Criar Basic Auth (Base64)
    credentials = f"{client_id}:{client_secret}"
    credentials_b64 = base64.b64encode(credentials.encode()).decode()
    
    # Headers da requisição
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {credentials_b64}'
    }
    
    # Adicionar Developer Application Key se existir
    if dev_app_key:
        headers['Developer-Application-Key'] = dev_app_key
    
    # Corpo da requisição
    data = {
        'grant_type': 'client_credentials'
    }
    
    try:
        # Fazer a requisição
        print("Solicitando token de acesso (Sandbox)...")
        print(f"URL: {url}")
        
        response = requests.post(
            url,
            headers=headers,
            data=data,
            timeout=30
        )
        
        # Verificar se deu certo
        if response.status_code == 200:
            token_data = response.json()
            access_token = token_data.get('access_token')
            expires_in = token_data.get('expires_in', 'N/A')
            
            print("\n[OK] Token obtido com sucesso!")
            print(f"Token (primeiros 30 chars): {access_token[:30]}...")
            print(f"Expira em: {expires_in} segundos")
            
            return access_token
        else:
            print(f"\n[ERRO] Status: {response.status_code}")
            print(f"Resposta: {response.text}")
            return None
            
    except requests.exceptions.Timeout:
        print("\n[ERRO] Timeout na requisicao de autenticacao")
        return None
    except requests.exceptions.RequestException as e:
        print(f"\n[ERRO] Erro na requisicao: {str(e)}")
        return None

# Teste direto (executar apenas este arquivo)
if __name__ == "__main__":
    print("=" * 60)
    print("TESTE DE AUTENTICACAO - BANCO DO BRASIL SANDBOX")
    print("=" * 60)
    
    token = get_token()
    
    if token:
        print("\n" + "=" * 60)
        print("[SUCESSO] AUTENTICACAO FUNCIONOU!")
        print("=" * 60)
        print(f"\nToken completo:\n{token}")
    else:
        print("\n" + "=" * 60)
        print("[FALHA] NAO FOI POSSIVEL AUTENTICAR")
        print("=" * 60)
        print("Verifique suas credenciais no arquivo .env")