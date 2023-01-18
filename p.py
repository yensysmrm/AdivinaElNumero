import pygame
import random
from playsound import playsound
from pygame.locals import *

FONDO = (32, 30, 32)
BLANCO = (0, 0, 0)
COLOR_TEXTO = (50, 60, 80)

pygame.init()
dimensiones = [600, 560]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Adivina el númro")
imagen_panel = pygame.image.load("panel.png")
imagen_boton = pygame.image.load("button.png")
imagen_boton_pressed = pygame.image.load("buttonPressed.png")
imagen_boton_cuadro = pygame.image.load("button.png")
imagen_boton_cuadro_pressed = pygame.image.load("buttonSquarePressed.png")
imagen_text = pygame.image.load("panelInset_brown.png")
fuente = pygame.font.SysFont('Courier', 20)
fuente_numero = pygame.font.SysFont('Courier', 20)


def dibujar_texto(texto, contenedor_imagen, contenedor_rec, fuente_render, color):
    text = fuente_render.render(texto, 1, color)
    centro = text.get_rect()
    diferencia_x = contenedor_imagen.center[0] - centro.center[0]
    diferencia_y = contenedor_imagen.center[1] - centro.center[1]
    pantalla.blit(text, [contenedor_rec.left + diferencia_x, contenedor_rec.top + diferencia_y])


def generar_numero():
    numero = str(random.randint(1, 100))
    return numero


def dibujar_botones_iniciales(lista_botones):
    panel = pygame.transform.scale(imagen_panel, [560, 520])
    pantalla.blit(panel, [20, 20])
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])
        dibujar_texto(boton['texto'], boton['imagen'].get_rect(), boton['rect'], fuente, BLANCO)


def set_text(campo, texto):
    dibujar_texto(texto, campo['imagen'].get_rect(), campo['rect'], fuente_numero, COLOR_TEXTO)


def main():
    game_over = False
    clock = pygame.time.Clock()

    boton_cuadro = pygame.transform.scale(imagen_boton_cuadro, [90, 90])
    boton_cuadro_pressed = pygame.transform.scale(imagen_boton_cuadro_pressed, [90, 90])
    input_text = pygame.transform.scale(imagen_text, [440, 50])

    r_boton_1_1 = imagen_boton.get_rect()
    r_boton_1_2 = imagen_boton.get_rect()
    r_boton_1_3 = imagen_boton.get_rect()
    r_boton_2_1 = boton_cuadro.get_rect()
    r_boton_2_2 = boton_cuadro.get_rect()
    r_boton_2_3 = boton_cuadro.get_rect()
    r_boton_2_4 = boton_cuadro.get_rect()
    r_boton_2_5 = boton_cuadro.get_rect()
    r_boton_2_6 = boton_cuadro.get_rect()
    r_boton_2_7 = boton_cuadro.get_rect()
    r_boton_2_8 = boton_cuadro.get_rect()
    r_boton_2_9 = boton_cuadro.get_rect()
    r_boton_2_0 = boton_cuadro.get_rect()
    input_text_rect = input_text.get_rect()
    input_text_rect.topleft = [80, 445]
    campo_texto = {'imagen': input_text, 'rect': input_text_rect}

    botones = []
    r_boton_1_1.topleft = [60, 80]
    botones.append({'texto': "Reiniciar", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_1, 'on_click': False})
    r_boton_1_2.topleft = [240, 80]
    botones.append({'texto': "Confirmar", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_2, 'on_click': False})
    r_boton_1_3.topleft = [400, 80]
    botones.append({'texto': "Borrar", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': r_boton_1_3, 'on_click': False})
    r_boton_2_1.topleft = [40, 180]
    botones.append({'texto': "1", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_1, 'on_click': False})
    r_boton_2_2.topleft = [140, 180]
    botones.append({'texto': "2", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_2, 'on_click': False})
    r_boton_2_3.topleft = [240, 180]
    botones.append({'texto': "3", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_3, 'on_click': False})
    r_boton_2_4.topleft = [340, 180]
    botones.append({'texto': "4", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_4, 'on_click': False})
    r_boton_2_5.topleft = [440, 180]
    botones.append({'texto': "5", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_5, 'on_click': False})
    r_boton_2_6.topleft = [40, 280]
    botones.append({'texto': "6", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_6, 'on_click': False})
    r_boton_2_7.topleft = [140, 280]
    botones.append({'texto': "7", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_7, 'on_click': False})
    r_boton_2_8.topleft = [240, 280]
    botones.append({'texto': "8", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_8, 'on_click': False})
    r_boton_2_9.topleft = [340, 280]
    botones.append({'texto': "9", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_9, 'on_click': False})
    r_boton_2_0.topleft = [440, 280]
    botones.append({'texto': "0", 'imagen': boton_cuadro, 'imagen_pressed': boton_cuadro_pressed, 'rect': r_boton_2_0, 'on_click': False})



    #dibujar_botones_iniciales(botones)
    click = False
    mostrar_numero = 0
    text=""
    puntos=0
    intentos=0
    numero_aleatorio = generar_numero()
    texto_entrada = ""
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False

        if botones[0]['on_click'] and click:
            puntos=0
            intentos=0
            numero_aleatorio = generar_numero()
            texto_entrada = ""
            mostrar_numero = 0
            click = False

        pantalla.fill(FONDO)
        dibujar_botones_iniciales(botones)
        pantalla.blit(input_text, campo_texto['rect'].topleft)

        if click and botones[1]['on_click']:
            if texto_entrada == numero_aleatorio:
                text = "Felicitaciones!"
                playsound("victoria.wav")
                numero_aleatorio = generar_numero()
                mostrar_numero=100
                texto_entrada = ""
                puntos=puntos+1
            else:
                if(len(texto_entrada) > 0):
                    mostrar_numero=100
                    if int(texto_entrada) < int(numero_aleatorio):
                        text="El número es mayor"
                    else:
                        text="El número es menor"
                    intentos=intentos+1
                texto_entrada = ""
            click = False
        if click and botones[2]['on_click']:
            texto_entrada=""
        if click:
            for i in range(3, 13):
                if botones[i]['on_click'] and len(texto_entrada) < 3:
                    if(len(texto_entrada)>0):
                        if(int(texto_entrada+botones[i]['texto'])<101):        
                            texto_entrada += botones[i]['texto']
                    elif int(botones[i]['texto'])>0:
                        texto_entrada += botones[i]['texto']
            click = False
        if mostrar_numero > 0:
            dibujar_texto(text, pygame.Surface([100, 40]).get_rect(), pygame.Rect([260, 400, 102, 42]), fuente_numero, COLOR_TEXTO)
            mostrar_numero -= 1
        dibujar_texto("Intentos: "+str(intentos), pygame.Surface([100, 40]).get_rect(), pygame.Rect([60, 380, 102, 42]), fuente_numero, COLOR_TEXTO)
        dibujar_texto("Puntuación: "+str(puntos), pygame.Surface([100, 40]).get_rect(), pygame.Rect([60, 410, 102, 42]), fuente_numero, COLOR_TEXTO)
        set_text(campo_texto, texto_entrada)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()