#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created April 2022
# This file contains Learning Guide 02's code.

import stage
import ugame


def game_scene():
    # this function is the main game game_scene
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)
    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()

    # repeat forever, game loop
    while True:
        pass  # placeholder


if __name__ == "__main__":
    game_scene()
