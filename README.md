# 📊 Datathon – Associação Passos Mágicos

## 🧠 Sobre o projeto
Este projeto foi desenvolvido como parte do Datathon da PosTech, com o objetivo de gerar insights e soluções baseadas em dados para a Associação Passos Mágicos, uma organização com mais de 35 anos de atuação que transforma a vida de crianças e jovens em situação de vulnerabilidade social por meio da educação.

A análise utiliza dados educacionais dos anos 2022, 2023 e 2024 para responder perguntas estratégicas de negócio, gerar insights acionáveis e construir um modelo preditivo de risco de defasagem escolar.

## 🎯 Objetivos
- Analisar o desenvolvimento educacional dos alunos
- Identificar padrões de desempenho, engajamento e aspectos psicossociais
- Avaliar a efetividade do programa educacional
- Criar um modelo preditivo para antecipar risco de defasagem
- Disponibilizar uma aplicação interativa com Streamlit

## 📌 Perguntas de negócio abordadas
- Evolução da defasagem dos alunos (IAN)
- Tendência de desempenho acadêmico (IDA)
- Relação entre engajamento e desempenho (IEG)
- Coerência da autoavaliação (IAA)
- Impacto de fatores psicossociais (IPS)
- Validação psicopedagógica (IPP)
- Identificação de fatores que influenciam o ponto de virada (IPV)
- Combinação de indicadores que impactam o INDE
- Previsão de risco com Machine Learning
- Avaliação da efetividade do programa

## 🧪 Tecnologias utilizadas
- Python
- Pandas / NumPy
- Scikit-learn
- Matplotlib / Seaborn / Plotly
- Streamlit
- Jupyter Notebook

## 🏗️ Arquitetura do projeto
    fiap-dtat-tech-challenge-5/
    ├── app/
    │   ├── components/         # Componentes da aplicação
    │   ├── pages/              # Tabs da aplicação
    │   ├── services/           # Regras de negócios e Funções Analíticas
    │   ├── styles/             # Estilos CSS da aplicação
    │   └── utils/              # Funções reutilizáveis
    │
    ├── data/
    │   ├── raw/                # Dados brutos (originais)
    │   ├── interim/            # Dados para análise
    │   └── processed/          # Dados tratado (produção)
    │
    ├── docs/
    │   ├── Dicionário Dados Datathon.pdf    # Dicionário de dados
    │   ├── PEDE_ Pontos importantes.pdf     # Como os indicadores são construídos
    │   └── POSTECH - Datathon - Fase 5.pdf  # Detalhes do Datathon
    │
    ├── models/
    │   └── modelo_risco_passos_magicos.pkl   # Modelo treinado
    │
    ├── notebooks/
    │   ├── 00_pre_eda.ipynb     # Preparação dos dados antes da Análise exploratória
    │   ├── 01_eda.ipynb         # Análise exploratória (Respondendo as perguntas) - Storytelling Técnico
    │   ├── 02_feature_eng.ipynb # Engenharia de atributos
    │   ├── 03_model.ipynb       # Modelagem preditiva
    │   └── 04_evaluation.ipynb  # Avaliação dos modelos
    │
    ├── reports/
    │   ├── roc_curve.png                                          # Gráfico da Curva ROC do modelo treinado
    │   ├── metrics.json                                           # Métricas do modelo treinado
    │   └── Apresentação Executiva - Datathon Passos Mágicos.pdf   # Apresentação Executiva
    │
    ├── src/
    │   ├── data/
    │   │   ├── load_data.py    # Carrega os dados brutos
    │   │   ├── make_interim.py # Processa os dados brutos 
    │   │   └── preprocess.py   # Biblioteca de funções para reaproveitamento
    │   │
    │   ├── features/
    │   │   └──  build_features.py # Gera o dataset para ser consumido pelo modelo
    │   │
    │   ├── models/
    │   │   ├── train.py        # Treina e cria o modelo preditivo escolhido
    │   │   └── evaluate.py     # Avalia o modelo usando métricas
    |   |
    │   ├── config.py       # Configuração com constantes como variáveis de ambiente com o diretórios e arquivos
    │   ├── constants.py    # Váriaveis que armazenam a configuração consumida pelo pipeline e o app
    │   └── pipeline.py     # Script com o roteiro de execução para a geração do modelo
    │
    ├── streamlit_app.py    # Aplicação principal do Streamlit
    ├── requirements.txt    # Pacotes necessários para rodar o projeto
    ├── README.md
    └── .gitignore


## 🤖 Modelo preditivo

O modelo foi desenvolvido para prever a probabilidade de um aluno entrar em risco de defasagem, utilizando:

Etapas:
- Feature Engineering
- Separação treino/teste
- Treinamento de modelos
- Avaliação (ex: accuracy, recall, ROC-AUC)
- Exportação do modelo

## 📈 Aplicação Streamlit

A aplicação permite:
- Visualizar indicadores educacionais
- Explorar insights da análise
- Simular risco de defasagem de alunos
- Apoiar decisões pedagógicas

## ▶️ Como rodar localmente:
    # Clone o repositório
    git clone https://github.com/AndrePantano/fiap-dtat-tech-challenge-5.git
    
    # Acesse a pasta
    cd fiap-dtat-tech-challenge-5
    
    # Instale as dependências
    pip install -r requirements.txt
    
    # Executar o pipeline do modelo
    python -m src.pipeline

    # Execute o app
    python -m streamlit run streamlit_app.py

## 🚀 Aplicação online
- Streamlit App: [https://fiap-dtat-tech-challenge-f5.streamlit.app/](https://fiap-dtat-tech-challenge-f5.streamlit.app/)

## 📦 Entregáveis do projeto
- Código no GitHub
- Notebook com modelo preditivo
- Apresentação (PPT ou PDF)
- Aplicação em Streamlit (deploy)
- Vídeo de apresentação (até 5 minutos)

## 💡 Principais insights esperados
- Identificação precoce de alunos em risco
- Relação entre engajamento e desempenho
- Impacto de fatores psicossociais
- Evidência da efetividade do programa educacional

## 🤝 Contribuição
Sinta-se à vontade para contribuir com melhorias, novas análises ou otimizações no modelo.

## 📄 Licença
Este projeto é de caráter educacional e sem fins lucrativos.

Fique à vontade para explorá-lo!
