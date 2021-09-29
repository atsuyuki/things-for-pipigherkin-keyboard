#PiPi-GHERKIN - Raspberry Pi PICO
import board
from kmk.keys import KC
from kmk.kmk_keyboard import KMKKeyboard
from kmk.matrix import DiodeOrientation
from kmk.hid import HIDModes

from keymap_jp import JP

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

##### OLED使ってみる ###

import busio
import adafruit_ssd1306
import time

i2c = busio.I2C(board.GP27, board.GP26, frequency=1_000_000)

display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x3c)

wakeup_neo = ''
for c in 'The Matrix has you...':
    wakeup_neo += c
    display.fill(0)
    display.text(wakeup_neo, 2, 15,1)
    display.show()
    time.sleep(0.1)

#display.invert(True)
display.show()

#####

gherkin.col_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7)
gherkin.row_pins = (board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)

gherkin.diode_orientation = DiodeOrientation.COLUMNS

gherkin.debug_enabled = True

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
        JP.Q, JP.W, JP.E, JP.R, JP.T, JP.Y, JP.U, JP.I, JP.O, JP.P,
        JP.A, JP.S, JP.D, JP.F, JP.G, JP.H, JP.J, JP.K, JP.L, JP.MINS,
        KC.LT(SYMBOL, JP.Z), KC.LT(LOWER, JP.X), JP.C, JP.V, JP.B, JP.N, JP.M, KC.MT(JP.COMM,KC.RALT), KC.MT(JP.DOT,KC.RSFT), KC.MT(JP.QUES,KC.RGUI),
				KC.MT(KC.TAB,KC.LCTL), KC.LT(RAISE, KC.SPC), KC.BSPC, KC.ENT,
    ],
    [
        KC.ESC, KC.UP, XXXXXXX, XXXXXXX, JP.LPRN, JP.RPRN, JP.DOT, KC.P7, KC.P8, KC.P9,
        KC.LEFT, KC.DOWN, KC.RGHT, KC.LANG2, JP.LBRC, JP.RBRC, KC.LANG1, KC.P4, KC.P5, KC.P6,
        CSE, GUISFTS, TEST, XXXXXXX, JP.LCBR, JP.RCBR, KC.P0, KC.P1, KC.P2, KC.P3,
				XXXXXXX, _______, XXXXXXX, JP.EQL,
    ],
    [
        JP.DLR, JP.YEN, JP.PIPE, JP.AMPR, JP.DQUO, JP.QUOT, JP.COLN, JP.SCLN, JP.CIRC, JP.TILD,
        JP.AT, JP.HASH, JP.PERC, JP.GRV, XXXXXXX, XXXXXXX, JP.ASTR, JP.SLSH, JP.PLUS, JP.UNDS,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, JP.LABK, JP.RABK, JP.EXLM,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    ],
    [
        KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.F11,
        KC.RGB_TOG, _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.F12,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    ]
]

if __name__ == '__main__':
    gherkin.go(hid_type=HIDModes.USB) #Wired USB enable