import pygame

pygame.init()

pygame.mixer.music.load("bordered_master.wav")
pygame.mixer.music.play(-1)
# input('hahaha')

screen = pygame.display.set_mode((800, 700))
done = False
is_blue = True
x = 30
y = 30

# curs, mask = pygame.cursors.compile_cursor(pygame.cursors.thickarrow_strings, 'X', '.')
# pygame.mouse.set_cursor((24, 24), (0, 0), curs, mask)
#
# thickarrow_strings = (               #sized 24x24
#   "XX                      ",
#   "XXX                     ",
#   "XXXX                    ",
#   "XX.XX                   ",
#   "XX..XX                  ",
#   "XX...XX                 ",
#   "XX....XX                ",
#   "XX.....XX               ",
#   "XX......XX              ",
#   "XX.......XX             ",
#   "XX........XX            ",
#   "XX........XXX           ",
#   "XX......XXXXX           ",
#   "XX.XXX..XX              ",
#   "XXXX XX..XX             ",
#   "XX   XX..XX             ",
#   "     XX..XX             ",
#   "      XX..XX            ",
#   "      XX..XX            ",
#   "       XXXX             ",
#   "       XX               ",
#   "                        ",
#   "                        ",
#   "                        ",
# )


clock = pygame.time.Clock()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3

    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))

    pygame.draw.rect(screen, color, pygame.Rect(x, y, 300, 300))

    pygame.display.flip()
    clock.tick(200)