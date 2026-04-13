import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - Enhanced")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 255, 0)
PURPLE = (150, 0, 255)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Game variables
score = 0
lives = 3
level = 1
enemies_killed_this_level = 0
enemies_needed_for_next_level = 10

# Level configuration
LEVEL_CONFIG = {
    1: {"enemy_count": 5, "enemy_speed_min": 1, "enemy_speed_max": 3, "spawn_rate": 0},
    2: {"enemy_count": 6, "enemy_speed_min": 1, "enemy_speed_max": 4, "spawn_rate": 0},
    3: {"enemy_count": 7, "enemy_speed_min": 2, "enemy_speed_max": 4, "spawn_rate": 0},
    4: {"enemy_count": 8, "enemy_speed_min": 2, "enemy_speed_max": 5, "spawn_rate": 0},
    5: {"enemy_count": 9, "enemy_speed_min": 2, "enemy_speed_max": 5, "spawn_rate": 0},
    6: {"enemy_count": 10, "enemy_speed_min": 3, "enemy_speed_max": 6, "spawn_rate": 0},
    7: {"enemy_count": 11, "enemy_speed_min": 3, "enemy_speed_max": 6, "spawn_rate": 0},
    8: {"enemy_count": 12, "enemy_speed_min": 3, "enemy_speed_max": 7, "spawn_rate": 0},
    9: {"enemy_count": 13, "enemy_speed_min": 4, "enemy_speed_max": 7, "spawn_rate": 0},
    10: {"enemy_count": 15, "enemy_speed_min": 4, "enemy_speed_max": 8, "spawn_rate": 0},
}

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 30))
        self.image.fill(GREEN)
        # Draw a simple spaceship shape
        pygame.draw.polygon(self.image, BLUE, [(20, 0), (40, 30), (20, 20), (0, 30)])
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed = 5
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.power_level = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        
        # Keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            
            if self.power_level == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
            elif self.power_level == 2:
                # Double shot
                bullet1 = Bullet(self.rect.centerx - 10, self.rect.top)
                bullet2 = Bullet(self.rect.centerx + 10, self.rect.top)
                all_sprites.add(bullet1, bullet2)
                bullets.add(bullet1, bullet2)
            else:
                # Triple shot
                bullet1 = Bullet(self.rect.centerx - 15, self.rect.top)
                bullet2 = Bullet(self.rect.centerx, self.rect.top)
                bullet3 = Bullet(self.rect.centerx + 15, self.rect.top)
                all_sprites.add(bullet1, bullet2, bullet3)
                bullets.add(bullet1, bullet2, bullet3)

    def power_up(self):
        if self.power_level < 3:
            self.power_level += 1

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((4, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed_min=1, speed_max=4):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        pygame.draw.circle(self.image, PURPLE, (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(speed_min, speed_max + 1)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

# PowerUp class
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y, power_type="health"):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.power_type = power_type
        
        if power_type == "health":
            self.image.fill(GREEN)
            pygame.draw.circle(self.image, WHITE, (10, 10), 8)
        else:  # weapon power
            self.image.fill(ORANGE)
            pygame.draw.circle(self.image, YELLOW, (10, 10), 8)
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 3

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.kill()

# Explosion class
class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.radius = 5
        self.max_radius = 30
        self.growth = 2
        self.x = x
        self.y = y
        self.image = pygame.Surface((self.max_radius * 2, self.max_radius * 2))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.radius += self.growth
        if self.radius > self.max_radius:
            self.kill()
        else:
            self.image.fill(BLACK)
            pygame.draw.circle(self.image, YELLOW, (self.max_radius, self.max_radius), self.radius)
            pygame.draw.circle(self.image, RED, (self.max_radius, self.max_radius), max(0, self.radius - 5))

# Sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
powerups = pygame.sprite.Group()
explosions = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Font for text
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)
large_font = pygame.font.Font(None, 72)

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def get_level_config(level_num):
    """Get configuration for a specific level"""
    if level_num in LEVEL_CONFIG:
        return LEVEL_CONFIG[level_num]
    else:
        # For levels beyond 10, scale difficulty
        extra_levels = level_num - 10
        return {
            "enemy_count": 15 + extra_levels,
            "enemy_speed_min": 4 + (extra_levels // 3),
            "enemy_speed_max": 8 + (extra_levels // 2),
            "spawn_rate": 0
        }

def start_level(level_num):
    """Initialize a new level"""
    global enemies_killed_this_level, enemies_needed_for_next_level
    
    enemies_killed_this_level = 0
    enemies_needed_for_next_level = 10 + (level_num * 2)  # Increases with each level
    
    # Clear existing enemies
    for enemy in enemies:
        enemy.kill()
    
    # Get level configuration
    config = get_level_config(level_num)
    
    # Create enemies for this level
    for i in range(config["enemy_count"]):
        enemy = Enemy(config["enemy_speed_min"], config["enemy_speed_max"])
        all_sprites.add(enemy)
        enemies.add(enemy)

def show_level_complete():
    """Display level complete message"""
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(BLACK)
    screen.blit(overlay, (0, 0))
    
    draw_text("LEVEL COMPLETE!", large_font, CYAN, WIDTH // 2, HEIGHT // 2 - 100)
    draw_text(f"Level {level} Cleared!", font, WHITE, WIDTH // 2, HEIGHT // 2 - 30)
    draw_text(f"Score: {score}", font, YELLOW, WIDTH // 2, HEIGHT // 2 + 20)
    draw_text("Press SPACE to Continue", small_font, GREEN, WIDTH // 2, HEIGHT // 2 + 80)

def show_game_over():
    draw_text("GAME OVER", large_font, RED, WIDTH // 2, HEIGHT // 2 - 80)
    draw_text(f"Final Score: {score}", font, WHITE, WIDTH // 2, HEIGHT // 2 - 10)
    draw_text(f"Level Reached: {level}", font, YELLOW, WIDTH // 2, HEIGHT // 2 + 30)
    draw_text("Press SPACE to Restart or ESC to Quit", small_font, WHITE, WIDTH // 2, HEIGHT // 2 + 80)

def reset_game():
    global score, lives, level, player
    score = 0
    lives = 3
    level = 1
    
    # Clear all sprites
    all_sprites.empty()
    enemies.empty()
    bullets.empty()
    powerups.empty()
    explosions.empty()
    
    # Recreate player
    player = Player()
    all_sprites.add(player)
    
    # Start level 1
    start_level(level)

# Initialize first level
start_level(level)

# Game states
PLAYING = 0
LEVEL_COMPLETE = 1
GAME_OVER = 2

game_state = PLAYING
level_complete_time = 0

# Game loop
running = True

while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_state == GAME_OVER:
                if event.key == pygame.K_SPACE:
                    game_state = PLAYING
                    reset_game()
                elif event.key == pygame.K_ESCAPE:
                    running = False
            elif game_state == LEVEL_COMPLETE:
                if event.key == pygame.K_SPACE:
                    level += 1
                    start_level(level)
                    game_state = PLAYING
            else:
                if event.key == pygame.K_SPACE:
                    player.shoot()

    if game_state == PLAYING:
        # Update
        all_sprites.update()
        
        # Auto shoot when holding space
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot()
        
        # Check bullet-enemy collisions
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 10
            enemies_killed_this_level += 1
            
            explosion = Explosion(hit.rect.centerx, hit.rect.centery)
            all_sprites.add(explosion)
            explosions.add(explosion)
            
            # Spawn new enemy only if we haven't completed the level
            if enemies_killed_this_level < enemies_needed_for_next_level:
                config = get_level_config(level)
                enemy = Enemy(config["enemy_speed_min"], config["enemy_speed_max"])
                all_sprites.add(enemy)
                enemies.add(enemy)
            
            # Random powerup spawn
            rand_val = random.random()
            if rand_val > 0.92:
                powerup = PowerUp(hit.rect.centerx, hit.rect.centery, "health")
                all_sprites.add(powerup)
                powerups.add(powerup)
            elif rand_val > 0.88:
                powerup = PowerUp(hit.rect.centerx, hit.rect.centery, "weapon")
                all_sprites.add(powerup)
                powerups.add(powerup)
        
        # Check if level is complete
        if enemies_killed_this_level >= enemies_needed_for_next_level and len(enemies) == 0:
            game_state = LEVEL_COMPLETE
            score += 100 * level  # Bonus points for completing level
            level_complete_time = pygame.time.get_ticks()
        
        # Check player-enemy collisions
        hits = pygame.sprite.spritecollide(player, enemies, True)
        for hit in hits:
            lives -= 1
            explosion = Explosion(hit.rect.centerx, hit.rect.centery)
            all_sprites.add(explosion)
            explosions.add(explosion)
            
            # Spawn new enemy
            if enemies_killed_this_level < enemies_needed_for_next_level:
                config = get_level_config(level)
                enemy = Enemy(config["enemy_speed_min"], config["enemy_speed_max"])
                all_sprites.add(enemy)
                enemies.add(enemy)
            
            if lives <= 0:
                game_state = GAME_OVER
        
        # Check player-powerup collisions
        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if hit.power_type == "health":
                lives += 1
                score += 50
            else:  # weapon power
                player.power_up()
                score += 75
    
    # Draw
    screen.fill(BLACK)
    
    # Draw stars background
    for i in range(50):
        x = random.randrange(WIDTH)
        y = random.randrange(HEIGHT)
        pygame.draw.circle(screen, WHITE, (x, y), 1)
    
    all_sprites.draw(screen)
    
    # Draw HUD
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    
    lives_text = small_font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (10, 40))
    
    level_text = small_font.render(f"Level: {level}", True, WHITE)
    screen.blit(level_text, (10, 70))
    
    # Draw level progress
    progress_text = small_font.render(f"Progress: {enemies_killed_this_level}/{enemies_needed_for_next_level}", True, CYAN)
    screen.blit(progress_text, (10, 100))
    
    # Draw power level
    power_text = small_font.render(f"Weapon: {'I' * player.power_level}", True, ORANGE)
    screen.blit(power_text, (10, 130))
    
    # Draw controls
    controls_text = small_font.render("Controls: Arrow Keys/AD to move, SPACE to shoot", True, WHITE)
    screen.blit(controls_text, (WIDTH // 2 - 200, HEIGHT - 30))
    
    if game_state == LEVEL_COMPLETE:
        show_level_complete()
    elif game_state == GAME_OVER:
        show_game_over()
    
    pygame.display.flip()

pygame.quit()