class ActionKind(Enum):
    RunningLeft = 0
    RunningRight = 1
    Idle = 2
    IdleLeft = 3
    IdleRight = 4
    JumpingLeft = 5
    JumpingRight = 6
    CrouchLeft = 7
    CrouchRight = 8
    Flying = 9
    Walking = 10
    Jumping = 11
    Walking2 = 12
@namespace
class SpriteKind:
    Bumper = SpriteKind.create()
    Goal = SpriteKind.create()
    Coin = SpriteKind.create()
    Flier = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    if sprite.vy > 0 and not (sprite.is_hitting_tile(CollisionDirection.BOTTOM)) or sprite.y < otherSprite.top:
        otherSprite.destroy(effects.ashes, 250)
        otherSprite.vy = -50
        sprite.vy = -2 * pixelsToMeters
        info.change_score_by(1)
        music.power_up.play()
    else:
        info.change_life_by(-1)
        sprite.say("Ow!", invincibilityPeriod)
        music.power_down.play()
    pause(invincibilityPeriod)
sprites.on_overlap(SpriteKind.player, SpriteKind.Bumper, on_on_overlap)

def initializeAnimations():
    initializeHeroAnimations()
    initializeCoinAnimation()
    initializeFlierAnimations()
def giveIntroduction():
    game.set_dialog_frame(img("""
        . 2 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                2 2 1 1 1 1 1 1 1 1 1 1 1 2 2 . 
                2 1 1 2 2 2 2 2 2 2 2 2 1 1 2 . 
                2 1 2 2 1 1 1 1 1 1 1 2 2 1 2 . 
                2 1 2 1 1 1 1 1 1 1 1 1 2 1 2 . 
                2 1 2 1 1 1 1 1 1 1 1 1 2 1 2 . 
                2 1 2 1 1 1 1 1 1 1 1 1 2 1 2 . 
                2 1 2 1 1 1 1 1 1 1 1 1 2 1 2 . 
                2 1 2 1 1 1 1 1 1 1 1 1 2 1 2 . 
                2 1 2 1 1 1 1 1 1 1 1 1 2 1 2 . 
                2 1 2 1 1 1 1 1 1 1 1 1 2 1 2 . 
                2 1 2 2 1 1 1 1 1 1 1 2 2 1 2 . 
                2 1 1 2 2 2 2 2 2 2 2 2 1 1 2 . 
                2 2 1 1 1 1 1 1 1 1 1 1 1 2 2 . 
                . 2 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                . . . . . . . . . . . . . . . .
    """))
    game.set_dialog_cursor(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . f f 5 5 5 5 f f . . . . 
                . . . . f 5 5 5 5 5 5 f . . . . 
                . . . f 5 5 5 4 4 5 5 5 f . . . 
                . . . f 5 5 5 4 4 5 5 5 f . . . 
                . . . f 5 5 5 4 4 5 5 5 f . . . 
                . . . f 5 5 5 4 4 5 5 5 f . . . 
                . . . . f 5 5 5 5 5 5 f . . . . 
                . . . . f f 5 5 5 5 f f . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    showInstruction("Move with the left and right buttons.")
    showInstruction("Jump with the up or A button.")
    showInstruction("Double jump by pressing jump again.")
def initializeLevel2(level: number):
    global playerStartLocation
    effects.clouds.start_screen_effect()
    playerStartLocation = tiles.get_tiles_by_type(assets.tile("""
        tile6
    """))[0]
    tiles.place_on_tile(hero2, playerStartLocation)
    tiles.set_tile_at(playerStartLocation, assets.tile("""
        tile0
    """))
def initializeCoinAnimation():
    global coinAnimation
    coinAnimation = animation.create_animation(ActionKind.Idle, 200)
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . f f 5 5 5 5 f f . . . . 
                . . . . f 5 5 5 5 5 5 f . . . . 
                . . . f 5 5 5 4 4 5 5 5 f . . . 
                . . . f 5 5 5 4 4 5 5 5 f . . . 
                . . . f 5 5 5 4 4 5 5 5 f . . . 
                . . . f 5 5 5 4 4 5 5 5 f . . . 
                . . . . f 5 5 5 5 5 5 f . . . . 
                . . . . f f 5 5 5 5 f f . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . f f 5 f 5 5 5 f . . . . . 
                . . . f 5 f 5 5 5 5 5 f . . . . 
                . . f 5 f 5 5 5 4 5 5 f . . . . 
                . . f 5 f 5 5 5 4 4 5 5 f . . . 
                . . f 5 f 5 5 5 4 4 5 5 f . . . 
                . . f 5 f 5 5 5 4 5 5 f . . . . 
                . . . f 5 f 5 5 5 5 5 f . . . . 
                . . . . f 5 f 5 5 5 f . . . . . 
                . . . . f f f f f f . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f f f f f . . . . . . 
                . . . . f f 5 f 5 f f . . . . . 
                . . . f f 5 f 5 5 5 f . . . . . 
                . . . f 5 f 5 5 5 5 f f . . . . 
                . . . f 5 f 5 5 4 5 5 f . . . . 
                . . . f 5 f 5 5 4 5 5 f . . . . 
                . . . f 5 f 5 5 5 5 f f . . . . 
                . . . f f 5 f 5 5 5 f . . . . . 
                . . . . f f 5 f 5 f f . . . . . 
                . . . . . f f f f f . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . . f f f f f . . . . . . 
                . . . . . f 5 f 5 f f . . . . . 
                . . . . . f 5 f 5 5 f . . . . . 
                . . . . . f 5 f 5 5 f . . . . . 
                . . . . . f 5 f 5 5 f . . . . . 
                . . . . . f 5 f 5 5 f . . . . . 
                . . . . . f 5 f 5 f f . . . . . 
                . . . . . f f f f f . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . . . f f f f f . . . . . 
                . . . . . f f 5 f 5 f . . . . . 
                . . . . . f 5 5 f 5 f . . . . . 
                . . . . . f 5 5 f 5 f . . . . . 
                . . . . . f 5 5 f 5 f . . . . . 
                . . . . . f 5 5 f 5 f . . . . . 
                . . . . . f f 5 f 5 f . . . . . 
                . . . . . . f f f f f . . . . . 
                . . . . . . f f f f . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f . . . . . 
                . . . . . f f 5 f 5 f f . . . . 
                . . . . . f 5 5 5 f 5 f f . . . 
                . . . . f f 5 5 5 5 f 5 f . . . 
                . . . . f 5 5 4 5 5 f 5 f . . . 
                . . . . f 5 5 4 5 5 f 5 f . . . 
                . . . . f f 5 5 5 5 f 5 f . . . 
                . . . . . f 5 5 5 f 5 f f . . . 
                . . . . . f f 5 f 5 f f . . . . 
                . . . . . . f f f f f . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . f 5 5 5 f 5 f f . . . 
                . . . . f 5 5 5 5 5 f 5 f . . . 
                . . . . f 5 5 4 5 5 5 f 5 f . . 
                . . . f 5 5 4 4 5 5 5 f 5 f . . 
                . . . f 5 5 4 4 5 5 5 f 5 f . . 
                . . . . f 5 5 4 5 5 5 f 5 f . . 
                . . . . f 5 5 5 5 5 f 5 f . . . 
                . . . . . f 5 5 5 f 5 f . . . . 
                . . . . . . f f f f f f . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.destroy(effects.trail, 250)
    otherSprite2.y += -3
    info.change_score_by(3)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin, on_on_overlap2)

def attemptJump():
    global doubleJumpSpeed, canDoubleJump
    # else if: either fell off a ledge, or double jumping
    if hero.is_hitting_tile(CollisionDirection.BOTTOM):
        hero.vy = -4 * pixelsToMeters
    elif canDoubleJump:
        doubleJumpSpeed = -3 * pixelsToMeters
        # Good double jump
        if hero.vy >= -40:
            doubleJumpSpeed = -4.5 * pixelsToMeters
            hero.start_effect(effects.trail, 500)
            scene.camera_shake(2, 250)
        hero.vy = doubleJumpSpeed
        canDoubleJump = False
def animateIdle():
    global mainIdleLeft, mainIdleRight
    mainIdleLeft = animation.create_animation(ActionKind.IdleLeft, 100)
    animation.attach_animation(hero, mainIdleLeft)
    mainIdleLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d d d d d d d d d e e d f . 
                . f d d f d d d d f d d e d f . 
                . f d d f d d d d f d d d e f . 
                . f d d f d d d d f d d d f . . 
                . f d d d d d d d d d d d f . . 
                . f a c c c c c c c c a b f . . 
                . f d d c c c c c c d d d f . . 
                . f d f f f b b f f f d d f . . 
                . . f a a a a a a a a a b f . . 
                . . . f a a b f f a a b f . . . 
                . . . f a a b f f a a b f . . . 
                . . . . f f f . . f f f . . . .
    """))
    mainIdleRight = animation.create_animation(ActionKind.IdleRight, 100)
    animation.attach_animation(hero, mainIdleRight)
    mainIdleRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d e e d d d d d d d d d f . 
                . f d e d d f d d d d f d d f . 
                . f e d d d f d d d d f d d f . 
                . . f d d d f d d d d f d d f . 
                . . f d d d d d d d d d d d f . 
                . . f b a c c c c c c c c a f . 
                . . f d d d c c c c c c d d f . 
                . . f d d f f f b b f f f d f . 
                . . f b a a a a a a a a a f . . 
                . . . f b a a f f b a a f . . . 
                . . . f b a a f f b a a f . . . 
                . . . . f f f . . f f f . . . .
    """))

def on_player1_button_up_pressed():
    attemptJump()
controller.player1.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player1_button_up_pressed)

def setLevelTileMap(level2: number):
    clearGame()
    if level2 == 0:
        tiles.set_tilemap(tilemap("""
            level
        """))
    elif level2 == 1:
        tiles.set_tilemap(tilemap("""
            level_0
        """))
    elif level2 == 2:
        tiles.set_tilemap(tilemap("""
            level_1
        """))
    elif level2 == 3:
        tiles.set_tilemap(tilemap("""
            level_2
        """))
    elif level2 == 4:
        tiles.set_tilemap(tilemap("""
            level_3
        """))
    elif level2 == 5:
        tiles.set_tilemap(tilemap("""
            level_4
        """))
    elif level2 == 6:
        tiles.set_tilemap(tilemap("""
            level_5
        """))
    elif level2 == 7:
        tiles.set_tilemap(tilemap("""
            level_6
        """))
    initializeLevel(level2)
    initializeLevel2(level2)
def animateJumps2():
    global mainJumpLeft2, mainJumpRight2
    # Because there isn't currently an easy way to say "play this animation a single time
    # and stop at the end", this just adds a bunch of the same frame at the end to accomplish
    # the same behavior
    mainJumpLeft2 = animation.create_animation(ActionKind.JumpingLeft, 100)
    animation.attach_animation(hero2, mainJumpLeft2)
    mainJumpLeft2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d d d d d d d d d e e d f . 
                . f d d f d d d d f d d e d f . 
                . f d d f d d d d f d d d e f . 
                . f d d f d d d d f d d d f . . 
                . f d d d d d d d d d d d f . . 
                . f a c c c c c c c c a b f . . 
                . f d d c c c c c c d d d f . . 
                . f d f f f b b f f f d d f . . 
                . . f a a a a a a a a a b f . . 
                . . . f a a b f f a a b f . . . 
                . . . f a a b f f a a b f . . . 
                . . . . f f f . . f f f . . . .
    """))
    mainJumpLeft2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d d d d d d d d d e e d f . 
                . f d d f d d d d f d d e d f . 
                . f d d f d d d d f d d d e f . 
                . f d d f d d d d f d d d f . . 
                . f d d d d d d d d d d d f . . 
                . f a c c c c c c c c a b f . . 
                . f d d c c c c c c d d d f . . 
                . f d f f f b b f f f d d f . . 
                . . f a a a a a a a a a b f . . 
                . . . f a a b f f a a b f . . . 
                . . . . f f f . . f f f . . . . 
                . . . . . . . . . . . . . . . .
    """))
    for index in range(30):
        mainJumpLeft2.add_animation_frame(img("""
            . . . . . . . . . . . . . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f e e e e e e e e e e f . . 
                        . f e e e e e e e e e e e e f . 
                        . f d d d d d d d d d e e d f . 
                        . f d d f d d d d f d d e d f . 
                        . f d d f d d d d f d d d e f . 
                        . f d d f d d d d f d d d f . . 
                        . f d d d d d d d d d d d f f . 
                        . d a b c c c c c c c c b a d . 
                        . d a c c c c c c c c c c a d . 
                        . f f f f f b b f f f f f f f . 
                        . . f a a a a a a a a a b f . . 
                        . . . f a a b f f a a b f . . . 
                        . . . . f f f . . f f f . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    mainJumpRight2 = animation.create_animation(ActionKind.JumpingRight, 100)
    animation.attach_animation(hero2, mainJumpRight2)
    mainJumpRight2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d e e d d d d d d d d d f . 
                . f d e d d f d d d d f d d f . 
                . f e d d d f d d d d f d d f . 
                . . f d d d f d d d d f d d f . 
                . . f d d d d d d d d d d d f . 
                . . f b a c c c c c c c c a f . 
                . . f d d d c c c c c c d d f . 
                . . f d d f f f b b f f f d f . 
                . . f b a a a a a a a a a f . . 
                . . . f b a a f f b a a f . . . 
                . . . f b a a f f b a a f . . . 
                . . . . f f f . . f f f . . . .
    """))
    mainJumpRight2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d e e d d d d d d d d d f . 
                . f d e d d f d d d d f d d f . 
                . f e d d d f d d d d f d d f . 
                . . f d d d f d d d d f d d f . 
                . . f d d d d d d d d d d d f . 
                . . f b a c c c c c c c c a f . 
                . . f d d d c c c c c c d d f . 
                . . f d d f f f b b f f f d f . 
                . . f b a a a a a a a a a f . . 
                . . . f b a a f f b a a f . . . 
                . . . . f f f . . f f f . . . . 
                . . . . . . . . . . . . . . . .
    """))
    for index2 in range(30):
        mainJumpRight2.add_animation_frame(img("""
            . . . . . . . . . . . . . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f e e e e e e e e e e f . . 
                        . f e e e e e e e e e e e e f . 
                        . f d e e d d d d d d d d d f . 
                        . f d e d d f d d d d f d d f . 
                        . f e d d d f d d d d f d d f . 
                        . . f d d d f d d d d f d d f . 
                        . f f d d d d d d d d d d d f . 
                        . d a b c c c c c c c c b a d . 
                        . d a c c c c c c c c c c a d . 
                        . f f f f f f f b b f f f f f . 
                        . . f b a a a a a a a a a f . . 
                        . . . f b a a f f b a a f . . . 
                        . . . . f f f . . f f f . . . . 
                        . . . . . . . . . . . . . . . .
        """))
def initializeFlierAnimations():
    global flierFlying, flierIdle
    flierFlying = animation.create_animation(ActionKind.Flying, 100)
    flierFlying.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . f 4 4 4 4 4 4 4 f . . . 
                . . . f 4 5 5 4 4 4 5 5 4 f . . 
                . f . f 4 4 4 5 4 5 4 4 4 f . f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . . . f 4 4 5 5 5 5 5 4 4 f . . 
                . . . . f 4 5 4 4 4 5 4 f . . . 
                . . . . . f f f f f f f . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    flierFlying.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . f 4 4 4 4 4 4 4 f . . . 
                . . . f 4 5 5 4 4 4 5 5 4 f . . 
                . . . f 4 4 4 5 4 5 4 4 4 f . . 
                . . f 4 4 4 4 4 4 4 4 4 4 4 f . 
                . . f 4 4 4 4 5 4 5 4 4 4 4 f . 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                . f 4 f 4 4 5 5 5 5 5 4 4 f 4 f 
                . f f . f 4 5 4 4 4 5 4 f . f f 
                . f . . . f f f f f f f . . . f 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    flierFlying.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . f 4 4 4 4 4 4 4 f . . . 
                . . . f 4 5 5 4 4 4 5 5 4 f . . 
                . f . f 4 4 4 5 4 5 4 4 4 f . f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . . . f 4 4 5 5 5 5 5 4 4 f . . 
                . . . . f 4 5 4 4 4 5 4 f . . . 
                . . . . . f f f f f f f . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    flierIdle = animation.create_animation(ActionKind.Idle, 100)
    flierIdle.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . f 4 4 4 4 4 4 4 f . . . 
                . . . f 4 5 5 4 4 4 5 5 4 f . . 
                . f . f 4 4 4 5 4 5 4 4 4 f . f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . . . f 4 4 5 5 5 5 5 4 4 f . . 
                . . . . f 4 5 4 4 4 5 4 f . . . 
                . . . . . f f f f f f f . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))

def on_player2_button_a_pressed():
    attemptJump_p2()
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player2_button_down_pressed():
    if not (hero.is_hitting_tile(CollisionDirection.BOTTOM)):
        hero.vy += 80
controller.player2.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player2_button_down_pressed)

def animateRun():
    global mainRunLeft, mainRunRight
    mainRunLeft = animation.create_animation(ActionKind.RunningLeft, 100)
    animation.attach_animation(hero, mainRunLeft)
    mainRunLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f . . . . . . 
                . . f e e e e e e e f . . . . . 
                . f e e e e e e e e e f . . . . 
                . f d d d d e d d e e f . . . . 
                . f d d f d d e d e e f . . . . 
                . f d d f d d d e e e f . . . . 
                . f d d f d d d d d d f . . . . 
                . f d d d d d d d d d f . . . . 
                . . f c c c a a c c b f . . . . 
                . . f c c d d d c c b f . . . . 
                . . f b f f d d f f f f . . . . 
                . . f a a a a a a a b f . . . . 
                . . . f a a a a b f f . . . . . 
                . . . f a a a a b f . . . . . . 
                . . . . f f f f f . . . . . . .
    """))
    mainRunLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . f f f f f f f . . . . . . 
                . . f e e e e e e e f . . . . . 
                . f e e e e e e e e e f . . . . 
                . f d d d d e d d e e f . . . . 
                . f d d f d d e d e e f . . . . 
                . f d d f d d d e e e f . . . . 
                . f d d f d d d d d d f . . . . 
                . f d d d d d d d d d f . . . . 
                . . f c c c c a a c b f . . . . 
                . . f c c c c d d c b f . . . . 
                . . f b f f d d d f f f f . . . 
                . . f a a a a a a a a b f f . . 
                . . . f a a b f f a a a f f . . 
                . . . . f f f . f f f f f . . .
    """))
    mainRunLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f . . . . . . 
                . . f e e e e e e e f . . . . . 
                . f e e e e e e e e e f . . . . 
                . f d d d d e d d e e f . . . . 
                . f d d f d d e d e e f . . . . 
                . f d d f d d d e e e f . . . . 
                . f d d f d d d d d d f . . . . 
                . f d d d d d d d d d f . . . . 
                . . f c c c a a c c b f . . . . 
                . . f c c d d d c c b f . . . . 
                . . f b f f d d f f f f . . . . 
                . . f a a a a a a a b f . . . . 
                . . . f a a a a b f f . . . . . 
                . . . f a a a a b f . . . . . . 
                . . . . f f f f f . . . . . . .
    """))
    mainRunLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . f f f f f f f . . . . . . 
                . . f e e e e e e e f . . . . . 
                . f e e e e e e e e e f . . . . 
                . f d d d d e d d e e f . . . . 
                . f d d f d d e d e e f . . . . 
                . f d d f d d d e e e f . . . . 
                . f d d f d d d d d d f . . . . 
                . f d d d d d d d d d f . . . . 
                . . f c a a c c c c b f . . . . 
                . f d d d b c c c c b f . . . . 
                f f f d d f f f f f f f . . . . 
                f f f a a a a a a a b f . . . . 
                . f a a b f a a b f f . . . . . 
                . f f f f . f f f . . . . . . .
    """))
    mainRunRight = animation.create_animation(ActionKind.RunningRight, 100)
    animation.attach_animation(hero, mainRunRight)
    mainRunRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f f . . . 
                . . . . . f e e e e e e e f . . 
                . . . . f e e e e e e e e e f . 
                . . . . f e e d d e d d d d f . 
                . . . . f e e d e d d f d d f . 
                . . . . f e e e d d d f d d f . 
                . . . . f d d d d d d f d d f . 
                . . . . f d d d d d d d d d f . 
                . . . . f b c c a a c c c f . . 
                . . . . f b c c d d d c c f . . 
                . . . . f f f f d d f f b f . . 
                . . . . f b a a a a a a a f . . 
                . . . . . f f b a a a a f . . . 
                . . . . . . f b a a a a f . . . 
                . . . . . . . f f f f f . . . .
    """))
    mainRunRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f f . . . 
                . . . . . f e e e e e e e f . . 
                . . . . f e e e e e e e e e f . 
                . . . . f e e d d e d d d d f . 
                . . . . f e e d e d d f d d f . 
                . . . . f e e e d d d f d d f . 
                . . . . f d d d d d d f d d f . 
                . . . . f d d d d d d d d d f . 
                . . . . f b c a a c c c c f . . 
                . . . . f b c d d c c c c f . . 
                . . . f f f f d d d f f b f . . 
                . . f f b a a a a a a a a f . . 
                . . f f a a a f f b a a f . . . 
                . . . f f f f . . f f f . . . .
    """))
    mainRunRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f f . . . 
                . . . . . f e e e e e e e f . . 
                . . . . f e e e e e e e e e f . 
                . . . . f e e d d e d d d d f . 
                . . . . f e e d e d d f d d f . 
                . . . . f e e e d d d f d d f . 
                . . . . f d d d d d d f d d f . 
                . . . . f d d d d d d d d d f . 
                . . . . f b c c a a c c c f . . 
                . . . . f b c c d d d c c f . . 
                . . . . f f f f d d f f b f . . 
                . . . . f b a a a a a a a f . . 
                . . . . . f f b a a a a f . . . 
                . . . . . . f b a a a a f . . . 
                . . . . . . . f f f f f . . . .
    """))
    mainRunRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f f . . . 
                . . . . . f e e e e e e e f . . 
                . . . . f e e e e e e e e e f . 
                . . . . f e e d d e d d d d f . 
                . . . . f e e d e d d f d d f . 
                . . . . f e e e d d d f d d f . 
                . . . . f d d d d d d f d d f . 
                . . . . f d d d d d d d d d f . 
                . . . . f b c c c c a a c f . . 
                . . . . f b c c c c b d d d f . 
                . . . . f f f f f f f d d f f f 
                . . . . f b a a a a a a a f f f 
                . . . . . f f b a a f b a a f . 
                . . . . . . . f f f . f f f . .
    """))
def animateJumps():
    global mainJumpLeft, mainJumpRight
    # Because there isn't currently an easy way to say "play this animation a single time
    # and stop at the end", this just adds a bunch of the same frame at the end to accomplish
    # the same behavior
    mainJumpLeft = animation.create_animation(ActionKind.JumpingLeft, 100)
    animation.attach_animation(hero, mainJumpLeft)
    mainJumpLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d d d d d d d d d e e d f . 
                . f d d f d d d d f d d e d f . 
                . f d d f d d d d f d d d e f . 
                . f d d f d d d d f d d d f . . 
                . f d d d d d d d d d d d f . . 
                . f a c c c c c c c c a b f . . 
                . f d d c c c c c c d d d f . . 
                . f d f f f b b f f f d d f . . 
                . . f a a a a a a a a a b f . . 
                . . . f a a b f f a a b f . . . 
                . . . f a a b f f a a b f . . . 
                . . . . f f f . . f f f . . . .
    """))
    mainJumpLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d d d d d d d d d e e d f . 
                . f d d f d d d d f d d e d f . 
                . f d d f d d d d f d d d e f . 
                . f d d f d d d d f d d d f . . 
                . f d d d d d d d d d d d f . . 
                . f a c c c c c c c c a b f . . 
                . f d d c c c c c c d d d f . . 
                . f d f f f b b f f f d d f . . 
                . . f a a a a a a a a a b f . . 
                . . . f a a b f f a a b f . . . 
                . . . . f f f . . f f f . . . . 
                . . . . . . . . . . . . . . . .
    """))
    for index3 in range(30):
        mainJumpLeft.add_animation_frame(img("""
            . . . . . . . . . . . . . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f e e e e e e e e e e f . . 
                        . f e e e e e e e e e e e e f . 
                        . f d d d d d d d d d e e d f . 
                        . f d d f d d d d f d d e d f . 
                        . f d d f d d d d f d d d e f . 
                        . f d d f d d d d f d d d f . . 
                        . f d d d d d d d d d d d f f . 
                        . d a b c c c c c c c c b a d . 
                        . d a c c c c c c c c c c a d . 
                        . f f f f f b b f f f f f f f . 
                        . . f a a a a a a a a a b f . . 
                        . . . f a a b f f a a b f . . . 
                        . . . . f f f . . f f f . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    mainJumpRight = animation.create_animation(ActionKind.JumpingRight, 100)
    animation.attach_animation(hero, mainJumpRight)
    mainJumpRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d e e d d d d d d d d d f . 
                . f d e d d f d d d d f d d f . 
                . f e d d d f d d d d f d d f . 
                . . f d d d f d d d d f d d f . 
                . . f d d d d d d d d d d d f . 
                . . f b a c c c c c c c c a f . 
                . . f d d d c c c c c c d d f . 
                . . f d d f f f b b f f f d f . 
                . . f b a a a a a a a a a f . . 
                . . . f b a a f f b a a f . . . 
                . . . f b a a f f b a a f . . . 
                . . . . f f f . . f f f . . . .
    """))
    mainJumpRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d e e d d d d d d d d d f . 
                . f d e d d f d d d d f d d f . 
                . f e d d d f d d d d f d d f . 
                . . f d d d f d d d d f d d f . 
                . . f d d d d d d d d d d d f . 
                . . f b a c c c c c c c c a f . 
                . . f d d d c c c c c c d d f . 
                . . f d d f f f b b f f f d f . 
                . . f b a a a a a a a a a f . . 
                . . . f b a a f f b a a f . . . 
                . . . . f f f . . f f f . . . . 
                . . . . . . . . . . . . . . . .
    """))
    for index4 in range(30):
        mainJumpRight.add_animation_frame(img("""
            . . . . . . . . . . . . . . . . 
                        . . . f f f f f f f f f f . . . 
                        . . f e e e e e e e e e e f . . 
                        . f e e e e e e e e e e e e f . 
                        . f d e e d d d d d d d d d f . 
                        . f d e d d f d d d d f d d f . 
                        . f e d d d f d d d d f d d f . 
                        . . f d d d f d d d d f d d f . 
                        . f f d d d d d d d d d d d f . 
                        . d a b c c c c c c c c b a d . 
                        . d a c c c c c c c c c c a d . 
                        . f f f f f f f b b f f f f f . 
                        . . f b a a a a a a a a a f . . 
                        . . . f b a a f f b a a f . . . 
                        . . . . f f f . . f f f . . . . 
                        . . . . . . . . . . . . . . . .
        """))
def animateCrouch():
    global mainCrouchLeft, mainCrouchRight
    mainCrouchLeft = animation.create_animation(ActionKind.CrouchLeft, 100)
    animation.attach_animation(hero, mainCrouchLeft)
    mainCrouchLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d d d d d d d d d e e d f . 
                . f d d f d d d d f d d e d f . 
                . f d d f d d d d f d d d e f . 
                . f d d f d d d d f d d d f . . 
                . f d d d d d d d d d d d f . . 
                . f a c c c c c c c c a b f . . 
                . f d c c c c c c c c c d d f . 
                f d d f f f b b f f f f d d f . 
                . f f a a a a a a a a a b f . . 
                . . . f f f f . f f f f f . . .
    """))
    mainCrouchRight = animation.create_animation(ActionKind.CrouchRight, 100)
    animation.attach_animation(hero, mainCrouchRight)
    mainCrouchRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d e e d d d d d d d d d f . 
                . f d e d d f d d d d f d d f . 
                . f e d d d f d d d d f d d f . 
                . . f d d d f d d d d f d d f . 
                . . f d d d d d d d d d d d f . 
                . . f b a c c c c c c c c a f . 
                . f d d c c c c c c c c c d f . 
                . f d d f f f f b b f f f d d f 
                . . f b a a a a a a a a a f f . 
                . . . f f f f f . f f f f . . .
    """))
def clearGame():
    for value in sprites.all_of_kind(SpriteKind.Bumper):
        value.destroy()
    for value2 in sprites.all_of_kind(SpriteKind.Coin):
        value2.destroy()
    for value3 in sprites.all_of_kind(SpriteKind.Goal):
        value3.destroy()
    for value4 in sprites.all_of_kind(SpriteKind.Flier):
        value4.destroy()
def animateCrouch2():
    global mainCrouchLeft2, mainCrouchRight2
    mainCrouchLeft2 = animation.create_animation(ActionKind.CrouchLeft, 100)
    animation.attach_animation(hero2, mainCrouchLeft2)
    mainCrouchLeft2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d d d d d d d d d e e d f . 
                . f d d f d d d d f d d e d f . 
                . f d d f d d d d f d d d e f . 
                . f d d f d d d d f d d d f . . 
                . f d d d d d d d d d d d f . . 
                . f a c c c c c c c c a b f . . 
                . f d c c c c c c c c c d d f . 
                f d d f f f b b f f f f d d f . 
                . f f a a a a a a a a a b f . . 
                . . . f f f f . f f f f f . . .
    """))
    mainCrouchRight2 = animation.create_animation(ActionKind.CrouchRight, 100)
    animation.attach_animation(hero2, mainCrouchRight2)
    mainCrouchRight2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d e e d d d d d d d d d f . 
                . f d e d d f d d d d f d d f . 
                . f e d d d f d d d d f d d f . 
                . . f d d d f d d d d f d d f . 
                . . f d d d d d d d d d d d f . 
                . . f b a c c c c c c c c a f . 
                . f d d c c c c c c c c c d f . 
                . f d d f f f f b b f f f d d f 
                . . f b a a a a a a a a a f f . 
                . . . f f f f f . f f f f . . .
    """))

def on_player2_button_up_pressed():
    attemptJump_p2()
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def on_overlap_tile(sprite3, location):
    global currentLevel
    info.change_life_by(1)
    currentLevel += 1
    if hasNextLevel():
        game.splash("Next level unlocked!")
        setLevelTileMap(currentLevel)
    else:
        game.over(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile1
    """),
    on_overlap_tile)

def on_on_overlap3(sprite4, otherSprite3):
    info.change_life_by(-1)
    sprite4.say("Ow!", invincibilityPeriod * 1.5)
    music.power_down.play()
    pause(invincibilityPeriod * 1.5)
sprites.on_overlap(SpriteKind.player, SpriteKind.Flier, on_on_overlap3)

def createEnemies():
    global bumper, flier
    # enemy that moves back and forth
    for value5 in tiles.get_tiles_by_type(assets.tile("""
        tile4
    """)):
        bumper = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . f f f f f f . . . . . . 
                            . . . f 7 2 7 7 7 2 f . . . . . 
                            . . f 7 7 7 2 7 2 7 7 f . . . . 
                            . . f 7 7 7 7 7 7 7 7 7 f . . . 
                            . f 7 7 7 2 7 7 7 2 7 7 f . . . 
                            . f 7 7 7 2 7 7 7 2 7 7 7 f . . 
                            . f 7 7 7 7 7 7 7 7 7 7 7 7 f . 
                            . f 7 7 7 7 2 2 2 7 7 7 7 7 f . 
                            . . f 7 7 2 2 7 2 2 7 7 7 7 f . 
                            . . f 7 7 2 7 7 7 2 2 7 7 7 f . 
                            . . . f 7 7 7 7 7 7 7 7 7 7 f . 
                            . . . . f f 7 7 7 7 7 7 7 f . . 
                            . . . . . . f f f f f f f . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Bumper)
        tiles.place_on_tile(bumper, value5)
        tiles.set_tile_at(value5, assets.tile("""
            tile0
        """))
        bumper.ay = gravity
        if Math.percent_chance(50):
            bumper.vx = Math.random_range(30, 60)
        else:
            bumper.vx = Math.random_range(-60, -30)
    # enemy that flies at player
    for value6 in tiles.get_tiles_by_type(assets.tile("""
        tile7
    """)):
        flier = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . f 4 4 4 4 4 4 4 f . . . 
                            . . . f 4 5 5 4 4 4 5 5 4 f . . 
                            . f . f 4 4 4 5 4 5 4 4 4 f . f 
                            . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                            . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                            . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                            . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                            . . . f 4 4 5 5 5 5 5 4 4 f . . 
                            . . . . f 4 5 4 4 4 5 4 f . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Flier)
        tiles.place_on_tile(flier, value6)
        tiles.set_tile_at(value6, assets.tile("""
            tile0
        """))
        animation.attach_animation(flier, flierFlying)
        animation.attach_animation(flier, flierIdle)

def on_player1_button_a_pressed():
    attemptJump()
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def showInstruction(text: str):
    game.show_long_text(text, DialogLayout.BOTTOM)
    music.ba_ding.play()
    info.change_score_by(1)
def initializeHeroAnimations2():
    animateRun2()
    animateIdle2()
    animateCrouch2()
    animateJumps2()
def initializeHeroAnimations():
    animateRun()
    animateIdle()
    animateCrouch()
    animateJumps()
def animateIdle2():
    global mainIdleLeft2, mainIdleRight2
    mainIdleLeft2 = animation.create_animation(ActionKind.IdleLeft, 100)
    animation.attach_animation(hero2, mainIdleLeft2)
    mainIdleLeft2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d d d d d d d d d e e d f . 
                . f d d f d d d d f d d e d f . 
                . f d d f d d d d f d d d e f . 
                . f d d f d d d d f d d d f . . 
                . f d d d d d d d d d d d f . . 
                . f a c c c c c c c c a b f . . 
                . f d d c c c c c c d d d f . . 
                . f d f f f b b f f f d d f . . 
                . . f a a a a a a a a a b f . . 
                . . . f a a b f f a a b f . . . 
                . . . f a a b f f a a b f . . . 
                . . . . f f f . . f f f . . . .
    """))
    mainIdleRight2 = animation.create_animation(ActionKind.IdleRight, 100)
    animation.attach_animation(hero2, mainIdleRight2)
    mainIdleRight2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f f f f . . . 
                . . f e e e e e e e e e e f . . 
                . f e e e e e e e e e e e e f . 
                . f d e e d d d d d d d d d f . 
                . f d e d d f d d d d f d d f . 
                . f e d d d f d d d d f d d f . 
                . . f d d d f d d d d f d d f . 
                . . f d d d d d d d d d d d f . 
                . . f b a c c c c c c c c a f . 
                . . f d d d c c c c c c d d f . 
                . . f d d f f f b b f f f d f . 
                . . f b a a a a a a a a a f . . 
                . . . f b a a f f b a a f . . . 
                . . . f b a a f f b a a f . . . 
                . . . . f f f . . f f f . . . .
    """))
def attemptJump_p2():
    global DubleJumpSpeed2, canDubleJump2
    # else if: either fell off a ledge, or double jumping
    if hero2.is_hitting_tile(CollisionDirection.BOTTOM):
        hero2.vy = -4 * pexelsToMeters2
    elif canDubleJump2:
        DubleJumpSpeed2 = -3 * pexelsToMeters2
        # Good double jump
        if hero2.vy >= -40:
            DubleJumpSpeed2 = -4.5 * pexelsToMeters2
            hero2.start_effect(effects.trail, 500)
            scene.camera_shake(2, 250)
        hero2.vy = DubleJumpSpeed2
        canDubleJump2 = False
def createPlayer(player2: Sprite):
    player2.ay = gravity
    scene.camera_follow_sprite(hero)
    player2.z = 5
    controller.player1.move_sprite(hero, 100, 0)
    info.set_life(3)
    info.set_score(0)
def createPlayer2(player22: Sprite):
    player22.ay = gravity
    controller.player2.move_sprite(player22)
    player22.z = 5
    info.set_life(3)
    info.set_score(0)
def initializeLevel(level3: number):
    global playerStartLocation
    effects.clouds.start_screen_effect()
    playerStartLocation = tiles.get_tiles_by_type(assets.tile("""
        tile6
    """))[0]
    tiles.place_on_tile(hero, playerStartLocation)
    tiles.set_tile_at(playerStartLocation, assets.tile("""
        tile0
    """))
    createEnemies()
    spawnGoals()

def on_player2_connected():
    global Player2, hero2, invincibilityPeriod, pexelsToMeters2, gravity2, levelCount, currentLevel2
    Player2 = 1
    hero2 = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . f f f f f f f f f f . . . 
                    . . f e e e e e e e e e e f . . 
                    . f e e e e e e e e e e e e f . 
                    . f d e e d d d d d d d d d f . 
                    . f d e d d f d d d d f d d f . 
                    . f e d d d f d d d d f d d f . 
                    . . f d d d f d d d d f d d f . 
                    . . f d d d d d d d d d d d f . 
                    . . f b a 3 3 3 3 3 3 3 3 a f . 
                    . . f d d d 3 3 3 3 3 3 d d f . 
                    . . f d d f f f b b f f f d f . 
                    . . f b 3 3 3 3 3 3 3 3 3 f . . 
                    . . . f b 3 3 f f b 3 3 f . . . 
                    . . . f b 3 3 f f b 3 3 f . . . 
                    . . . . f f f . . f f f . . . .
        """),
        SpriteKind.player)
    # how long to pause between each contact with a
    # single enemy
    invincibilityPeriod = 600
    pexelsToMeters2 = 30
    gravity2 = 9.81 * pexelsToMeters2
    scene.set_background_image(img("""
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9989998999899989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998999899989998999899989998999899989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                9989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989998999899989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
                9899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999999999999999999999999999
                8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
                9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
    """))
    initializeHeroAnimations2()
    createPlayer2(hero2)
    levelCount = 9
    currentLevel2 = 0
    setLevelTileMap(currentLevel2)
controller.player2.on_event(ControllerEvent.CONNECTED, on_player2_connected)

def hasNextLevel():
    return currentLevel != levelCount
def animateRun2():
    global mainRunLeft2, mainRunRigth2
    mainRunLeft2 = animation.create_animation(ActionKind.RunningLeft, 100)
    animation.attach_animation(hero2, mainRunLeft2)
    mainRunLeft2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f . . . . . . 
                . . f e e e e e e e f . . . . . 
                . f e e e e e e e e e f . . . . 
                . f d d d d e d d e e f . . . . 
                . f d d f d d e d e e f . . . . 
                . f d d f d d d e e e f . . . . 
                . f d d f d d d d d d f . . . . 
                . f d d d d d d d d d f . . . . 
                . . f c c c 3 3 c c b f . . . . 
                . . f c c d d d c c b f . . . . 
                . . f b f f d d f f f f . . . . 
                . . f a 3 3 3 3 3 3 b f . . . . 
                . . . f 3 3 3 3 b f f . . . . . 
                . . . f 3 3 3 3 b f . . . . . . 
                . . . . f f f f f . . . . . . .
    """))
    mainRunLeft2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . f f f f f f f . . . . . . 
                . . f e e e e e e e f . . . . . 
                . f e e e e e e e e e f . . . . 
                . f d d d d e d d e e f . . . . 
                . f d d f d d e d e e f . . . . 
                . f d d f d d d e e e f . . . . 
                . f d d f d d d d d d f . . . . 
                . f d d d d d d d d d f . . . . 
                . . f c c c c a a c b f . . . . 
                . . f c c c c d d c b f . . . . 
                . . f b f f d d d f f f f . . . 
                . . f a a a a a a a a b f f . . 
                . . . f a a b f f a a a f f . . 
                . . . . f f f . f f f f f . . .
    """))
    mainRunLeft2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f f . . . . . . 
                . . f e e e e e e e f . . . . . 
                . f e e e e e e e e e f . . . . 
                . f d d d d e d d e e f . . . . 
                . f d d f d d e d e e f . . . . 
                . f d d f d d d e e e f . . . . 
                . f d d f d d d d d d f . . . . 
                . f d d d d d d d d d f . . . . 
                . . f c c c a a c c b f . . . . 
                . . f c c d d d c c b f . . . . 
                . . f b f f d d f f f f . . . . 
                . . f a a a a a a a b f . . . . 
                . . . f a a a a b f f . . . . . 
                . . . f a a a a b f . . . . . . 
                . . . . f f f f f . . . . . . .
    """))
    mainRunLeft2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . f f f f f f f . . . . . . 
                . . f e e e e e e e f . . . . . 
                . f e e e e e e e e e f . . . . 
                . f d d d d e d d e e f . . . . 
                . f d d f d d e d e e f . . . . 
                . f d d f d d d e e e f . . . . 
                . f d d f d d d d d d f . . . . 
                . f d d d d d d d d d f . . . . 
                . . f c a a c c c c b f . . . . 
                . f d d d b c c c c b f . . . . 
                f f f d d f f f f f f f . . . . 
                f f f a a a a a a a b f . . . . 
                . f a a b f a a b f f . . . . . 
                . f f f f . f f f . . . . . . .
    """))
    mainRunRigth2 = animation.create_animation(ActionKind.RunningRight, 100)
    animation.attach_animation(hero2, mainRunRigth2)
    mainRunRigth2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f f . . . 
                . . . . . f e e e e e e e f . . 
                . . . . f e e e e e e e e e f . 
                . . . . f e e d d e d d d d f . 
                . . . . f e e d e d d f d d f . 
                . . . . f e e e d d d f d d f . 
                . . . . f d d d d d d f d d f . 
                . . . . f d d d d d d d d d f . 
                . . . . f b c c a a c c c f . . 
                . . . . f b c c d d d c c f . . 
                . . . . f f f f d d f f b f . . 
                . . . . f b a a a a a a a f . . 
                . . . . . f f b a a a a f . . . 
                . . . . . . f b a a a a f . . . 
                . . . . . . . f f f f f . . . .
    """))
    mainRunRigth2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f f . . . 
                . . . . . f e e e e e e e f . . 
                . . . . f e e e e e e e e e f . 
                . . . . f e e d d e d d d d f . 
                . . . . f e e d e d d f d d f . 
                . . . . f e e e d d d f d d f . 
                . . . . f d d d d d d f d d f . 
                . . . . f d d d d d d d d d f . 
                . . . . f b c a a c c c c f . . 
                . . . . f b c d d c c c c f . . 
                . . . f f f f d d d f f b f . . 
                . . f f b a a a a a a a a f . . 
                . . f f a a a f f b a a f . . . 
                . . . f f f f . . f f f . . . .
    """))
    mainRunRigth2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f f . . . 
                . . . . . f e e e e e e e f . . 
                . . . . f e e e e e e e e e f . 
                . . . . f e e d d e d d d d f . 
                . . . . f e e d e d d f d d f . 
                . . . . f e e e d d d f d d f . 
                . . . . f d d d d d d f d d f . 
                . . . . f d d d d d d d d d f . 
                . . . . f b c c a a c c c f . . 
                . . . . f b c c d d d c c f . . 
                . . . . f f f f d d f f b f . . 
                . . . . f b a a a a a a a f . . 
                . . . . . f f b a a a a f . . . 
                . . . . . . f b a a a a f . . . 
                . . . . . . . f f f f f . . . .
    """))
    mainRunRigth2.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . f f f f f f f . . . 
                . . . . . f e e e e e e e f . . 
                . . . . f e e e e e e e e e f . 
                . . . . f e e d d e d d d d f . 
                . . . . f e e d e d d f d d f . 
                . . . . f e e e d d d f d d f . 
                . . . . f d d d d d d f d d f . 
                . . . . f d d d d d d d d d f . 
                . . . . f b c c c c a a c f . . 
                . . . . f b c c c c b d d d f . 
                . . . . f f f f f f f d d f f f 
                . . . . f b a a a a a a a f f f 
                . . . . . f f b a a f b a a f . 
                . . . . . . . f f f . f f f . .
    """))
def spawnGoals():
    global coin
    for value7 in tiles.get_tiles_by_type(assets.tile("""
        tile5
    """)):
        coin = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . f f f f . . . . . . 
                            . . . . f f 5 5 5 5 f f . . . . 
                            . . . . f 5 5 5 5 5 5 f . . . . 
                            . . . f 5 5 5 4 4 5 5 5 f . . . 
                            . . . f 5 5 5 4 4 5 5 5 f . . . 
                            . . . f 5 5 5 4 4 5 5 5 f . . . 
                            . . . f 5 5 5 4 4 5 5 5 f . . . 
                            . . . . f 5 5 5 5 5 5 f . . . . 
                            . . . . f f 5 5 5 5 f f . . . . 
                            . . . . . . f f f f . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Coin)
        tiles.place_on_tile(coin, value7)
        animation.attach_animation(coin, coinAnimation)
        animation.set_action(coin, ActionKind.Idle)
        tiles.set_tile_at(value7, assets.tile("""
            tile0
        """))

def on_player1_button_down_pressed():
    if not (hero.is_hitting_tile(CollisionDirection.BOTTOM)):
        hero.vy += 80
controller.player1.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player1_button_down_pressed)

heroFacingLeft = False
heroFacingLeft2 = False
coin: Sprite = None
mainRunRigth2: animation.Animation = None
mainRunLeft2: animation.Animation = None
currentLevel2 = 0
gravity2 = 0
DubleJumpSpeed2 = 0
pexelsToMeters2 = 0
canDubleJump2 = False
mainIdleRight2: animation.Animation = None
mainIdleLeft2: animation.Animation = None
flier: Sprite = None
bumper: Sprite = None
mainCrouchRight2: animation.Animation = None
mainCrouchLeft2: animation.Animation = None
mainCrouchRight: animation.Animation = None
mainCrouchLeft: animation.Animation = None
mainJumpRight: animation.Animation = None
mainJumpLeft: animation.Animation = None
mainRunRight: animation.Animation = None
mainRunLeft: animation.Animation = None
flierIdle: animation.Animation = None
flierFlying: animation.Animation = None
mainJumpRight2: animation.Animation = None
mainJumpLeft2: animation.Animation = None
mainIdleRight: animation.Animation = None
mainIdleLeft: animation.Animation = None
doubleJumpSpeed = 0
canDoubleJump = False
coinAnimation: animation.Animation = None
hero2: Sprite = None
playerStartLocation: tiles.Location = None
currentLevel = 0
levelCount = 0
gravity = 0
pixelsToMeters = 0
invincibilityPeriod = 0
hero: Sprite = None
Player2 = 0
Player2 = 0
hero = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . f f f f f f f f f f . . . 
            . . f e e e e e e e e e e f . . 
            . f e e e e e e e e e e e e f . 
            . f d e e d d d d d d d d d f . 
            . f d e d d f d d d d f d d f . 
            . f e d d d f d d d d f d d f . 
            . . f d d d f d d d d f d d f . 
            . . f d d d d d d d d d d d f . 
            . . f b a c c c c c c c c a f . 
            . . f d d d c c c c c c d d f . 
            . . f d d f f f b b f f f d f . 
            . . f b a a a a a a a a a f . . 
            . . . f b a a f f b a a f . . . 
            . . . f b a a f f b a a f . . . 
            . . . . f f f . . f f f . . . .
    """),
    SpriteKind.player)
# how long to pause between each contact with a
# single enemy
invincibilityPeriod = 600
pixelsToMeters = 30
gravity = 9.81 * pixelsToMeters
scene.set_background_image(img("""
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9989998999899989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989998999899989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998999899989998999899989998999899989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        9989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989898999898989998989899989998999899989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
        8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
        9899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999989999999899999998999999999999999999999999999999
        8989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989898989
        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
"""))
initializeAnimations()
createPlayer(hero)
levelCount = 9
currentLevel = 0
setLevelTileMap(currentLevel)
giveIntroduction()
# set up hero animations

def on_on_update():
    global heroFacingLeft2
    if Player2 < 0:
        if hero2.vx < 0:
            heroFacingLeft2 = True
        elif hero2.vx > 0:
            heroFacingLeft2 = False
        if hero2.is_hitting_tile(CollisionDirection.TOP):
            hero2.vy = 0
        if controller.player2.is_pressed(ControllerButton.DOWN):
            if heroFacingLeft2:
                animation.set_action(hero2, ActionKind.Walking2)
            else:
                animation.set_action(hero2, ActionKind.Walking2)
        elif hero2.vy < 20 and not (hero2.is_hitting_tile(CollisionDirection.BOTTOM)):
            if heroFacingLeft2:
                animation.set_action(hero2, ActionKind.Walking2)
            else:
                animation.set_action(hero2, ActionKind.Walking2)
        elif hero2.vx < 0:
            animation.set_action(hero2, ActionKind.Walking2)
        elif hero2.vx > 0:
            animation.set_action(hero2, ActionKind.Walking2)
        else:
            if heroFacingLeft2:
                animation.set_action(hero2, ActionKind.Walking2)
            else:
                animation.set_action(hero2, ActionKind.Walking2)
game.on_update(on_on_update)

# Flier movement

def on_on_update2():
    if Player2 < 0:
        for value8p2 in sprites.all_of_kind(SpriteKind.Flier):
            if abs(value8p2.x - value8p2.x) < 60:
                if value8p2.x - hero2.x < -5:
                    value8p2.vx = 25
                elif value8p2.x - hero2.x > 5:
                    value8p2.vx = -25
                if value8p2.y - hero2.y < -5:
                    value8p2.vy = 25
                elif value8p2.y - hero2.y > 5:
                    value8p2.vy = -25
                animation.set_action(value8p2, ActionKind.Flying)
            else:
                value8p2.vy = -20
                value8p2.vx = 0
                animation.set_action(value8p2, ActionKind.Idle)
game.on_update(on_on_update2)

# Reset double jump when standing on wall

def on_on_update3():
    global canDoubleJump, canDubleJump2
    if hero.is_hitting_tile(CollisionDirection.BOTTOM):
        canDoubleJump = True
    if hero2.is_hitting_tile(CollisionDirection.BOTTOM):
        canDubleJump2 = True
game.on_update(on_on_update3)

# set up hero animations

def on_on_update4():
    global heroFacingLeft
    if hero.vx < 0:
        heroFacingLeft = True
    elif hero.vx > 0:
        heroFacingLeft = False
    if hero.is_hitting_tile(CollisionDirection.TOP):
        hero.vy = 0
    if controller.player1.is_pressed(ControllerButton.DOWN):
        if heroFacingLeft:
            animation.set_action(hero, ActionKind.CrouchLeft)
        else:
            animation.set_action(hero, ActionKind.CrouchRight)
    elif hero.vy < 20 and not (hero.is_hitting_tile(CollisionDirection.BOTTOM)):
        if heroFacingLeft:
            animation.set_action(hero, ActionKind.JumpingLeft)
        else:
            animation.set_action(hero, ActionKind.JumpingRight)
    elif hero.vx < 0:
        animation.set_action(hero, ActionKind.RunningLeft)
    elif hero.vx > 0:
        animation.set_action(hero, ActionKind.RunningRight)
    else:
        if heroFacingLeft:
            animation.set_action(hero, ActionKind.IdleLeft)
        else:
            animation.set_action(hero, ActionKind.IdleRight)
game.on_update(on_on_update4)

# bumper movement

def on_on_update5():
    for value9 in sprites.all_of_kind(SpriteKind.Bumper):
        if value9.is_hitting_tile(CollisionDirection.LEFT):
            value9.vx = Math.random_range(30, 60)
        elif value9.is_hitting_tile(CollisionDirection.RIGHT):
            value9.vx = Math.random_range(-60, -30)
game.on_update(on_on_update5)

# Flier movement

def on_on_update6():
    for value8 in sprites.all_of_kind(SpriteKind.Flier):
        if abs(value8.x - hero.x) < 60:
            if value8.x - hero.x < -5:
                value8.vx = 25
            elif value8.x - hero.x > 5:
                value8.vx = -25
            if value8.y - hero.y < -5:
                value8.vy = 25
            elif value8.y - hero.y > 5:
                value8.vy = -25
            animation.set_action(value8, ActionKind.Flying)
        else:
            value8.vy = -20
            value8.vx = 0
            animation.set_action(value8, ActionKind.Idle)
game.on_update(on_on_update6)
