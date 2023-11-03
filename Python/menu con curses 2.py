import curses

def main(stdscr):
    curses.curs_set(0)  # Oculta el cursor
    stdscr.clear()
    stdscr.refresh()
    stdscr.keypad(1)

    opciones = [
        "✨ Opción 1",
        "✨ Opción 2",
        "✨ Opción 3",
        "✨ Salir",
    ]
    seleccion = 0

    while True:
        stdscr.clear()
        altura, ancho = stdscr.getmaxyx()

        # Configuración de colores personalizados
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

        # Efecto visual de separador
        stdscr.attron(curses.color_pair(3))
        stdscr.hline(altura // 2 - 1, 0, "-", ancho)
        stdscr.attroff(curses.color_pair(3))

        for i, opcion in enumerate(opciones):
            x = ancho // 2 - len(opcion) // 2
            y = altura // 2 - len(opciones) // 2 + i

            if i == seleccion:
                stdscr.attron(curses.color_pair(1) | curses.A_BOLD)
                stdscr.addstr(y, x, opcion)
                stdscr.attroff(curses.color_pair(1) | curses.A_BOLD)
            else:
                stdscr.attron(curses.color_pair(2))
                stdscr.addstr(y, x, opcion)
                stdscr.attroff(curses.color_pair(2))

        stdscr.refresh()

        tecla = stdscr.getch()

        if tecla == curses.KEY_UP and seleccion > 0:
            seleccion -= 1
        elif tecla == curses.KEY_DOWN and seleccion < len(opciones) - 1:
            seleccion += 1
        elif tecla == 10:  # Tecla Enter
            if seleccion == len(opciones) - 1:
                break

if __name__ == "__main__":
    curses.wrapper(main)
