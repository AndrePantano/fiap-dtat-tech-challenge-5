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
    datathon-passos-magicos/
    │
    ├── data/
    │   ├── raw/                # Dados brutos (originais)
    │   ├── processed/          # Dados tratados
    │   └── external/           # Dados externos (se houver)
    │
    ├── notebooks/
    │   ├── 01_eda.ipynb         # Análise exploratória
    │   ├── 02_feature_eng.ipynb # Engenharia de atributos
    │   ├── 03_model.ipynb       # Modelagem preditiva
    │   └── 04_evaluation.ipynb  # Avaliação dos modelos
    │
    ├── src/
    │   ├── data/
    │   │   ├── load_data.py
    │   │   ├── preprocess.py
    │   │
    │   ├── features/
    │   │   ├── build_features.py
    │   │
    │   ├── models/
    │   │   ├── train.py
    │   │   ├── predict.py
    │   │   └── evaluate.py
    │   │
    │   ├── visualization/
    │   │   ├── plots.py
    │
    │   └── utils/
    │       ├── helpers.py
    │
    ├── app/
    │   ├── streamlit_app.py    # Aplicação principal
    │   ├── pages/              # Páginas adicionais (opcional)
    │   └── components/         # Componentes reutilizáveis
    │
    ├── models/
    │   ├── trained_model.pkl   # Modelo treinado
    │   └── scaler.pkl         # Normalizadores (se aplicável)
    │
    ├── reports/
    │   ├── presentation.pdf    # Storytelling executivo PDF ou PPTX
    │   └── figures/            # Gráficos exportados
    │
    ├── requirements.txt
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
    git clone https://github.com/seu-repo/datathon-passos-magicos.git
    
    # Acesse a pasta
    cd datathon-passos-magicos
    
    # Instale as dependências
    pip install -r requirements.txt
    
    # Execute o app
    streamlit run app/streamlit_app.py

## 🚀 Deploy
A aplicação deve ser publicada no:
- Streamlit Community Cloud

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
