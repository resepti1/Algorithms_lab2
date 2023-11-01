import pygame
import os


x = []
y = []

# отримання директорії скріпта
script_directory = os.path.dirname(os.path.abspath(__file__))

# отримання шляху зберігання результату
output_image_path = os.path.join(script_directory, "output.jpg")

# зчитування координат з файлу
with open('DS7.txt', 'r') as file:
    for line in file:
        coordinates = line.split()
        y.append(int(coordinates[0]))
        x.append(int(coordinates[1]))
    

pygame.init()

width, height = 960, 540
point_color = (0, 0, 0) 

center_x = width // 2
center_y = height // 2

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Lab2")


font = pygame.font.Font(None, 36)

text_X = font.render("X", True, (255,0,0))
text_Y = font.render("Y", True, (255,0,0))

running = True

#цикл вікна
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # очищення екрану
    screen.fill((255, 255, 255))  # Заполнение экрана черным цветом

    # виведення точок
    for i in range(len(x)):
        reflected_y = height - y[i]
        pygame.draw.circle(screen, point_color, (x[i], reflected_y), 1)
    
    # виведення осі Х
    pygame.draw.line(screen, (0, 0, 0), (4, height), (4, 0), 2)

    # виведення осі У
    pygame.draw.line(screen, (0, 0, 0), (4, height - 4), (width, height-4), 2)
    
    # виведення тексту
    screen.blit(text_Y, (10,1))
    screen.blit(text_X, (width - 20, height - 30))

    # Оновелння екрану
    pygame.display.flip()

# збереження результату
pygame.image.save(screen, output_image_path)
# Завершення Pygame
pygame.quit()
