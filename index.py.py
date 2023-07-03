import pyttsx3
import keyboard

def play_sound(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def key_pressed(event):
    key = event.name
    if key in ['return',]:
        return 
    elif key=='capslock':
        key='capslock'
    elif key=="fn":
        key='fn'
   

    play_sound(key)

    
    symbols = {',': 'comma',   
        ';': 'semicolon',
        '.': 'dot',
        '!': 'exclamation',
        '[':'open bracket',
        ']':'close bracket',
        '{': 'open braces',
        '}': 'close braces',
        '/': 'slash',
        '+':'plus',
        '-':'minus',
        '(':'open parenthesis',
        ')':'close parenthesis',
        '':'single quotes',
        " ": 'double quotes',
    


       
    }
    if key in symbols:
        symbol = symbols[key]
        play_sound(symbol)

keyboard.on_press(key_pressed)

keyboard.wait('esc')  


  

