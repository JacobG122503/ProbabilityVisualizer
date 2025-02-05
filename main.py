import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import random
import PySimpleGUI as sg

matplotlib.use('TkAgg')

def main():
    while True:
        layout = [
            [sg.Text("Please pick which Probability Visualizer you want!", justification='center', expand_x=True)],
            [sg.Column([[sg.Button('Die Roll')], [sg.Button('Coin Flip')]],
                       justification='center', element_justification='center', expand_x=True)],
            [sg.Button('Exit')]
        ]

        #Center window
        window = sg.Window('Home Screen', layout, finalize=True, location=(sg.Window.get_screen_size()[0] // 2 - 200, sg.Window.get_screen_size()[1] // 2 - 150))

        event, values = window.read()
        window.close()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Die Roll':
            DieRolling()
        elif event == 'Coin Flip':
            CoinFlip()

def CoinFlip():
    side = ["Heads", "Tails"]
    amount = [0, 0]

    #Input window
    layout = [
        [sg.Text('How many times do you want to flip the coin?')],
        [sg.InputText(key='-INPUT-')],
        [sg.Button('Run'), sg.Button('Back')],
        [sg.Canvas(key='-CANVAS-')]
    ]

    window = sg.Window('Coin Flip Simulator', layout, finalize=True, location=(sg.Window.get_screen_size()[0] // 2 - 200, sg.Window.get_screen_size()[1] // 2 - 150))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Back':
            break
        if event == 'Run':
            try:
                coinFlips = int(values['-INPUT-'])

                for _ in range(coinFlips):
                    coin = random.randint(0, 1)
                    amount[coin] += 1

                #Set up and display bar graph
                fig, ax = plt.subplots()
                ax.bar(side, amount, color='mediumseagreen')
                ax.set_title('Coin Flipping')
                ax.set_xlabel('Side')
                ax.set_ylabel('Amount')

                #Clear previous plot if exists
                for child in window['-CANVAS-'].TKCanvas.winfo_children():
                    child.destroy()

                draw_figure(window['-CANVAS-'].TKCanvas, fig)

            except ValueError:
                sg.popup_error("Please enter a valid number!")

    window.close()

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

def DieRolling():
    attemptsBar = []
    amount = []

    #Input window
    layout = [
        [sg.Text('How many times do you want to roll the die?')],
        [sg.InputText(key='-INPUT-')],
        [sg.Button('Run'), sg.Button('Back')],
        [sg.Canvas(key='-CANVAS-')]
    ]

    window = sg.Window('Die Rolling Simulator', layout, finalize=True, location=(sg.Window.get_screen_size()[0] // 2 - 200, sg.Window.get_screen_size()[1] // 2 - 150))

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Back':
            break
        if event == 'Run':
            try:
                dieInput = int(values['-INPUT-'])
                attemptsBar.clear()
                amount.clear()

                #Clear previous plot if exists
                for child in window['-CANVAS-'].TKCanvas.winfo_children():
                    child.destroy()

                #Set up and display bar graph
                fig, ax = plt.subplots()
                bars = ax.bar([], [], color='mediumseagreen')
                ax.set_title('Die Rolling')
                ax.set_xlabel('Attempt #s')
                ax.set_ylabel('Amount')

                canvas = FigureCanvasTkAgg(fig, window['-CANVAS-'].TKCanvas)
                canvas.draw()
                canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

                data = []

                # Animation update function
                def update(frame):
                    attempts = 1
                    die = random.randint(1, 6)
                    while die != 6:
                        die = random.randint(1, 6)
                        attempts += 1

                    if attempts not in attemptsBar:
                        attemptsBar.append(attempts)
                        amount.append(1)
                    else:
                        idx = attemptsBar.index(attempts)
                        amount[idx] += 1

                    ax.clear()
                    ax.bar(attemptsBar, amount, color='mediumseagreen')
                    ax.set_title('Die Rolling')
                    ax.set_xlabel('Attempt #s')
                    ax.set_ylabel('Amount')

                    canvas.draw()

                ani = FuncAnimation(fig, update, frames=dieInput, interval=0, repeat=False)

            except ValueError:
                sg.popup_error("Please enter a valid number!")

    window.close()

if __name__ == "__main__":
    main()