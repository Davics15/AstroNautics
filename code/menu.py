#!/usr/bin/python
# -*- coding: utf-8 -*
import pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Shinobi", COLOR_WHITE, ((WIN_WIDTH / 2), 60))
            self.menu_text(50, "Expedition", COLOR_WHITE, ((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPTION)):
                self.menu_text(27, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 180 + 30 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont('Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
