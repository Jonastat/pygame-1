import pygame

class Enemigo: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = 60
        self.alto = 60
        self.velocidad = 5
        self.color = "purple"
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        self.vida = 3

    def dibujar(self, ventana):
        self.rect = pygame.Rect(self.x,self.y,self.ancho,self.alto)
        pygame.draw.rect(ventana,self.color,self.rect)

    def movimiento(self):
        self.y += self.velocidad