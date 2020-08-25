
import PySimpleGUI as sg 
from calc_layout import layout

sg.LOOK_AND_FEEL_TABLE['my'] = {'BACKGROUND': '#212322',
                                        'TEXT': 'white',
                                        'INPUT': 'black',
                                        'TEXT_INPUT': 'white',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('white', 'black'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 0, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }
sg.theme('my')


window = sg.Window('Calculator',
layout,
resizable = None,
auto_size_buttons = None ,
return_keyboard_events = True
)
symbols = {
        '×':'*',
        '÷':'/',
        '–':'-'}

specials = '⅟x x² √x % +∕-'.split()

answered = None
valid_keys = '0123456789/*-+()÷×.–'
operators = '+-*/=÷×–'

while True:
    event,value = window.read()

    
    if event == None:
        break

    if event in valid_keys:
        if value['display'] == '0' or value['display'] == 'Error' or answered:
            window['display'].update(event)
            
            answered = False
        elif event in operators:
            window['mini-display'].update(value['mini-display']+value['display']+event)
            window['display'].update('')
        else:
        	window['display'].update(value['display']+event)

    elif event in specials:
        if event == '√x':
            from math import sqrt
            temp1 = sqrt( float(value['display']) )
            if temp1.is_integer():    temp1 = int(temp1)
            window['display'].update(temp1)

        elif event == 'x²':
            temp2 = float(value['display']) ** 2
            if temp2.is_integer():   temp2 = int(temp2)

            window['display'].update(temp2)

        elif event == '⅟x':
            window['display'].update('(1/('+value['display']+'))')

        elif event == '%':
             window['display'].update('('+value['display']+'/100)')

        elif event == '+∕-':

            if value['display'][0] == '+' :
                window['display'].update('-'+value['display'][1:])
            elif value['display'][0] == '-':
                window['display'].update('+'+value['display'][1:])
            else:
                window['display'].update('-'+value['display'])

    elif event == 'C'  or event == 'Delete:46':
        window['display'].update('0')
        window['mini-display'].update('')

    elif event == 'CE' or event == ' ':
        window['display'].update('0')

    elif event == 'answer' or event.encode('utf-8') == b'\r' or event == '=':
        try:
            window['mini-display'].update(value['mini-display']+value['display'])
            display_val = value['mini-display']+value['display']

            for i in symbols.keys():
                display_val = display_val.replace(i,symbols[i])
            result = eval(display_val)
        except:
            result = 'Error'
        answered = True

        window['display'].update(result)

    elif event == 'backspace' or event == 'BackSpace:8':
        window['display'].update(value['display'][:-1])

   