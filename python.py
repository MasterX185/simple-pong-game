import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Mein Pygame Fenster")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0)) 

    # Schläger-Parameter definieren
    schlaeger_breite = 10
    schlaeger_hoehe = 100
    schlaeger_farbe = (255, 255, 255)
    schlaeger_x = 50
    schlaeger_y = (screen_height - schlaeger_hoehe) // 2
    schlaeger = pygame.Rect(schlaeger_x, schlaeger_y, schlaeger_breite, schlaeger_hoehe)

    laufendes_spiel = True
    while laufendes_spiel:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                laufendes_spiel = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    # Bewege den Schläger nach oben
                    schlaeger.y -= 5  # Beispiel: 5 Pixel pro Tastendruck
                if event.key == pygame.K_DOWN:
                    # Bewege den Schläger nach unten
                    schlaeger.y += 5  # Beispiel: 5 Pixel pro Tastendruck

        # Stelle sicher, dass der Schläger nicht aus dem Bildschirmbereich herausragt
        schlaeger.y = max(0, schlaeger.y)
        schlaeger.y = min(screen_height - schlaeger_hoehe, schlaeger.y)

        # Schläger neu zeichnen
        screen.fill((0, 0, 0)) # Bildschirm löschen (schwarz)
        pygame.draw.rect(screen, schlaeger_farbe, schlaeger)

        # ... (weitere Spiel-Logik, z.B. Ballbewegung und Kollisionserkennung) ...

        pygame.display.flip()  # Bildschirm aktualisieren

    pygame.display.flip() 

pygame.quit()