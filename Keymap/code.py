#PiPi-GHERKIN - Raspberry Pi PICO
import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes
gherkin = KMKKeyboard()

from kmk.modules.modtap import ModTap
gherkin.modules.append(ModTap())

from kmk.modules.layers import Layers
gherkin.modules.append(Layers())

from kmk.extensions.international import International
gherkin.extensions.append(International())

from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes
rgb_ext = RGB(
		pixel_pin = board.GP28,
        num_pixels = 11,
        animation_speed = 3,
        animation_mode = AnimationModes.SWIRL,
        )
gherkin.extensions.append(rgb_ext)

gherkin.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
gherkin.row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)

gherkin.diode_orientation = DiodeOrientation.COLUMNS

gherkin.debug_enabled = True

_______ = KC.TRNS
XXXXXXX = KC.NO

gherkin.keymap = [
		[   
        KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,
        KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.MINS,
        KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM,    KC.DOT,    KC.QUES,
        KC.MT(KC.TAB, KC.LCTRL),   KC.LT(1,KC.SPC),    KC.BSPC,    KC.ENT
    ],
    [
        _______, KC.UP,   _______, _______,  _______, _______, _______,  KC.P7, KC.P8, KC.P9,
        KC.LEFT, KC.DOWN, KC.RGHT, KC.LANG2, _______, _______, KC.LANG1, KC.P4, KC.P5, KC.P6,
        _______, _______, _______, _______,  _______, _______, KC.P0,    KC.P1, KC.P2, KC.P3,
        _______, KC.TRNS, KC.DEL,  _______
    ]
]

if __name__ == '__main__':
    gherkin.go(hid_type=HIDModes.USB) #Wired USB enable