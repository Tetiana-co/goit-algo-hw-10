import pulp

model = pulp.LpProblem("Maximize_Beverage_Production", pulp.LpMaximize)
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

model += lemonade + fruit_juice  # Цільова функція

# Обмеження
model += 2 * lemonade + fruit_juice <= 100  # Вода
model += lemonade <= 50  # Цукор
model += lemonade <= 30  # Лимонний сік
model += 2 * fruit_juice <= 40  # Фруктове пюре

model.solve()

print(f"Лимонад: {lemonade.value()}, Сік: {fruit_juice.value()}, Всього: {lemonade.value() + fruit_juice.value()}")
