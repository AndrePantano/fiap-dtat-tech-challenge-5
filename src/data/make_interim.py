import pandas as pd
import datetime
from src.data.load_data import carregar_dados
from pathlib import Path
from src.data.preprocess import limpar_colunas, padronizar_pedra, limpar_idade

# Carregando os dados - notar que aqui as abas estão nomeadas como 
# "PEDE2022", "PEDE2023" e "PEDE2024"
df_2022, df_2023, df_2024 = carregar_dados()

# Colunas - Transformando e padronizando

# Aplica a função de limpeza em cada DataFrame
df_2022 = limpar_colunas(df_2022)
df_2023 = limpar_colunas(df_2023)
df_2024 = limpar_colunas(df_2024)

# Identificando as colunas comuns entre os anos
colunas_comuns = set(df_2022.columns) & set(df_2023.columns) & set(df_2024.columns)

# exibindo as colunas que não são comuns
colunas_2022 = set(df_2022.columns)
colunas_2023 = set(df_2023.columns)
colunas_2024 = set(df_2024.columns)
colunas_unicas_2022 = colunas_2022 - colunas_comuns
colunas_unicas_2023 = colunas_2023 - colunas_comuns
colunas_unicas_2024 = colunas_2024 - colunas_comuns

# removendo a coluna 'destaque_ipv.1' do df_2023
df_2023.drop(columns=['destaque_ipv.1'], inplace=True)
# removendo a coluna 'ativo/_inativo.1' do df_2024
df_2024.drop(columns=['ativo/_inativo.1'], inplace=True)

# removendo a coluna 'pedra_23' do df_2023
df_2023.drop(columns=['pedra_23'], inplace=True)
# renomeando a coluna 'pedra_2023' para 'pedra_23' no df_2023
df_2023.rename(columns={'pedra_2023': 'pedra_23'}, inplace=True)
# renomeando a coluna 'pedra_2024' para 'pedra_24' no df_2024
df_2024.rename(columns={'pedra_2024': 'pedra_24'}, inplace=True)
# removendo a coluna 'inde_23' do df_2023
df_2023.drop(columns=['inde_23'], inplace=True)
# renomeando a coluna 'inde_2023' para 'inde_23' no df_2023
df_2023.rename(columns={'inde_2023': 'inde_23'}, inplace=True)
# removendo a coluna 'inde_24' do df_2024
df_2024.rename(columns={'inde_2024': 'inde_24'}, inplace=True)

# convertendo o nome das colunas do df_2022 para o mesmo nome dos outros anos
df_2022.rename(
    columns={
        "nome": "nome_anonimizado",
        "portug": "por",
        "defas": "defasagem",
        "ano_nasc": "data_de_nasc",
        "idade_22": "idade",
        "ingles": "ing",
        "matem": "mat",
    },
    inplace=True,
)

# Adicionando as colunas 'rec_av3' e 'rec_av4' para o df_2024
df_2024['rec_av3'] = pd.NA
df_2024['rec_av4'] = pd.NA

# Adicionando a coluna "ano_base" para cada DataFrame
df_2022['ano_base'] = 2022
df_2023['ano_base'] = 2023
df_2024['ano_base'] = 2024

# Identificando as colunas comuns entre os anos
colunas_comuns = set(df_2022.columns) & set(df_2023.columns) & set(df_2024.columns)

# Exibindo as colunas que não são comuns
colunas_2022 = set(df_2022.columns)
colunas_2023 = set(df_2023.columns)
colunas_2024 = set(df_2024.columns)
colunas_unicas_2022 = colunas_2022 - colunas_comuns
colunas_unicas_2023 = colunas_2023 - colunas_comuns
colunas_unicas_2024 = colunas_2024 - colunas_comuns

# Unindo os DataFrames em um único DataFrame
df_completo = pd.concat([df_2022, df_2023, df_2024], ignore_index=True)

# Transformando e padronizando
# Removendo a coluna "nome_anonimizado"
df_completo.drop(columns=['nome_anonimizado'], inplace=True)
# Cemovendo o prefixo 'RA-' da coluna 'ra'
df_completo['ra'] = df_completo['ra'].str.replace('RA-', '', regex=False)
# Convertendo a coluna 'ra' para inteiro, tratando erros de conversão   
df_completo['ra'] = pd.to_numeric(df_completo['ra'], errors='coerce').astype('Int64')

# Substitui 'ALFA' da coluna 'fase' por '0' antes de tentar extrair o número
df_completo['fase'] = df_completo['fase'].astype('string') # evita erros caso haja valores numéricos misturados com strings
df_completo['fase'] = df_completo['fase'].replace('ALFA', '0')
df_completo['fase'] = df_completo['fase'].str.extract(r'(\d+)').astype('Int64')

# Convertendo a coluna 'turma' para string
df_completo['turma'] = df_completo['turma'].astype('string')
# Convertendo o valor '9' da coluna 'turma' em 'N/A'
df_completo['turma'] = df_completo['turma'].replace('9', 'a definir')
# Convertendo a turma de 'ALFA C - G0/G1' para 'C' e fazendo o mesmo para as outras turmas
df_completo['turma'] = df_completo['turma'].str.replace('ALFA ', '', regex=False)
df_completo['turma'] = df_completo['turma'].str.replace(' - G0/G1', '', regex=False)
df_completo['turma'] = df_completo['turma'].str.replace(' - G2/G3', '', regex=False)

# Agora converte os valores '1A', '1B', '1C', etc. para apenas 'A', 'B', 'C', etc.
df_completo['turma'] = df_completo['turma'].str.replace(r'^\d+', '', regex=True)

# Padronizando a coluna 'genero' para ter apenas 'masculino' e 'feminino'
df_completo['genero'] = df_completo['genero'].str.lower().str.strip()
df_completo['genero'] = df_completo['genero'].replace({'menino': 'masculino', 'menina': 'feminino'})

# Padronizando as colunas das pedras de 'pedra_20' a 'pedra_24'
for i in range(20, 25):
    df_completo[f'pedra_{i}'] = padronizar_pedra(df_completo[f'pedra_{i}'])

# Converte converte o valor 'incluir' em nulo
for i in range(20, 25):
    df_completo[f'pedra_{i}'] = df_completo[f'pedra_{i}'].replace('incluir', pd.NA)

# Convertendo a data de narcimento que contem apenas o ano para o formato "01/01/AAAA" para manter a consistência com os outros anos
df_completo['data_de_nasc'] = df_completo['data_de_nasc'].apply(lambda x: f"01/01/{x}" if isinstance(x, (int, float)) else x)   
# Convertendo a coluna 'data_de_nasc' do formato timestamp para datetime no formato "DD/MM/AAAA", tratando erros com 'coerce' para evitar problemas de conversão
df_completo['data_de_nasc'] = pd.to_datetime(df_completo['data_de_nasc'], errors='coerce').dt.strftime('%d/%m/%Y')

# Aplicando a função na coluna
df_completo['idade'] = df_completo['idade'].apply(limpar_idade).astype('Int64')

# Transforma os nulos de 'instituicao_de_ensino' em 'outros'
df_completo['instituicao_de_ensino'] = df_completo['instituicao_de_ensino'].fillna('outros')
# Transforma os nulos de 'escola' em 'outros'
df_completo['escola'] = df_completo['escola'].fillna('outros')

# Converte a coluna 'ano_ingresso' em inteiro, tratando erros com 'coerce' para evitar problemas de conversão
df_completo['ano_ingresso'] = pd.to_numeric(df_completo['ano_ingresso'], errors='coerce').astype('Int64')
df_completo['cg'] = pd.to_numeric(df_completo['cg'], errors='coerce').astype('Int64')
df_completo['cf'] = pd.to_numeric(df_completo['cf'], errors='coerce').astype('Int64')
df_completo['ct'] = pd.to_numeric(df_completo['ct'], errors='coerce').astype('Int64')
df_completo['no_av'] = pd.to_numeric(df_completo['no_av'], errors='coerce').astype('Int64')
df_completo['defasagem'] = pd.to_numeric(df_completo['defasagem'], errors='coerce').astype('Int64')
df_completo['ano_base'] = pd.to_numeric(df_completo['ano_base'], errors='coerce').astype('Int64')

# Converte a coluna 'inde_22' em float, tratando erros com 'coerce' para evitar problemas de conversão
df_completo['inde_22'] = pd.to_numeric(df_completo['inde_22'], errors='coerce').astype('Float64')
df_completo['inde_23'] = pd.to_numeric(df_completo['inde_23'], errors='coerce').astype('Float64')
df_completo['iaa'] = pd.to_numeric(df_completo['iaa'], errors='coerce').astype('Float64')
df_completo['ieg'] = pd.to_numeric(df_completo['ieg'], errors='coerce').astype('Float64')
df_completo['ips'] = pd.to_numeric(df_completo['ips'], errors='coerce').astype('Float64')
df_completo['ida'] = pd.to_numeric(df_completo['ida'], errors='coerce').astype('Float64')
df_completo['mat'] = pd.to_numeric(df_completo['mat'], errors='coerce').astype('Float64')
df_completo['por'] = pd.to_numeric(df_completo['por'], errors='coerce').astype('Float64')
df_completo['ing'] = pd.to_numeric(df_completo['ing'], errors='coerce').astype('Float64')
df_completo['ipv'] = pd.to_numeric(df_completo['ipv'], errors='coerce').astype('Float64')
df_completo['ian'] = pd.to_numeric(df_completo['ian'], errors='coerce').astype('Float64')
df_completo['ipp'] = pd.to_numeric(df_completo['ipp'], errors='coerce').astype('Float64')

# Converte a coluna 'rec_av1' em string, tratando erros com 'coerce' para evitar problemas de conversão
df_completo['rec_av1'] = df_completo['rec_av1'].astype('string')
df_completo['rec_av2'] = df_completo['rec_av2'].astype('string')
df_completo['rec_av3'] = df_completo['rec_av3'].astype('string')
df_completo['rec_av4'] = df_completo['rec_av4'].astype('string')
df_completo['rec_psicologia'] = df_completo['rec_psicologia'].astype('string')
df_completo['indicado'] = df_completo['indicado'].astype('string')
df_completo['atingiu_pv'] = df_completo['atingiu_pv'].astype('string')
df_completo['destaque_ieg'] = df_completo['destaque_ieg'].astype('string')
df_completo['destaque_ida'] = df_completo['destaque_ida'].astype('string')
df_completo['destaque_ipv'] = df_completo['destaque_ipv'].astype('string')

# Converte o valor 'INCLUIR' da coluna 'inde_24' em nulo
df_completo['inde_24'] = df_completo['inde_24'].replace('INCLUIR', pd.NA)
# Converte a coluna 'inde_24' em float, tratando erros com 'coerce' para evitar problemas de conversão
df_completo['inde_24'] = pd.to_numeric(df_completo['inde_24'], errors='coerce').astype('Float64')

# Agrupando as colunas de acordo com o tipo de informação

# Definindo as listas de colunas por grupo
cols_identificacao = ['ra', 'genero', 'data_de_nasc', 'idade']
cols_contexto = ['escola', 'instituicao_de_ensino', 'ano_ingresso', 'fase', 'turma', 'fase_ideal', 'ativo/_inativo' , 'defasagem']

# Os indicadores principais que são o core do desafio
cols_indicadores_chave = ['ian', 'ida', 'ieg', 'iaa', 'ips', 'ipp', 'ipv', 'atingiu_pv']

# Disciplinas e sub-conceitos
cols_notas_disciplinas = ['mat', 'por', 'ing', 'cg', 'cf', 'ct']

# Evolução temporal do índice global e classificação
cols_historico_global = [
    'pedra_20', 'pedra_21', 
    'pedra_22', 'inde_22', 
    'pedra_23', 'inde_23', 
    'pedra_24', 'inde_24'
]

# Dados de quem avaliou e textos de recomendação/destaque
cols_avaliacoes_feedback = [
    'no_av', 'avaliador1', 'rec_av1', 'avaliador2', 'rec_av2', 
    'avaliador3', 'rec_av3', 'avaliador4', 'rec_av4', 'avaliador5', 'avaliador6', 
    'rec_psicologia', 'indicado', 'destaque_ieg', 'destaque_ida', 'destaque_ipv'
]

cols_metadados = ['ano_base']

# Criando a nova ordem completa
nova_ordem = (cols_identificacao + cols_contexto + cols_indicadores_chave + 
              cols_notas_disciplinas + cols_historico_global + 
              cols_avaliacoes_feedback + cols_metadados)

# Reordenando o DataFrame
df_completo = df_completo[nova_ordem]

# Gerando o arquivo ajustado
BASE_DIR = Path(__file__).resolve().parents[2]

OUTPUT_DIR = BASE_DIR / "data" / "interim"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "pede_interim.csv"

df_completo.to_csv(
    OUTPUT_FILE,
    sep=";",
    index=False
)