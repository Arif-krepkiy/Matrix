import pygame as pg
import random

class MatrixLetters:
    def __init__(self, app):
        self.app = app
        #self.letters = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛ ДЖЯЧСМИТЬБЮ123456789"
        self.letters = "イカガサザタダナハバパマヤラワウキギシジチヂニヒビピミリヰエクグスズツヅヌフブプム" \
                       "ユルオケゲゼテデネヘベペメコゴソゾトドノホボポモヨロヲ0123456789象形文字指事会意形声転注仮借元基本下素峠榊畑働"
        self.font_size = 15
        self.font = pg.font.Font('MS Mincho.ttf', self.font_size, bold=True)
        self.columns = app.WIDTH // self.font_size
        self.drops = [1 for i in range(0, self.columns)]

    def draw(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (0,255,0))
            pos = i * self.font_size, (self.drops[i]- 1) * self.font_size
            self.app.surface.blit(char_render,pos)
            if self.drops[i] * self.font_size > app.HEIGHT and random.uniform(0,1) > 0.975:
                self.drops[i] = 0
            else :
                self.drops[i] = self.drops[i] + 1


    def run(self):
        self.draw()




class MatrixApp:
    def __init__(self): # инициализация приложения
        self.RES = self.WIDTH, self.HEIGHT = 1920, 1280
        pg.init()
        self.screen = pg.display.set_mode(self.RES)
        self.surface = pg.Surface(self.RES,pg.SRCALPHA) # поверхность отрисовки
        self.clock = pg.time.Clock() #для отслеживания времени
        self.matrixletters = MatrixLetters(self)

    def draw(self):
        self.surface.fill((0,0,0,10)) #закраска раб.поверхности
        self.matrixletters.run()
        self.screen.blit(self.surface, (0,0))

    def run(self):
        while True:  #главный цикл программы
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.flip()
            self.clock.tick(30)


if __name__ == '__main__':
    app = MatrixApp()
    app.run()


lette = "イカガサザタダナハバパマヤラワウキギシジチヂニヒビピミリヰエクグスズツヅヌフブプムユルオケゲゼテデネヘベペメコゴソゾトドノホボポモヨロヲ0123456789"


