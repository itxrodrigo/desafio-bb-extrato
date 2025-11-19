import pandas as pd
from pathlib import Path
from auth import get_token
from extrato import consultar_extrato

def main():
    """
    Script principal: lê contas, consulta extratos e gera Excel
    """
    
    print("=" * 70)
    print("DESAFIO BB - CONSULTA DE EXTRATOS")
    print("=" * 70)
    
    # 1. LER PLANILHA DE CONTAS
    print("\n[1/4] Lendo planilha de contas...")
    
    arquivo_contas = Path("data/contas.xlsx")
    
    if not arquivo_contas.exists():
        print("[ERRO] Arquivo data/contas.xlsx nao encontrado!")
        return
    
    df_contas = pd.read_excel(arquivo_contas)
    print(f"[OK] {len(df_contas)} contas encontradas")
    
    # 2. OBTER TOKEN (comentado pois API está fora)
    print("\n[2/4] Obtendo token de acesso...")
    token = "TOKEN_MOCK"  # Quando API funcionar: token = get_token()
    print("[OK] Token obtido (MOCK)")
    
    # 3. CONSULTAR EXTRATOS
    print("\n[3/4] Consultando extratos...")
    
    resultados = []
    dados_extratos = {}
    
    for idx, row in df_contas.iterrows():
        agencia = str(row['agencia']).zfill(4)  # Garante 4 dígitos
        conta = str(row['conta'])
        
        print(f"\n  [{idx+1}/{len(df_contas)}] Ag {agencia} / Conta {conta}")
        
        # Consultar extrato
        resultado = consultar_extrato(agencia, conta, token, usar_mock=True)
        
        if resultado['sucesso']:
            print(f"    [OK] {len(resultado['dados'])} lancamentos")
            
            # Guardar dados
            dados_extratos[f"{agencia}-{conta}"] = resultado['dados']
            
            # Log
            resultados.append({
                'agencia': agencia,
                'conta': conta,
                'status': 'OK',
                'qtd_lancamentos': len(resultado['dados'])
            })
        else:
            print(f"    [ERRO] {resultado['erro']}")
            
            # Log de erro
            resultados.append({
                'agencia': agencia,
                'conta': conta,
                'status': f"ERRO: {resultado['erro']}",
                'qtd_lancamentos': 0
            })
    
    # 4. GERAR PLANILHA FINAL
    print("\n[4/4] Gerando planilha final...")
    
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    arquivo_saida = output_dir / "extrato.xlsx"
    
    with pd.ExcelWriter(arquivo_saida, engine='openpyxl') as writer:
        
        # Criar aba para cada conta com dados
        for nome_conta, lancamentos in dados_extratos.items():
            if lancamentos:
                df_extrato = pd.DataFrame(lancamentos)
                df_extrato.to_excel(writer, sheet_name=nome_conta, index=False)
                print(f"  [OK] Aba criada: {nome_conta}")
        
        # Criar aba de LOG
        df_log = pd.DataFrame(resultados)
        df_log.to_excel(writer, sheet_name='Log_Execucao', index=False)
        print(f"  [OK] Aba criada: Log_Execucao")
    
    print(f"\n[CONCLUIDO] Arquivo salvo: {arquivo_saida}")
    print("=" * 70)

if __name__ == "__main__":
    main()