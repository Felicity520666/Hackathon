##IMPORTS##
import pygame
import random
import math
import asyncio


async def main():        
    clock = pygame.time.Clock()
    ##INIT#
    pygame.font.init()
    pygame.mixer.init()
    sound_effect = pygame.mixer.Sound("Hit.mp3")
    sound_effect.set_volume(0.5)
    Next_Level = pygame.mixer.Sound("Harder.mp3")
    BGM = pygame.mixer.Sound("Overture.mp3")
    Heal = pygame.mixer.Sound("Heal.mp3")
    Heal.set_volume(0.5)
    pygame.init()

    BGM.play(-1)
    ##SCREEN SETUP##
    Width = 800
    Height = 800
    Pause = 0

    ##PLAYER##
    PlayerPos = 350
    backcolor = 100
    Score = 0
    Health = 3
    Immune = False
    ImmunePause = 0
    PlayerImage = 0
    MoveSpeed = 2

    ##Lift and PlayerY Sine movement##
    amplitude = 25
    angle = 0
    ##X axis
    amplitude = 20
    angley = 0

    ##spike falling
    amplitude2 = 50
    angle2 = 0

    ##BACKGROUND##
    Fallstage = 0
    Fallstage2 = -800

    ##EVIL STUFF##
    Generated = False
    EvilPosY = 0
    EvilPosX = 0
    EvilSize = 0

    ##EVIL STUFF2##
    AnotherVariable = True
    Generated2 = True
    Evil2PosY = 0
    Evil2PosX = 0
    Evil2Size = 0

    ##EVIL STUFF3##
    AnotherVariable2 = True
    Generated3 = True
    Evil3PosY = 0
    Evil3PosX = 0

    screen = pygame.display.set_mode((Width, Height))

    ##IMAGES##
    LiftImage = pygame.image.load("Lift.png").convert_alpha()
    PlayerHurt = pygame.image.load("Injured.png").convert_alpha()
    PlayerOK = pygame.image.load("Bunny.png").convert_alpha()
    SpikeImage = pygame.image.load("Spike1.png").convert_alpha()
    BG1 = pygame.image.load("Background1.png").convert_alpha()
    BG2 = pygame.image.load("Background2.png").convert_alpha()

    PlayerImage = PlayerOK
    ##CHANGE SCREENCOLOR##
    running = True
    while running:
        Pause += 1
        
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if Health == 0:
            print("Game Over")
            screen.fill((0, 0, 0))
            # Display Score
            font = pygame.font.SysFont("New Times Roman", 50)

            score_text = f"Score: {Score}"  
            text_surface = font.render(score_text, True, (0, 0, 0))

            screen.blit(text_surface, (640, 15))
            break
        else:
            # Move OUTSIDE event loop
            if keys[pygame.K_LEFT]:
                if PlayerPos > 50:
                    PlayerPos -= 6
            elif keys[pygame.K_RIGHT]:
                if PlayerPos < 625:
                    PlayerPos += 6
            elif keys[pygame.K_a]:
                if PlayerPos > 50:
                    PlayerPos -= 6
            elif keys[pygame.K_d]:
                if PlayerPos < 625:
                    PlayerPos += 6
            if backcolor < 0:
                backcolor = 0
            screen.fill((backcolor, backcolor, backcolor))

                  ##BACKGROUND2##
            image = pygame.transform.flip(BG2, True, False)

            rect = pygame.Rect(50, Fallstage2, 680, 1600)
            scaled_image = pygame.transform.scale(image, rect.size)
            scaled_image.set_alpha(100)

            screen.blit(scaled_image, rect)
            
            rect = pygame.Rect(50, Fallstage2+1600, 680, 1600)
            scaled_image = pygame.transform.scale(image, rect.size)
            scaled_image.set_alpha(100)

            screen.blit(scaled_image, rect)
            
            Fallstage2 -= MoveSpeed/3
            
            if Fallstage2 < -1600:
                Fallstage2 = 0
                
            ##BACKGROUND##

            rect = pygame.Rect(0, Fallstage, 800, 1600)
            scaled_image = pygame.transform.scale(BG1, rect.size)

            screen.blit(scaled_image, rect)
            
            rect = pygame.Rect(0, Fallstage+1600, 800, 1600)
            scaled_image = pygame.transform.scale(BG1, rect.size)

            screen.blit(scaled_image, rect)
            
            Fallstage -= MoveSpeed
            
            if Fallstage < -1600:
                Fallstage = 0
                

                
            ##PLAYER
            image = PlayerImage
            
            ##SINE MOVEMENT
            angle += MoveSpeed
            angley += MoveSpeed/2
            
            obj_y = 150 + (math.sin(angle*0.01) * amplitude)
            obj_x = PlayerPos + (math.sin(angley*0.01) * amplitude)

            rect = pygame.Rect(int(obj_x), (int(obj_y)), 50, 50)
            scaled_image = pygame.transform.scale(image, rect.size)

            screen.blit(scaled_image, rect)
        
            ##DRAW EVIL STUFF
            if Generated == False:
                Generated = True
                
                EvilPosY = 800
                EvilPosX = random.randint(85,575)
                EvilSize = random.randint(1,10) * 50
                
            evil1 = pygame.Rect(EvilPosX, EvilPosY, EvilSize, 50)
            pygame.draw.rect(screen, (150, 75, 0), evil1)
            
            ##DRAW EVIL STUFF2
            if Generated2 == False:
                Generated2 = True
                
                Evil2PosY = 800
                Evil2PosX = random.randint(50,625)
                Evil2Size = random.randint(1,10) * 50
                
            evil2 = pygame.Rect(Evil2PosX, Evil2PosY, Evil2Size, 50)
            pygame.draw.rect(screen, (150, 75, 0), evil2)
            
             ##DRAW EVIL STUFF3
            if Generated3 == False:
                Generated3 = True
                
                Evil3PosY = -150
                Evil3PosX = random.randint(50,625)
                
            obj_x = Evil3PosX + (math.sin(angle2*0.01) * amplitude2)
            angle2 += MoveSpeed
                    
            evilfake = pygame.Rect(int(obj_x), Evil3PosY, 150, 150)
            evil3 = pygame.Rect(int(obj_x)+75, Evil3PosY+50, 75, 100)

            if AnotherVariable2 == False:

                scaled_image = pygame.transform.scale(SpikeImage, evil3.size)

                screen.blit(scaled_image, evil3)
            
            ##COLLISIONS##
            if rect.colliderect(evil1) and Immune == False:
                Health -= 1
                Immune = True
                ImmunePause = Pause+100
                PlayerImage = PlayerHurt
                sound_effect.play()
                
            if Immune == True and ImmunePause == Pause:
                Immune = False
                PlayerImage = PlayerOK
                Heal.play()
                
             ##COLLISIONS##
            if rect.colliderect(evil2) and Immune == False:
                Health -= 1
                Immune = True
                ImmunePause = Pause+100
                PlayerImage = PlayerHurt
                sound_effect.play()
                
            if Immune == True and ImmunePause == Pause:
                Immune = False
                PlayerImage = PlayerOK
                Heal.play()
                
              ##COLLISIONS##
            if rect.colliderect(evil3) and Immune == False and AnotherVariable2 == False:
                Health -= 1
                Immune = True
                ImmunePause = Pause+100
                PlayerImage = PlayerHurt
                sound_effect.play()
                
            if Immune == True and ImmunePause == Pause:
                Immune = False
                PlayerImage = PlayerOK
                Heal.play()
            
             # Display Score
            font = pygame.font.SysFont("New Times Roman", 50)

            score_text = f"Score: {Score}"  
            text_surface = font.render(score_text, True, (0, 0, 0))

            screen.blit(text_surface, (640, 15))
            
             # Display Health
            font = pygame.font.SysFont("New Times Roman", 50)

            score_text = f"Health: {Health}" 
            text_surface = font.render(score_text, True, (0, 0, 0))

            screen.blit(text_surface, (640, 50))
            
             ##LIFT
            obj_y = -125 + (math.sin(angle*0.01) * amplitude)
            obj_x = -100 + (math.sin(angley*0.01) * amplitude)

            lift = pygame.Rect(int(obj_x), (int(obj_y)), 1000, 600)        

            scaled_image = pygame.transform.scale(LiftImage, lift.size)
            screen.blit(scaled_image, lift)
            
            ##DISPLAY##
            pygame.display.update()
            EvilPosY = EvilPosY - MoveSpeed
            if AnotherVariable == False:
                Evil2PosY = Evil2PosY - MoveSpeed
            if AnotherVariable2 == False:
                Evil3PosY = Evil3PosY + MoveSpeed/2

            ##RESET IF THE EVIL THING IS OFF SCREEN##
            if EvilPosY < -50:
                Generated = False
                Score += 1
                backcolor -= 1
                EvilPosY = 10000
            if EvilPosY < 400 and AnotherVariable == True:
                AnotherVariable = False
                Generated2 = False
                backcolor -= 1
            if Evil2PosY < -50:
                AnotherVariable = True
                Score += 1
                backcolor -= 1
                Evil2PosY = 10000
            if Evil3PosY > 850:
                AnotherVariable2 = False
                Generated3 = False
                Score += 1
                backcolor -= 1
                EvilPos3Y = 0
                
            if Score == 5:
                if MoveSpeed == 2:
                    MoveSpeed += 1
                    Next_Level.play()
            elif Score == 10:
                if MoveSpeed == 3:
                    MoveSpeed += 1
                    Next_Level.play()
            elif Score == 15:
                if MoveSpeed == 4:
                    MoveSpeed += 1
                    Next_Level.play()
            elif Score == 20:
                if AnotherVariable2 == True:
                     AnotherVariable2 = False
                     Generated3 = False
                     Next_Level.play()
            elif Score == 30:
                if MoveSpeed == 5:
                    MoveSpeed += 1
                    Next_Level.play()
            elif Score == 50:
                if MoveSpeed == 6:
                    MoveSpeed += 1
                    Next_Level.play()
                
        delta_time_ms = clock.tick(60) # Limits loop to 60 FPS

            
    pygame.quit()

    ##CREATE THE PLAYER (REACTANGLE)##
    
if __name__ == "__main__":
    asyncio.run(main())

