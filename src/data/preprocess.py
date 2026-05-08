import datetime

# Cria funcao "limpar_colunas" para limpar e padronizar os nomes das colunas
def limpar_colunas(df):
    df.columns = (
        df.columns.str.strip()  # Remove espaços em branco
        .str.lower()  # Converte para minúsculas
        .str.replace(" ", "_")  # Substitui espaços por underscores
        .str.replace("(", "")  # Remove parênteses
        .str.replace(")", "")  # Remove parênteses
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8") # remove acentos        
    )
    return df

# Remove acentos e normaliza os nomes das colunas de pedra
def padronizar_pedra(coluna):
    coluna = coluna.str.lower().str.strip()
    coluna = coluna.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    return coluna

# padronizar idade
def limpar_idade(valor):
    # Se for um objeto de data, pegamos apenas o dia
    if isinstance(valor, datetime.datetime):
        return valor.day
    # Se for um número (ou string de número), convertemos para inteiro
    try:
        return int(float(valor))
    except:
        return None # Caso haja algum valor bizarro que não seja data nem número