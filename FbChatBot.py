import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

structure = ctypes.Structure
VK_SHIFT = 0x0F
VK_SPACE = 0x20
VK_RETURN = 0x0D

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
    
    
    hexcode = [0x30,0x31,0x32,0x33,0x34,0x35,0x36,0x37,0x38,0x39,0x41,0x42,0x43,0x44,0x45,0x46,0x47,0x48,0x49,0x4A,0x4B,0x4C,0x4D,0x4E,0x4F,0x50,0x51,0x52,0x53,0x54,0x55,0x56,0x57,0x58,0x59,0x5A,0x0D,]
    alphanum =["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",VK_RETURN]
    captial = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    message = list(message)

    for i,n in enumerate(message):

        for j in range(0,len(hexcode)):
            if n == alphanum[j]:
                message[i] = hexcode[j]
        for t in range(0,len(captial)):
            if n == captial[t]:
                PressKey(VK_SHIFT)
                message[i]= hexcode[t+9]
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
    click(500,500)
    Message(m)
    time.sleep(0.5)
    PressKey(VK_RETURN)
    ReleaseKey(VK_RETURN)
    time.sleep(4)
    abc = abc+1
