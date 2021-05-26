def on_countdown_end():
    game.over(True, effects.confetti)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy(effects.star_field, 100)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

projectile2: Sprite = None
projectile: Sprite = None
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . . . 2 2 2 2 2 2 2 2 . . . . 
            . . . 2 4 2 2 2 2 2 2 c 2 . . . 
            . . 2 c 4 2 2 2 2 2 2 c c 2 . . 
            . 2 c c 4 4 4 4 4 4 2 c c 4 2 d 
            . 2 c 2 e e e e e e e b c 4 2 2 
            . 2 2 e b b e b b b e e b 4 2 2 
            . 2 e b b b e b b b b e 2 2 2 2 
            . e e 2 2 2 e 2 2 2 2 2 e 2 2 2 
            . e e e e e e f e e e f e 2 d d 
            . e e e e e e f e e f e e e 2 d 
            . e e e e e e f f f e e e e e e 
            . e f f f f e e e e f f f e e e 
            . . f f f f f e e f f f f f e . 
            . . . f f f . . . . f f f f . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite)
mySprite.set_stay_in_screen(True)
scene.set_background_image(assets.image("""
    Freeway
"""))
scroller.scroll_background_with_speed(-90, 0)
info.start_countdown(35)

def on_forever():
    global projectile
    projectile = sprites.create_projectile_from_side(img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f f 2 2 f f f . . . . 
                    . . . f f f 2 2 2 2 f f f . . . 
                    . . f f f e e e e e e f f f . . 
                    . . f f e 2 2 2 2 2 2 e e f . . 
                    . . f e 2 f f f f f f 2 e f . . 
                    . . f f f f e e e e f f f f . . 
                    . f f e f b f 4 4 f b f e f f . 
                    . f e e 4 1 f d d f 1 4 e e f . 
                    . . f e e d d d d d d e e f . . 
                    . . . f e e 4 4 4 4 e e f . . . 
                    . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                    . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        -90,
        0)
    projectile.y = randint(15, 115)
    pause(1000)
forever(on_forever)

def on_forever2():
    global projectile2
    projectile2 = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . 5 . 5 . . . . . . 
                    . . . . . . f 5 5 5 f . . . . . 
                    . . . . . f 6 2 5 5 6 f . . . . 
                    . . . . f 6 6 6 6 1 6 6 f . . . 
                    . . . . f 6 6 6 6 6 1 6 f . . . 
                    . . . . f d f d 6 6 6 1 f . . . 
                    . . . . f d f d 6 6 6 6 f f . . 
                    . . . . f d 3 d d 6 6 6 f 6 f . 
                    . . . . . f d d d f f 6 f f . . 
                    . . . . . . f f 3 3 f f 6 6 f . 
                    . . . . . f 5 3 3 d d f f f . . 
                    . . . . . f 3 3 3 f d d f . . . 
                    . . . . . . f 3 5 f f f . . . . 
                    . . . . . f 3 3 3 3 f . . . . . 
                    . . . . . . f f f f f . . . . .
        """),
        -145,
        0)
    projectile2.y = randint(15, 115)
    pause(2100)
forever(on_forever2)
