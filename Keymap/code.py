#PiPi-GHERKIN - Raspberry Pi PICO
import board
#from kmk.extensions.keymap_extras.keymap_jp import KC2JP
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes

import kmk.extensions.keymap_extras.keymap_jp


gherkin = KMKKeyboard()

from kmk.modules.modtap import ModTap
gherkin.modules.append(ModTap())

from kmk.modules.layers import Layers
gherkin.modules.append(Layers())

from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes
rgb_ext = RGB(
		pixel_pin = board.GP28,
        num_pixels = 11,
        animation_speed = 3,
        animation_mode = AnimationModes.SWIRL,
        )
gherkin.extensions.append(rgb_ext)

from kmk.handlers.sequences import send_string
TEST = send_string(r'123456yuiop[]')

from oledDisplay import oled
gherkin.extensions.append(oled(board.GP27, board.GP26,toDisplay='/pipigherkinlogo-3.bmp'))

gherkin.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
gherkin.row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)

gherkin.diode_orientation = DiodeOrientation.COLUMNS

gherkin.debug_enabled = False

gherkin.tap_time = 120

_______ = KC.TRNS
XXXXXXX = KC.NO
CSE = KC.LCTL(KC.LSFT(KC.ESC))
GUISFTS = KC.LGUI(KC.LSFT(KC.S))

RAISE = 1
SYMBOL = 2
LOWER = 3

gherkin.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P,
        KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.MINS,
        KC.LT(SYMBOL, KC.Z), KC.LT(LOWER, KC.X), KC.C, KC.V, KC.B, KC.N, KC.M, KC.MT(KC.COMM,KC.RALT), KC.MT(KC.DOT,KC.RSFT), KC.MT(KC.QUES,KC.RGUI),
				KC.MT(KC.TAB,KC.LCTL), KC.LT(RAISE, KC.SPC), KC.BSPC, KC.ENT,
    ],
    [
        KC.ESC, KC.UP, XXXXXXX, XXXXXXX, KC.LPRN, KC.RPRN, KC.DOT, KC.P7, KC.P8, KC.P9,
        KC.LEFT, KC.DOWN, KC.RGHT, KC.LANG2, KC.LBRC, KC.RBRC, KC.LANG1, KC.P4, KC.P5, KC.P6,
        CSE, GUISFTS, TEST, XXXXXXX, KC.LCBR, KC.RCBR, KC.P0, KC.P1, KC.P2, KC.P3,
				KC.RGB_TOG, _______, KC.DEL, KC.EQL,
    ],
    [
        KC.DLR, KC.JYEN, KC.PIPE, KC.AMPR, KC.DQUO, KC.QUOT, KC.COLN, KC.SCLN, KC.CIRC, KC.TILD,
        KC.AT, KC.HASH, KC.PERC, KC.GRV, XXXXXXX, XXXXXXX, KC.ASTR, KC.SLSH, KC.PLUS, KC.UNDS,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.LABK, KC.RABK, KC.EXLM,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.F11,
        XXXXXXX, _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.F12,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    ]
]

if __name__ == '__main__':
    gherkin.go(hid_type=HIDModes.USB) #Wired USB enable