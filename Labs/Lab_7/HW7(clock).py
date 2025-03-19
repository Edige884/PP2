import pygame
import datetime

pygame.init()
wind = pygame.display.set_mode((1400,1050))
clock = pygame.time.Clock()

imgMicky = pygame.image.load("C:/Users/Edige/Desktop/PP2_git/Labs/Lab_7/Clock pictures/Micky.png")
imgSec = pygame.image.load("C:/Users/Edige/Desktop/PP2_git/Labs/Lab_7/Clock pictures/secArm.png")
imgMin = pygame.image.load("C:/Users/Edige/Desktop/PP2_git/Labs/Lab_7/Clock pictures/minArm.png")

centerMinArm = (700,525)  
centerSecArm = (700,525) 

def rotate_arm(image,angle,center):
    rotated_image = pygame.transform.rotate(image,-angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image,new_rect.topleft

imgMin,b = rotate_arm(imgMin,50,centerMinArm)
imgSec,c = rotate_arm(imgSec,5,centerSecArm)

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
    now = datetime.datetime.now()
    MIN = now.minute
    SEC = now.second

    sec_angle = 6*SEC 
    min_angle = 6*MIN 

    rotated_Min,posL = rotate_arm(imgMin,sec_angle,centerMinArm)
    rotated_Sec,posR = rotate_arm(imgSec,min_angle,centerSecArm)

    wind.fill((255,255,255))
    wind.blit(imgMicky,(0,0))  
    wind.blit(rotated_Min,posL)  
    wind.blit(rotated_Sec,posR) 

    pygame.display.flip()
    clock.tick(60)  
    
pygame.quit()