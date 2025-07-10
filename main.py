import asyncio
import pygame
import math

pygame.init()
screen = pygame.display.set_mode((320, 240))
clock = pygame.time.Clock()

async def main():
    ticks = 0
    max_ticks = 30  # 3x the original duration (was 10)
    center = (160, 120)
    length = 50

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0))  # black background

        # Compute angle: full rotation every 10 ticks
        angle = ((ticks % 10) / 10) * 2 * math.pi
        end_x = center[0] + math.cos(angle) * length
        end_y = center[1] + math.sin(angle) * length

        pygame.draw.line(screen, (255, 255, 255), center, (end_x, end_y), 4)

        pygame.display.update()
        await asyncio.sleep(0)
        clock.tick(10)  # still 10 FPS

        ticks += 1
        print("---------- Tick ----------")
        if ticks >= max_ticks:
            pygame.quit()
            return

asyncio.run(main())