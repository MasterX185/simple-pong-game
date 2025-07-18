import pygame
import random

pygame.init()

player_lives = 3
font = pygame.font.Font(None, 74) # Eine Schriftart für die Anzeige

ki_lives = 3 # Lebensanzahl für die KI
font_ki = pygame.font.Font(None, 74) # Schriftart für die KI

# --- Fenster- und Farbeinstellungen ---
screen_wiisplay.set_mode((screen_width, screen_height))
pygame.display.setdth = 800
screen_height = 600
screen = pygame.d_caption("Pong")

schwarz = (0, 0, 0)
weiss = (255, 255, 255)
rot = (225, 0, 0)

# --- Spiel-Objekte ---
schlaeger_breite = 15
schlaeger_hoehe = 100

# Spieler-Schläger (links)
spieler_schlaeger = pygame.Rect(50, (screen_height - schlaeger_hoehe) // 2, schlaeger_breite, schlaeger_hoehe)
spieler_geschwindigkeit = 0

# KI-Schläger (rechts)
ki_schlaeger = pygame.Rect(screen_width - 50 - schlaeger_breite, (screen_height - schlaeger_hoehe) // 2, schlaeger_breite, schlaeger_hoehe)
ki_geschwindigkeit = 4 # Geschwindigkeit der KI

# Ball
ball = pygame.Rect(screen_width // 2 - 15, screen_height // 2 - 15, 30, 30)
ball_geschwindigkeit_x = 5
ball_geschwindigkeit_y = 5

# --- Game Loop ---
uhr = pygame.time.Clock()
running = True
while running:
    # --- Ereignisbehandlung (User Input) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Spielereingabe für Bewegung
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                spieler_geschwindigkeit = -6
            if event.key == pygame.K_DOWN:
                spieler_geschwindigkeit = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                spieler_geschwindigkeit = 0

    # --- Bewegungslogik ---

    # Spielerbewegung
    spieler_schlaeger.y += spieler_geschwindigkeit
    if spieler_schlaeger.top < 0:
        spieler_schlaeger.top = 0
    if spieler_schlaeger.bottom > screen_height:
        spieler_schlaeger.bottom = screen_height

    # Ballbewegung
    ball.x += ball_geschwindigkeit_x
    ball.y += ball_geschwindigkeit_y

    # Ball-Kollision mit Wänden (oben/unten)
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_geschwindigkeit_y *= -1

    # Ball-Kollision mit Schlägern
    if ball.colliderect(spieler_schlaeger) or ball.colliderect(ki_schlaeger):
        ball_geschwindigkeit_x *= -1

    # Überprüfen, ob der Ball den Bildschirm verlässt (Lebensabzug)
    if ball.left <= 0: # Ball hat linken Rand verlassen (KI punktet / Spieler verliert Leben)
        player_lives -= 1
        ball.center = (screen_width / 2, screen_height / 2) # Ball zurücksetzen
        ball_geschwindigkeit_x *= random.choice((1, -1)) # Zufällige Startrichtung
        ball_geschwindigkeit_y *= random.choice((1, -1))

    if ball.right >= screen_width: # Ball hat rechten Rand verlassen (Spieler punktet / KI verliert "Leben")
        ki_lives -= 1
        ball.center = (screen_width / 2, screen_height / 2) # Ball zurücksetzen
        ball_geschwindigkeit_x *= random.choice((1, -1))
        ball_geschwindigkeit_y *= random.choice((1, -1))

    # KI-Schläger Begrenzung (optional, falls du KI bewegst)
    if ki_schlaeger.top < 0:
        ki_schlaeger.top = 0
    if ki_schlaeger.bottom > screen_height:
        ki_schlaeger.bottom = screen_height

    # --- Zeichnen ---
    screen.fill(schwarz)
    pygame.draw.rect(screen, weiss, spieler_schlaeger)
    pygame.draw.rect(screen, weiss, ki_schlaeger)
    pygame.draw.ellipse(screen, weiss, ball)
    pygame.draw.aaline(screen, weiss, (screen_width // 2, 0), (screen_width // 2, screen_height))

    # Lebensanzeige rendern und anzeigen
    lives_text = font.render(f"Lives: {player_lives}", True, weiss)
    screen.blit(lives_text, (screen_width // 2 - lives_text.get_width() // 2, 20))

    # KI-Lebensanzeige oben rechts anzeigen
    ki_lives_text = font_ki.render(f"KI: {ki_lives}", True, weiss)
    screen.blit(ki_lives_text, (screen_width - ki_lives_text.get_width() - 20, 20))

    # Spiel beenden, wenn keine Leben mehr übrig sind
    if player_lives <= 0 or ki_lives <= 0:
        game_over_text = font.render("GAME OVER", True, weiss)
        screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False

    pygame.display.flip()
    uhr.tick(60)

pygame.quit()