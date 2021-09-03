import pyautogui, time, os
from pynput.mouse import Listener


def ClearScreen():

   if os.name == 'posix':
      _ = os.system('clear')
   else:
    _ = os.system('cls')


def read_cursor_position(): #abandoned when done it anyway
    pass


def print_blinking_text(text1, text2): # this thing was a misktake... thank god I didn't started it. WOOH! 
    pass


def start(x_axis,y_axis):
    ClearScreen()
    print('Press Ctrl-C to quit.\n\n')

    print("Enter value of time counter...\n\n")    
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    remaining_time= (hours * 3600) + (minutes * 60) + seconds #coverting time into seconds
    ClearScreen()

    print('Press Ctrl-C to quit.\n')
    print("This program will click !! \n")

    
    x = "->Remaining time:" + str(remaining_time)
    max_lenght = len(x)


    while True:

     while len(x) < max_lenght:
      x = x + " "
     
     print(x, end='')
     time.sleep(1)
     print('\b' * max_lenght, end='', flush=True)
     remaining_time = remaining_time - 1
     x = "->Remaining time:" + str(remaining_time)

     if remaining_time == 0:
      pyautogui.click(x=x_axis, y=y_axis)
      break


def on_move(x, y):
    pass

def on_click(x, y, button, pressed):
    global Xs, Ys

    if not pressed: # Stop listener
        Xs = x
        Ys = y
        return False

def on_scroll(x, y, dx, dy):
    pass

def main():
    ClearScreen()
    try:
        print("Click anywhere you want to be clicked !")
        
        with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
            listener.join()

        start(Xs, Ys)

    except KeyboardInterrupt:

        ClearScreen()
        print ("\nBye....")
        time.sleep(2)
        ClearScreen()



if __name__ == "__main__":
   main()
    
