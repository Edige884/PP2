import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Drawing App")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

drawing = False
last_pos = None
current_color = BLACK
brush_size = 5
current_tool = "pen"

drawings = []

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                last_pos = event.pos
                
                if current_tool in ["rectangle", "circle"]:
                    drawings.append({
                        "type": current_tool,
                        "start_pos": event.pos,
                        "end_pos": event.pos,
                        "color": current_color,
                        "size": brush_size
                    })
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False
                last_pos = None
        
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if current_tool == "pen":
                    if last_pos:
                        drawings.append({
                            "type": "line",
                            "start_pos": last_pos,
                            "end_pos": event.pos,
                            "color": current_color,
                            "size": brush_size
                        })
                    last_pos = event.pos
                
                elif current_tool == "eraser":
                    if last_pos:
                        drawings.append({
                            "type": "line",
                            "start_pos": last_pos,
                            "end_pos": event.pos,
                            "color": WHITE,
                            "size": brush_size
                        })
                    last_pos = event.pos
                
                elif current_tool in ["rectangle", "circle"]:
                    if drawings and drawings[-1]["type"] in ["rectangle", "circle"]:
                        drawings[-1]["end_pos"] = event.pos
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                current_tool = "pen"
            elif event.key == pygame.K_r:
                current_tool = "rectangle"
            elif event.key == pygame.K_c:
                current_tool = "circle"
            elif event.key == pygame.K_e:
                current_tool = "eraser"
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
            elif event.key == pygame.K_5:
                current_color = YELLOW
            elif event.key == pygame.K_6:
                current_color = PURPLE
            elif event.key == pygame.K_7:
                current_color = CYAN
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                brush_size = min(50, brush_size + 1)
            elif event.key == pygame.K_MINUS:
                brush_size = max(1, brush_size - 1)
    
    screen.fill(WHITE)
    
    for element in drawings:
        if element["type"] == "line":
            pygame.draw.line(screen, element["color"], element["start_pos"], element["end_pos"], element["size"])
        elif element["type"] == "rectangle":
            start_x = min(element["start_pos"][0], element["end_pos"][0])
            start_y = min(element["start_pos"][1], element["end_pos"][1])
            width = abs(element["end_pos"][0] - element["start_pos"][0])
            height = abs(element["end_pos"][1] - element["start_pos"][1])
            pygame.draw.rect(screen, element["color"], (start_x, start_y, width, height), element["size"])
        elif element["type"] == "circle":
            center_x = (element["start_pos"][0] + element["end_pos"][0]) // 2
            center_y = (element["start_pos"][1] + element["end_pos"][1]) // 2
            radius = int(math.sqrt((element["end_pos"][0] - element["start_pos"][0])**2 + 
                               (element["end_pos"][1] - element["start_pos"][1])**2) // 2)
            pygame.draw.circle(screen, element["color"], (center_x, center_y), radius, element["size"])
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()