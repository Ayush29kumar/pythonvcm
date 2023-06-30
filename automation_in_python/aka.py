import re
lock_phrases = ['Lock the screen' ,'Lock screen' ,'Secure the screen' ,'Activate screen lock' ,'Engage screen lock' ,'Turn on screen lock' ,'Enable screen lock' ,'Initiate screen lock' ,'Put the screen on lock' ,'Lock the display' ,'Lock display' ,'Activate display lock' ,'Engage display lock' ,'Turn on display lock' ,'Enable display lock' ,'Initiate display lock' ,'Put the display on lock' ,'Lock the monitor' ,'Lock monitor' ,'Activate monitor lock' ,'Engage monitor lock' ,'Turn on monitor lock' ,'Enable monitor lock' ,'Initiate monitor lock' ,'Put the monitor on lock' ,'Activate screen security' ,'Engage screen security' ,'Turn on screen security' ,'Enable screen security' ,'Initiate screen security' ,'Activate screen protection' ,'Engage screen protection' ,'Turn on screen protection' ,'Enable screen protection' ,]
unlock_phrases = ['Unlock the screen' ,'Unlock screen' ,'Release the screen lock' ,'Deactivate screen lock' ,'Turn off screen lock' ,'Disable screen lock' ,'Unlock the display' ,'Unlock display' ,'Release the display lock' ,'Deactivate display lock' ,'Turn off display lock' ,'Disable display lock' ,'Unlock the monitor' ,'Unlock monitor' ,'Release the monitor lock' ,'Deactivate monitor lock' ,'Turn off monitor lock' ,'Disable monitor lock' ,'Disable screen security' ,'Deactivate screen security' ,'Turn off screen security' ,'Disable screen protection' ,'Deactivate screen protection' ,'Turn off screen protection' ,'Remove screen lock' ,'Remove display lock' ,'Remove monitor lock' ,'Stop screen lock' ,'Stop display lock' ,'Stop monitor lock' ,'Disable screen password' ,'Deactivate screen password' ,'Turn off screen password' ,]
user_input = input("enter the command")
user_input = user_input.lower()
user_input = re.sub(r'[^\w\s]', '', user_input)  # Remove special characters
is_lock_command = any(phrase in user_input for phrase in lock_phrases)
is_unlock_command = any(phrase in user_input for phrase in unlock_phrases)
if is_lock_command:
    # Execute lock screen command
    print("Locking the screen...")
    # Add your lock screen command here
elif is_unlock_command:
    # Execute unlock screen command
    print("Unlocking the screen...")
    # Add your unlock screen command here
else:
    print("Command not recognized.")
