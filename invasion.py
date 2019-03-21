import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
#from alien import Alien
import game_functions as gf

def run_game():
	#inicjalizacja gry i utworzenie obiektu ekranu
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Inwazja obcych")


	stats = GameStats(ai_settings)
	ship = Ship(ai_settings, screen)
	bullets = Group()
	#alien = Alien(ai_settings, screen) jeden obcy
	aliens = Group()

	gf.create_fleet(ai_settings, screen, ship, aliens)

	while True:
		gf.check_events(ai_settings, screen, ship, bullets)
		if stats.game_active:
			ship.update()
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, 
			bullets)
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
			

		
run_game()