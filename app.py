import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# Функция решета Эратосфена для нахождения простых чисел
def sieve_of_eratosthenes(limit):
    sieve = np.ones(limit + 1, dtype=bool)
    sieve[:2] = False
    for num in range(2, int(limit ** 0.5) + 1):
        if sieve[num]:
            sieve[num * num:limit + 1:num] = False
    return np.nonzero(sieve)[0]


# Функция для визуализации
def plot_primes(limit, point_size):
    primes = sieve_of_eratosthenes(limit)

    x = np.sqrt(primes) * np.cos(primes)
    y = np.sqrt(primes) * np.sin(primes)

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.scatter(x, y, s=point_size, c='red', alpha=0.75)
    ax.set_title(f"Prime Number Spiral (up to {limit})")

    return fig


# Интерфейс Streamlit
st.title("Визуализация простых чисел")
limit = st.slider('Предел для поиска простых чисел', min_value=1000, max_value=1000000, value=1000000, step=1000)
point_size = st.slider('Размер точек', min_value=1, max_value=20, value=5)

# Построение графика
fig = plot_primes(limit, point_size)
st.pyplot(fig)
