import pygame
import random
pygame.init()

#Code for bubble sort

maxElements = 200 #tylko to trzeba zmieniac

numberOfElements = 50
multiplier = 4

SCREEN_WIDTH = maxElements * multiplier
SCREEN_HEIGHT = 700


screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT+30])
pygame.display.set_caption("Bubble sort")


elements = []
for i in range(1, numberOfElements+1):
    elements.append(i)
random.shuffle(elements)


results = []
steps = 0
running = True
while running:
    
    
    
    pygame.time.Clock().tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
                  
    
    screen.fill((0, 0, 0))
    
    changed = False
    for i in range(0, numberOfElements-1):
        if(elements[i] > elements[i+1]):
            changed = True
            elements[i], elements[i+1] = elements[i+1], elements[i]
            screen.fill((0, 0, 0))
            for j in range(0, numberOfElements):
                pygame.draw.rect(screen, (255,255,255), pygame.Rect(j*multiplier, SCREEN_HEIGHT-elements[j]*multiplier/2, multiplier, elements[j]*multiplier/2))
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(i*multiplier, SCREEN_HEIGHT-elements[i]*multiplier/2, multiplier, elements[i]*multiplier/2))
            pygame.draw.rect(screen, (255,0,0), pygame.Rect((i+1)*multiplier, SCREEN_HEIGHT-elements[i+1]*multiplier/2, multiplier, elements[i+1]*multiplier/2))
            steps += 1
            font = pygame.font.SysFont('calibri', 30)
            img = font.render("elements: " + str(numberOfElements) + "  steps: " + str(steps), True, (255, 255, 255))
            screen.blit(img, (0, SCREEN_HEIGHT))
            pygame.display.update()
            pygame.time.delay(1) #o tu trzeba na wiecej zmienic zeby wolniej sie robilo
                
                
    if(changed == False):
        numberOfElements += 50
        results.append(steps)
        pygame.time.delay(500)
        steps = 0
        elements = []
        if(maxElements < numberOfElements):
            running = False
            font = pygame.font.SysFont('calibri', 24)
            screen.fill((0, 0, 0))
            for x in range(0, len(results)):
                img = font.render(str(results[x]), True, (255, 255, 255))
                screen.blit(img, (10, x*30+10))
            pygame.display.update()
            pygame.time.delay(3000)
            break
        for i in range(1, numberOfElements+1):
            elements.append(i)
        random.shuffle(elements)
    

pygame.quit()
print(results)
f = open("wyniki.txt", "w+")
for result in results:
    f.write(str(result) + "\n")
f.close()


