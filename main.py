import matplotlib.pyplot as plt
import random
import time
import os

# Run with python3 main.py

def main():
    clear()
    attemptsBar = []
    amount = []
    
    timeMin = float(input("How long would you like the program to run for? (in minutes): "))
    timeSec = timeMin * 60
    start_time = time.time()
    end_time = start_time + timeSec
    
    # Loop start
    while time.time() < end_time:
        # Die loop
        attempts = 1
        die = random.randint(1, 6)
        # Rolling until 6
        while die != 6:
            die = random.randint(1, 6)
            attempts += 1
        
        # If # of attempts is not already in attemptsBar, add to it.
        if attempts not in attemptsBar:
            attemptsBar.append(attempts)
            amount.append(1)
        else:
            # If it is already in attemptsBar, find the position and increment the count
            idx = attemptsBar.index(attempts)
            amount[idx] += 1
    
    # Set up and display bar graph
    plt.bar(attemptsBar, amount, color='mediumseagreen')
    plt.title('Die Rolling')
    plt.xlabel('Attempt #s')
    plt.ylabel('Amount')
    plt.show()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
