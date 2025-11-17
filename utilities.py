import pygame

def draw_text(gameDisplay:pygame.Surfase, msg, color, x, y, s, center=True):
    screen_text = pygame.font.SysFont("Calibri", s).render(msg, True, color)
    if center:
        rect = screen_text.get_rect()
        rect.center = (x, y)
    else:
        rect = pygame.Rect(x, y, s, s)
    gameDisplay.blit(screen_text, rect)
def is_colliding(centerX, centerY, centerXTo, centerYTo, radius):
    is_horizontal_colliding = (
        centerX > centerXTo - radius  and
        centerX < centerXTo + radius
    )
    is_vertical_colliding = (
        centerY > centerYTo - radius and 
        centerY < centerYTo + radius
    )    
    return is_horizontal_colliding and is_vertical_colliding 