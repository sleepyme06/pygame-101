# Pygame Notes

## Overview
- Games are like movies (many images per second) but interactive: the images change based on input and game state.
- Movies: fixed sequence of frames (e.g., 24 fps) — no user input.
- Games: continuous loop that:
  - reads input,
  - updates game state (positions, physics, AI),
  - renders the frame,
  - repeats.

## How videogames work (simple)
1. Run a game loop at a target frame rate.
2. Poll and handle input (keyboard, mouse, joystick).
3. Update positions, collisions, timers, and game logic.
4. Draw everything to the screen (background, sprites, UI).
5. Repeat until quit.

## Pygame responsibilities
- Create a window and surface to draw on.
- Load images and sounds.
- Provide an event queue for input.
- Let you blit surfaces and control frame timing.

## Key concepts
- Surface: image or screen you can draw onto.
- Blit: copy a surface onto another (screen.blit).
- Rect: position/size used for drawing and collision (get_rect()).
- convert()/convert_alpha(): optimize surfaces for faster blitting.
- Event loop: handle pygame events each frame (e.g., QUIT, KEYDOWN).
- Delta/clock: keep consistent motion and FPS (pygame.time.Clock).

## Typical game loop (high level)
- clear screen (screen.fill)
- handle events
- update game objects (positions, animations, collisions)
- draw game objects (screen.blit, pygame.draw)
- update display (pygame.display.update() or flip)
- tick clock (clock.tick(FPS))

## Project files 
- graphics/        # image assets used by the examples (snail, fly, ground, sky, player, etc.)
  - snail1.png
  - snail2.png
  - Fly1.png
  - Fly2.png
  - ground.png
  - sky.png
  - player_stand.png (or player sprites)
            
- tut/         # optional tutorial folder (if present)
  - creating_a_window.py
  - display_image.py
  - animation.py
  - player_char.py
  - diff_lev.py
  - sprite.py(todo)

- pygame.md        # this notes file  
- game.py #to run the game
 
## Prerequsites  
- oops  
ps:have done oops in cpp so to move in python read this:
https://chatgpt.com/share/68f09d83-e928-800f-b0e5-255e76f619f0 


## Resources
- Clearcode tutorials
- Pygame docs: https://www.pygame.org/docs/
