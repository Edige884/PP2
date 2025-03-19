import pygame 

pygame.init()
pygame.mixer.init()

songs = ["C:/Users/Edige/Desktop/PP2_git/Labs/Lab_7/Music/New Jeans.mp3", "C:/Users/Edige/Desktop/PP2_git/Labs/Lab_7/Music/KRUSHSEXX.mp3", "C:/Users/Edige/Desktop/PP2_git/Labs/Lab_7/Music/Nukteler.mp3", "C:/Users/Edige/Desktop/PP2_git/Labs/Lab_7/Music/IDEAL.mp3", "C:/Users/Edige/Desktop/PP2_git/Labs/Lab_7/Music/Танцы под луной.mp3"]

i = 0

pygame.mixer.music.load(songs[i])
pygame.mixer.music.play()

SCREEN_WIDTH, SCREEN_HEIGHT = 612, 612
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My music")

fon = pygame.image.load("C:/Users/Edige/Desktop/PP2_git/Labs/Lab_7/Music/fon.png").convert()
fon_x = (SCREEN_WIDTH - fon.get_width()) // 2
fon_y = (SCREEN_HEIGHT - fon.get_height()) // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_UP:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.play()
            elif event.key == pygame.K_DOWN:
                pygame.mixer.music.pause()
    
    screen.fill((255, 255, 255))
    screen.blit(fon, (fon_x, fon_y))

    pygame.display.update()

pygame.quit()
