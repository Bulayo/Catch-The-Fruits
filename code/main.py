from settings import *
from player import Player

class Game:

    def __init__(self):
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Catch The Fruits By Bulayo")
        self.clock = pygame.time.Clock()

        # Images
        self.player_img = pygame.image.load(join("assets","catcher.png"))
        self.fruit_img = [pygame.image.load(join("image", f"fruitassets_0{index}")) for index in range(0, 24)]

        # Groups
        self.all_sprites = pygame.sprite.Group()
        self.fruit_sprites = pygame.sprite.Group()

        self.running = True

        # Object
        self.player = Player(self.all_sprites, (WIDTH / 2, 477), self.player_img)


    def run(self):
        while self.running:
            self.WIN.fill((50, 50, 50))
            dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update
            self.all_sprites.update(dt)

            # Draw
            self.all_sprites.draw(self.WIN)

            pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()