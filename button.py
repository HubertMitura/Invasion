import pygame.font

class Button():
	def __init__(self, ai_settings, screen, msg):
		self.screen = screen
		self.screen.rect = screen.get_rect()

		self.width, self.height = 200, 50
		self.button_color = (0, 255, 0)
