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


# Визуализация: Прямоугольная спираль простых чисел
def plot_spiral_primes(limit, point_size, color):
    primes = sieve_of_eratosthenes(limit)

    x = np.sqrt(primes) * np.cos(primes)
    y = np.sqrt(primes) * np.sin(primes)

    fig, ax = plt.subplots(figsize=(10, 10), facecolor='black')
    ax.scatter(x, y, s=point_size, c=color, alpha=0.75)
    ax.set_facecolor('black')
    ax.set_title(f"Prime Number Spiral (up to {limit})", color='white')
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    return fig


# Визуализация: Полярное распределение простых чисел
def plot_polar_primes(limit, point_size, color):
    primes = sieve_of_eratosthenes(limit)

    theta = primes % (2 * np.pi)
    r = np.sqrt(primes)

    fig = plt.figure(figsize=(10, 10), facecolor='black')
    ax = fig.add_subplot(111, projection='polar')
    ax.scatter(theta, r, s=point_size, c=color, alpha=0.75)
    ax.set_facecolor('black')
    ax.set_title(f"Polar Prime Distribution (up to {limit})", color='white')

    return fig


# Интерфейс Streamlit
st.title("Визуализация простых чисел")

# Ползунки для управления
limit = st.slider('Предел для поиска простых чисел', min_value=1000, max_value=1000000, value=100000, step=1000)
point_size = st.slider('Размер точек', min_value=1, max_value=20, value=5)

# Выбор типа визуализации
plot_type = st.selectbox("Выберите тип визуализации", ["Прямоугольная спираль", "Полярная визуализация"])

# Выбор цвета точек
color = st.color_picker('Выберите цвет точек', '#FF0000')

# Построение графика на основе выбора
if plot_type == "Прямоугольная спираль":
    fig = plot_spiral_primes(limit, point_size, color)
else:
    fig = plot_polar_primes(limit, point_size, color)

# Отображение графика
st.pyplot(fig)
