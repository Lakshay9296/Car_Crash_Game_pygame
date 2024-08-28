import pygame
import random

def main():
    pygame.init()

    pygame.display.set_caption("Ultimate Road Rage")

    width = 500
    height = 800

    sc = pygame.display.set_mode((width, height))

    font=pygame.font.SysFont("Times New Roman",24)

    car = pygame.image.load('car.png')
    car_width, car_height = car.get_size()
    car = pygame.transform.smoothscale(car, (70, int(car_height * (70 / car_width))))
    x = (width * 0.43)
    y = (height * 0.8)

    bg = pygame.image.load('road.png')
    bg = pygame.transform.scale(bg, (width, height))
    bg_y=0

    bar = pygame.image.load('barrigade.png')
    bar_width,bar_height = bar.get_size()
    bar = pygame.transform.smoothscale(bar, (100, int(bar_height*(100/bar_width))))

    bars = {"x": 50, "y": -bar_height}

    go = pygame.image.load('GameOver.png')
    go = pygame.transform.scale(go,(width,go.get_height()))

    play= pygame.image.load('play.png')
    play = pygame.transform.scale(play,(150,150))

    name= pygame.image.load('name.png')
    name_width,name_height = name.get_size()
    name= pygame.transform.smoothscale(name, (400, int(name_height*(400/name_width))))

    exit= pygame.image.load('exit.png')
    exit_width,exit_height = exit.get_size()
    exit = pygame.transform.smoothscale(exit, (200, int(exit_height*(200/exit_width))))


    run = True
    gameOver=False
    score=0
    last_score=0
    best_score=0
    level=1
    levels = {10: 2, 20: 3, 30: 4, 40: 5, 50: "God Mode"}
    game_started=False

    while run:
        if (game_started):
            bg_y+=0.2
            sc.blit(bg, (0, bg_y))
            sc.blit(bg,(0,bg_y - height))
            if bg_y>height:
                bg_y=0
            sc.blit(car, (x, y))
            sc.blit(bar, (bars["x"], bars["y"]))
            
            score_rect=pygame.Rect(0,0,500,30)
            pygame.draw.rect(sc,(255,255,255),score_rect)
            
            score_text=font.render(f' SCORE: {score}',True,(0,0,0))
            sc.blit(score_text,(30,0))
            
            level_text=font.render(f'LEVEL: {level}',True,(0,0,0))
            sc.blit(level_text,(270,0))
            
            pygame.display.update()
            
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                x -= 0.4
                if x < 0:
                    x = 0
            elif key[pygame.K_d]:
                x += 0.4
                if x > width - car.get_width():
                    x = width - car.get_width()
            
            for _ in bars:
                if score<=10:
                    bars["y"] += 0.15
                elif score>10 and score<=20:
                    bars["y"] += 0.2
                elif score>20 and score<=30:
                    bars["y"] += 0.3
                elif score>30 and score<=40:
                    bars["y"] += 0.4
                elif score>40:
                    bars["y"] += 0.5
                    
                if bars["y"] > height:
                    bars["y"] = -bar_height
                    bars["x"] = random.choice([i for i in range(30,390,30)])
                    score+=1
                    if score in levels:
                        level = levels[score]
                            
            car_rect=car.get_rect(topleft=(x,y))
            bar_rect=bar.get_rect(topleft=(bars['x'],bars['y']))
            if car_rect.colliderect(bar_rect):
                gameOver=True
            
        else:
            sc.blit(bg, (0, 0))
            sc.blit(name,(47,50))
            sc.blit(play, (175, 350))
            play_rect = play.get_rect(topleft=(175, 350))
            
            sc.blit(exit,(150,535))
            exit_rect = exit.get_rect(topleft=(150, 535))
            
            last_score_rect=pygame.Rect(150,650,200,70)
            pygame.draw.rect(sc,(255,255,255),last_score_rect)
            
            last_score_text=font.render(f'LAST SCORE: {last_score}',True,(0,0,0))
            sc.blit(last_score_text,(160,655))
            
            best_score_text=font.render(f'BEST SCORE: {best_score}',True,(0,0,0))
            sc.blit(best_score_text,(160,685))
            
            pygame.display.update()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_started:
                mouse_x,mouse_y=pygame.mouse.get_pos()
                if play_rect.collidepoint(mouse_x,mouse_y):
                    game_started=True
                elif exit_rect.collidepoint(mouse_x,mouse_y):
                    run = False
        
        if gameOver:
            sc.blit(go, (0, 200))
            pygame.display.update()
            pygame.time.wait(2000)
            if score>last_score:
                best_score=score
            last_score = score
            score = 0
            level = 1
            bars = {"x": 50, "y": -bar_height}
            x = (width * 0.43)
            game_started = False
            gameOver = False


    pygame.quit()
    
    
if __name__=='__main__':
    main()