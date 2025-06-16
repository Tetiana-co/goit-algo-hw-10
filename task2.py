import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# --- 1. Графік функції та області під кривою ---
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від 0 до 2')
plt.grid()
plt.show()

# --- 2. Метод Монте-Карло ---
def monte_carlo_integrate(f, a, b, N=10**6):
    x_rand = np.random.uniform(a, b, N)
    y_rand = f(x_rand)
    integral = (b - a) * np.mean(y_rand)
    return integral

N = 1_000_000
result_mc = monte_carlo_integrate(f, a, b, N)
print(f"Метод Монте-Карло: {result_mc:.6f}")

# --- 3. Аналітичний розрахунок ---
result_analytical = (b**3 - a**3) / 3
print(f"Аналітичний розрахунок: {result_analytical:.6f}")

# --- 4. SciPy quad ---
result_quad, error = spi.quad(f, a, b)
print(f"SciPy quad: {result_quad:.6f} (помилка: {error:.2e})")
