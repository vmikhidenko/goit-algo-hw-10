import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Визначення функції, яку потрібно інтегрувати
def f(x):
    return np.sin(x)

# Межі інтегрування
a = 0          # Нижня межа
b = np.pi      # Верхня межа
num_points = 100000  # Кількість випадкових точок для методу Монте-Карло

# Максимальне значення функції на інтервалі [a, b]
f_max = 1.0  # Оскільки sin(x) досягає максимуму 1

# Метод Монте-Карло для обчислення інтегралу
np.random.seed(0)  # Для відтворюваності результатів
x_random = np.random.uniform(a, b, num_points)
y_random = np.random.uniform(0, f_max, num_points)
under_curve = y_random < f(x_random)
area_monte_carlo = (under_curve.sum() / num_points) * (b - a) * f_max

# Перевірка результату за допомогою SciPy функції quad
result_quad, error_quad = spi.quad(f, a, b)

# Виведення результатів
print("Результат Монте-Карло: ", area_monte_carlo)
print("Результат SciPy quad: ", result_quad)
print("Абсолютна похибка функції quad: ", error_quad)

# Візуалізація графіка
x_values = np.linspace(a - 0.5, b + 0.5, 400)
y_values = f(x_values)

fig, ax = plt.subplots()
ax.plot(x_values, y_values, 'r', linewidth=2)
ix = np.linspace(a, b, 400)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x_values[0], x_values[-1]])
ax.set_ylim([0, f_max + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) від {} до {}'.format(a, b))
plt.grid()
plt.show()
