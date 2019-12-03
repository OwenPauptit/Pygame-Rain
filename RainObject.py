import pygame, random, time#, winsound

class rain:

    def __init__(self,width,height):
        self.x = random.randint(0,width)
        self.z = random.randint(3,9)
        if self.z%3==0: self.z = 3
        elif self.z%4==0: self.z = 4
        else: self.z = 5
        self.y = 0-(random.randint(self.z*2,height))
        self.Rect = (self.x,self.y,int(self.z/2),self.z*2)
        self.bgColour = colours.greyblue
        self.rainColour = colours.grey
        self.ground = height
        self.width = width
        self.height = height

    def fall(self,speed):
        self.y = self.y + self.z * speed
        if self.y > self.ground:
            self.y = 0 - (random.randint(self.z, self.height/2))
            self.x = random.randint(0, self.width)

    def drawSelf(self,screen):
        self.Rect = (self.x,self.y,int(self.z/2),self.z*2)
        pygame.draw.rect(screen,self.rainColour,self.Rect)

    def purpleRain(self):
        if self.bgColour == colours.greyblue:
            self.bgColour = colours.greypurple
            self.rainColour = colours.purple
            #winsound.PlaySound("purplerain.mp3",winsound.SND_ASYNC)
            return 1
        else:
            self.bgColour = colours.greyblue
            self.rainColour = colours.grey
            return 0

###########################################################################

class colours:
    greypurple = (217, 207, 230)
    greyblue = (83, 92, 145)
    purple = (80, 24, 153)
    grey = (175,177,196)

############################################################################

def calcSpeed(width):
    maxSpeed = 2.25
    minSpeed = 0.25
    x,_ = pygame.mouse.get_pos()
    speed = (x/width)*(maxSpeed-minSpeed)+minSpeed
    return speed

##################################################################################

def main(numDrops=500):
    pygame.mixer.pre_init(44100, 16, 2, 4096)
    pygame.init()                                                       #initialising variables and modules
    screenWidth = 600
    screenHeight = 400
    screen = pygame.display.set_mode((screenWidth,screenHeight))
    pygame.display.set_caption("Rain")
    screen.fill(colours.greyblue)
    rainArr = []
    pygame.mixer.init()
    purpleRainAudio = pygame.mixer.Sound("purplerain.wav")
    rainAudio = pygame.mixer.Sound("rain.wav").play(-1)
    playAudio = 2

    for i in range(0,numDrops):                                         #Creating raindrops
        rainDrop = rain(screenWidth,screenHeight)
        rainArr.append(rainDrop)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == ord("p"):  #Puurrple rain purrrple rain
                    for drop in rainArr:
                        playAudio = drop.purpleRain()
                if event.key == pygame.K_SPACE:
                    if playAudio == 3:
                        playAudio = currentAudio
                    else:
                        if rainArr[0].rainColour == colours.purple:
                            purpleRainAudio.stop()
                            currentAudio = 1
                        else:
                            rainAudio.stop()
                            currentAudio = 0
                        playAudio = 3

        if playAudio == 1:                                              #Checks whether program needs to play or stop music
            pygame.display.set_caption("Purple Rain")
            rainAudio.fadeout(2000)
            purpleRainAudio.play()
            playAudio = 2
        elif playAudio == 0:
            pygame.display.set_caption("Rain")
            purpleRainAudio.fadeout(3000)
            playAudio = 2
            rainAudio = pygame.mixer.Sound("rain.wav").play(-1,fade_ms=3000)

        speed = calcSpeed(screenWidth)

        screen.fill(rainArr[0].bgColour)
        for drop in rainArr:
            drop.drawSelf(screen)
            drop.fall(speed)
        pygame.display.update()
        time.sleep(0.01)

##############################################################################

if __name__ == "__main__":
    main()