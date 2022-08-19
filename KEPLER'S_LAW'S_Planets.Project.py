#Nome do autor: Matheus Daniel Koren
#Matrícula Universidade Federal do Rio Grande (FURG): 135435
#Nome do projeto: KEPLER'S LAW'S PROJECT
#Data Início: 08/07/22
#Data Término: em desenvolvimento

#INSPIRED BY https://www.youtube.com/watch?v=WTLPmUHTPqo
#ASTRONOMICAL INFOS OF http://www.astronoo.com/pt/artigos/caracteristicas-dos-planetas.html

import itertools
import pygame
import sys
import math
from matplotlib import pyplot as plt
from math import*
import time
import numpy as np
from threading import Timer
from pygame import mixer
from itertools import product
from operator import mod
import sympy as sym

#CONSIDERAÇÕES IMPORTANTE:
#1 [AU] = 1.496e+8 [Km]
#1 DIA = 86400 segundos
#Condição inicial Sol (0,0)

#VELOCIDADES ORBITAIS MÉDIAS
#VENUS = 35.02 #[km/s]
#TERRA = 29.78 #[km/s] =  # (29.78 [km/s] * 1000[m]) = 29780 [m/s] = 29780 m/s * (1 AU/1.496e+11 m) = 1.99064e-7 [AU / s] = 1.99064e-7[AU / s] * ( 86400 segundos / 1 dia) =  0.0171991296 [AU/dia]
#MERCURY = 48.92
#MARS = 24.07
#JUPITER = 13.05
#URANUS = 6.81
#NEPTUNE = 5.43
#PLUTO = 4.72

#CONSTANTE GRAVITACIONAL
#G=(6.67e-11) #NOTAÇÃO [N*m^2 / kg^2] ou [m^3/kg*s^2

#MASSAS DE CADA PLANETA ou ESTRELA
#SOL=1.989e30 #NOTAÇÃO  #[Kg]
#TERRA=5.97e24 #NOTAÇÃO  #[Kg]
#VENUS=4.86e24  #NOTAÇÃO #[Kg]
#MARTE= 0.6418e24  #NOTAÇÃO #[kg]
#JUPITER= 1898.6e24  #NOTAÇÃO #[kg]
#URANUS= 86.810e24  #NOTAÇÃO #[kg]
#MERCURY= 0.3302e24  #NOTAÇÃO #[kg]
#SATURN= 568.46e24  #NOTAÇÃO #[kg]
#NEPTUNE= 102.43e24	 #NOTAÇÃO #[kg]
#PLUTO= ?

#AFÉLIO / PERIÉLIO  [milhão km 10e6]
#Mercúrio 69.817445 / 46.001009
#Vênus 108.942780 / 107.476170
#Terra 152.098233*106/ 47.098291
#Marte 249.232432/ 206.645215
#Júpiter 816.001807/740.679835
#Saturno 1503.509229/1349.823615
#Urano 3006.318143/2734.998229
#Netuno 4537.039826/4459.753056
#Plutão 7376.124302/4436.756954


#ANGULOS DE INCLINAÇÃO GRAUS
#EARTH = 0
#MERCURY = 7.004870
#VENUS = 3.390000
#MARS = 1.850610
#JUPITER = 1.305300
#URANUS = 0.772556
#NETUNO = 1.769170
#PLUTO = 17.141750
#SATURN = 2.484460

#DISTANCIAS MÉDIAS
#SOL= 0  [AU]
#TERRA_SOL= 1 [AU] = 149.600.000 [km] ou 1[AU] = 1.496e+8 [km]
#VENUS_SOL= 0.72333 [AU] = 108208627.8 [km]
#MARTE_SOL= 1.52366 [AU] = 227936291.7 [km]
#JUPITER_SOL = 5.2 [AU]
#SATURN_SOL = 9.6 [AU]
#URANUS_SOL = 19.2 [AU]
#NEPTUNE_SOL = 30 [AU]
#MERCURY_SOL = 0.4 [AU]
#PLUTO_SOL = 33.56 [AU]


#SEMIEIXOMAIOR e periodo
#LUA DE MARTE
#Deimos =  23463.2 km = 0.0001568418046 AU
#Phobos = 9376 km = 6.267469e-5 AU

#LUA DE JUPITER
#MÉTIS OU JUPITER XVI 128 000 km = 0.000855627152 AU, periodo 0,295dias
#ANDRASTEIA OU JUPITER XV 129,000 km = 0.000862311739 AU, periodo 0,298 dias
#AMALTEIA 181 400 km = 0.0012125841 AU, periodo 0,498 dias
#TEBE QUARTO SATELITE NATURAL 221.900 km = 0.00148330988 AU , periodo 0,675dias
#io 421700.00000005931361 KM =0.002818890389461 AU , periodo 	1,769dias
#EUROPA 670900 km = 0.0044846895 AU ,    PERIODO 3.551181 dias
#	Ganímedes 	1 070 400km = 0.007155182056 AU periodo 	7,155dias
#callisto 1 882 700	km = 0.01258507218 AU, periodo 16,690	 dias

#LUA DE SATURNO
#Mimas 185 520KM = 0.0012401246 au +0,9424218	d
#Encélado 	238 020km = 0.00159106543 au 1,370218d
#Tétis 294 660km = 0.00196968044 au 	+1,887802d
#Dione 377 400 = 0.00252276318 au	+2,736915d
#Titã 1 221 830 = 0.0081674290836 au	+15,945421d
#Jápeto 3 561 300 = 0.02380582012 au	+79,330183d
#Hipérion 1 481 100 = 0.009900541987 au	+21,276609d

#INICIANDO PYGAMES
pygame.init()
WIDTH, HEIGHT = [1200,1200]
DISPLAY= pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("MECÂNICA CELESTE")
mixer.music.load("assets/sound/bg.wav")
mixer.music.play(-1)
bg = pygame.image.load("assets/images/bg.gif").convert_alpha()
bg = pygame.transform.scale(bg,(2000,2000))
#COLORS
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
VENUSCOLOR = (255,198,73)
SATURNCOLOR = (204, 153, 102)
MERCURYCOLOR = (116, 123, 129)
MARSCOLOR = (156,46, 53)
NEPTUNECOLOR = (72, 112, 221)
URANUSCOLOR = (79, 208, 231)
JUPITERCOLOR = (188, 175, 178)
PLUTOCOLOR = (150, 133, 112)
FONT = pygame.font.SysFont("comicsans", 16)


class Planet:
    AU =149600000000 #149.6e6*1000 #1.496e+8
    G = 6.67428e-11
    SCALE = 250/AU # 1AU = 100 pixels     ALGUNS KM PER SECOND
    TIMESTEP =3600*24 # (3600*24) # 1 day=3600*24 [s] , 1 ano=3.156e+7[s]

    def __init__(self, x, y, z, radius, color, mass, angle, afelio, perielio, periodoorbital, raiomediodoplaneta):
        self.x = x
        self.y = y
        self.z = z
        self.force = 0
        self.xyzmodulo = 0
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.orbitpares = []
        self.sun = False
        self.distance_to_sun = 0
        self.distance_x = 0
        self.distance_y = 0
        self.distance_z = 0
        self.distance_xyz_lista = []
        self.distance_modulo = 0
        self.position_x = 0
        self.position_y = 0
        self.position_z = 0
        self.position_x_lista = []
        self.position_y_lista = []
        self.position_xy_lista = []
        self.position_xyz_float = 0
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0
        self.angle = angle
        self.afelio = afelio
        self.perielio = perielio
        self.K = 0
        self.U = 0
        self.velTAN = 0
        self.velTANx = 0
        self.velTANy = 0
        self.velTANz = 0
        self.velTANcoordenadas = 0
        self.velTANcoordenadasLISTA = []
        self.velXvelYvelZ = []
        self.VangularX = 0
        self.VangularY = 0
        self.VangularZ = 0
        self.Vangular = 0
        self.Vangularcoordenadas = 0
        self.VangularLISTA = []
        self.I = []
        self.KplusU = []
        self.angulo = 0
        self.L = 0
        self.Lx = 0
        self.Ly = 0
        self.Lz = 0
        self.Lsquart = 0
        self.Llista = []
        self.Px = 0
        self.Py = 0
        self.Pz = 0
        self.P = 0
        self.Plista = []
        self.Wcomperiodo = 0
        self.periodoorbital = periodoorbital
        self.Etotalporunidadedemassa = 0
        self.time = 0
        self.Wangular = 0
        self.gravity = 0
        self.raiomediodoplaneta = raiomediodoplaneta
        self.velocidadeescape = 0
        self.updated_pointpares = []
        self.posicaodesenhoX= 0
        self.posicaodesenhoY= 0
        self.posicaodesenhoXY= 0
        self.xdesenho = 0
        self.ydesenho = 0
        self.xydesenho = 0
        self.tandesenho = 0
        self.planoperpendicularaovetormomentoangular = 0


    def draw(self, DISPLAY):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2


        if len(self.orbit) > 2:
            updated_points = []
            updated_pointpares = []
            for point in self.orbit:
                x, y, z = point
                x = (x * self.SCALE + WIDTH / 2)
                y = (y * self.SCALE + HEIGHT / 2)
                z = 0

                updated_points.append((x, y, z))
                updated_pointpares.append((x,y))

                self.updated_pointpares.append(updated_pointpares)
                self.xdesenho = x
                self.ydesenho = y
                self.xydesenho = x,y
                self.tandesenho = np.sqrt(x**2 + y**2)

                #DESENHA VARIAS LINHAS DO SOL ATE O PLANETA QUE FICAM NA TELA
                #pygame.draw.line(DISPLAY, self.color, (x, y), (self.SCALE + WIDTH / 2, self.SCALE + HEIGHT / 2), 1)
                #pygame.draw.line(DISPLAY, MARSCOLOR,(earth.xdesenho, earth.ydesenho), (mars.xdesenho, mars.ydesenho),1)

                #DESENHAS LINHAS DE ORBITA
            #pygame.draw.lines(DISPLAY, self.color, False, updated_pointpares, 1)

                #DESENHA LINHAS DE UM PLANETA AO OUTRO
            #pygame.draw.line(DISPLAY, MARSCOLOR,(earth.x*earth.SCALE + WIDTH/2, earth.y*earth.SCALE + HEIGHT/2), (mars.x*mars.SCALE + WIDTH/2, mars.y*mars.SCALE + HEIGHT/2),1)
            #pygame.draw.line(DISPLAY, VENUSCOLOR,(earth.x * earth.SCALE + WIDTH / 2, earth.y * earth.SCALE + HEIGHT / 2),(venus.x * venus.SCALE + WIDTH / 2, venus.y * venus.SCALE + HEIGHT / 2), 1)
            #pygame.draw.line(DISPLAY, MERCURYCOLOR,(earth.x * earth.SCALE + WIDTH / 2, earth.y * earth.SCALE + HEIGHT / 2),(mercury.x * mercury.SCALE + WIDTH / 2, mercury.y * mercury.SCALE + HEIGHT / 2), 1)
            #pygame.draw.line(DISPLAY, JUPITERCOLOR,(earth.x * earth.SCALE + WIDTH / 2, earth.y * earth.SCALE + HEIGHT / 2),(jupiter.x * jupiter.SCALE + WIDTH / 2, jupiter.y * jupiter.SCALE + HEIGHT / 2), 1)
            #pygame.draw.line(DISPLAY, SATURNCOLOR,(earth.x * earth.SCALE + WIDTH / 2, earth.y * earth.SCALE + HEIGHT / 2),(saturn.x * saturn.SCALE + WIDTH / 2, saturn.y * saturn.SCALE + HEIGHT / 2), 1)

                #DESENHA LINHAS DO PLANETA ATÉ O SOL
            #pygame.draw.line(DISPLAY, self.color, (x, y), (self.SCALE + WIDTH/2, self.SCALE + HEIGHT/2),1)

                #DESENHA LINHAS QUE PASSAM DO PLANETA
            #pygame.draw.line(DISPLAY, mars.color, (mars.position_x, mars.position_y), (mars.SCALE + WIDTH/2, mars.SCALE + HEIGHT/2),1)
            #pygame.draw.line(DISPLAY, BLUE, (earth.position_x, earth.position_y),(earth.SCALE + WIDTH / 2, earth.SCALE + HEIGHT / 2), 1)

        #DESENHA OS PLANETAS
        pygame.draw.circle(DISPLAY, self.color, (x,y), self.radius)


        if not self.sun:

            #TEXTO NOME DOS PLANETAS
            nomeplanetaterra_text = FONT.render('EARTH', 3, BLUE)
            DISPLAY.blit( nomeplanetaterra_text, (earth.xdesenho - nomeplanetaterra_text.get_width() / 2, earth.ydesenho - nomeplanetaterra_text.get_height() / 2+20))
            nomeplanetamars_text = FONT.render('MARS', 3, MARSCOLOR)
            DISPLAY.blit( nomeplanetamars_text, (mars.xdesenho - nomeplanetamars_text.get_width() / 2, mars.ydesenho - nomeplanetamars_text.get_height() / 2+20))
            nomeplanetavenus_text = FONT.render('VENUS', 3, VENUSCOLOR)
            DISPLAY.blit( nomeplanetavenus_text, (venus.xdesenho - nomeplanetavenus_text.get_width() / 2, venus.ydesenho - nomeplanetavenus_text.get_height() / 2+20))
            nomeplanetaneptune_text = FONT.render('NEPTUNE', 3, NEPTUNECOLOR)
            DISPLAY.blit( nomeplanetaneptune_text, (neptune.xdesenho - nomeplanetaneptune_text.get_width() / 2, neptune.ydesenho - nomeplanetaneptune_text.get_height() / 2+20))
            nomeplanetajupiter_text = FONT.render('JUPITER', 3, JUPITERCOLOR)
            DISPLAY.blit( nomeplanetajupiter_text, (jupiter.xdesenho - nomeplanetajupiter_text.get_width() / 2, jupiter.ydesenho - nomeplanetajupiter_text.get_height() / 2+20))
            nomeplanetauranus_text = FONT.render('URANUS', 3, URANUSCOLOR)
            DISPLAY.blit( nomeplanetauranus_text, (uranus.xdesenho - nomeplanetauranus_text.get_width() / 2, uranus.ydesenho - nomeplanetauranus_text.get_height() / 2+20))
            nomeplanetamercury_text = FONT.render('MERCURY', 3, MERCURYCOLOR)
            DISPLAY.blit( nomeplanetamercury_text, (mercury.xdesenho - nomeplanetamercury_text.get_width() / 2, mercury.ydesenho - nomeplanetamercury_text.get_height() / 2+20))
            nomeplanetasaturn_text = FONT.render('SATURN', 3, SATURNCOLOR)
            DISPLAY.blit( nomeplanetasaturn_text, (saturn.xdesenho - nomeplanetasaturn_text.get_width() / 2, saturn.ydesenho - nomeplanetasaturn_text.get_height() / 2+20))

            #TEXTO DISTANCIA NO LADO DA TELA DE CADA PLANETA EM ORDEM
            distance_text = FONT.render("Distância relativa ao Sol [km]", 1, WHITE)
            DISPLAY.blit(distance_text,(1, 0))
            distance_text_mercury = FONT.render(f"{round(mercury.distance_to_sun / 1000, 1)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(distance_text_mercury, (1, 20))
            distance_text_venus = FONT.render(f"{round(venus.distance_to_sun / 1000, 1)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(distance_text_venus, (1, 40))
            distance_text_earth = FONT.render(f"{round(earth.distance_to_sun / 1000 , 1)}", 0.5, BLUE)
            DISPLAY.blit(distance_text_earth, (1,60))
            distance_text_mars = FONT.render(f"{round(mars.distance_to_sun / 1000, 1)}", 0.5, MARSCOLOR)
            DISPLAY.blit(distance_text_mars, (1, 80))
            distance_text_jupiter = FONT.render(f"{round(jupiter.distance_to_sun / 1000, 1)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(distance_text_jupiter, (1, 100))
            distance_text_saturn = FONT.render(f"{round(saturn.distance_to_sun / 1000, 1)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(distance_text_saturn, (1, 120))
            distance_text_uranus = FONT.render(f"{round(uranus.distance_to_sun / 1000, 1)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(distance_text_uranus, (1, 140))
            distance_text_neptune = FONT.render(f"{round(neptune.distance_to_sun / 1000, 1)}",0.5, NEPTUNECOLOR)
            DISPLAY.blit(distance_text_neptune, (1, 160))


            #TEXTO VELOCIDADE DE CADA PLANETA
            veltan_text = FONT.render("Velocidade de órbita [km/s]", 1, WHITE)
            DISPLAY.blit(veltan_text, (1, 420))
            veltan_text_mercury = FONT.render(f"{round(mercury.velTAN, 1)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(veltan_text_mercury, (1,440))
            veltan_text_venus = FONT.render(f"{round(venus.velTAN, 1)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(veltan_text_venus, (1, 460))
            veltan_text_earth = FONT.render(f"{round(earth.velTAN, 1)}", 0.5, BLUE)
            DISPLAY.blit(veltan_text_earth, (1, 480))
            veltan_text_mars = FONT.render(f"{round(mars.velTAN, 1)}", 0.5, MARSCOLOR)
            DISPLAY.blit(veltan_text_mars, (1, 500))
            veltan_text_jupiter = FONT.render(f"{round(jupiter.velTAN, 1)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(veltan_text_jupiter, (1, 520))
            veltan_text_saturn = FONT.render(f"{round(saturn.velTAN, 1)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(veltan_text_saturn, (1, 540))
            veltan_text_uranus = FONT.render(f"{round(uranus.velTAN, 1)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(veltan_text_uranus, (1, 560))
            veltan_text_neptune = FONT.render(f"{round(neptune.velTAN, 1)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(veltan_text_neptune, (1, 580))

            #TEXTO ENERGIA CINÉTICA
            energiacinetica_text = FONT.render("Energia cinética de órbita [kg*(km^2/s^2)]", 1, WHITE)
            DISPLAY.blit(energiacinetica_text, (650, 0))
            energiacinetica_text_mercury = FONT.render(f"{round(mercury.K, 1)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(energiacinetica_text_mercury, (650,20))
            energiacinetica_text_venus = FONT.render(f"{round(venus.K, 1)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(energiacinetica_text_venus, (650,40))
            energiacinetica_text_earth = FONT.render(f"{round(earth.K, 1)}", 0.5, BLUE)
            DISPLAY.blit(energiacinetica_text_earth, (650, 60))
            energiacinetica_text_mars = FONT.render(f"{round(mars.K, 1)}", 0.5, MARSCOLOR)
            DISPLAY.blit(energiacinetica_text_mars, (650, 80))
            energiacinetica_text_jupiter = FONT.render(f"{round(jupiter.K, 1)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(energiacinetica_text_jupiter, (650, 100))
            energiacinetica_text_saturn = FONT.render(f"{round(saturn.K, 1)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(energiacinetica_text_saturn, (650, 120))
            energiacinetica_text_uranus = FONT.render(f"{round(uranus.K, 1)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(energiacinetica_text_uranus, (650, 140))
            energiacinetica_text_neptune = FONT.render(f"{round(neptune.K, 1)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(energiacinetica_text_neptune, (650, 160))
        
            #TEXTO ENERGIA POTENCIAL
            energiapotencial_text = FONT.render("Energia potencial de órbita [J]", 1, WHITE)
            DISPLAY.blit(energiapotencial_text, (250, 0))
            energiapotencial_text_mercury = FONT.render(f"{round(mercury.U, 1)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(energiapotencial_text_mercury, (250,20))
            energiapotencial_text_venus = FONT.render(f"{round(venus.U, 1)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(energiapotencial_text_venus, (250, 40))
            energiapotencial_text_earth = FONT.render(f"{round(earth.U, 1)}", 0.5, BLUE)
            DISPLAY.blit(energiapotencial_text_earth, (250, 60))
            energiapotencial_text_mars = FONT.render(f"{round(mars.U, 1)}", 0.5, MARSCOLOR)
            DISPLAY.blit(energiapotencial_text_mars, (250, 80))
            energiapotencial_text_jupiter = FONT.render(f"{round(jupiter.U, 1)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(energiapotencial_text_jupiter, (250, 100))
            energiapotencial_text_saturn = FONT.render(f"{round(saturn.U, 1)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(energiapotencial_text_saturn, (250, 120))
            energiapotencial_text_uranus = FONT.render(f"{round(uranus.U, 1)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(energiapotencial_text_uranus, (250, 140))
            energiapotencial_text_neptune = FONT.render(f"{round(neptune.U, 1)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(energiapotencial_text_neptune, (250, 160))

            #TEXTO ENERGIA TOTAL POR UNIDADE DE MASSA
            energiatotalporunidadedemassa_text = FONT.render("Energia total K + U", 1, WHITE)
            DISPLAY.blit(energiatotalporunidadedemassa_text, (1000, 0))
            energiatotalporunidadedemassa_text_mercury = FONT.render(f"{round(mercury.Etotalporunidadedemassa, 1)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(energiatotalporunidadedemassa_text_mercury, (1000,20))
            energiatotalporunidadedemassa_text_venus = FONT.render(f"{round(venus.Etotalporunidadedemassa, 1)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(energiatotalporunidadedemassa_text_venus, (1000,40))
            energiatotalporunidadedemassa_text_earth = FONT.render(f"{round(earth.Etotalporunidadedemassa, 1)}", 0.5, BLUE)
            DISPLAY.blit(energiatotalporunidadedemassa_text_earth, (1000, 60))
            energiatotalporunidadedemassa_text_mars = FONT.render(f"{round(mars.Etotalporunidadedemassa, 1)}", 0.5, MARSCOLOR)
            DISPLAY.blit(energiatotalporunidadedemassa_text_mars, (1000, 80))
            energiatotalporunidadedemassa_text_jupiter = FONT.render(f"{round(jupiter.Etotalporunidadedemassa, 1)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(energiatotalporunidadedemassa_text_jupiter, (1000, 100))
            energiatotalporunidadedemassa_text_saturn = FONT.render(f"{round(saturn.Etotalporunidadedemassa, 1)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(energiatotalporunidadedemassa_text_saturn, (1000, 120))
            energiatotalporunidadedemassa_text_uranus = FONT.render(f"{round(uranus.Etotalporunidadedemassa, 1)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(energiatotalporunidadedemassa_text_uranus, (1000, 140))
            energiatotalporunidadedemassa_text_neptune = FONT.render(f"{round(neptune.Etotalporunidadedemassa, 1)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(energiatotalporunidadedemassa_text_neptune, (1000, 160))

            #TEXTO MOMENTO ANGULAR
            momentoangular_text = FONT.render("Momento angular por unidade de massa", 1, WHITE)
            DISPLAY.blit(momentoangular_text, (1300, 0))
            momentoangular_text_mercury = FONT.render(f"{(mercury.L)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(momentoangular_text_mercury, (1300,20))
            momentoangular_text_venus = FONT.render(f"{(venus.L)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(momentoangular_text_venus, (1300,40))
            momentoangular_text_earth = FONT.render(f"{(earth.L)}", 0.5, BLUE)
            DISPLAY.blit(momentoangular_text_earth, (1300, 60))
            momentoangular_text_mars = FONT.render(f"{(mars.L)}", 0.5, MARSCOLOR)
            DISPLAY.blit(momentoangular_text_mars, (1300, 80))
            momentoangular_text_jupiter = FONT.render(f"{(jupiter.L)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(momentoangular_text_jupiter, (1300, 100))
            momentoangular_text_saturn = FONT.render(f"{(saturn.L)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(momentoangular_text_saturn, (1300, 120))
            momentoangular_text_uranus = FONT.render(f"{(uranus.L)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(momentoangular_text_uranus, (1300, 140))
            momentoangular_text_neptune = FONT.render(f"{(neptune.L)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(momentoangular_text_neptune, (1300, 160))

            #TEXTO ângulo
            angulo_text = FONT.render("Ângulo, planeta-sol", 1, WHITE)
            DISPLAY.blit(angulo_text, (1, 220))
            angulo_text_mercury = FONT.render(f"{(mercury.angulo)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(angulo_text_mercury, (1,240))
            angulo_text_venus = FONT.render(f"{(venus.angulo)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(angulo_text_venus, (1,260))
            angulo_text_earth = FONT.render(f"{(earth.angulo)}", 0.5, BLUE)
            DISPLAY.blit(angulo_text_earth, (1, 280))
            angulo_text_mars = FONT.render(f"{(mars.angulo)}", 0.5, MARSCOLOR)
            DISPLAY.blit(angulo_text_mars, (1, 300))
            angulo_text_jupiter = FONT.render(f"{(jupiter.angulo)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(angulo_text_jupiter, (1, 320))
            angulo_text_saturn = FONT.render(f"{(saturn.angulo)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(angulo_text_saturn, (1, 340))
            angulo_text_uranus = FONT.render(f"{(uranus.angulo)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(angulo_text_uranus, (1,360))
            angulo_text_neptune = FONT.render(f"{(neptune.angulo)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(angulo_text_neptune, (1, 380))

            # TEXTO PERIODO ORBITAL
            angulo_text = FONT.render("Período orbital [Dias]", 1, WHITE)
            DISPLAY.blit(angulo_text, (1, 620))
            angulo_text_mercury = FONT.render(f"{((sqrt(1 * (0.4 ** 3))) * 365.25)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(angulo_text_mercury, (1, 640))
            angulo_text_venus = FONT.render(f"{((sqrt(1 * (0.72333 ** 3))) * 365.25)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(angulo_text_venus, (1, 660))
            angulo_text_earth = FONT.render(f"{((sqrt(1 * (1 ** 3))) * 365.25)}", 0.5, BLUE)
            DISPLAY.blit(angulo_text_earth, (1, 680))
            angulo_text_mars = FONT.render(f"{((sqrt(1 * (1.52366 ** 3))) * 365.25)}", 0.5, MARSCOLOR)
            DISPLAY.blit(angulo_text_mars, (1, 700))
            angulo_text_jupiter = FONT.render(f"{((sqrt(1 * (5.2 ** 3))) * 365.25)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(angulo_text_jupiter, (1, 720))
            angulo_text_saturn = FONT.render(f"{((sqrt(1 * (9.6 ** 3))) * 365.25)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(angulo_text_saturn, (1, 740))
            angulo_text_uranus = FONT.render(f"{((sqrt(1 * (19.2 ** 3))) * 365.25)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(angulo_text_uranus, (1, 760))
            angulo_text_neptune = FONT.render(f"{((sqrt(1 * (30 ** 3))) * 365.25)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(angulo_text_neptune, (1, 780))

            #TEXTO SEMI EIXO MAIOR
            semieixomaior_text = FONT.render("Semi-eixo maior [AU]", 1, WHITE)
            DISPLAY.blit(semieixomaior_text, (1, 820))
            semieixomaior_text_mercury = FONT.render(f"{0.4}",0.5, MERCURYCOLOR)
            DISPLAY.blit(semieixomaior_text_mercury, (1, 840))
            semieixomaior_text_venus = FONT.render(f"{(0.72333)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(semieixomaior_text_venus, (1, 860))
            semieixomaior_text_earth = FONT.render(f"{(1)}", 0.5, BLUE)
            DISPLAY.blit(semieixomaior_text_earth, (1, 880))
            semieixomaior_text_mars = FONT.render(f"{(1.52366)}", 0.5, MARSCOLOR)
            DISPLAY.blit(semieixomaior_text_mars, (1, 900))
            semieixomaior_text_jupiter = FONT.render(f"{(5.2)}",0.5, JUPITERCOLOR)
            DISPLAY.blit(semieixomaior_text_jupiter, (1, 920))
            semieixomaior_text_saturn = FONT.render(f"{(9.6)}",0.5, SATURNCOLOR)
            DISPLAY.blit(semieixomaior_text_saturn, (1, 940))
            semieixomaior_text_uranus = FONT.render(f"{(19.2)}",0.5, URANUSCOLOR)
            DISPLAY.blit(semieixomaior_text_uranus, (1, 960))
            semieixomaior_text_neptune = FONT.render(f"{(30)}",0.5, NEPTUNECOLOR)
            DISPLAY.blit(semieixomaior_text_neptune, (1, 980))

            #TEXTO FORÇA GRAVITACIONAL
            forcagravitacional_text = FONT.render("Força gravitacional [N]", 1, WHITE)
            DISPLAY.blit(forcagravitacional_text, (1700, 0))
            forcagravitacional_text_mercury = FONT.render(f"{(mercury.force)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(forcagravitacional_text_mercury, (1700,20))
            forcagravitacional_text_venus = FONT.render(f"{(venus.force)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(forcagravitacional_text_venus, (1700,40))
            forcagravitacional_text_earth = FONT.render(f"{(earth.force)}", 0.5, BLUE)
            DISPLAY.blit(forcagravitacional_text_earth, (1700, 60))
            forcagravitacional_text_mars = FONT.render(f"{(mars.force)}", 0.5, MARSCOLOR)
            DISPLAY.blit(forcagravitacional_text_mars, (1700, 80))
            forcagravitacional_text_jupiter = FONT.render(f"{(jupiter.force)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(forcagravitacional_text_jupiter, (1700, 100))
            forcagravitacional_text_saturn = FONT.render(f"{(saturn.force)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(forcagravitacional_text_saturn, (1700, 120))
            forcagravitacional_text_uranus = FONT.render(f"{(uranus.force)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(forcagravitacional_text_uranus, (1700, 140))
            forcagravitacional_text_neptune = FONT.render(f"{(neptune.force)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(forcagravitacional_text_neptune, (1700, 160))

            # TEXTO ACELERAÇÃO DA GRAVIDADE
            gravity_text = FONT.render("Aceleração da gravidade [m/s**2]", 1, WHITE)
            DISPLAY.blit(gravity_text, (1700, 200))
            gravity_text_mercury = FONT.render(f"{(mercury.gravity)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(gravity_text_mercury, (1700, 220))
            gravity_text_venus = FONT.render(f"{(venus.gravity)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(gravity_text_venus, (1700, 240))
            gravity_text_earth = FONT.render(f"{(earth.gravity)}", 0.5, BLUE)
            DISPLAY.blit(gravity_text_earth, (1700, 260))
            gravity_text_mars = FONT.render(f"{(mars.gravity)}", 0.5, MARSCOLOR)
            DISPLAY.blit(gravity_text_mars, (1700, 280))
            gravity_text_jupiter = FONT.render(f"{(jupiter.gravity)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(gravity_text_jupiter, (1700, 300))
            gravity_text_saturn = FONT.render(f"{(saturn.gravity)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(gravity_text_saturn, (1700, 320))
            gravity_text_uranus = FONT.render(f"{(uranus.gravity)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(gravity_text_uranus, (1700, 340))
            gravity_text_neptune = FONT.render(f"{(neptune.gravity)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(gravity_text_neptune, (1700, 360))

            # TEXTO VELOCIDADE DE ESCAPE
            velocidadeescape_text = FONT.render("Velocidade de escape [km/s]", 1, WHITE)
            DISPLAY.blit(velocidadeescape_text, (1700, 400))
            velocidadeescape_text_mercury = FONT.render(f"{(mercury.velocidadeescape)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(velocidadeescape_text_mercury, (1700, 420))
            velocidadeescape_text_venus = FONT.render(f"{(venus.velocidadeescape)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(velocidadeescape_text_venus, (1700, 440))
            velocidadeescape_text_earth = FONT.render(f"{(earth.velocidadeescape)}", 0.5, BLUE)
            DISPLAY.blit(velocidadeescape_text_earth, (1700, 460))
            velocidadeescape_text_mars = FONT.render(f"{(mars.velocidadeescape)}", 0.5, MARSCOLOR)
            DISPLAY.blit(velocidadeescape_text_mars, (1700, 480))
            velocidadeescape_text_jupiter = FONT.render(f"{(jupiter.velocidadeescape)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(velocidadeescape_text_jupiter, (1700, 500))
            velocidadeescape_text_saturn = FONT.render(f"{(saturn.velocidadeescape)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(velocidadeescape_text_saturn, (1700, 520))
            velocidadeescape_text_uranus = FONT.render(f"{(uranus.velocidadeescape)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(velocidadeescape_text_uranus, (1700, 540))
            velocidadeescape_text_neptune = FONT.render(f"{(neptune.velocidadeescape)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(velocidadeescape_text_neptune, (1700, 560))

            # TEXTO AFELIO
            afelio_text = FONT.render("Afélio [km]", 1, WHITE)
            DISPLAY.blit(afelio_text, (1700, 600))
            afelio_text_mercury = FONT.render(f"{(mercury.afelio)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(afelio_text_mercury, (1700, 620))
            afelio_text_venus = FONT.render(f"{(venus.afelio)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(afelio_text_venus, (1700, 640))
            afelio_text_earth = FONT.render(f"{(earth.afelio)}", 0.5, BLUE)
            DISPLAY.blit(afelio_text_earth, (1700, 660))
            afelio_text_mars = FONT.render(f"{(mars.afelio)}", 0.5, MARSCOLOR)
            DISPLAY.blit(afelio_text_mars, (1700, 680))
            afelio_text_jupiter = FONT.render(f"{(jupiter.afelio)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(afelio_text_jupiter, (1700, 700))
            afelio_text_saturn = FONT.render(f"{(saturn.afelio)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(afelio_text_saturn, (1700, 720))
            afelio_text_uranus = FONT.render(f"{(uranus.afelio)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(afelio_text_uranus, (1700, 740))
            afelio_text_neptune = FONT.render(f"{(neptune.afelio)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(afelio_text_neptune, (1700, 760))

            #TEXTO PERIÉLIO
            perielio_text = FONT.render("Periélio [km]", 1, WHITE)
            DISPLAY.blit(perielio_text, (1700, 800))
            perielio_text_mercury = FONT.render(f"{(mercury.perielio)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(perielio_text_mercury, (1700, 820))
            perielio_text_venus = FONT.render(f"{(venus.perielio)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(perielio_text_venus, (1700, 840))
            perielio_text_earth = FONT.render(f"{(earth.perielio)}", 0.5, BLUE)
            DISPLAY.blit(perielio_text_earth, (1700, 860))
            perielio_text_mars = FONT.render(f"{(mars.perielio)}", 0.5, MARSCOLOR)
            DISPLAY.blit(perielio_text_mars, (1700, 880))
            perielio_text_jupiter = FONT.render(f"{(jupiter.perielio)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(perielio_text_jupiter, (1700, 900))
            perielio_text_saturn = FONT.render(f"{(saturn.perielio)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(perielio_text_saturn, (1700, 920))
            perielio_text_uranus = FONT.render(f"{(uranus.perielio)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(perielio_text_uranus, (1700, 940))
            perielio_text_neptune = FONT.render(f"{(neptune.perielio)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(perielio_text_neptune, (1700, 960))

            # TEXTO PLANO PERPENDICULAR
            planoperpendicularaovetormoomentoangular_text = FONT.render("Plano Perpendicular ao vetor momento angular", 1, WHITE)
            DISPLAY.blit(planoperpendicularaovetormoomentoangular_text, (1300, 800))
            planoperpendicularaovetormomentoangular_text_mercury = FONT.render(f"{(mercury.planoperpendicularaovetormomentoangular)}", 0.5, MERCURYCOLOR)
            DISPLAY.blit(planoperpendicularaovetormomentoangular_text_mercury, (1300, 820))
            planoperpendicularaovetormomentoangular_text_venus = FONT.render(f"{(venus.planoperpendicularaovetormomentoangular)}", 0.5, VENUSCOLOR)
            DISPLAY.blit(planoperpendicularaovetormomentoangular_text_venus, (1300, 840))
            planoperpendicularaovetormomentoangular_text_earth = FONT.render(f"{(earth.planoperpendicularaovetormomentoangular)}", 0.5, BLUE)
            DISPLAY.blit(planoperpendicularaovetormomentoangular_text_earth, (1300, 860))
            planoperpendicularaovetormomentoangular_text_mars = FONT.render(f"{(mars.planoperpendicularaovetormomentoangular)}", 0.5, MARSCOLOR)
            DISPLAY.blit(planoperpendicularaovetormomentoangular_text_mars, (1300, 880))
            planoperpendicularaovetormomentoangular_text_jupiter = FONT.render(f"{(jupiter.planoperpendicularaovetormomentoangular)}", 0.5, JUPITERCOLOR)
            DISPLAY.blit(planoperpendicularaovetormomentoangular_text_jupiter, (1300, 900))
            planoperpendicularaovetormomentoangular_text_saturn = FONT.render(f"{(saturn.planoperpendicularaovetormomentoangular)}", 0.5, SATURNCOLOR)
            DISPLAY.blit(planoperpendicularaovetormomentoangular_text_saturn, (1300, 920))
            planoperpendicularaovetormomentoangular_text_uranus = FONT.render(f"{(uranus.planoperpendicularaovetormomentoangular)}", 0.5, URANUSCOLOR)
            DISPLAY.blit(planoperpendicularaovetormomentoangular_text_uranus, (1300, 940))
            planoperpendicularaovetormomentoangular_text_neptune = FONT.render(f"{(neptune.planoperpendicularaovetormomentoangular)}", 0.5, NEPTUNECOLOR)
            DISPLAY.blit(planoperpendicularaovetormomentoangular_text_neptune, (1300, 960))

    #GRAVITY FORCE
    def attraction(self, other):
    #DISTANCE PLANETS
        other_x, other_y, other_z = other.x, other.y, other.z
        self.distance_x = other_x - self.x   #(Distancia entre um planeta e o sol X)  x' - x  = dx
        self.distance_y = other_y - self.y   #(Distancia entre um planeta e o sol Y)  y'- y = dy
        self.distance_z = 0
        self.distance_modulo = math.sqrt(self.distance_x ** 2 + self.distance_y ** 2 + self.distance_z ** 2)   #sqrt(dx^2 + dy^2 + dz^2)
        self.distance_xyz = self.distance_x, self.distance_y, self.distance_z
        self.distance_xyz_lista.append(self.distance_xyz)

        if other.sun:
            self.distance_to_sun = self.distance_modulo

        #ATTRACTION FORCE  #F=(G*M*m)/r^2
        force = self.G * (self.mass * other.mass) / (self.distance_modulo ** 2)
        force_x = math.cos(math.atan2(self.distance_y,self.distance_x)) * force
        force_y = math.sin(math.atan2(self.distance_y,self.distance_x)) * force
        force_z = 0
        return  force_x, force_y, force_z



    def update_position(self, planets):
        total_fx = total_fy = total_fz = 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy, fz = self.attraction(planet)
            total_fx += fx
            total_fy += fy
            total_fz += fz
        self.x_vel += (total_fx * self.TIMESTEP) / self.mass
        self.y_vel += (total_fy * self.TIMESTEP) / self.mass
        self.z_vel += (total_fz * self.TIMESTEP) / self.mass
        self.x += (self.x_vel * self.TIMESTEP ) #metros
        self.y += (self.y_vel * self.TIMESTEP)
        self.z += (self.z_vel * self.TIMESTEP)
        self.orbitpares.append((self.x, self.y))
        self.orbit.append((self.x, self.y, self.z))
        self.position_x = self.x /1000
        self.position_y = self.y /1000
        self.position_z = self.z /1000
        self.position_xyz_float = self.position_x, self.position_y, self.position_z
        self.xyzmodulo = (math.sqrt(self.x**2 + self.y**2 + self.z**2)) / 1000 #kilometros
        self.position_x_lista.append(self.position_x)
        self.position_y_lista.append(self.position_y)
        self.position_xy_lista.append((self.position_x, self.position_y))


        #GRAVITIONAL FORCE OF PLANETS  #N
        if self.distance_to_sun !=0:
            self.force = self.G * (self.mass * sun.mass) / (self.distance_to_sun** 2)

        #KINECT ENERGY #m*km**2/s**2
        self.K = (1/2) * (self.mass) * (self.velTAN*1000)**2

        #POTENCIONAL ENERGY
        if self.distance_to_sun != 0:
            self.U = - (((self.G) * (sun.mass) * (self.mass)) / ((self.distance_to_sun/1000)))
        else:
            self.U = 0

        #K - U (Kinect Energy plus Potential Energy)
        self.KplusU = (self.K + self.U)

        #ACELERAÇÃO DA  GRAVIDADE DE CADA PLANETA
        if self.distance_to_sun!=0:
            self.gravity = ((self.G) * self.mass)/(self.raiomediodoplaneta*1000)**2

        #VELOCIDADE DE ESCAPE DE CADA PLANETA
        if self.distance_to_sun!=0:
           self.velocidadeescape = np.sqrt((2*self.G*self.mass/(self.raiomediodoplaneta*1000)))/1000

        #ENERGIA TOTAL POR UNIDADE DE MASSA, E = 1/2 V^2 - GM/R
        if self.distance_to_sun!=0:
            self.Etotalporunidadedemassa = ((1/2) * (self.mass) * (self.velTAN*1000)**2) + (-((self.G) * (sun.mass) * (self.mass)) / ((self.distance_to_sun)))

        #LINEAR MOMENTUM
        self.Px = (self.mass)* (self.position_x)
        if self.distance_y !=0:
            self.Py = (self.mass) * (self.position_y)
        self.Pz = (self.mass) * (self.position_z)
        self.P = self.Px, self.Py, self.Pz
        self.Plista.append (self.P)

        #VELOCIDADE ANGULAR  se Vtan = Raio * velocidade angular, Vangular = Vtan / raio
        self.VangularX = self.velTANx / self.position_x
        self.VangularY = self.velTANy / self.position_y
        if self.position_z !=0:
            self.VangularZ = self.velTANz / self.position_z
        if self.distance_to_sun!=0:
            self.Vangular = self.velTAN / self.distance_to_sun

        self.Vangularcoordenadas = self.VangularX, self.VangularY, self.VangularZ
        self.VangularLISTA.append(self.Vangularcoordenadas)

        #PLANO PERPENDICULAR AO VETOR MOEMNTO ANGULAR
        self.planoperpendicularaovetormomentoangular = ((self.distance_to_sun)*(self.Lz))/(self.mass)


        #MOMENTO ANGULAR POR UNIDADE DE MASSA (posição do planeta X velocidade angular) r X dr
        self.Lx = (((self.position_y*self.z_vel) - (self.position_z*self.y_vel)))
        self.Ly = (((self.position_z*self.x_vel) - (self.position_x*self.z_vel)))
        self.Lz = (((self.position_x*self.y_vel) - (self.position_y*self.x_vel)))
        self.L = self.Lx, self.Ly, self.Lz
        self.Lsquart = np.sqrt (self.Lx**2 + self.Ly**2 + self.Lz**2)
        self.Llista.append(self.L)

        #ANGULO
        self.angulo = ((atan2(self.position_y, self.position_x)) * 180 / np.pi)

        #VELOCIDADE TANGENCIAL
        self.velTAN = (np.sqrt((self.x_vel)**2 + (self.y_vel)**2 + (self.z_vel)**2))/1000  #RESULTADO EM m/s***** se dividir por 1000 fica KM/S
        self.velTANx = (np.sqrt(self.x_vel**2)) /1000
        self.velTANy = (np.sqrt(self.y_vel**2)) /1000
        self.velTANz = (np.sqrt(self.z_vel**2)) /1000
        self.velTANcoordenadas = self.velTANx, self.velTANy, self.velTANz
        self.velTANcoordenadasLISTA.append(self.velTANcoordenadas)

        #VELOCIDADE ANGULAR COM PERÍODO  #RAD/S
        if self.periodoorbital!=0:
            self.Wcomperiodo = (2*np.pi)/self.periodoorbital*86400


        #POSIÇÕES PARA DESENHO
        posicaodesenhoX = self.x * self.SCALE + WIDTH / 2
        posicaodesenhoY = self.y * self.SCALE + HEIGHT /2
        posicaodesenhoXY = self.posicaodesenhoX, self.posicaodesenhoY




        #PERIODO ORBITAL #ANOS   T = sqrt((R^3*4pi^2)/(G*M)) mas T^2 / R^3 = CONSTANTE  T^2terra / R^2terra= 1 [year]/[au], and 1 year = 365.25, so Tqualquer= sqrt (Rqualquer^3 * 1)   ou T = 2*pi*sqrt(a**3/GM), and a = (aphelium + perihelium) / 2
        periodo_orbital_terra = (sqrt(1*(1**3)))* 365.25
        periodo_orbital_marte = (sqrt(1*(1.52366**3)))*365.25
        periodo_orbital_venus = (sqrt(1*(0.72333**3)))*365.25
        periodo_orbital_jupiter = (sqrt(1*(5.2**3)))*365.25
        periodo_orbital_saturn = (sqrt(1 * (9.6 ** 3)))*365.25
        periodo_orbital_uranus = (sqrt(1 * (19.2 ** 3)))*365.25
        periodo_orbital_mercury = (sqrt(1 * (0.4** 3)))*365.25
        periodo_orbital_neptune = (sqrt(1 * (30** 3)))*365.25
        periodo_orbital_todos_planets =  periodo_orbital_terra,  periodo_orbital_marte,  periodo_orbital_venus,  periodo_orbital_jupiter,  periodo_orbital_saturn,  periodo_orbital_uranus,  periodo_orbital_mercury,  periodo_orbital_neptune
        #LUAS DE MARTE
        periodo_orbital_phobos = (0.3189/365.25)  #dia / 1 ano, resposta em anos
        periodo_orbital_deimos = (1.263/365.25)
        periodo_orbital_todos_moonsmars =  periodo_orbital_phobos,  periodo_orbital_deimos
        #LUAS DE JUPITER
        periodo_orbital_metis = (0.295/365.25)
        periodo_orbital_andrasteia = (0.298/365.25)
        periodo_orbital_amalteia = (0.498/365.25)
        periodo_orbital_tebe = (0.675/365.25)
        periodo_orbital_io = (1.769/365.25)
        periodo_orbital_europa = (3.551181/365.25)
        periodo_orbital_ganimedes = (7.155/365.25)
        periodo_orbital_callisto = (16.690/365.25)
        periodo_orbital_todos_moonsjupiter =  periodo_orbital_metis,  periodo_orbital_andrasteia,  periodo_orbital_amalteia,  periodo_orbital_tebe,  periodo_orbital_io,  periodo_orbital_europa,  periodo_orbital_ganimedes,  periodo_orbital_callisto
        #LUAS DE SATURNO
        periodo_orbital_mimas = (0.9424218/365.25)
        periodo_orbital_encelado = (1.370218/365.25)
        periodo_orbital_tetis = (1.887802/365.25)
        periodo_orbital_dione = (2.736915/365.25)
        periodo_orbital_tita = (15.945421/365.25)
        periodo_orbital_japeto = (79.330183/365.25)
        periodo_orbital_hiperion = (21.276609/365.25)
        periodo_orbital_todos_moonssaturn =  periodo_orbital_mimas,  periodo_orbital_encelado,  periodo_orbital_tetis,  periodo_orbital_dione,  periodo_orbital_tita,  periodo_orbital_japeto,  periodo_orbital_hiperion

        periodo_orbital_todos = periodo_orbital_todos_planets,  periodo_orbital_todos_moonssaturn,  periodo_orbital_todos_moonsmars,  periodo_orbital_todos_moonsjupiter


        #PERIODO ORBITAL AO QUADRADO
        periodo_orbital_aoquadrado_terra = (periodo_orbital_terra/365.25)**2
        periodo_orbital_aoquadrado_marte = (periodo_orbital_marte / 365.25) ** 2
        periodo_orbital_aoquadrado_venus = (periodo_orbital_venus/365.25)**2
        periodo_orbital_aoquadrado_jupiter = (periodo_orbital_jupiter / 365.25) ** 2
        periodo_orbital_aoquadrado_saturn = (periodo_orbital_saturn / 365.25) ** 2
        periodo_orbital_aoquadrado_uranus = (periodo_orbital_uranus / 365.25) ** 2
        periodo_orbital_aoquadrado_mercury = (periodo_orbital_mercury / 365.25) ** 2
        periodo_orbital_aoquadrado_neptune = (periodo_orbital_neptune / 365.25) ** 2
        periodo_orbital_aoquadrado_todos_planets = periodo_orbital_aoquadrado_terra, periodo_orbital_aoquadrado_marte, periodo_orbital_aoquadrado_venus, periodo_orbital_aoquadrado_jupiter, periodo_orbital_aoquadrado_saturn, periodo_orbital_aoquadrado_uranus, periodo_orbital_aoquadrado_mercury,periodo_orbital_aoquadrado_neptune
        #LUAS MARTE
        periodo_orbital_aoquadrado_phobos = (periodo_orbital_phobos) ** 2
        periodo_orbital_aoquadrado_deimos = (periodo_orbital_deimos) ** 2
        periodo_orbital_aoquadrado_todos_moonsmars = periodo_orbital_aoquadrado_phobos, periodo_orbital_aoquadrado_deimos
        #LUAS JUPITER
        periodo_orbital_aoquadrado_metis = (periodo_orbital_metis ) ** 2
        periodo_orbital_aoquadrado_andrasteia = (periodo_orbital_andrasteia ) ** 2
        periodo_orbital_aoquadrado_amalteia = (periodo_orbital_amalteia) ** 2
        periodo_orbital_aoquadrado_tebe = (periodo_orbital_tebe) ** 2
        periodo_orbital_aoquadrado_io = (periodo_orbital_io ) ** 2
        periodo_orbital_aoquadrado_europa = (periodo_orbital_europa ) ** 2
        periodo_orbital_aoquadrado_ganimedes = (periodo_orbital_ganimedes) ** 2
        periodo_orbital_aoquadrado_callisto = (periodo_orbital_callisto) ** 2
        periodo_orbital_aoquadrado_todos_jupiter =  periodo_orbital_aoquadrado_metis,  periodo_orbital_aoquadrado_andrasteia,  periodo_orbital_aoquadrado_amalteia,  periodo_orbital_aoquadrado_tebe,  periodo_orbital_aoquadrado_io,  periodo_orbital_aoquadrado_europa,  periodo_orbital_aoquadrado_ganimedes,  periodo_orbital_aoquadrado_callisto
        #LUAS SATURNO
        periodo_orbital_aoquadrado_mimas = (periodo_orbital_mimas) ** 2
        periodo_orbital_aoquadrado_encelado = (periodo_orbital_encelado) ** 2
        periodo_orbital_aoquadrado_tetis = (periodo_orbital_tetis) ** 2
        periodo_orbital_aoquadrado_dione = (periodo_orbital_dione) ** 2
        periodo_orbital_aoquadrado_tita = (periodo_orbital_tita) ** 2
        periodo_orbital_aoquadrado_japeto = (periodo_orbital_japeto) ** 2
        periodo_orbital_aoquadrado_hiperion = (periodo_orbital_hiperion) ** 2
        periodo_orbital_aoquadrado_todos_saturno =  periodo_orbital_aoquadrado_mimas,  periodo_orbital_aoquadrado_encelado,  periodo_orbital_aoquadrado_tetis,  periodo_orbital_aoquadrado_dione,  periodo_orbital_aoquadrado_tita,  periodo_orbital_aoquadrado_japeto,  periodo_orbital_aoquadrado_hiperion

        periodo_orbital_aoquadrado_todos  =  periodo_orbital_aoquadrado_todos_saturno,  periodo_orbital_aoquadrado_todos_jupiter, periodo_orbital_aoquadrado_todos_planets, periodo_orbital_aoquadrado_todos_moonsmars


        #CBUE OF SEMI MAJOR AXIS
        r_cubo_terra = 1**3
        r_cubo_marte = 1.52366 ** 3
        r_cubo_venus = 0.72333**3
        r_cubo_jupiter = 5.2**3
        r_cubo_saturn = 9.6**3
        r_cubo_uranus = 19.2**3
        r_cubo_mercury = 0.4**3
        r_cubo_neptune = 30**3
        r_cubo_todos_planets = r_cubo_terra, r_cubo_marte, r_cubo_venus, r_cubo_jupiter, r_cubo_saturn, r_cubo_uranus, r_cubo_mercury, r_cubo_neptune
        #LUAS MARTE
        r_cubo_deimos =  0.0001568418046** 3
        r_cubo_phobos = 0.00006267469** 3
        r_cubo_todos_moonsmars = r_cubo_deimos, r_cubo_phobos
        #LUAS JUPITER
        r_cubo_metis = 0.000855627152 ** 3
        r_cubo_andrasteia =  0.000862311739 ** 3
        r_cubo_amalteia = 0.0012125841 ** 3
        r_cubo_tebe = 0.00148330988  ** 3
        r_cubo_io = 0.002818890389461 ** 3
        r_cubo_europa = 0.0044846895 ** 3
        r_cubo_ganimedes = 0.007155182056 ** 3
        r_cubo_callisto =0.01258507218  ** 3
        r_cubo_todos_moonsjupiter = r_cubo_metis, r_cubo_andrasteia, r_cubo_amalteia, r_cubo_tebe, r_cubo_io, r_cubo_europa, r_cubo_ganimedes, r_cubo_callisto
        #LUAS SATURNO
        r_cubo_mimas= 0.0012401246  ** 3
        r_cubo_encelado = 0.00159106543 ** 3
        r_cubo_tetis = 0.00196968044 ** 3
        r_cubo_dione = 0.00252276318 ** 3
        r_cubo_tita = 0.0081674290836 ** 3
        r_cubo_japeto = 0.02380582012 ** 3
        r_cubo_hiperion = 0.009900541987 ** 3
        r_cubo_todos_moonssaturno = r_cubo_mimas, r_cubo_encelado, r_cubo_tetis, r_cubo_dione, r_cubo_tita, r_cubo_japeto, r_cubo_hiperion
        r_cubo_todos = r_cubo_todos_moonsmars, r_cubo_todos_moonsjupiter, r_cubo_todos_moonssaturno, r_cubo_todos_planets

        #CONSTANTE KEPLER T^2 / R^3  [AU^2] /
        #PLANETS
        constante_kepler_terra = (periodo_orbital_aoquadrado_terra) / (r_cubo_terra)
        constante_kepler_venus = (periodo_orbital_aoquadrado_venus) / (r_cubo_venus)
        constante_kepler_marte = (periodo_orbital_aoquadrado_marte) / (r_cubo_marte)
        constante_kepler_jupiter = (periodo_orbital_aoquadrado_jupiter) / (r_cubo_jupiter)
        constante_kepler_saturn = (periodo_orbital_aoquadrado_saturn) / (r_cubo_saturn)
        constante_kepler_uranus = (periodo_orbital_aoquadrado_uranus) / (r_cubo_uranus)
        constante_kepler_mercury = (periodo_orbital_aoquadrado_mercury) / (r_cubo_mercury)
        constante_kepler_neptune = (periodo_orbital_aoquadrado_neptune) / (r_cubo_neptune)
        constante_kepler_todos_planets = constante_kepler_terra, constante_kepler_venus, constante_kepler_marte, constante_kepler_jupiter, constante_kepler_saturn, constante_kepler_uranus, constante_kepler_mercury, constante_kepler_neptune
        soma_constantes_kepler_planets = (constante_kepler_terra + constante_kepler_venus + constante_kepler_marte + constante_kepler_jupiter + constante_kepler_saturn + constante_kepler_uranus + constante_kepler_mercury + constante_kepler_neptune)/8

        #MOONS OF MARS
        constante_kepler_phobos = (periodo_orbital_aoquadrado_phobos) / (r_cubo_phobos)
        constante_kepler_deimos = (periodo_orbital_aoquadrado_deimos) / (r_cubo_deimos)
        constante_kepler_todos_moonsmars = constante_kepler_phobos, constante_kepler_deimos
        #JUPITER MOONS
        constante_kepler_metis = (periodo_orbital_aoquadrado_metis) / (r_cubo_metis)
        constante_kepler_andrasteia = (periodo_orbital_aoquadrado_andrasteia) / (r_cubo_andrasteia)
        constante_kepler_tebe = (periodo_orbital_aoquadrado_tebe) / (r_cubo_tebe)
        constante_kepler_io = (periodo_orbital_aoquadrado_io) / (r_cubo_io)
        constante_kepler_europa = (periodo_orbital_aoquadrado_europa) / (r_cubo_europa)
        constante_kepler_ganimedes = (periodo_orbital_aoquadrado_ganimedes) / (r_cubo_ganimedes)
        constante_kepler_callisto = (periodo_orbital_aoquadrado_callisto) / (r_cubo_callisto)
        constante_kepler_todos_moonsjupiter = constante_kepler_metis, constante_kepler_andrasteia, constante_kepler_tebe, constante_kepler_io, constante_kepler_europa, constante_kepler_ganimedes, constante_kepler_callisto
        soma_constantes_kepler_jupitermoons = (constante_kepler_metis + constante_kepler_andrasteia + constante_kepler_tebe + constante_kepler_io + constante_kepler_europa + constante_kepler_ganimedes + constante_kepler_callisto)/7

        #SATURN MOONS
        constante_kepler_mimas = (periodo_orbital_aoquadrado_mimas) / (r_cubo_mimas)
        constante_kepler_encelado = (periodo_orbital_aoquadrado_encelado) / (r_cubo_encelado)
        constante_kepler_tetis = (periodo_orbital_aoquadrado_tetis) / (r_cubo_tetis)
        constante_kepler_dione = (periodo_orbital_aoquadrado_dione) / (r_cubo_dione)
        constante_kepler_tita = (periodo_orbital_aoquadrado_tita) / (r_cubo_tita)
        constante_kepler_japeto = (periodo_orbital_aoquadrado_japeto) / (r_cubo_japeto)
        constante_kepler_hiperion = (periodo_orbital_aoquadrado_hiperion) / (r_cubo_hiperion)
        constante_kepler_todos_moonssaturn = constante_kepler_mimas, constante_kepler_encelado,constante_kepler_tetis, constante_kepler_dione, constante_kepler_tita, constante_kepler_japeto, constante_kepler_hiperion
        soma_constantes_kepler_saturnmoons = (constante_kepler_mimas + constante_kepler_encelado + constante_kepler_tetis + constante_kepler_dione + constante_kepler_tita + constante_kepler_japeto + constante_kepler_hiperion) / 7

        constante_kepler_todos = constante_kepler_todos_planets, constante_kepler_todos_moonssaturn, constante_kepler_todos_moonsmars, constante_kepler_todos_moonsjupiter

        self.time = (pygame.time.get_ticks() / 1000) # miliseconds dividido por1000 resposta em segundos


        #GRÁFICO T**2 / R**3  KEPLER THIRD LAW
        #PLANETS
       # plt.subplot(1, 3, 1)
       # plt.ylabel('Log Cube of semimajor axis [AU³]')
       # plt.xlabel('Log Square of orbital period [yr²]')
       # plt.title("The Harmonic Law of the Solar System")
       # plt.xscale("log")
       # plt.yscale("log")
       # plt.axis(True)
       # plt.grid(True)
       # plt.annotate("Earth", (r_cubo_terra, periodo_orbital_aoquadrado_terra), textcoords="offset points",xytext=(0, 10), ha='center')
       # plt.scatter(r_cubo_terra, periodo_orbital_aoquadrado_terra, s=3, color="black", marker="*", linewidths=8, linestyle="--")
       # plt.annotate("Venus", (r_cubo_venus, periodo_orbital_aoquadrado_venus), textcoords="offset points",xytext=(0, 10), ha='center')
       # plt.scatter(r_cubo_venus, periodo_orbital_aoquadrado_venus, s=3, color="black", marker="*", linewidths=8, linestyle="--")
       # plt.annotate("Mars", (r_cubo_marte, periodo_orbital_aoquadrado_marte), textcoords="offset points",xytext=(0, 10), ha='center')
       # plt.scatter(r_cubo_marte, periodo_orbital_aoquadrado_marte, s=3, color="black", marker="*", linewidths=8, linestyle="--")
       # plt.annotate("Jupiter", (r_cubo_jupiter, periodo_orbital_aoquadrado_jupiter), textcoords="offset points",xytext=(0, 10), ha='center')
       # plt.scatter(r_cubo_jupiter, periodo_orbital_aoquadrado_jupiter, s=3, color="black", marker="*", linewidths=8, linestyle="--")
       # plt.annotate("Saturn", (r_cubo_saturn, periodo_orbital_aoquadrado_saturn), textcoords="offset points", xytext=(0, 10), ha='center')
       # plt.scatter(r_cubo_saturn, periodo_orbital_aoquadrado_saturn, s=3, color="black", marker="*", linewidths=8, linestyle="--")
       # plt.annotate("Neptune", (r_cubo_neptune, periodo_orbital_aoquadrado_neptune), textcoords="offset points",xytext=(0, 10), ha='center')
       # plt.scatter(r_cubo_neptune, periodo_orbital_aoquadrado_neptune, s=3, color="black", marker="*", linewidths=8, linestyle="--")
       # plt.annotate("Uranus", (r_cubo_uranus, periodo_orbital_aoquadrado_uranus), textcoords="offset points",xytext=(0, 10), ha='center')
       # plt.scatter(r_cubo_uranus, periodo_orbital_aoquadrado_uranus, s=3, color="black", marker="*", linewidths=8, linestyle="--")
       # plt.annotate("Mercury", (r_cubo_mercury, periodo_orbital_aoquadrado_mercury), textcoords="offset points",xytext=(0, 10), ha='center')
       # plt.scatter(r_cubo_mercury, periodo_orbital_aoquadrado_mercury, s=3, color="black", marker="*", linewidths=8, linestyle="--")
        #plt.scatter(periodo_orbital_aoquadrado_todos_planets, r_cubo_todos_planets, s=3, color="black", marker="*", linewidths=8,linestyle="--")
        #plt.show()

        # GRÁFICO T**2 / R**3  KEPLER THIRD LAW
        #MOONS OF MARS
       # plt.subplot(2, 2, 2)
       # plt.ylabel('Cube of semimajor axis [AU³]')
       # plt.xlabel('Square of orbital period [yr²]')
       # plt.title("The Harmonic Law of the Moons of Mars")
       # plt.xscale("log")
       # plt.yscale("log")
       # plt.axis(True)
       # plt.grid(True)
       # plt.scatter(periodo_orbital_aoquadrado_todos_moonsmars, r_cubo_todos_moonsmars, s=3, color="black", marker="*",linewidths=8, linestyle="--")
       # plt.show()

        # GRÁFICO T**2 / R**3  LUAS DE JÚPITER
        #MOONS OF JUPITER
       # plt.subplot(1,3,2)
        #plt.ylabel('Log Cube of semimajor axis [AU³]')
        #plt.xlabel('Log Square of orbital period [yr²]')
        #plt.title("The Harmonic Law of Jupiter's Moons")
        #plt.xscale("log")
        #plt.yscale("log")
        #plt.axis(True)
        #plt.grid(True)
        #plt.annotate("Metis", (r_cubo_metis, periodo_orbital_aoquadrado_metis), textcoords="offset points", xytext=(0, -10), ha='center')
        #plt.scatter(r_cubo_metis, periodo_orbital_aoquadrado_metis, s=3, color="black", marker="*", linewidths=4, linestyle="--")
        #plt.annotate("Andrasteia", (r_cubo_andrasteia, periodo_orbital_aoquadrado_andrasteia), textcoords="offset points",xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_andrasteia, periodo_orbital_aoquadrado_andrasteia, s=3, color="black", marker="*", linewidths=4, linestyle="--")
        #plt.annotate("Tebe", (r_cubo_tebe, periodo_orbital_aoquadrado_tebe), textcoords="offset points", xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_tebe, periodo_orbital_aoquadrado_tebe, s=3, color="black", marker="*", linewidths=4, linestyle="--")
        #plt.annotate("Io", (r_cubo_io, periodo_orbital_aoquadrado_io), textcoords="offset points",xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_io, periodo_orbital_aoquadrado_io, s=3, color="black", marker="*", linewidths=4, linestyle="--")
        #plt.annotate("Europa", (r_cubo_europa, periodo_orbital_aoquadrado_europa), textcoords="offset points",xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_europa, periodo_orbital_aoquadrado_europa, s=3, color="black", marker="*", linewidths=4, linestyle="--")
        #plt.annotate("Ganimedes", (r_cubo_ganimedes, periodo_orbital_aoquadrado_ganimedes), textcoords="offset points",xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_ganimedes, periodo_orbital_aoquadrado_ganimedes, s=3, color="black", marker="*", linewidths=4, linestyle="--")
        #plt.annotate("Callisto", (r_cubo_callisto, periodo_orbital_aoquadrado_callisto), textcoords="offset points", xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_callisto, periodo_orbital_aoquadrado_callisto, s=3, color="black", marker="*", linewidths=4, linestyle="--")
        #plt.scatter(periodo_orbital_aoquadrado_todos_jupiter,r_cubo_todos_moonsjupiter, s=3, color="black", marker="*", linewidths=4, linestyle="--")
        #plt.show()



        # GRÁFICO T**2 / R**3  MOONS OF SATURN  plt.figure(figsize = (8,3)) , plt.legend(loc='upper right', fontsize = 10, ncol=2) , plt.tick_params(axis='both', labelsize=10)
        #MOONS OF SATURN
        #plt.subplot(1,3,3)
        #plt.ylabel('Log Cube of semimajor axis [AU³]')
        #plt.xlabel('Log Square of orbital period [yr²]')
        #plt.title("The Harmonic Law of Saturn's Moons")
        #plt.xscale("log")
        #plt.yscale("log")
        #plt.axis(True)
        #plt.grid(True)
        #plt.annotate("Mimas",(r_cubo_mimas, periodo_orbital_aoquadrado_mimas),textcoords="offset points", xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_mimas, periodo_orbital_aoquadrado_mimas, s=3, color="black", marker="*", linewidths=8,linestyle="--")
        #plt.annotate("Encelado", (r_cubo_encelado, periodo_orbital_aoquadrado_encelado), textcoords="offset points", xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_encelado, periodo_orbital_aoquadrado_encelado, s=3, color="black", marker="*", linewidths=8,linestyle="--")
        #plt.annotate("Tetis", (r_cubo_tetis, periodo_orbital_aoquadrado_tetis), textcoords="offset points", xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_tetis, periodo_orbital_aoquadrado_tetis, s=3, color="black", marker="*", linewidths=8,linestyle="--")
        #plt.annotate("Dione", (r_cubo_dione, periodo_orbital_aoquadrado_dione), textcoords="offset points",xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_dione, periodo_orbital_aoquadrado_dione, s=3, color="black", marker="*", linewidths=8,linestyle="--")
        #plt.annotate("Titã", (r_cubo_tita, periodo_orbital_aoquadrado_tita), textcoords="offset points", xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_tita, periodo_orbital_aoquadrado_tita, s=3, color="black", marker="*", linewidths=8,linestyle="--")
        #plt.annotate("Japeto", (r_cubo_japeto, periodo_orbital_aoquadrado_japeto), textcoords="offset points", xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_japeto, periodo_orbital_aoquadrado_japeto, s=3, color="black", marker="*", linewidths=8,linestyle="--")
        #plt.annotate("Hiperion", (r_cubo_hiperion, periodo_orbital_aoquadrado_hiperion), textcoords="offset points", xytext=(0, 10), ha='center')
        #plt.scatter(r_cubo_hiperion, periodo_orbital_aoquadrado_hiperion, s=3, color="black", marker="*", linewidths=8,linestyle="--")
        #plt.scatter(periodo_orbital_aoquadrado_todos_saturno, r_cubo_todos_moonssaturno, s=3, color="black", marker="*", linewidths=8,linestyle="--")
        #plt.show()


        # CALCULOS E SALVAMENTE DE DADOS
        return constante_kepler_todos, r_cubo_todos, periodo_orbital_aoquadrado_todos, periodo_orbital_todos, soma_constantes_kepler_planets, soma_constantes_kepler_saturnmoons, soma_constantes_kepler_jupitermoons

        # ESCREVER CONSTANTE KEPLER NA TELA
        # keplerconstante_text = FONT.render("Kepler constant (T**2)/(R**3)[year]/[AU]", 1, WHITE)
        # DISPLAY.blit(keplerconstante_text, (450, 720))
        # constante_kepler_todos = constante_kepler_terra, constante_kepler_venus, constante_kepler_marte
        # text_constante_kepler_terra = FONT.render(f"{(constante_kepler_terra)}", 0.5, BLUE)
        # DISPLAY.blit(text_constante_kepler_terra, (450, 740))
        # text_constante_kepler_venus = FONT.render(f"{(constante_kepler_venus)}", 0.5, VENUSCOLOR)
        # DISPLAY.blit(text_constante_kepler_venus, (450, 760))
        # text_constante_kepler_marte = FONT.render(f"{(constante_kepler_marte)}", 0.5, RED)
        # DISPLAY.blit(text_constante_kepler_marte, (450, 780))




#PLANETS (X, Y, Z, RADIUS, COLOR, MASS, ANGLE,AFELIO, PERIELIO, PERIODOORBITAL, raiomediodoplaneta)
sun = Planet(0, 0, 0, 25, YELLOW, 1.989 * 10 ** 30,0,0,0, 0, 695000)
sun.sun = True

earth = Planet(1 * Planet.AU, 0, 0, 7, BLUE, 5.97 * 10 ** 24, 0, 152098233, 47098291, (sqrt(1 * (1 ** 3))) * 365.25, 6378.14)
earth.y_vel = 29.78 * 1000 #29.78[m/s] * 1000 [km/s]

venus = Planet(0.723 * Planet.AU, 0, 0, 8, VENUSCOLOR, 4.86 * 10 ** 24, 3.39,108942780 , 107476170, (sqrt(1 * (0.72333 ** 3))) * 365.25, 6051.8)
venus.y_vel = -35.02 * 1000

mars = Planet(1.52366 * Planet.AU, 0, 0, 5, MARSCOLOR, 0.6418 * 10 ** 24, 1.85061,249232432, 206645215, (sqrt(1 * (1.52366 ** 3))) * 365.25, 3397.2)
mars.y_vel = 24.07 * 1000

mercury = Planet(0.38 * Planet.AU, 0, 0, 5, MERCURYCOLOR, 0.3302 * 10 ** 24, 7.004870,69817445 ,46001009, (sqrt(1 * (0.4 ** 3))) * 365.25, 2439.7)
mercury.y_vel = 48.92 * 1000

saturn = Planet(9.54 * Planet.AU, 0, 0, 9, SATURNCOLOR, 568.46 * 10 ** 24, 2.484460,1503509229,1349823615, (sqrt(1 * (9.6 ** 3))) * 365.25, 60268)
saturn.y_vel = 9.64 * 1000

uranus = Planet(19.18 * Planet.AU, 0, 0, 10, URANUSCOLOR, 86.810 * 10 ** 24, 0.772556,3006318143,2734998229, (sqrt(1 * (19.2 ** 3))) * 365.25, 25559)
uranus.y_vel = 6.81 * 1000

neptune = Planet(30.11 * Planet.AU, 10, 0, 1, NEPTUNECOLOR, 102.43 * 10 ** 24, 1.769170,4537039826,4459753056, (sqrt(1 * (30 ** 3))) * 365.25, 24746)
neptune.y_vel = 5.43 * 1000

jupiter = Planet(5.21 * Planet.AU, 0, 0, 10, JUPITERCOLOR, 1898.6 * 10 ** 24, 0.05,816001807,740679835, (sqrt(1 * (5.2 ** 3))) * 365.25, 71492)
jupiter.y_vel = 13.05 * 1000

planets = [sun, earth, venus, mars, mercury, saturn, uranus, neptune, jupiter]




def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick() #60 FRAMES PER SECOND
        DISPLAY.fill((0, 0, 0))


        #BACKGROUND AND IMAGES
        DISPLAY.blit(bg, (0, 0))
        #DISPLAY.blit(DISPLAY, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #DRAW PLANETS
        for planet in planets:
            planet.update_position(planets)
            planet.draw(DISPLAY)


            # GRÁFICOS DE ÓRBITA DA TERRA e MARTE
        #plt.ylabel('y [AU]')
        #plt.xlabel('x [AU]')
        #plt.title("ÓRBITA DOS PLANETAS")
        #plt.grid(True)
        #plt.gca().legend(('Órbita da Terra', 'Órbita de Marte', 'Órbita de Vênus', 'Órbita de Mercúrio', 'Sol'))
        #plt.scatter(earth.x, earth.y, s=3, color="b", marker="*", linewidths=1, linestyle="--")
        #plt.scatter(mars.x, mars.y, s=3, color="red", marker="*", linewidths=1, linestyle="--")
        #plt.scatter(venus.x, venus.y, s=3, color="pink", marker="*", linewidths=1, linestyle="--")
        #plt.scatter(mercury.x, mercury.y, s=3, color="green", marker="*", linewidths=1, linestyle="--")
        #plt.scatter(sun.x, sun.y, s=10, color="black", marker="*", linewidths=1, linestyle="--")
        #plt.show()

        #DESENHA O ENCONTRO DAS ORBITAS
        #plt.subplot(2,3,1)
        #plt.ylabel('y [KM]')
        #plt.xlabel('x [KM]')
        #plt.title("PONTO MÉDIO ENTRE MARTE E TERRA")
        #plt.grid(True)
        #plt.scatter(earth.x * earth.SCALE + HEIGHT / 2 - mars.x * mars.SCALE + HEIGHT / 2, earth.y * earth.SCALE + WIDTH / 2 - mars.y * mars.SCALE + WIDTH / 2, color='red', marker='.', linewidths=0.5, linestyle='--')
        #plt.axis()
        #plt.show()

        #plt.subplot(2,3,2)
        #plt.ylabel('y [KM]')
        #plt.xlabel('x [KM]')
        #plt.title("PONTO MÉDIO ENTRE VÊNUS E TERRA")
        #plt.grid(True)
        #plt.scatter(earth.x * earth.SCALE + HEIGHT / 2 - venus.x * venus.SCALE + HEIGHT / 2, earth.y * earth.SCALE + WIDTH / 2 - venus.y * venus.SCALE + WIDTH / 2, color='b', marker='.', linewidths=0.5, linestyle='--')
        #plt.axis()
        #plt.show()
        #plt.subplot(2,3,3)

        #plt.ylabel('y [KM]')
        #plt.xlabel('x [KM]')
        #plt.title("PONTO MÉDIO ENTRE NETUNO E TERRA")
        #plt.grid(True)
        #plt.scatter(earth.x * earth.SCALE + HEIGHT / 2 - neptune.x * neptune.SCALE + HEIGHT / 2, earth.y * earth.SCALE + WIDTH / 2 - neptune.y * neptune.SCALE + WIDTH / 2, color='y', marker='.', linewidths=0.5, linestyle='--')
        #plt.axis()
        #plt.show()

        #plt.subplot(2,3,4)
        #plt.ylabel('y [KM]')
        #plt.xlabel('x [KM]')
        #plt.title("PONTO MÉDIO ENTRE MERCÚRIO E TERRA")
        #plt.grid(True)
        #plt.scatter(earth.x * earth.SCALE + HEIGHT / 2 - mercury.x * mercury.SCALE + HEIGHT / 2, earth.y * earth.SCALE + WIDTH / 2 - mercury.y * mercury.SCALE + WIDTH / 2, color='g', marker='.', linewidths=0.5, linestyle='--')
        #plt.axis()
        #plt.show()

        #plt.subplot(2,3,5)
        #plt.ylabel('y [KM]')
        #plt.xlabel('x [KM]')
        #plt.title("PONTO MÉDIO ENTRE SATURNO E TERRA")
        #plt.grid(True)
        #plt.scatter(earth.x * earth.SCALE + HEIGHT / 2 - saturn.x * saturn.SCALE + HEIGHT / 2, earth.y * earth.SCALE + WIDTH / 2 - saturn.y * saturn.SCALE + WIDTH / 2, color='orange', marker='.', linewidths=0.5, linestyle='--')
        #plt.axis()
        #plt.show()

        #plt.subplot(2,3,6)
        #plt.ylabel('y [KM]')
        #plt.xlabel('x [KM]')
        #plt.title("PONTO MÉDIO ENTRE JÚPITER E TERRA")
        #plt.grid(True)
        #plt.scatter(earth.x * earth.SCALE + HEIGHT / 2 - jupiter.x * jupiter.SCALE + HEIGHT / 2, earth.y * earth.SCALE + WIDTH / 2 - jupiter.y * jupiter.SCALE + WIDTH / 2, color='pink', marker='.', linewidths=0.5, linestyle='--')
        #plt.axis()
        #plt.show()

        #GRAFICO PONTO MEDIO
        #plt.subplot(1,3,1)
        #plt.ylabel('y [KM]')
        #plt.xlabel('x [KM]')
        #plt.title("PONTO MÉDIO ENTRE VÊNUS E O SOL")
        #plt.grid(True)
        #plt.scatter(sun.x * sun.SCALE + HEIGHT / 2 - venus.x * venus.SCALE + HEIGHT / 2, sun.y * sun.SCALE + WIDTH / 2 - venus.y * venus.SCALE + WIDTH / 2, color='orange', marker='*', linewidths=0.5, linestyle='--')
        #plt.axis()
        #plt.show()

        #plt.subplot(1,3,2)
        #plt.ylabel('y [KM]')
        #plt.xlabel('x [KM]')
        #plt.title("PONTO MÉDIO ENTRE MERCÚRIO E O SOL")
        #plt.grid(True)
        #plt.scatter(sun.x * sun.SCALE + HEIGHT / 2 - mercury.x * mercury.SCALE + HEIGHT / 2, sun.y * sun.SCALE + WIDTH / 2 - mercury.y * mercury.SCALE + WIDTH / 2, color='b', marker='*', linewidths=0.5, linestyle='--')
        #plt.axis()
        #plt.show()


        #plt.ylabel('y [KM]')
        #plt.xlabel('x [KM]')
        #plt.title("PONTO MÉDIO ENTRE MARTE E TERRA")
        #plt.grid(True)
        #plt.scatter(np.sqrt((earth.x * earth.SCALE + HEIGHT / 2)**2 - (mars.x * mars.SCALE + HEIGHT / 2)**2), sqrt((earth.y * earth.SCALE + WIDTH / 2)**2 - (mars.y * mars.SCALE + WIDTH / 2)**2), color='r', marker='*', linewidths=0.5, linestyle='--')
        #plt.axis()
        #plt.show()


        pygame.display.update()




    pygame.quit()




main()
