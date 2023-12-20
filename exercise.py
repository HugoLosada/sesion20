import PySimpleGUI as sg

def main():
    # Definir el diseño de la interfaz de usuario
    layout = [
        [sg.InputText(key='-NUM1-'), sg.Text('+'), sg.InputText(key='-NUM2-')],
        [sg.Button('Sumar'), sg.Text('Resultado:'), sg.Text('', key='-RESULT-')],
    ]

    # Crear la ventana
    window = sg.Window('Calculadora Simple', layout)

    # Bucle principal para manejar eventos
    while True:
        event, values = window.read()

        # Salir del bucle si se cierra la ventana
        if event == sg.WINDOW_CLOSED:
            break

        # Manejar eventos del botón Sumar
        if event == 'Sumar':
            num1 = values['-NUM1-']
            num2 = values['-NUM2-']

            # Validar si los campos de entrada contienen números
            if num1.isdigit() and num2.isdigit():
                result = int(num1) + int(num2)
                window['-RESULT-'].update(result)
            else:
                sg.popup_error('Por favor, ingresa números válidos.')

    # Cerrar la ventana al salir del bucle
    window.close()

if __name__ == '__main__':
    main()