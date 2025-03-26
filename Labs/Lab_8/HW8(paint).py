import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    radius = 15
    mode = 'blue'
    tool = 'pencil'
    points = []
    drawing = False
    start_pos = (0, 0)

    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'

                if event.key == pygame.K_p:
                    tool = 'pencil'
                elif event.key == pygame.K_e:
                    tool = 'eraser'
                elif event.key == pygame.K_c:
                    tool = 'circle'
                elif event.key == pygame.K_v:
                    tool = 'rectangle'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if tool in ['circle', 'rectangle']:
                        drawing = True
                        start_pos = event.pos
                    elif tool == 'pencil':
                        radius = min(200, radius + 1)
                elif event.button == 3:
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and tool in ['circle', 'rectangle']:
                    drawing = False
                    end_pos = event.pos
                    if tool == 'rectangle':
                        drawRectangle(screen, start_pos, end_pos, mode)
                    elif tool == 'circle':
                        drawCircle(screen, start_pos, end_pos, mode)

            if event.type == pygame.MOUSEMOTION:
                if tool == 'pencil' and event.buttons[0]:
                    position = event.pos
                    points.append(position)
                    points = points[-256:]
                elif tool == 'eraser' and event.buttons[0]:
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)

        screen.fill((0, 0, 0))

        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

def drawRectangle(screen, start_pos, end_pos, color_mode):
    colors = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}
    color = colors.get(color_mode, (255, 255, 255))
    rect_x = min(start_pos[0], end_pos[0])
    rect_y = min(start_pos[1], end_pos[1])
    rect_width = abs(start_pos[0] - end_pos[0])
    rect_height = abs(start_pos[1] - end_pos[1])
    pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_height), 2)

def drawCircle(screen, start_pos, end_pos, color_mode):
    colors = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}
    color = colors.get(color_mode, (255, 255, 255))
    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
    pygame.draw.circle(screen, color, start_pos, radius, 2)

main()
