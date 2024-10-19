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

    return fig, ax


# Визуализация: Спираль золотого сечения (спираль Фибоначчи) на распределении простых чисел
def add_golden_spiral(ax, limit, point_size, color):
    phi = (1 + np.sqrt(5)) / 2  # Золотое сечение
    theta = np.linspace(0, 4 * np.pi, limit)  # Угловая координата
    r = phi ** theta  # Радиальная координата

    x = r * np.cos(theta)
    y = r * np.sin(theta)

    ax.scatter(x, y, s=point_size, c=color, alpha=0.75, label="Golden Spiral")


# Интерфейс Streamlit
st.title("Визуализация простых чисел")

# Ползунки для управления
limit = st.slider('Предел для поиска простых чисел', min_value=1000, max_value=1000000, value=100000, step=1000)
point_size = st.slider('Размер точек', min_value=1, max_value=20, value=5)

# Выбор цвета для точек распределения простых чисел
prime_color = st.color_picker('Цвет точек для простых чисел', '#FF0000')

# Флажок для включения/отключения спирали золотого сечения
show_golden_spiral = st.checkbox('Отобразить спираль золотого сечения')

# Если отображение спирали включено, то также появляется выбор цвета
if show_golden_spiral:
    spiral_color = st.color_picker('Цвет точек для спирали золотого сечения', '#00FF00')

# Построение графика
fig, ax = plot_spiral_primes(limit, point_size, prime_color)

# Добавление спирали золотого сечения, если выбрано
if show_golden_spiral:
    add_golden_spiral(ax, limit, point_size, spiral_color)

# Отображение графика
st.pyplot(fig)
