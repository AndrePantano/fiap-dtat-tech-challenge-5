FEATURES = ['ida', 'ieg', 'ips', 'ipp', 'fase','ipv']
FEATURES_RESUMIDAS = ['ida', 'ieg', 'ips', 'ipp','ipv']
FEATURES_INDICATORS = ["ida","ieg", "ips", "ipp", "ian", "ipv", "iaa"]

FEATURE_LABELS = {
    "ida": "Desempenho acadêmico",
    "ieg": "Engajamento",
    "ips": "Psicossocial",
    "ipp": "Psicopedagógico",
    "ian": "Adequação de nível",
    "ipv": "Ponto de virada",
    "iaa": "Auto Avaliação",
    "fase": "Fase Atual"    
}

FEATURE_HELP = {
    "ida": "Qualidade do desempenho acadêmico do aluno.",
    "ieg": "Nível de participação, constância e envolvimento nas atividades.",
    "ips": "Indicadores psicossociais observados ao longo do acompanhamento.",
    "ipp": "Leitura psicopedagógica do desenvolvimento e do suporte necessário.",
    "ian": "Aderência do aluno ao nível/fase esperada.",
    "ipv": "Sinal de evolução e mudança positiva na trajetória do estudante.",
    "iaa": "Indicador de auto avaliação do aluno",
    "fase": "Fase atual do aluno"    
}

FEATURE_DESCRIPTIONS = {
    "ida": "Principal pilar acadêmico do modelo. Quedas aqui tendem a puxar o risco para cima.",
    "ieg": "Representa tração, presença e participação. O notebook mostra que ele caminha junto com o IDA.",
    "ips": "Tem baixa correlação direta com o risco, mas pode sinalizar efeitos indiretos ou mais tardios.",
    "ipp": "Apoio psicopedagógico aparece como alavanca relevante para evolução e para o IPV.",
    "ian": "Ajuda a contextualizar o nível do aluno, mas não é o principal fator explicativo do risco.",
    "ipv": "Resume o quanto o aluno está virando a curva. Tem forte relação com INDE, IDA e IEG.",
    "fase": "Fase atual do aluno"    
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
    "fase": (
        "Adicionar título",
        "Adicionar ação",
    )
}