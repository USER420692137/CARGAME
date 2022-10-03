def LOAD(NAME):
            import pygame

            x = 1920
            y = 1200

            color = (255,255,255)

            window = pygame.display.set_mode((x, y), pygame.FULLSCREEN)
            rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(100, 100)

            window.fill(color)

            pygame.display.set_caption('Show Text')
            font = pygame.font.Font('freesansbold.ttf', 32)

            LOADtext = font.render("LOADING...", True, (0, 0, 0), (127,127,127))

            LOADtextRect = LOADtext.get_rect()

            LOADtextRect.center = (x // 2, y // 2)

            window.blit(LOADtext, LOADtextRect)
            
            print("========================================")

            motherLOCK = "saves/" + str(NAME)

            f = open(motherLOCK, "r")
            save = f.read().splitlines()

            """
              DANE DO WCZYTANIA GRY
            """

            money = save[0]
            level = save[1]
            stage = save[2]

            """

            KONIEC DANYCH

            """

            startYoMOM(money, level, stage)
                    
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    pygame.display.update()
                    pygame.display.flip()

            pygame.quit()
            exit()

class startYoMOM():
    def __init__(self, money, level,stage):
        if int(stage) == 1:
            print("LOAD")
            from stages.stageone import stage
            stage(money, level)
        if int(stage) == 2:
            print("LOAD")
            from stages.stageone import Mission
            Mission(money, level)