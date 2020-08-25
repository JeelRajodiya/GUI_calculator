import PySimpleGUI as sg

bt_num_data = {
'size':(9,3),
'pad':(1.4,1.4),
'font':(0,16),
'button_color':('white','black'),
'border_width': 0
}
bt_sym_data = {
    'size':(9,3),
'pad':(1.4,1.4),
'font':(0,16),
'button_color':('white','#0C0C0C'),
'border_width': 0
}

def get_base64(img):
    import base64
    return base64.b64encode(img.read())
    
backspace_img = open('images/backspace.png','rb')
equal_img = open('images/equal.png','rb')
divide_img = open('images/divide.png','rb')

layout = [
    [sg.Text('Standard',background_color = '#212322',text_color = 'white',font= (0,16))],
    [sg.In('',font = (0,10),key = 'mini-display', text_color = '#A0A0A0',background_color = '#212322',readonly = True,disabled_readonly_background_color='#212322',border_width=0,size=(60,25))],
    [sg.In('0',font = (0,40),text_color = 'white',pad=(0,0),readonly = True,disabled_readonly_background_color='#212322',border_width=0,size=(15,25),key = 'display')],
   
    [sg.Button('%', **bt_sym_data ),
    sg.Button('CE',  **bt_sym_data),
    sg.Button('C',**bt_sym_data),
    sg.B('',**bt_sym_data,image_data= get_base64(backspace_img),key = 'backspace')
    ],
    [sg.B('⅟x',**bt_sym_data),
    sg.B('x²',**bt_sym_data),
    sg.B('√x',**bt_sym_data),
    sg.B('',image_data= get_base64(divide_img),key = '÷',**bt_sym_data)
    ],
    [sg.B('7',**bt_num_data),
    sg.B('8',**bt_num_data),
    sg.B('9',**bt_num_data),
    sg.B('×',**bt_sym_data)
    ],
    [sg.B('4',**bt_num_data),
    sg.B('5',**bt_num_data),
    sg.B('6',**bt_num_data),
    sg.B('–',**bt_sym_data)
    ],
    [sg.B('1',**bt_num_data),
    sg.B('2',**bt_num_data),
    sg.B('3',**bt_num_data),
    sg.B('+',**bt_sym_data)
    ],  
    [sg.B('+∕-',**bt_num_data),
    sg.B('0',**bt_num_data),
    sg.B('.',**bt_num_data),
    sg.B('',**bt_sym_data,image_data=get_base64(equal_img),key = 'answer')
    ]


]
