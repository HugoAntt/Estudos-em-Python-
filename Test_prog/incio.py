import numpy as np
from scipy.stats import norm

# Função para calcular a probabilidade de aprovação com base em uma distribuição normal
def prob_aprovacao(media, desvio_padrao, limite_aprovacao):
    z_score = (limite_aprovacao - media) / desvio_padrao
    prob_aprovacao = norm.cdf(z_score)
    return prob_aprovacaoF

# Exemplo de uso da função
media_notas = 70  # Média das notas dos alunos
desvio_padrao = 10  # Desvio padrão das notas dos alunos
limite_aprovacao = 60  # Limite de nota para aprovação

probabilidade_aprovacao = prob_aprovacao(media_notas, desvio_padrao, limite_aprovacao)
print("Probabilidade de aprovação:", probabilidade_aprovacao)
