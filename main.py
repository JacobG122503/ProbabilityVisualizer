import matplotlib.pyplot as plt
import random
import PySimpleGUI as sg

#Run with python3 main.py
def main():
    attemptsBar = []
    amount = []

    #Input window
    layout = [
        [sg.Text('How many times do you want to roll the die?')],
        [sg.InputText(key='-INPUT-')],
        [sg.Button('Run'), sg.Button('Exit')]
    ]

    window = sg.Window('Die Rolling Simulator', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == 'Run':
            dieInput = int(values['-INPUT-'])
            #Loop start
            for i in range(dieInput):
                #Die loop
                attempts = 1
                die = random.randint(1, 6)
                #Rolling until 6
                while die != 6:
                    die = random.randint(1, 6)
                    attempts += 1

                #If # of attempts is not already in attemptsBar, add to it.
                if attempts not in attemptsBar:
                    attemptsBar.append(attempts)
                    amount.append(1)
                else:
                    #If it is already in attemptsBar, find the position and increment the count
                    idx = attemptsBar.index(attempts)
                    amount[idx] += 1

            #Set up and display bar graph
            plt.bar(attemptsBar, amount, color='mediumseagreen')
            plt.title('Die Rolling')
            plt.xlabel('Attempt #s')
            plt.ylabel('Amount')
            plt.show()

    window.close()

if __name__ == "__main__":
    main()
