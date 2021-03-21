def A(font_size, special_char:str, row):
    space = ' '
    if row == 0:
        print('', special_char*(font_size-2),'', end = ''); return
    if font_size//2 == row:
        print(special_char*(font_size), end = ''); return
    else:
        print(special_char, space*(font_size-2), special_char, sep = '', end = '')

def B(font_size, special_char:str, row):
    space = ' '
    if row == 0 or row == (font_size)//2 or row == font_size-1:
        print(special_char*(font_size-1), '', end = '')

    else:
        print(special_char, space*(font_size-2), special_char, sep = '', end = '') 

def C(font_size, special_char:str, row):
    space = ' '
    if row == 0 or row == font_size-1:
        print("",special_char*(font_size-1), end = '')
    else:
        print(special_char, space*(font_size-2), end = '')

def D(font_size, special_char:str, row):
    space = ' '
    if row == 0 or row == font_size-1:
        print(special_char*(font_size-1),'', end = '')
    else:
        print(special_char, space*(font_size-2), special_char, sep = '', end = '')

def fw_slash(font_size, special_char:str, row):
    space = ' '
    print(space*(font_size-row), special_char, space*(row+1), sep = '', end = '')

def bw_slash(font_size, special_char:str, row):
    space = ' '
    print(space*(row+1), special_char, space*(font_size-row), sep = '', end = '')

def colon(font_size, special_char:str, row):
    space = ' '
    if row == ((font_size//2)//2) or row == (font_size//2) + (font_size//4):
        if font_size%2 == 0:
            print(space*(font_size//2), special_char, space*((font_size//2)-1), sep = '', end = '')
        else:
            print(space*(font_size//2), special_char, space*((font_size//2)), sep = '', end = '')
    else:
        print(space*font_size, sep = '', end = '')

def num_0(font_size, special_char:str, row):
    space = ' '
    if row == 0 or row == font_size-1:
        print('', special_char*(font_size-1),'', end = '')
    else:
        print(special_char, space*(font_size-row-2), special_char, space*(row), special_char, sep = '', end = '')

def num_1(font_size, special_char:str, row):
    space = ' '
    if row == 1:
        print(space*((font_size//2)-2), special_char, ' ', special_char, space*(font_size//2), sep = '', end = '')
    elif row == 2 and font_size > 5:
        print(space*((font_size//2)-3), special_char, '  ', special_char, space*(font_size//2), sep = '', end = '')
    elif row == font_size-1:
        print(special_char*font_size, end = '')
    else:
        print(space*(font_size//2), special_char, space*(font_size//2), sep = '', end = '')

def num_2(font_size, special_char:str, row):
    space = ' '
    if row == 0 or row == (font_size//2) or row == font_size-1:
        print(special_char*font_size, end = '')
    elif row<(font_size//2):
        print(space*(font_size-1), special_char, end = '', sep = '')
    else:
        print(special_char, space*(font_size-1), end = '', sep = '')
    
def num_3(font_size, special_char:str, row):
    space = ' '
    if row == 0 or row == (font_size//2) or row == font_size-1:
        print(special_char*font_size, end = '')
    else:
        print(space*(font_size-1), special_char, end = '', sep = '')
    
def num_4(font_size, special_char:str, row):
    space = ' '
    if row == (font_size//2):
        print(special_char*font_size, end = '')
    elif row > ((font_size//2)-3):
        print(special_char, space*(font_size-3), special_char, end = ' ', sep = '')

def num_5(font_size, special_char:str, row):
    pass
def num_6(font_size, special_char:str, row):
    pass
def num_7(font_size, special_char:str, row):
    space = ' '
    if row == 0:
        print(special_char*(font_size),sep = '', end = '')
    else:
        print(special_char, space*(font_size-2), special_char, sep = '', end = '')
    
def num_8(font_size, special_char:str, row):
    space = ' '
    if row == 0 or row == (font_size//2) or row == font_size:
        print('', special_char*(font_size-2),'', sep = '', end = '')
    else:
        print(space*(font_size-1), special_char, sep = '', end = '')

def num_9(font_size, special_char:str, row):
    pass

'''  
def E(font_size, special_char:str, row):

def F(font_size, special_char:str, row):

def G(font_size, special_char:str, row):

def H(font_size, special_char:str, row):

def I(font_size, special_char:str, row):

def J(font_size, special_char:str, row):

def K(font_size, special_char:str, row):

def L(font_size, special_char:str, row):

def M(font_size, special_char:str, row):

def N(font_size, special_char:str, row):

def O(font_size, special_char:str, row):

def P(font_size, special_char:str, row):

def Q(font_size, special_char:str, row):

def R(font_size, special_char:str, row):

def S(font_size, special_char:str, row):

def T(font_size, special_char:str, row):

def U(font_size, special_char:str, row):

def V(font_size, special_char:str, row):

def W(font_size, special_char:str, row):

def X(font_size, special_char:str, row):

def Y(font_size, special_char:str, row):

def Z(font_size, special_char:str, row):

def num_0(font_size, special_char:str, row):

'''