import pygame

class menu():
    def __init__(self):
            self.x = 1920
            self.y = 1200

            pygame.init()
            self.window = pygame.display.set_mode((self.x, self.y), pygame.FULLSCREEN)
            self.rect = pygame.Rect(*self.window.get_rect().center, 0, 0).inflate(100, 100)

            self.color = (255,255,255)                    
            self.color2 = (255, 255, 255)

            self.window.fill(self.color)

            pygame.display.set_caption('Show Text')
            self.font = pygame.font.Font('freesansbold.ttf', 32)

            self.LOADtext = self.font.render('LOAD', True, (0, 0, 0), (255, 255, 255))
            self.NewGAMEtext = self.font.render('NEW GAME', True, (0, 0, 0), (255, 255, 255))

            self.LOADtextRect = self.LOADtext.get_rect()
            self.NewGAMEtextRect = self.NewGAMEtext.get_rect()

            self.LOADtextRect.center = (self.x // 2.12, self.y // 2)
            self.NewGAMEtextRect = (self.x // 2.2, self.y // 1.797)

            run = True 
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                self.load = pygame.draw.rect(self.window,self.color,(860,575,200,50))

                self.new = pygame.draw.rect(self.window, self.color2,(860,655,200,50))

                self.point = pygame.mouse.get_pos()

                self.collideLOAD = self.load.collidepoint(self.point)
                self.collideNEW = self.new.collidepoint(self.point)

                self.window.blit(self.LOADtext, self.LOADtextRect)
                self.window.blit(self.NewGAMEtext, self.NewGAMEtextRect)

                self.LOADtext = self.font.render('LOAD GAME', True, (0, 0, 0), self.color)
                self.NewGAMEtext = self.font.render('NEW GAME', True, (0, 0, 0), self.color2)

                if self.collideLOAD:
                    self.color = (200, 200, 200)
                    if event.type == pygame.MOUSEBUTTONUP:
                        print("log.1.0")
                        gameChoose()
                else:
                    self.color = (255, 255, 255)

                if self.collideNEW:
                    self.color2 = (200, 200, 200)
                    if event.type == pygame.MOUSEBUTTONUP:
                        print("log.1.1")
                        gameCreate()  

                else:
                    self.color2 = (255, 255, 255)
                
                pygame.display.update() 
                pygame.display.flip()

            pygame.quit()
            exit()

#########################################################################################

class gameCreate():
    def __init__(self):
        import sys
        import os
        from saveTemp import data
        print("YO")
        
        pygame.init()

        self.data = data

        self.x = 1920
        self.y = 1200

        self.window = pygame.display.set_mode((self.x, self.y),pygame.FULLSCREEN)
        self.rect = pygame.Rect(*self.window.get_rect().center, 0, 0).inflate(100, 100)
        
        base_font = pygame.font.Font(None, 32)
        user_text = ''
        
        input_rect = pygame.Rect(200, 200, 140, 32)
        
        color_active = pygame.Color('lightskyblue3')
        
        color_passive = pygame.Color('chartreuse4')
        self.color = (200,200,200)

        self.window.fill((255, 255, 255))

        color = (200,200,200)
        
        active = False

        pygame.display.set_caption('Show Text')
        self.font = pygame.font.Font('freesansbold.ttf', 32)

        self.okTEXT = self.font.render('OK', True, (0, 0, 0), (255, 255, 255))

        self.okTEXTrect = self.okTEXT.get_rect()

        self.okTEXTrect.center = (self.x // 2.12, self.y // 2)

        print("YO2")
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
            
                if event.type == pygame.KEYDOWN:
            
                    if event.key == pygame.K_BACKSPACE:
            
                        user_text = user_text[:-1]
            
                    else:
                        user_text += event.unicode

                self.point = pygame.mouse.get_pos()
            
                self.load = pygame.draw.rect(self.window,self.color,(860,575,200,50))

                self.butt2 = pygame.draw.rect(self.window, color, input_rect)

                self.collideButt = self.load.collidepoint(self.point)
                    
                if active:
                    color = color_active
                else:
                    color = color_passive
                    
                text_surface = base_font.render(user_text, True, (255, 255, 255))

                input_rect.w = max(100, text_surface.get_width()+10)
                
                self.window.blit(text_surface, (input_rect.x+5, input_rect.y+5)) 
                self.window.blit(self.okTEXT, self.okTEXTrect)

                self.okTEXT = self.font.render('OK', True, (0, 0, 0), self.color)

                if self.collideButt:
                    self.color = (150, 150, 150)
                    if event.type == pygame.MOUSEBUTTONUP:
                        print("log.2.3")
                        try:
                            rel_path = str("saves/" + str(user_text))
                            with open(rel_path, 'w') as f:
                                try:
                                    f.write(self.data)
                                except:
                                    self.invalidTEXT = self.font.render('INVALID NAME', True, (0, 0, 0), self.color)
                                    self.invalidTEXTrect = self.invalidTEXT.get_rect()
                                    self.invalidTEXTrect = (self.x // 2.2, self.y // 1.597)
                                    self.invalidTEXT = self.font.render('INVALID NAME', True, (0, 0, 0), self.color)
                                    print("ERROR 101")
                        except:
                            self.invalidTEXT = self.font.render('INVALID NAME', True, (0, 0, 0), self.color)
                            self.invalidTEXTrect = self.invalidTEXT.get_rect()
                            self.invalidTEXTrect = (self.x // 2.2, self.y // 1.597)
                            self.invalidTEXT = self.font.render('INVALID NAME', True, (0, 0, 0), self.color)
                            print("ERROR 102")

                else:
                    self.color = (200, 200, 200)

                pygame.display.update() 
                pygame.display.flip()

#########################################################################################

class gameChoose():
    def __init__(self):
            print("log.3.0")
            import keyboard
            import os
            print("log.3.1")
            print("LOADED PACKAGES END")

            self.x = 1920
            self.y = 1200

            self.z = 0

            minusX = 50
            minusY = 50

            pygame.init()
            self.window = pygame.display.set_mode((self.x, self.y), pygame.FULLSCREEN)
            self.rect = pygame.Rect(*self.window.get_rect().center, 0, 0).inflate(100, 100)

            self.color = (255,255,255)
            self.window.fill(self.color)

            dir_path = 'saves'

            fileNames = []

            for path in os.listdir(dir_path):
                if os.path.isfile(os.path.join(dir_path, path)):
                    self.z += 1
                    fileNames.append(str(path))

            pygame.display.set_caption('Show Text')
            self.font = pygame.font.Font('freesansbold.ttf', 32)

            buttons = {}

            nameNUM = 0

            self.color = (127,127,127)

            endNUM = ""

            for N in range(self.z):
                endNUM = fileNames[nameNUM]
                buttons[endNUM] = pygame.draw.rect(self.window, self.color,(860,655 - minusY,200,50))
                minusY += 100
                nameNUM += 1
            print(buttons)

            text = ""
            textNum = 0

            YposTEXT = 1.905
            
            for XYZ in range(len(fileNames)):
                text = fileNames[textNum]
                textNum += 1

                self.LOADtext = self.font.render(text, True, (0, 0, 0), (127,127,127))

                self.LOADtextRect = self.LOADtext.get_rect()

                self.LOADtextRect.center = (self.x // 2, self.y // YposTEXT)

                YposTEXT += 0.35
                
                self.window.blit(self.LOADtext, self.LOADtextRect)

                colliaders = {}
            print(fileNames)
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False

                    textNum = 0

                    self.point = pygame.mouse.get_pos()

                    for GG in range(len(buttons)):
                        endNUMS = buttons[fileNames[textNum]]
                        colliaders["collide" + str(GG)] = endNUMS.collidepoint(self.point)             
                        textNum += 1  
                    
                    for HITbWOS in range(len(colliaders)):
                        collide = colliaders["collide" + str(HITbWOS)]

                        FILENAME = fileNames[HITbWOS]
                        if collide:
                            self.color = (200,200,200)
                            if event.type == pygame.MOUSEBUTTONUP:
                                from gameSystems import LOAD
                                LOAD(FILENAME)

                    pygame.display.update()
                    pygame.display.flip()

            pygame.quit()
            exit()

#########################################################################################

menu()