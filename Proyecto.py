import numpy as np
from collections import Counter

def simulate_match(xg_home, xg_away, n_sim=50000):
    """
    Simula un partido usando:
    - Distribución de Poisson para modelar goles.
    - Monte Carlo para repetir muchos escenarios.
    - Probabilidad compuesta para calcular resultados.
    """

    # Goles generados por Poisson
    home_goals = np.random.poisson(xg_home, n_sim)
    away_goals = np.random.poisson(xg_away, n_sim)

    # Contadores
    home_win = np.sum(home_goals > away_goals)
    draw = np.sum(home_goals == away_goals)
    away_win = np.sum(home_goals < away_goals)

    # Probabilidades
    p_home_win = home_win / n_sim * 100
    p_draw = draw / n_sim * 100
    p_away_win = away_win / n_sim * 100

    # Marcadores más probables
    scores = list(zip(home_goals, away_goals))
    most_common_score, freq = Counter(scores).most_common(1)[0]

    return p_home_win, p_draw, p_away_win, most_common_score


# ------------------------------- #
#          PROGRAMA PRINCIPAL
# ------------------------------- #

print("=== PREDICCIÓN SIMPLE DE PARTIDO ===")
print("Modelo: Poisson + Monte Carlo\n")

# Ingresas directamente los valores xG de cada equipo
xg_home = float(input("Ingresa xG del equipo LOCAL: "))
xg_away = float(input("Ingresa xG del equipo VISITANTE: "))

# Simulación
p_home, p_empate, p_away, marcador = simulate_match(xg_home, xg_away)

# Resultados
print("\n--- RESULTADOS DE LA SIMULACIÓN ---")
print(f"Probabilidad de victoria LOCAL:     {p_home:.2f}%")
print(f"Probabilidad de EMPATE:             {p_empate:.2f}%")
print(f"Probabilidad de victoria VISITANTE: {p_away:.2f}%")

print("\nMarcador más probable:")
print(f"{marcador[0]} - {marcador[1]}")

