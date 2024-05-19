import numpy as np
from scipy.stats import norm

# Função para calcular a probabilidade de aprovação com base em uma distribuição normal
def prob_aprovacao(media, desvio_padrao, limite_aprovacao):
    """
    Calcula a probabilidade de um aluno ser aprovado com base em uma distribuição normal.

    Parâmetros:
    media (float): Média das notas dos alunos.
    desvio_padrao (float): Desvio padrão das notas dos alunos.
    limite_aprovacao (float): Limite de nota para aprovação.

    Retorna:
    float: Probabilidade de um aluno ser aprovado.
    """
    if desvio_padrao <= 0:
        raise ValueError("O desvio padrão deve ser maior que zero.")
    
    z_score = (limite_aprovacao - media) / desvio_padrao
    prob_aprovacao = norm.cdf(z_score)
    return prob_aprovacao

# Exemplo de uso da função
media_notas = 70  # Média das notas dos alunos
desvio_padrao = 10  # Desvio padrão das notas dos alunos
limite_aprovacao = 60  # Limite de nota para aprovação

try:
    probabilidade_aprovacao = prob_aprovacao(media_notas, desvio_padrao, limite_aprovacao)
    print("Probabilidade de aprovação:", probabilidade_aprovacao)
except ValueError as e:
    print("Erro:", e)
