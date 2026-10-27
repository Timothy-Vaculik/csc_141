from secrets import choice


x_direction = choice([1, -1])

x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

x_step = x_direction * x_distance

y_direction = choice([1, -1])
y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
y_step = y_direction * y_distance