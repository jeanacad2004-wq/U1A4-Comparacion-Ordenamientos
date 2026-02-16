import random
import statistics as stats
import timeit
import csv
from typing import List, Dict, Tuple

# -----------------------------
# 1) Implementaciones de ordenamiento
# -----------------------------
def bubble_sort(arr: List[int]) -> List[int]:
    """Ordena una lista usando Bubble Sort (O(n^2)). Devuelve una NUEVA lista."""
    a = arr.copy()
    n = len(a)

    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

    return a


def quicksort(arr: List[int]) -> List[int]:
    """
    Quicksort recursivo (promedio O(n log n)).
    Devuelve una NUEVA lista.
    """
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + mid + quicksort(right)


# -----------------------------
# 2) Generación de datos (tamaños + escenarios)
# -----------------------------
def generate_data(n: int, scenario: str, seed: int = 42) -> List[int]:
    """
    scenario:
      - "random": lista aleatoria
      - "reversed": lista invertida
    """
    rnd = random.Random(seed + n)  # semilla estable por tamaño

    if scenario == "random":
        a = list(range(n))
        rnd.shuffle(a)
        return a

    if scenario == "reversed":
        return list(range(n, 0, -1))

    raise ValueError("Escenario no válido. Usa: random, reversed")


# -----------------------------
# 3) Medición con timeit + repeticiones
# -----------------------------
def measure_sort_time(sort_fn, data: List[int], repeats: int = 5) -> Tuple[float, float, List[float]]:
    """
    Mide tiempos (segundos) usando timeit con múltiples repeticiones.
    Devuelve: (promedio, desviación_estándar, lista_de_tiempos)
    """
    timer = timeit.Timer(lambda: sort_fn(data))
    times = timer.repeat(repeat=repeats, number=1)

    mean_t = stats.mean(times)
    stdev_t = stats.stdev(times) if repeats > 1 else 0.0

    return mean_t, stdev_t, times


# -----------------------------
# 4) Ejecución del experimento
# -----------------------------
def run_experiment(
    sizes=(100, 1000, 5000, 10000),
    scenarios=("random", "reversed"),
    repeats=5
) -> List[Dict]:
    algorithms = [
        ("Burbuja", bubble_sort),
        ("Quicksort", quicksort),
    ]

    results = []

    for scenario in scenarios:
        for n in sizes:
            data = generate_data(n, scenario=scenario)

            for alg_name, alg_fn in algorithms:
                mean_t, stdev_t, _ = measure_sort_time(alg_fn, data, repeats=repeats)

                results.append({
                    "escenario": scenario,
                    "n": n,
                    "algoritmo": alg_name,
                    "repeticiones": repeats,
                    "promedio_s": mean_t,
                    "desv_std_s": stdev_t
                })

    return results


# -----------------------------
# 5) Imprimir tabla en consola
# -----------------------------
def print_results_table(results: List[Dict]) -> None:
    header = f"{'Escenario':<12} {'n':>8} {'Algoritmo':<10} {'Rep':>4} {'Promedio (s)':>14} {'DesvStd (s)':>12}"
    print(header)
    print("-" * len(header))

    for r in results:
        print(
            f"{r['escenario']:<12} "
            f"{r['n']:>8} "
            f"{r['algoritmo']:<10} "
            f"{r['repeticiones']:>4} "
            f"{r['promedio_s']:>14.6f} "
            f"{r['desv_std_s']:>12.6f}"
        )


# -----------------------------
# 6) Guardar resultados en CSV
# -----------------------------
def save_results_to_csv(results: List[Dict], filename: str = "resultados_ordenamiento.csv") -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Encabezados
        writer.writerow([
            "escenario",
            "n",
            "algoritmo",
            "repeticiones",
            "promedio_s",
            "desv_std_s"
        ])

        # Filas
        for r in results:
            writer.writerow([
                r["escenario"],
                r["n"],
                r["algoritmo"],
                r["repeticiones"],
                r["promedio_s"],
                r["desv_std_s"]
            ])

    print(f"\n✅ CSV guardado como: {filename}")


# -----------------------------
# 7) MAIN
# -----------------------------
if __name__ == "__main__":
    results = run_experiment(
        sizes=(100, 1000, 5000, 10000),
        scenarios=("random", "reversed"),
        repeats=5
    )

    print_results_table(results)
    save_results_to_csv(results)