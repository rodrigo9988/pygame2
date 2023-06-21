import pygame
import sys
import colores
from configuracion import *


class Intro_game:
    def __init__(self, pantalla, limite_ranking):
        self.limite_ranking = limite_ranking
        self.pantalla = pantalla
        self.fondo = pygame.image.load("imagenes/fondo.png")
        self.fondo = pygame.transform.scale(
            self.fondo, (ANCHO_VENTANA, ALTO_VENTANA))
        self.rect_fondo = self.fondo.get_rect()
        self.imagen_play = pygame.image.load("imagenes/play.png")
        self.imagen_play = pygame.transform.scale(self.imagen_play, (100, 100))
        self.rect_play = self.imagen_play.get_rect()
        self.rect_play.centerx = ANCHO_VENTANA / 2
        self.rect_play.centery = ALTO_VENTANA - 150
        self.intro_font = pygame.font.SysFont("Arial", 48)
        self.intro_font_sub = pygame.font.SysFont("Arial", 35)
        self.intro_title = self.intro_font.render(
            "Galaxy Game", True, colores.WHITE)
        self.intro_subtitle = self.intro_font_sub.render(
            "Ingrse su nombre o presione play", True, colores.WHITE)
        self.clock = pygame.time.Clock()
        self.ingrar_nombre()  # Llama a la función de ingreso de texto al inicializar Intro_game
        self.cargar_json()

    def ingrar_nombre(self):
        self.font_input = pygame.font.SysFont("Arial", 30)
        self.ingreso = ''
        ingreso_width = 200
        ingreso_height = 40
        ingreso_x = (ANCHO_VENTANA - ingreso_width) / 2
        ingreso_y = (ALTO_VENTANA - ingreso_height) - 250
        self.ingreso_rect = pygame.Rect(
            ingreso_x, ingreso_y, ingreso_width, ingreso_height)
        # if self.ingreso == '':
        #     self.ingreso = "No name"


    def cargar_json(self):
        try:
            with open("./juego2/datos.json", "r") as archivo_json:
                self.ranking = json.load(archivo_json)
        except json.JSONDecodeError:
            #print("El archivo JSON está vacío.")
            self.ranking = []
        except FileNotFoundError:
            print("La lista no existe y se creo una nueva.")
            self.ranking = []


    def mostrar_ranking(self):
        # Ordenar el ranking por puntaje descendente
        ranking_ordenado = sorted(
            self.ranking, key=lambda jugador: jugador["score"], reverse=True)

        # Configuracion del texto del ranking
        font_ranking = pygame.font.SysFont("Arial", 24)

        # Posicion inicial de la tabla
        self.y_pos = 400  
        self.x_pos = ANCHO_VENTANA - 250
        self.textos_ranking = []

        for i, jugador in enumerate(ranking_ordenado[:self.limite_ranking]):
            nombre = jugador["nombre"]
            score = jugador["score"]
            texto_jugador = font_ranking.render(
                f"{i+1}. {nombre}: {score}", True, colores.WHITE)
            self.textos_ranking.append(texto_jugador)  # Agregar un nuevo jugador
            # Blitear cada jugador
            self.pantalla.blit(texto_jugador, (self.x_pos, self.y_pos))
            # A cada bliteo se le suma 30pixel
            self.y_pos += 30


    def run(self):
        while True:
            self.clock.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    if evento.button == 1:  # Clic izquierdo del mouse
                        if self.rect_play.collidepoint(evento.pos):
                            return self.ingreso  # Sale del bucle y retorna el nombre
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN:
                        return self.ingreso  # Sale del bucle y retorna el nombre
                    elif evento.key == pygame.K_BACKSPACE:
                        self.ingreso = self.ingreso[:-1]
                    else:
                        self.ingreso += evento.unicode

            #blit del fondo
            self.pantalla.blit(self.fondo, self.rect_fondo)
            #blit del boton play
            self.pantalla.blit(self.imagen_play, self.rect_play)
            #blite del ranking
            self.mostrar_ranking()
            #blit del titulo
            self.pantalla.blit(self.intro_title, (ANCHO_VENTANA / 2 -
                               self.intro_title.get_width() / 2, ALTO_VENTANA/2 - 100))
            #blit del subtitulo
            self.pantalla.blit(self.intro_subtitle, (ANCHO_VENTANA /
                               2 - self.intro_subtitle.get_width() / 2, 350))
            # Entrada del usuario
            pygame.draw.rect(self.pantalla, colores.ALICEBLUE,
                             self.ingreso_rect, 2)
            # self.font_input_surface = self.font_input.render(
            #     self.ingreso, True, colores.BLACK)
            self.pantalla.blit(self.font_input.render(self.ingreso, True, colores.ALICEBLUE), (
                self.ingreso_rect.x + 5, self.ingreso_rect.y + 5))  # Dibujar texto de entrada
            pygame.display.flip()
        pygame.quit()
