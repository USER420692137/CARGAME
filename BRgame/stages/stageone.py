import pygame
import math

x = 1920
y = 1200

WINDOW_WIDTH    = 600
WINDOW_HEIGHT   = 600
WINDOW_SURFACE  = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE

class stage():
    def __init__(self, money, level):
        import pygame

        print("DEBUG START STAGE 1")

        x = 1920
        y = 1200

        color = (255,255,255)

        self.window = pygame.display.set_mode((x, y), pygame.FULLSCREEN)
        rect = pygame.Rect(*self.window.get_rect().center, 0, 0).inflate(100, 100)

        pygame.display.set_caption('Show Text')
        font = pygame.font.Font('freesansbold.ttf', 32)

        X = x

        Y = 575

        nextSceneCOUNT = -505

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.window.fill(color)
                    
            SCHOOLbus = pygame.draw.rect(self.window,(102,205,170),(X,Y,500,200))

            X = X - 1  

            if X == nextSceneCOUNT:
                print("NEXT SCENE TYPED")
                stage.nextScene(money, level)

            pygame.display.flip()

        pygame.quit()

    def nextScene(money, level):
        import pygame

        x = 1920
        y = 1200

        c = 0

        window = pygame.display.set_mode((x, y), pygame.FULLSCREEN)
        rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(100, 100)

        pygame.display.set_caption('Show Text')
        font = pygame.font.Font('freesansbold.ttf', 32)

        color = (255,255,255)

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            window.fill(color)

            HANK = pygame.draw.rect(window,(205,183,158),(750,400,400,400))
            HANKcoat = pygame.draw.rect(window,(0,0,0),(700,800,500,400))

            HANKtalk = font.render("BUS GONE, LETS START", True, (0, 0, 0), (127,127,127))

            HANKtalkRect = HANKtalk.get_rect()

            HANKtalkRect.center = (x // 1.3, y // 1.5)

            window.blit(HANKtalk, HANKtalkRect)

            c += 1

            if c == 1000:
                print("MISSION START")

                Mission(money, level)

            pygame.display.update()
            pygame.display.flip()

        pygame.quit()

class CarSprite( pygame.sprite.Sprite ):
    """ Car Sprite with basic acceleration, turning, braking and reverse """

    def __init__( self, car_image, x, y, rotations=360 ):
        """ A car Sprite which pre-rotates up to <rotations> lots of
            angled versions of the image.  Depending on the sprite's
            heading-direction, the correctly angled image is chosen.
            The base car-image should be pointing North/Up.          """
        pygame.sprite.Sprite.__init__(self)
        # Pre-make all the rotated versions
        # This assumes the start-image is pointing up-screen
        # Operation must be done in degrees (not radians)
        self.rot_img   = []
        self.min_angle = ( 360 / rotations ) 
        for i in range( rotations ):
            # This rotation has to match the angle in radians later
            # So offet the angle (0 degrees = "north") by 90° to be angled 0-radians (so 0 rad is "east")
            rotated_image = pygame.transform.rotozoom( car_image, 360-90-( i*self.min_angle ), 1 )
            self.rot_img.append( rotated_image )
        self.min_angle = math.radians( self.min_angle )   # don't need degrees anymore
        # define the image used
        self.image       = self.rot_img[0]
        self.rect        = self.image.get_rect()
        self.rect.center = ( x, y )
        # movement
        self.reversing = False
        self.heading   = 0                           # pointing right (in radians)
        self.speed     = 0    
        self.velocity  = pygame.math.Vector2( 0, 0 )
        self.position  = pygame.math.Vector2( x, y )

    def turn( self, angle_degrees ):
        """ Adjust the angle the car is heading, if this means using a 
            different car-image, select that here too """
        ### TODO: car shouldn't be able to turn while not moving
        self.heading += math.radians( angle_degrees ) 
        # Decide which is the correct image to display
        image_index = int( self.heading / self.min_angle ) % len( self.rot_img )
        # Only update the image if it's changed
        if ( self.image != self.rot_img[ image_index ] ):
            x,y = self.rect.center
            self.image = self.rot_img[ image_index ]
            self.rect  = self.image.get_rect()
            self.rect.center = (x,y)

    def accelerate( self, amount ):
        """ Increase the speed either forward or reverse """
        if ( not self.reversing ):
            self.speed += amount
        else: 
            self.speed -= amount

    def brake( self ):
        """ Slow the car by half """
        self.speed /= 2
        if ( abs( self.speed ) < 0.1 ):
            self.speed = 0

    def reverse( self ):
        """ Change forward/reverse, reset any speed to 0 """
        self.speed     = 0
        self.reversing = not self.reversing

    def update( self ):
        """ Sprite update function, calcualtes any new position """
        self.velocity.from_polar( ( self.speed, math.degrees( self.heading ) ) )
        self.position += self.velocity
        self.rect.center = ( round(self.position[0]), round(self.position[1] ) )

class Mission():
    def __init__(self, money,level):
        import keyboard
        import pygame

        pygame.mixer.init()

        x = 1920
        y = 1200

        WINDOW_WIDTH    = x
        WINDOW_HEIGHT   = y
        WINDOW_SURFACE  = pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE

        window = pygame.display.set_mode((x, y), pygame.FULLSCREEN)
        rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(100, 100)

        pygame.display.set_caption('Show Text')
        font = pygame.font.Font('freesansbold.ttf', 32)

        color = (255,255,255)

        CarPoseX = 1500
        CarPoseY = 1000

        CarSizeA = 100
        CarSizeB = 400

        AngleOfCAR = 0

        V = 1
        V1 = 1

        # mapka

        background = window

        car_image  = pygame.image.load( 'pixilart-drawing_1.png' ).convert_alpha()

        black_car = CarSprite( car_image, WINDOW_WIDTH//2, WINDOW_HEIGHT//2 )
        car_sprites = pygame.sprite.Group() #Single()
        car_sprites.add( black_car )

        clock = pygame.time.Clock()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif ( event.type == pygame.VIDEORESIZE ):
                    WINDOW_WIDTH  = event.w
                    WINDOW_HEIGHT = event.h
                    window = pygame.display.set_mode( ( WINDOW_WIDTH, WINDOW_HEIGHT ), WINDOW_SURFACE )
                    background = pygame.transform.smoothscale( road_image, ( WINDOW_WIDTH, WINDOW_HEIGHT ) )
                elif ( event.type == pygame.MOUSEBUTTONUP ):
                    # On mouse-click
                    pass
                elif ( event.type == pygame.KEYUP ):
                    if ( event.key == pygame.K_h ):  
                        print( 'meep-meep' )
                    elif ( event.key == pygame.K_r ):  
                        print( 'resersing' )
                        black_car.reverse()
                    elif ( event.key == pygame.K_UP ):  
                        print( 'accelerate' )
                        black_car.accelerate( 0.5 )
                    elif ( event.key == pygame.K_DOWN ):  
                        print( 'brake' )
                        black_car.brake( )

            keys = pygame.key.get_pressed()
            if ( keys[pygame.K_LEFT] ):
                black_car.turn( -1.8 )  # degrees
            if ( keys[pygame.K_RIGHT] ):
                black_car.turn( 1.8 )

            window.fill(color)
            
            car_sprites.update()

            window.blit( background, ( 0, 0 ) ) # backgorund
            car_sprites.draw( window )

            LEVEL = level

            LEVELtext = font.render("LEVEL " + str(LEVEL), True, (0, 0, 0), (127,127,127))

            LEVELtextRECT = LEVELtext.get_rect()

            LEVELtextRECT = (x // 2, y // 1.1)

            window.blit(LEVELtext, LEVELtextRECT)
            
            clock.tick_busy_loop(60)

            pygame.display.flip()

        pygame.quit()
