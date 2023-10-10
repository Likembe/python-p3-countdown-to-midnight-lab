def countdown(number):
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print("HAPPY NEW YEAR!")

countdown(10)

import time

def countdown_with_sleep(number):
    if number < 0:
        print("Countdown should start from a non-negative number.")
        return
    
    for i in range(number, 0, -1):
        print(f"{i} SECOND(S)!")
        time.sleep(1)

    print("HAPPY NEW YEAR!")

#Example usage:
countdown_with_sleep(10)


