# Імпортуємо необхідні бібліотеки
from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, PULP_CBC_CMD

# Створюємо нову задачу лінійного програмування для максимізації
model = LpProblem(name="Оптимізація-виробництва", sense=LpMaximize)

# Оголошуємо змінні рішення: кількість виробленого лимонаду та фруктового соку
lemonade = LpVariable(name="Лимонад", lowBound=0, cat='Integer')
fruit_juice = LpVariable(name="Фруктовий сік", lowBound=0, cat='Integer')

# Додаємо цільову функцію: максимізувати загальну кількість продуктів
model += lemonade + fruit_juice, "Загальна кількість продуктів"

# Додаємо обмеження на ресурси

# Обмеження на воду
model += (2 * lemonade + 1 * fruit_juice <= 100), "Обмеження на воду"

# Обмеження на цукор
model += (1 * lemonade <= 50), "Обмеження на цукор"

# Обмеження на лимонний сік
model += (1 * lemonade <= 30), "Обмеження на лимонний сік"

# Обмеження на фруктове пюре
model += (2 * fruit_juice <= 40), "Обмеження на фруктове пюре"

# Розв'язуємо задачу
status = model.solve(PULP_CBC_CMD(msg=False))

# Виводимо результати
print(f"Статус розв'язку: {LpStatus[model.status]}, {'Максимізація' if model.sense == LpMaximize else 'Мінімізація'}")

print(f"Оптимальна кількість виробленого лимонаду: {lemonade.varValue}")
print(f"Оптимальна кількість виробленого фруктового соку: {fruit_juice.varValue}")

print(f"Максимальна загальна кількість продуктів: {model.objective.value()}")
