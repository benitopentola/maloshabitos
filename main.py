import tkinter as tk
import time

root = tk.Tk()
root.title("Control de Malos Hábitos")

# Crear una lista para almacenar los malos hábitos y un diccionario para el tiempo de inicio
habits_list = []
habits_time = {}

# Crear una etiqueta para el cuadro de texto
label = tk.Label(root, text="Introduce el mal hábito:")
label.pack()

# Crear el cuadro de texto
habit_input = tk.Entry(root)
habit_input.pack()

# Crear un botón para enviar el mal hábito
def submit_habit():
    habit_name = habit_input.get()
    habits_list.append(habit_name)
    habits_time[habit_name] = time.time()
    update_habits()

submit_button = tk.Button(root, text="Enviar", command=submit_habit)
submit_button.pack()

# Crear una función para actualizar la lista de hábitos en la pantalla
def update_habits():
    habits_string = "\n".join(habits_list)
    habits_label.config(text=habits_string)
    for habit in habits_list:
        duration = int(time.time() - habits_time[habit])
        habits_time_label[habit].config(text=f'{duration} seconds')

# Crear una etiqueta para mostrar la lista de hábitos
habits_label = tk.Label(root)
habits_label.pack()

# Crear una etiqueta para mostrar el tiempo transcurrido para cada hábito
habits_time_label = {}
for habit in habits_list:
    habits_time_label[habit] = tk.Label(root)
    habits_time_label[habit].pack()

# Crear un botón para reiniciar el cronómetro para cada hábito
def reset_timer(habit_name):
    habits_time[habit_name] = time.time()
    update_habits()

for habit in habits_list:
    reset_button = tk.Button(root, text="Reiniciar", command=lambda: reset_timer(habit))
    reset_button.pack()

root.mainloop()

