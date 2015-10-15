import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

structure = ctypes.Structure

PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def PressKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):

    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( hexKeyCode, 0x48, 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def click(x, y, numclicks=1):
      #Sets cursor position, remember: 0,0 is the very top left!
    SetCursorPos = ctypes.windll.user32.SetCursorPos

    #this is the mouse event for left click
    mouse_event = ctypes.windll.user32.mouse_event
    SetCursorPos(x, y)
    for i in xrange(numclicks):
      
#this means left mouse click down, but without releasing
     mouse_event(2, 0, 0, 0, 0)
   
#this means releasing of the mouse, or mouse left up
     mouse_event(4, 0, 0, 0, 0)

def Message(message):
    VK_SHIFT = 0x0F
    VK_SPACE = 0x20
    #KEY_0 = 0x30
    #KEY_1 = 0x31
    #KEY_2 = 0x32
    #KEY_3 = 0x33
    #KEY_4 = 0x34
    #KEY_5 = 0x35
    #KEY_6 = 0x36
    #KEY_7 = 0x37
    #KEY_8 = 0x38
    #KEY_9 = 0x39
    #KEY_A = 0x41
    #KEY_B = 0x42
    #KEY_C = 0x43
    #KEY_D = 0x44
    #KEY_E = 0x45
    #KEY_F = 0x46
    #KEY_G = 0x47
    #KEY_H = 0x48
    #KEY_I = 0x49
    #KEY_J = 0x4A
    #KEY_K = 0x4B
    #KEY_L = 0x4C
    #KEY_M = 0x4D
    #KEY_N = 0x4E
    #KEY_O = 0x4F
    #KEY_P = 0x50
    #KEY_Q = 0x51
    #KEY_R = 0x52
    #KEY_S = 0x53
    #KEY_T = 0x54
    #KEY_U = 0x55
    #KEY_V = 0x56
    #KEY_W = 0x57
    #KEY_X = 0x58
    #KEY_Y = 0x59
    #KEY_Z = 0x5A
    #VK_RETURN = 0x0D
    
    message = list(message)

    for i,n in enumerate(message):
        if n == "0":
            message[i]= 0x30
        if n == "1":
            message[i]= 0x31
        if n == "2":
            message[i]= 0x32
        if n == "3":
            message[i]= 0x33
        if n == "4":
            message[i]= 0x34
        if n == "5":
            message[i]= 0x35
        if n == "6":
            message[i]= 0x36
        if n == "7":
            message[i]= 0x37
        if n == "8":
            message[i]= 0x38
        if n == "9":
            message[i]= 0x39
        if n == "a":
            message[i]= 0x41
        if n == "b":
            message[i]= 0x42
        if n == "c":
            message[i]= 0x43
        if n == "d":
            message[i]= 0x44
        if n == "e":
            message[i]= 0x45
        if n == "f":
            message[i]= 0x46
        if n == "g":
            message[i]= 0x47
        if n == "h":
            message[i]= 0x48
        if n == "i":
            message[i]= 0x49
        if n == "j":
            message[i]= 0x4A
        if n == "k":
            message[i]= 0x4B
        if n == "l":
            message[i]= 0x4C
        if n == "m":
            message[i]= 0x4D
        if n == "n":
            message[i]= 0x4E
        if n == "o":
            message[i]= 0x4F
        if n == "p":
            message[i]= 0x50
        if n == "q":
            message[i]= 0x51
        if n == "r":
            message[i]= 0x52
        if n == "s":
            message[i]= 0x53
        if n == "t":
            message[i]= 0x54
        if n == "u":
            message[i]= 0x55
        if n == "v":
            message[i]= 0x56
        if n == "w":
            message[i]= 0x57
        if n == "x":
            message[i]= 0x58
        if n == "y":
            message[i]= 0x59
        if n == "z":
            message[i]= 0x5A
        if n == "A":
            PressKey(VK_SHIFT)
            message[i]= 0x41
            ReleaseKey(VK_SHIFT)
        if n == "B":
            PressKey(VK_SHIFT)
            message[i]= 0x42
            ReleaseKey(VK_SHIFT)
        if n == "C":
            PressKey(VK_SHIFT)
            message[i]= 0x43
            ReleaseKey(VK_SHIFT)
        if n == "D":
            PressKey(VK_SHIFT)
            message[i]= 0x44
            ReleaseKey(VK_SHIFT)
        if n == "E":
            PressKey(VK_SHIFT)
            message[i]= 0x45
            ReleaseKey(VK_SHIFT)
        if n == "F":
            PressKey(VK_SHIFT)
            message[i]= 0x46
            ReleaseKey(VK_SHIFT)
        if n == "G":
            PressKey(VK_SHIFT)
            message[i]= 0x47
            ReleaseKey(VK_SHIFT)
        if n == "H":
            PressKey(VK_SHIFT)
            message[i]= 0x48
            ReleaseKey(VK_SHIFT)
        if n == "I":
            PressKey(VK_SHIFT)
            message[i]= 0x49
            ReleaseKey(VK_SHIFT)
        if n == "J":
            PressKey(VK_SHIFT)
            message[i]= 0x4A
            ReleaseKey(VK_SHIFT)
        if n == "K":
            PressKey(VK_SHIFT)
            message[i]= 0x4B
            ReleaseKey(VK_SHIFT)
        if n == "L":
            PressKey(VK_SHIFT)
            message[i]= 0x4C
            ReleaseKey(VK_SHIFT)
        if n == "M":
            PressKey(VK_SHIFT)
            message[i]= 0x4D
            ReleaseKey(VK_SHIFT)
        if n == "N":
            PressKey(VK_SHIFT)
            message[i]= 0x4E
            ReleaseKey(VK_SHIFT)
        if n == "O":
            PressKey(VK_SHIFT)
            message[i]= 0x4F
            ReleaseKey(VK_SHIFT)
        if n == "P":
            PressKey(VK_SHIFT)
            message[i]= 0x50
            ReleaseKey(VK_SHIFT)
        if n == "Q":
            PressKey(VK_SHIFT)
            message[i]= 0x51
            ReleaseKey(VK_SHIFT)
        if n == "R":
            PressKey(VK_SHIFT)
            message[i]= 0x52
            ReleaseKey(VK_SHIFT)
        if n == "S":
            PressKey(VK_SHIFT)
            message[i]= 0x53
            ReleaseKey(VK_SHIFT)
        if n == "T":
            PressKey(VK_SHIFT)
            message[i]= 0x54
            ReleaseKey(VK_SHIFT)
        if n == "U":
            PressKey(VK_SHIFT)
            message[i]= 0x55
            ReleaseKey(VK_SHIFT)
        if n == "V":
            PressKey(VK_SHIFT)
            message[i]= 0x56
            ReleaseKey(VK_SHIFT)
        if n == "W":
            PressKey(VK_SHIFT)
            message[i]= 0x57
            ReleaseKey(VK_SHIFT)
        if n == "X":
            PressKey(VK_SHIFT)
            message[i]= 0x58
            ReleaseKey(VK_SHIFT)
        if n == "Y":
            PressKey(VK_SHIFT)
            message[i]= 0x59
            ReleaseKey(VK_SHIFT)
        if n == "Z":
            PressKey(VK_SHIFT)
            message[i]= 0x5A
            ReleaseKey(VK_SHIFT)
        if n == ' ':
            message[i]= 0x20
        if n == ',':
            message[i]= 0x2C
        if n == '.':
            message[i]= 0x2E
        if n == '!':
            message[i]= 0x21
        if n == ':':
            message[i]= 0x3A

        PressKey(message[i])
        ReleaseKey(message[i])
    PressKey(VK_RETURN)
    ReleaseKey(VK_RETURN)

abc = 0

m = raw_input("Enter bot message here:\n")
while abc <15:
    click(900,710)
    Message(m)
    time.sleep(0.2)
    abc = abc+1
