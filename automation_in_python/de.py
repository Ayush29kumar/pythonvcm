import re

def lock_screen():
    # Code to lock the screen
    print("Locking the screen...")

def unlock_screen():
    # Code to unlock the screen
    print("Unlocking the screen...")

def adjust_screen_brightness():
    # Code to adjust screen brightness
    print("Adjusting screen brightness...")

def change_screen_resolution():
    # Code to change screen resolution
    print("Changing screen resolution...")

def rotate_screen_orientation():
    # Code to rotate screen orientation
    print("Rotating screen orientation...")

def switch_display_mode():
    # Code to switch display mode
    print("Switching display mode...")

def activate_screen_saver():
    # Code to activate screen saver
    print("Activating screen saver...")

def adjust_screen_timeout():
    # Code to adjust screen timeout
    print("Adjusting screen timeout...")

def calibrate_touch_screen():
    # Code to calibrate touch screen
    print("Calibrating touch screen...")

# Define the list of recognized commands and their associated phrases
commands = {
    # Screen lock and unlock commands
    'Lock the screen' : lock_screen,'Lock screen' : lock_screen,'Secure the screen' : lock_screen,'Activate screen lock' : lock_screen,'Engage screen lock' : lock_screen,'Turn on screen lock' : lock_screen,'Enable screen lock' : lock_screen,'Initiate screen lock' : lock_screen,'Put the screen on lock' : lock_screen,'Lock the display' : lock_screen,'Lock display' : lock_screen,'Activate display lock' : lock_screen,'Engage display lock' : lock_screen,'Turn on display lock' : lock_screen,'Enable display lock' : lock_screen,'Initiate display lock' : lock_screen,'Put the display on lock' : lock_screen,'Lock the monitor' : lock_screen,'Lock monitor' : lock_screen,'Activate monitor lock' : lock_screen,'Engage monitor lock' : lock_screen,'Turn on monitor lock' : lock_screen,'Enable monitor lock' : lock_screen,'Initiate monitor lock' : lock_screen,'Put the monitor on lock' : lock_screen,'Activate screen security' : lock_screen,'Engage screen security' : lock_screen,'Turn on screen security' : lock_screen,'Enable screen security' : lock_screen,'Initiate screen security' : lock_screen,'Activate screen protection' : lock_screen,'Engage screen protection' : lock_screen,'Turn on screen protection' : lock_screen,'Enable screen protection' : lock_screen,
'Unlock the screen' : unlock_screen,'Unlock screen' : unlock_screen,'Release the screen lock' : unlock_screen,'Deactivate screen lock' : unlock_screen,'Turn off screen lock' : unlock_screen,'Disable screen lock' : unlock_screen,'Unlock the display' : unlock_screen,'Unlock display' : unlock_screen,'Release the display lock' : unlock_screen,'Deactivate display lock' : unlock_screen,'Turn off display lock' : unlock_screen,'Disable display lock' : unlock_screen,'Unlock the monitor' : unlock_screen,'Unlock monitor' : unlock_screen,'Release the monitor lock' : unlock_screen,'Deactivate monitor lock' : unlock_screen,'Turn off monitor lock' : unlock_screen,'Disable monitor lock' : unlock_screen,'Disable screen security' : unlock_screen,'Deactivate screen security' : unlock_screen,'Turn off screen security' : unlock_screen,'Disable screen protection' : unlock_screen,'Deactivate screen protection' : unlock_screen,'Turn off screen protection' : unlock_screen,'Remove screen lock' : unlock_screen,'Remove display lock' : unlock_screen,'Remove monitor lock' : unlock_screen,'Stop screen lock' : unlock_screen,'Stop display lock' : unlock_screen,'Stop monitor lock' : unlock_screen,'Disable screen password' : unlock_screen,'Deactivate screen password' : unlock_screen,'Turn off screen password' : unlock_screen,
    # Screen brightness adjustment commands
    'Increase screen brightness' : adjust_screen_brightness,'Raise screen brightness' : adjust_screen_brightness,'Brighten the screen' : adjust_screen_brightness,'Make the screen brighter' : adjust_screen_brightness,'Maximize screen brightness' : adjust_screen_brightness,'Turn up the screen brightness' : adjust_screen_brightness,'Enhance screen brightness' : adjust_screen_brightness,'Boost screen brightness' : adjust_screen_brightness,'Augment screen brightness' : adjust_screen_brightness,'Amplify screen brightness' : adjust_screen_brightness,'Up the screen brightness' : adjust_screen_brightness,'Heighten screen brightness' : adjust_screen_brightness,'Raise the brightness of the screen' : adjust_screen_brightness,'Increase the brightness of the display' : adjust_screen_brightness,'Adjust the brightness level of the screen' : adjust_screen_brightness,'Set the screen brightness to a higher level' : adjust_screen_brightness,

    # Screen resolution change commands
    'Switch screen resolution': change_screen_resolution, 'Adjust screen resolution': change_screen_resolution,
    'Modify screen resolution': change_screen_resolution, 'Set screen resolution': change_screen_resolution,
    'Change display resolution': change_screen_resolution, 'Switch to higher resolution': change_screen_resolution,
    'Switch to lower resolution': change_screen_resolution, 'Increase screen resolution': change_screen_resolution,
    'Decrease screen resolution': change_screen_resolution,
    'Set resolution to [specific resolution]': change_screen_resolution,
    'Switch to [specific resolution]': change_screen_resolution, 'Change screen display size': change_screen_resolution,
    'Adjust screen display resolution': change_screen_resolution, 'Modify monitor resolution': change_screen_resolution,
    'Set the resolution of the screen': change_screen_resolution,
    'Select a different screen resolution': change_screen_resolution,
    'Update screen resolution settings': change_screen_resolution, 'Alter screen resolution': change_screen_resolution,

    # Screen orientation rotation commands
    'Rotate screen orientation': rotate_screen_orientation, 'Change screen orientation': rotate_screen_orientation,
    'Flip screen vertically': rotate_screen_orientation, 'Flip screen horizontally': rotate_screen_orientation,
    'Rotate display orientation': rotate_screen_orientation, 'Adjust screen rotation': rotate_screen_orientation,
    'Modify screen orientation': rotate_screen_orientation, 'Switch screen orientation': rotate_screen_orientation,
    'Rotate the screen clockwise': rotate_screen_orientation,
    'Rotate the screen counterclockwise': rotate_screen_orientation,
    'Rotate the display 90 degrees': rotate_screen_orientation,
    'Rotate the display 180 degrees': rotate_screen_orientation,
    'Flip the screen vertically': rotate_screen_orientation, 'Flip the screen horizontally': rotate_screen_orientation,
    'Change the orientation of the screen': rotate_screen_orientation,
    'Rotate the screen to portrait mode': rotate_screen_orientation,
    'Rotate the screen to landscape mode': rotate_screen_orientation,
    'Switch the screen to vertical orientation': rotate_screen_orientation,
    'Switch the screen to horizontal orientation': rotate_screen_orientation, 'Rotate the monitors display orientation' : rotate_screen_orientation,

    # Display mode switch commands
    "switch display mode": switch_display_mode,
    "change display mode": switch_display_mode,
    "enable extended display": switch_display_mode,
    "enable duplicate display": switch_display_mode,

    # Screen saver activation commands
    'Start screen saver': activate_screen_saver, 'Enable screen saver': activate_screen_saver,
    'Activate screen saver': activate_screen_saver, 'Turn on screen saver': activate_screen_saver,
    'Launch screen saver': activate_screen_saver, 'Initiate screen saver': activate_screen_saver,
    'Engage screen saver': activate_screen_saver, 'Trigger screen saver': activate_screen_saver,
    'Enable display saver': activate_screen_saver, 'Activate display saver': activate_screen_saver,
    'Initiate display saver': activate_screen_saver, 'Turn on display saver': activate_screen_saver,
    'Launch display saver': activate_screen_saver, 'Enable monitor saver': activate_screen_saver,
    'Activate monitor saver': activate_screen_saver, 'Initiate monitor saver': activate_screen_saver,
    'Turn on monitor saver': activate_screen_saver, 'Launch monitor saver': activate_screen_saver,
    'Engage automatic screen saver': activate_screen_saver,
    'Activate idle screen protection': activate_screen_saver, 'Enable idle display timeout': activate_screen_saver,

    # Screen timeout adjustment commands
    'Adjust screen timeout': adjust_screen_timeout, 'Change screen timeout': adjust_screen_timeout,
    'Modify screen timeout': adjust_screen_timeout, 'Set screen timeout': adjust_screen_timeout,
    'Adjust display timeout': adjust_screen_timeout, 'Change display timeout': adjust_screen_timeout,
    'Modify display timeout': adjust_screen_timeout, 'Set display timeout': adjust_screen_timeout,
    'Adjust monitor timeout': adjust_screen_timeout, 'Change monitor timeout': adjust_screen_timeout,
    'Modify monitor timeout': adjust_screen_timeout, 'Set monitor timeout': adjust_screen_timeout,
    'Adjust screen sleep time': adjust_screen_timeout, 'Change screen sleep time': adjust_screen_timeout,
    'Modify screen sleep time': adjust_screen_timeout, 'Set screen sleep time': adjust_screen_timeout,
    'Adjust idle screen timeout': adjust_screen_timeout, 'Change idle screen timeout': adjust_screen_timeout,
    'Modify idle screen timeout': adjust_screen_timeout, 'Set idle screen timeout': adjust_screen_timeout,
    'Adjust screen inactivity timeout': adjust_screen_timeout,
    'Change screen inactivity timeout': adjust_screen_timeout,
    'Modify screen inactivity timeout': adjust_screen_timeout, 'Set screen inactivity timeout': adjust_screen_timeout,
    'Adjust the time before the screen turns off': adjust_screen_timeout,
    'Change the time before the screen turns off': adjust_screen_timeout,
    'Modify the time before the screen turns off': adjust_screen_timeout,
    'Set the time before the screen turns off': adjust_screen_timeout,

    # Touch screen calibration commands
    "calibrate touch screen": calibrate_touch_screen,
    "reset touch screen calibration": calibrate_touch_screen,
}

# Process user input
user_input = input("Enter a command: ")
user_input = re.sub(r'[^\w\s]', '', user_input.lower())
input_tokens = user_input.split()

# Match input with commands
matched_command = None
for command in commands:
    if any(token in command for token in input_tokens):
        matched_command = command
        break

# Execute the command
if matched_command is not None:
    # Call the corresponding function associated with the matched command
    commands[matched_command]()
else:
    print("Command not recognized.")

    """import pandas as pd
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC

    # Load the dataset from CSV
    df = pd.read_csv('a.csv')

    # Preprocessing
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['command'])
    y = df['category']

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = SVC()
    model.fit(X_train, y_train)

    # Predict
    user_input = input("Enter a command: ")
    user_input_transformed = vectorizer.transform([user_input])
    prediction = model.predict(user_input_transformed)

    # Output
    if prediction == 'lock_screen':
        print("Lock screen command detected!")
    elif prediction == 'unlock_screen':
        print("Unlock screen command detected!")
    else:
        print("Unknown command.")
    """

    import pandas as pd
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.model_selection import train_test_split
    from sklearn.svm import SVC
    from sklearn.feature_extraction import text

    """

    # Load the dataset from CSV
    df = pd.read_csv('a.csv')

    # Filter unlock screen commands
    unlock_commands = df[df['category'] == 'unlock_screen']
    stop_words = text.ENGLISH_STOP_WORDS.difference(['screen', 'unlock'])
    stop_words = list(stop_words)


    # Preprocessing
    vectorizer = CountVectorizer(stop_words=stop_words)
    X = vectorizer.fit_transform(unlock_commands['command'])
    y = unlock_commands['category']

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = SVC()
    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Model accuracy: {accuracy}")

    # Predict
    user_input = input("Enter a command: ")
    user_input_transformed = vectorizer.transform([user_input])
    prediction = model.predict(user_input_transformed)

    # Output
    if prediction == 'unlock_screen':
        print("Unlock screen command detected!")
    else:
        print("Unknown command.")
    """
    """import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import classification_report

    # Step 1: Load the data from CSV
    df = pd.read_csv('a.csv')

    # Step 2: Split the data into training and testing sets
    X = df['command']
    y = df['category']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 3: Feature extraction
    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    # Step 4: Train the model
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Step 5: Evaluate the model
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)

    # Step 6: Use the trained model
    new_commands = ['Lock the device', 'Unlock the device']
    new_commands_vectorized = vectorizer.transform(new_commands)
    predictions = model.predict(new_commands_vectorized)
    print(predictions)"""




