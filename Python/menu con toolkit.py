from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import radiolist_dialog

options = [
    ('Opción 1', 'opcion_1'),
    ('Opción 2', 'opcion_2'),
    ('Opción 3', 'opcion_3'),
    ('Salir', 'salir'),
]

selected_option = radiolist_dialog(
    title='Menú de Opciones',
    values=options,
).run()

if selected_option == 'salir':
    exit()
else:
    print(f'Has seleccionado: {selected_option}')
