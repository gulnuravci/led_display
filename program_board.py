import time
import frames
import board
import neopixel

RGB = {"Red": (255, 0, 0),
       "Orange": (255, 127, 0),
       "Yellow": (255, 255, 0),
       "Chartreuse": (127, 255, 0),
       "Green": (0, 255, 0),
       "Spring Green": (0, 255, 127),
       "Cyan": (0, 255, 255),
       "Azure": (0, 127, 255),
       "Blue": (0, 0, 255),
       "Violet": (127, 0, 255),
       "Magenta": (255, 0, 255),
       "Rose": (255, 0, 127),
       "White": (255, 255, 255)}

def play_animations(animations):
    clear()
    for animation in animations:
        animation
    clear()

def clear():
    pass

def heart_animation():
    for i in range(10):
        for frame in frames.heart_frames:
            time.sleep(0.25)
            set_pins(frame)
        for frame in frames.heart_frames[::-1]:
            time.sleep(0.25)
            set_pins(frame)
        clear()

def holding_hands_animation():
    for i in range(10):
        for frame in frames.holding_hands_frames:
            time.sleep(0.20)
            set_pins(frame)
    clear()

def set_pins(frame_dict):
    pin_board = [(0, 0, 0)] * 522
    for color, pins in frame_dict.items():
        if pins != []:
            for i in pins:
                pin_board[int(i)] = RGB[color]
    strip[:] = pin_board

def clear():
    strip[:] = [(0, 0, 0)] * 522

strip = neopixel.NeoPixel(board.D21, 522, brightness=0.05)

play_animations([heart_animation(), holding_hands_animation()])
