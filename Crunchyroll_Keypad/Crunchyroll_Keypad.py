#Things to add:
#
#
import pyautogui as pag
import time
import webbrowser as wb
import serial

# Instructions
instructions = ''' Select one of the followings : \n 
\t 0 : Lunching the app
\t 1 : Previous Chapter
\t 2 : Next Chapter
\t 3 : Saving the current Chapter
\t 4 : Saving the current Chapter and Exit
\t 9 : Finish the app 
'''

# SETTING UP A CONNECTION WITH ARDUINO
ser = serial.Serial('COM5', 9800, timeout=1)

# FLAG FOR THE APP
running = True

# FUNCTIONS:
# 0. START THE APP
def app_start():
    with open('current_chapter.txt', mode='r+') as file:
        chapter_link = file.readline()
        wb.open(chapter_link)
        time.sleep(3.5)
        pag.press('f')
        file.truncate(0)
        file.close()

# 1. PREVIOUS CHAPTER
def previous_chapter():
    #pag.hotkey('alt', 'tab')
    pag.press('esc')
    back_arrow_positionX, back_arrow_positionY = 22, 50 # These might change depending on the PC and browser
    pag.click(back_arrow_positionX, back_arrow_positionY)
    time.sleep(2.5)
    pag.press('f')

# 2. NEXT CHAPTER
def next_chapter():
    #pag.hotkey('alt', 'tab')
    next_arrow_positionX, next_arrow_positionY = 69, 700 # These might change depending on the PC
    pag.click(next_arrow_positionX, next_arrow_positionY)
    time.sleep(2.5) # Waiting until next chapter is loaded
    pag.press('f')

# 3. SAVING CURRENT CHAPTER
def saving_chapter():
    #pag.hotkey('alt', 'tab')
    pag.keyDown('esc') # Leaving full screen mode

    pag.press('space') # Pausing the video

    link_positionX, link_positionY = 167, 52 # These might change depending on the PC and browser
    pag.click(link_positionX, link_positionY)
    pag.hotkey('ctrl', 'c')  # Copy the link of the chapter

    pag.press('win')
    pag.press('space')
    time.sleep(0.1)
    pag.write('current_chapter')
    time.sleep(0.3)
    pag.press('enter')
    time.sleep(0.1)
    pag.hotkey('ctrl', 'v')
    time.sleep(0.1)
    pag.hotkey('alt', 'f4')
    time.sleep(0.1)
    pag.press('enter') # Saving the chapter's link in the "current_chapter.txt" file

    pag.hotkey('ctrl', 'w')

# 9. KILLING THE APP:
def app_killer():
    global running
    running = False

# 10. Check what wants the user to do
def check_users_input(user_input):
    if user_input == 0 or user_input == b'Launching the app\r\n':
        app_start()

    elif user_input == 1 or user_input == b'Previous Chapter\r\n':
        previous_chapter()

    elif user_input == 2 or user_input == b'Next Chapter\r\n':
        next_chapter()

    elif user_input == 3:
        saving_chapter()

    elif user_input == 4 or user_input == b'Saving Chapter and Exit\r\n':
        saving_chapter()
        app_killer()

    elif user_input == 9:
        app_killer()

    elif user_input == b'Instructions\r\n':
        print(instructions)

# Receiveng the input from th user and acting accordingly
print(instructions)
while running:
    user_input = ser.read(100)
    check_users_input(user_input)
