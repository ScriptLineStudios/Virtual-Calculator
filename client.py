import pygame, socket, pickle, math
pygame.init()

screen = pygame.display.set_mode((1200, 700))
display = pygame.Surface((600*2,1000))
clock = pygame.time.Clock()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

special_points = []

calc_str = ""

font = pygame.font.SysFont("Arial", 40)

has_appended = []


while True:
    display.fill((0,0,0))
    special_points = []

    data = client.recv(100000)
    data = pickle.loads(data)
    

    for index, data_point in enumerate(data):
        if index == 0:
            pygame.draw.circle(display, (0,255,0), (data_point[0]+200, data_point[1]), 2)
            special_points.append([[data_point[0], data_point[1]], [data[8][0], data[8][1]]])
        else:
            pygame.draw.circle(display, (0,255,0), (data_point[0]+200, data_point[1]), 2)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    clock.tick(60)
    screen.blit(pygame.transform.flip(display, True, False), (0,0))
    pygame.display.update()