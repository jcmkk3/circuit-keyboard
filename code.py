import board
import keypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

ROWS = (board.D0, board.D1, board.D2, board.D3, board.D4, board.D5)
COLS = (board.D6, board.D7, board.D8, board.D9, board.D10)
TRANSFORM = (
    (0,0), (1,0), (0,1), (1,1), (0,2), (1,2), (0,3), (1,3), (0,4), (1,4),
    (2,0), (3,0), (2,1), (3,1), (2,2), (3,2), (2,3), (3,3), (2,4), (3,4),
           (4,0), (5,0), (4,1),               (5,2), (4,3), (5,3),
                         (5,1), (4,2),        (5,4), (4,4)
)

KEYMAP = (
    Keycode.W, Keycode.F, Keycode.M, Keycode.P, Keycode.G, Keycode.K, Keycode.U, Keycode.O, Keycode.Y, Keycode.QUOTE,
    Keycode.R, Keycode.S, Keycode.N, Keycode.T, Keycode.B, Keycode.J, Keycode.A, Keycode.E, Keycode.I, Keycode.H,
               Keycode.C, Keycode.L, Keycode.D,                       Keycode.X, Keycode.COMMA, Keycode.PERIOD,
                          Keycode.FORWARD_SLASH, Keycode.SPACE, Keycode.SHIFT, Keycode.SEMICOLON
)

transform_map = {key: i for i, key in enumerate(TRANSFORM)}

keys = keypad.KeyMatrix(ROWS, COLS, columns_to_anodes=False)
kbd = Keyboard(usb_hid.devices)

while True:
    event = keys.events.get()
    if event:
        key_position = keys.key_number_to_row_column(event.key_number)
        keycode = KEYMAP[transform_map[key_position]]
        if event.pressed:
            kbd.press(keycode)
        if event.released:
            kbd.release(keycode)
