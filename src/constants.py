import pandas as pd

FEATURES = ['ida', 'ieg', 'ips', 'ipp', 'fase','idade']

FEATURE_LABELS = {
    "ida": "Desempenho acadêmico",
    "ieg": "Engajamento",
    "ips": "Psicossocial",
    "ipp": "Psicopedagógico",
    "ian": "Adequação de nível",
    "ipv": "Ponto de virada",
    "iaa": "Auto Avaliação"
}

FEATURE_HELP = {
    "ida": "Qualidade do desempenho acadêmico do aluno.",
    "ieg": "Nível de participação, constância e envolvimento nas atividades.",
    "ips": "Indicadores psicossociais observados ao longo do acompanhamento.",
    "ipp": "Leitura psicopedagógica do desenvolvimento e do suporte necessário.",
    "ian": "Aderência do aluno ao nível/fase esperada.",
    "ipv": "Sinal de evolução e mudança positiva na trajetória do estudante.",
    "iaa": "Indicador de auto avaliação do aluno"
}

FEATURE_DESCRIPTIONS = {
    "IDA": "Principal pilar acadêmico do modelo. Quedas aqui tendem a puxar o risco para cima.",
    "IEG": "Representa tração, presença e participação. O notebook mostra que ele caminha junto com o IDA.",
    "IPS": "Tem baixa correlação direta com o risco, mas pode sinalizar efeitos indiretos ou mais tardios.",
    "IPP": "Apoio psicopedagógico aparece como alavanca relevante para evolução e para o IPV.",
    "IAN": "Ajuda a contextualizar o nível do aluno, mas não é o principal fator explicativo do risco.",
    "IPV": "Resume o quanto o aluno está virando a curva. Tem forte relação com INDE, IDA e IEG.",
}

ACTION_LIBRARY = {
    "ida": (
        "Reforço pedagógico focalizado",
        "Priorizar revisão de lacunas em português e matemática, metas quinzenais e trilhas curtas de recuperação.",
    ),
    "ieg": (
        "Plano de engajamento",
        "Aumentar participação com rotina de acompanhamento, pactos de presença, mentorias e metas de entrega.",
    ),
    "ips": (
        "Acolhimento e escuta",
        "Monitorar fatores socioemocionais e abrir acompanhamento preventivo para evitar efeito tardio sobre desempenho.",
    ),
    "ipp": (
        "Ação psicopedagógica integrada",
        "Conectar coordenação, psicopedagogia e tutoria para revisar estratégias de estudo e barreiras de aprendizagem.",
    ),
    "ian": (
        "Adequação de trilha",
        "Rever se a fase, o ritmo e o plano pedagógico estão compatíveis com o momento do aluno.",
    ),
    "ipv": (
        "Consolidação do ponto de virada",
        "Definir marcos de curto prazo, celebrar avanços e manter o aluno em trajetória positiva nas próximas semanas.",
    ),
    "iaa": (
        "Adicionar título",
        "Adicionar ação",
    ),
}

NOTEBOOK_METRICS = {
    "Acurácia": "80%",
    "F1-score": 0.89,
    "Recall para Risco": 0.76,
    "Curva ROC(AUC)" : 0.89
}

DEFAULT_IMPORTANCES = pd.Series({
    "ipp": 0.436157,
    "ieg": 0.237873,
    "ida": 0.162431,
    "ips": 0.087016,
    "iaa": 0.076523
})


DEFAULT_BENCHMARKS = pd.DataFrame(
    {
        "media": {
            "IDA": 6.376,
            "IEG": 7.946,
            "IPS": 6.287,
            "IPP": 7.555,
            "IAN": 7.179,
            "IPV": 7.545,
        },
        "mediana": {
            "IDA": 6.667,
            "IEG": 8.600,
            "IPS": 7.500,
            "IPP": 7.500,
            "IAN": 5.000,
            "IPV": 7.583,
        },
        "q25": {
            "IDA": 5.100,
            "IEG": 7.300,
            "IPS": 5.020,
            "IPP": 7.083,
            "IAN": 5.000,
            "IPV": 6.984,
        },
    }
)
DEFAULT_YEAR_SUMMARY = pd.DataFrame(
    {
        "INDE": {2022: 7.036, 2023: 7.342, 2024: 7.397},
        "IDA": {2022: 6.093, 2023: 6.663, 2024: 6.351},
        "IEG": {2022: 7.891, 2023: 8.699, 2024: 7.375},
        "IPS": {2022: 6.905, 2023: 5.120, 2024: 6.830},
        "IPP": {2022: None, 2023: 7.563, 2024: 7.548},
        "IAN": {2022: 6.424, 2023: 7.244, 2024: 7.684},
        "IPV": {2022: 7.254, 2023: 8.028, 2024: 7.354},
    }
)
DEFAULT_CORRELATIONS = pd.Series(
    {"IDA": 0.785, "IEG": 0.745, "IPV": 0.721, "IPP": 0.540, "IAN": 0.405, "IPS": 0.200}
)
DEFAULT_SAMPLE_SIZE = 2845