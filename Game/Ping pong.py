import pygame

width = 500
height = 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (x, y, width, height)
        self.color = color
        self.vel = 5

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_a]:
            self.x -= self.vel
        if keys[pygame.K_d]:
            self.x += self.vel

        self.rect = (self.x, self.y, self.width, self.height)

def redraw_window(win, player1, player2, ball):
    win.fill((255, 255, 255))
    player1.draw(win)
    player2.draw(win)
    pygame.draw.circle(win, "red", ball.center, 10)
    pygame.display.update()

def main():
    run = True
    person1 = Player(50, 40, 50, 10, (255, 0, 255))
    person2 = Player(50, 450, 50, 10, (111, 2, 44))
    clock = pygame.time.Clock()
    ball = pygame.Rect(width/2-10, height/2-10, 20, 20)
    x_speed, y_speed = 1, 1

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        person1.move()
        person2.move()
        ball.x += x_speed
        ball.y += y_speed

        redraw_window(win, person1, person2, ball)

if __name__ == "__main__":
    main()
