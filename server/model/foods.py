from enum import Enum

class Foods(Enum):
	APPLE_PIE = {'name': 'apple_pie', 'calories': 237, 'proteins': 2.4, 'fats': 11, 'carbs': 34.6}
	BABY_BACK_RIBS = {'name': 'baby_back_ribs', 'calories': 290, 'proteins': 23, 'fats': 20, 'carbs': 5}
	BAKLAVA = {'name': 'baklava', 'calories': 417, 'proteins': 6, 'fats': 24, 'carbs': 46}
	BEEF_CARPACCIO = {'name': 'beef_carpaccio', 'calories': 175, 'proteins': 24, 'fats': 8, 'carbs': 0}
	BEEF_TARTARE = {'name': 'beef_tartare', 'calories': 146, 'proteins': 20, 'fats': 6, 'carbs': 0.1}
	BEET_SALAD = {'name': 'beet_salad', 'calories': 74, 'proteins': 2.3, 'fats': 3.4, 'carbs': 9.6}
	BEIGNETS = {'name': 'beignets', 'calories': 450, 'proteins': 7.6, 'fats': 25, 'carbs': 51}
	BIBIMBAP = {'name': 'bibimbap', 'calories': 118, 'proteins': 7.3, 'fats': 4.4, 'carbs': 12.3}
	BREAD_PUDDING = {'name': 'bread_pudding', 'calories': 156, 'proteins': 4.1, 'fats': 4.7, 'carbs': 23.4}
	BREAKFAST_BURRITO = {'name': 'breakfast_burrito', 'calories': 206, 'proteins': 8.4, 'fats': 11.1, 'carbs': 17.3}
	BRUSCHETTA = {'name': 'bruschetta', 'calories': 175, 'proteins': 4.6, 'fats': 6.2, 'carbs': 24.8}
	CAESAR_SALAD = {'name': 'caesar_salad', 'calories': 190, 'proteins': 3.4, 'fats': 16.6, 'carbs': 7.3}
	CANNOLI = {'name': 'cannoli', 'calories': 392, 'proteins': 7.6, 'fats': 25, 'carbs': 36.6}
	CAPRESE_SALAD = {'name': 'caprese_salad', 'calories': 120, 'proteins': 5.4, 'fats': 8.7, 'carbs': 5.7}
	CARROT_CAKE = {'name': 'carrot_cake', 'calories': 412, 'proteins': 4.7, 'fats': 22.4, 'carbs': 50.9}
	CEVICHE = {'name': 'ceviche', 'calories': 90, 'proteins': 12.6, 'fats': 1.5, 'carbs': 6.6}
	CHEESE_PLATE = {'name': 'cheese_plate', 'calories': 403, 'proteins': 21.1, 'fats': 33.1, 'carbs': 1.3}
	CHEESECAKE = {'name': 'cheesecake', 'calories': 321, 'proteins': 5.5, 'fats': 24.7, 'carbs': 22.5}
	CHICKEN_CURRY = {'name': 'chicken_curry', 'calories': 120, 'proteins': 13, 'fats': 5, 'carbs': 4}
	CHICKEN_QUESADILLA = {'name': 'chicken_quesadilla', 'calories': 301, 'proteins': 16.8, 'fats': 17.1, 'carbs': 19.2}
	CHICKEN_WINGS = {'name': 'chicken_wings', 'calories': 203, 'proteins': 18.6, 'fats': 13.3, 'carbs': 0}
	CHOCOLATE_CAKE = {'name': 'chocolate_cake', 'calories': 371, 'proteins': 3.6, 'fats': 15.6, 'carbs': 53.4}
	CHOCOLATE_MOUSSE = {'name': 'chocolate_mousse', 'calories': 217, 'proteins': 5, 'fats': 15, 'carbs': 20}
	CHURROS = {'name': 'churros', 'calories': 436, 'proteins': 5.1, 'fats': 22.1, 'carbs': 54.1}
	CLAM_CHOWDER = {'name': 'clam_chowder', 'calories': 56, 'proteins': 3.6, 'fats': 1.8, 'carbs': 6.6}
	CLUB_SANDWICH = {'name': 'club_sandwich', 'calories': 274, 'proteins': 13.3, 'fats': 14.3, 'carbs': 24.6}
	CRAB_CAKES = {'name': 'crab_cakes', 'calories': 192, 'proteins': 13.1, 'fats': 9.4, 'carbs': 12.5}
	CREME_BRULEE = {'name': 'creme_brulee', 'calories': 331, 'proteins': 5.3, 'fats': 24.9, 'carbs': 22.4}
	CROQUE_MADAME = {'name': 'croque_madame', 'calories': 346, 'proteins': 17.1, 'fats': 21.4, 'carbs': 23.8}
	CUP_CAKES = {'name': 'cup_cakes', 'calories': 356, 'proteins': 3.6, 'fats': 16.1, 'carbs': 50.7}
	DEVILED_EGGS = {'name': 'deviled_eggs', 'calories': 197, 'proteins': 6, 'fats': 17, 'carbs': 1}
	DONUTS = {'name': 'donuts', 'calories': 452, 'proteins': 4.9, 'fats': 25, 'carbs': 51}
	DUMPLINGS = {'name': 'dumplings', 'calories': 96, 'proteins': 4, 'fats': 3.8, 'carbs': 11.5}
	EDAMAME = {'name': 'edamame', 'calories': 121, 'proteins': 11.9, 'fats': 5.2, 'carbs': 9.9}
	EGGS_BENEDICT = {'name': 'eggs_benedict', 'calories': 353, 'proteins': 13, 'fats': 27, 'carbs': 11}
	ESCARGOTS = {'name': 'escargots', 'calories': 81, 'proteins': 16, 'fats': 1.4, 'carbs': 2}
	FALAFEL = {'name': 'falafel', 'calories': 333, 'proteins': 13.3, 'fats': 17.8, 'carbs': 31.8}
	FILET_MIGNON = {'name': 'filet_mignon', 'calories': 179, 'proteins': 27.3, 'fats': 7.6, 'carbs': 0}
	FISH_AND_CHIPS = {'name': 'fish_and_chips', 'calories': 196, 'proteins': 10.5, 'fats': 9.2, 'carbs': 17.8}
	FOIE_GRAS = {'name': 'foie_gras', 'calories': 462, 'proteins': 7, 'fats': 43, 'carbs': 2}
	FRENCH_FRIES = {'name': 'french_fries', 'calories': 312, 'proteins': 3.4, 'fats': 15.2, 'carbs': 41.4}
	FRENCH_ONION_SOUP = {'name': 'french_onion_soup', 'calories': 73, 'proteins': 3.5, 'fats': 2.2, 'carbs': 10.2}
	FRENCH_TOAST = {'name': 'french_toast', 'calories': 245, 'proteins': 9.21, 'fats': 9.1, 'carbs': 31.04}
	FRIED_CALAMARI = {'name': 'fried_calamari', 'calories': 175, 'proteins': 15, 'fats': 10, 'carbs': 9}
	FRIED_RICE = {'name': 'fried_rice', 'calories': 163, 'proteins': 4.3, 'fats': 5.2, 'carbs': 24.9}
	FROZEN_YOGURT = {'name': 'frozen_yogurt', 'calories': 127, 'proteins': 3.5, 'fats': 4, 'carbs': 21.2}
	GARLIC_BREAD = {'name': 'garlic_bread', 'calories': 350, 'proteins': 8.1, 'fats': 16.1, 'carbs': 44.8}
	GNOCCHI = {'name': 'gnocchi', 'calories': 130, 'proteins': 2.8, 'fats': 0.2, 'carbs': 28}
	GREEK_SALAD = {'name': 'greek_salad', 'calories': 101, 'proteins': 2.5, 'fats': 7.6, 'carbs': 5.4}
	GRILLED_CHEESE_SANDWICH = {'name': 'grilled_cheese_sandwich', 'calories': 350, 'proteins': 12, 'fats': 22, 'carbs': 27}
	GRILLED_SALMON = {'name': 'grilled_salmon', 'calories': 206, 'proteins': 22, 'fats': 12.3, 'carbs': 0}
	GUACAMOLE = {'name': 'guacamole', 'calories': 150, 'proteins': 2, 'fats': 13, 'carbs': 9}
	GYOZA = {'name': 'gyoza', 'calories': 177, 'proteins': 5.8, 'fats': 7.5, 'carbs': 22}
	HAMBURGER = {'name': 'hamburger', 'calories': 254, 'proteins': 14.1, 'fats': 13.3, 'carbs': 22.4}
	HOT_AND_SOUR_SOUP = {'name': 'hot_and_sour_soup', 'calories': 54, 'proteins': 3.4, 'fats': 2, 'carbs': 6.6}
	HOT_DOG = {'name': 'hot_dog', 'calories': 290, 'proteins': 11, 'fats': 25, 'carbs': 1.9}
	HUEVOS_RANCHEROS = {'name': 'huevos_rancheros', 'calories': 123, 'proteins': 6, 'fats': 8, 'carbs': 7}
	HUMMUS = {'name': 'hummus', 'calories': 166, 'proteins': 7.9, 'fats': 9.6, 'carbs': 14.3}
	ICE_CREAM = {'name': 'ice_cream', 'calories': 207, 'proteins': 3.5, 'fats': 11, 'carbs': 24}
	LASAGNA = {'name': 'lasagna', 'calories': 135, 'proteins': 8.8, 'fats': 5.4, 'carbs': 12.6}
	LOBSTER_BISQUE = {'name': 'lobster_bisque', 'calories': 91, 'proteins': 4.9, 'fats': 5.5, 'carbs': 6.4}
	LOBSTER_ROLL_SANDWICH = {'name': 'lobster_roll_sandwich', 'calories': 198, 'proteins': 13, 'fats': 8, 'carbs': 18}
	MACARONI_AND_CHEESE = {'name': 'macaroni_and_cheese', 'calories': 164, 'proteins': 7.6, 'fats': 8.3, 'carbs': 17.1}
	MACARONS = {'name': 'macarons', 'calories': 446, 'proteins': 6.4, 'fats': 20.5, 'carbs': 60.6}
	MISO_SOUP = {'name': 'miso_soup', 'calories': 40, 'proteins': 3, 'fats': 1.3, 'carbs': 4.3}
	MUSSELS = {'name': 'mussels', 'calories': 172, 'proteins': 24, 'fats': 4, 'carbs': 8}
	NACHOS = {'name': 'nachos', 'calories': 306, 'proteins': 7, 'fats': 17, 'carbs': 33}
	OMELETTE = {'name': 'omelette', 'calories': 154, 'proteins': 11, 'fats': 11, 'carbs': 1.7}
	ONION_RINGS = {'name': 'onion_rings', 'calories': 411, 'proteins': 3.4, 'fats': 22.8, 'carbs': 47}
	OYSTERS = {'name': 'oysters', 'calories': 68, 'proteins': 7, 'fats': 2.5, 'carbs': 4.2}
	PAD_THAI = {'name': 'pad_thai', 'calories': 214, 'proteins': 8.5, 'fats': 9.9, 'carbs': 22.3}
	PAELLA = {'name': 'paella', 'calories': 158, 'proteins': 6.7, 'fats': 6.4, 'carbs': 18.2}
	PANCAKES = {'name': 'pancakes', 'calories': 227, 'proteins': 6, 'fats': 10.2, 'carbs': 28}
	PANNA_COTTA = {'name': 'panna_cotta', 'calories': 298, 'proteins': 5.1, 'fats': 25.7, 'carbs': 11.2}
	PEKING_DUCK = {'name': 'peking_duck', 'calories': 337, 'proteins': 19, 'fats': 28, 'carbs': 1.5}
	PHO = {'name': 'pho', 'calories': 36, 'proteins': 3.1, 'fats': 0.3, 'carbs': 6.4}
	PIZZA = {'name': 'pizza', 'calories': 266, 'proteins': 11, 'fats': 10, 'carbs': 33}
	PORK_CHOP = {'name': 'pork_chop', 'calories': 231, 'proteins': 27.6, 'fats': 12.8, 'carbs': 0}
	POUTINE = {'name': 'poutine', 'calories': 267, 'proteins': 5.4, 'fats': 15.9, 'carbs': 23.4}
	PRIME_RIB = {'name': 'prime_rib', 'calories': 298, 'proteins': 22, 'fats': 22, 'carbs': 0}
	PULLED_PORK_SANDWICH = {'name': 'pulled_pork_sandwich', 'calories': 350, 'proteins': 20, 'fats': 15, 'carbs': 34}
	RAMEN = {'name': 'ramen', 'calories': 436, 'proteins': 10, 'fats': 22, 'carbs': 52}
	RAVIOLI = {'name': 'ravioli', 'calories': 217, 'proteins': 9.3, 'fats': 9.3, 'carbs': 24}
	RED_VELVET_CAKE = {'name': 'red_velvet_cake', 'calories': 393, 'proteins': 4.9, 'fats': 21.2, 'carbs': 48.8}
	RISOTTO = {'name': 'risotto', 'calories': 131, 'proteins': 2.3, 'fats': 5.4, 'carbs': 18}
	SAMOSA = {'name': 'samosa', 'calories': 309, 'proteins': 5.1, 'fats': 17.3, 'carbs': 33.1}
	SASHIMI = {'name': 'sashimi', 'calories': 138, 'proteins': 22.5, 'fats': 4.9, 'carbs': 0.1}
	SCALLOPS = {'name': 'scallops', 'calories': 111, 'proteins': 20.5, 'fats': 1, 'carbs': 5.4}
	SEAWEED_SALAD = {'name': 'seaweed_salad', 'calories': 45, 'proteins': 1.7, 'fats': 3.2, 'carbs': 6}
	SHRIMP_AND_GRITS = {'name': 'shrimp_and_grits', 'calories': 144, 'proteins': 8.8, 'fats': 7.4, 'carbs': 10.4}
	SPAGHETTI_BOLOGNESE = {'name': 'spaghetti_bolognese', 'calories': 115, 'proteins': 5.8, 'fats': 4.1, 'carbs': 12.2}
	SPAGHETTI_CARBONARA = {'name': 'spaghetti_carbonara', 'calories': 157, 'proteins': 6.1, 'fats': 8.1, 'carbs': 15.7}
	SPRING_ROLLS = {'name': 'spring_rolls', 'calories': 150, 'proteins': 4, 'fats': 4.1, 'carbs': 23.7}
	STEAK = {'name': 'steak', 'calories': 271, 'proteins': 25.6, 'fats': 19.7, 'carbs': 0}
	STRAWBERRY_SHORTCAKE = {'name': 'strawberry_shortcake', 'calories': 250, 'proteins': 3.6, 'fats': 12.7, 'carbs': 31.8}
	SUSHI = {'name': 'sushi', 'calories': 143, 'proteins': 5.5, 'fats': 1, 'carbs': 30.7}
	TACOS = {'name': 'tacos', 'calories': 226, 'proteins': 9.4, 'fats': 12.5, 'carbs': 19.5}
	TAKOYAKI = {'name': 'takoyaki', 'calories': 175, 'proteins': 7.5, 'fats': 9.6, 'carbs': 14.8}
	TIRAMISU = {'name': 'tiramisu', 'calories': 287, 'proteins': 4.2, 'fats': 17.2, 'carbs': 28.1}
	TUNA_TARTARE = {'name': 'tuna_tartare', 'calories': 165, 'proteins': 23.3, 'fats': 7.2, 'carbs': 0.9}
	WAFFLES = {'name': 'waffles', 'calories': 291, 'proteins': 6.8, 'fats': 14.3, 'carbs': 35.1}
	CIORBA_DE_BURTA = {'name': 'ciorba_de_burta', 'calories': 73, 'proteins': 9, 'fats': 3, 'carbs': 5}
	COZONAC = {'name': 'cozonac', 'calories': 326, 'proteins': 8, 'fats': 10, 'carbs': 48}
	PAPANASI = {'name': 'papanasi', 'calories': 310, 'proteins': 8, 'fats': 18, 'carbs': 30}
	SARMALE = {'name': 'sarmale', 'calories': 186, 'proteins': 8.5, 'fats': 12, 'carbs': 11}

	# def check_values(self):
	# 	item = self.value
	# 	if item['calories'] and item['proteins'] and item['fats'] and item['carbs']:
	# 		return True
	# 	else:
	# 		return False

class_labels = ['apple_pie',
 'baby_back_ribs',
 'baklava',
 'beef_carpaccio',
 'beef_tartare',
 'beet_salad',
 'beignets',
 'bibimbap',
 'bread_pudding',
 'breakfast_burrito',
 'bruschetta',
 'caesar_salad',
 'cannoli',
 'caprese_salad',
 'carrot_cake',
 'ceviche',
 'cheese_plate',
 'cheesecake',
 'chicken_curry',
 'chicken_quesadilla',
 'chicken_wings',
 'chocolate_cake',
 'chocolate_mousse',
 'churros',
 'ciorba_de_burta',
 'clam_chowder',
 'club_sandwich',
 'cozonac',
 'crab_cakes',
 'creme_brulee',
 'croque_madame',
 'cup_cakes',
 'deviled_eggs',
 'donuts',
 'dumplings',
 'edamame',
 'eggs_benedict',
 'escargots',
 'falafel',
 'filet_mignon',
 'fish_and_chips',
 'foie_gras',
 'french_fries',
 'french_onion_soup',
 'french_toast',
 'fried_calamari',
 'fried_rice',
 'frozen_yogurt',
 'garlic_bread',
 'gnocchi',
 'greek_salad',
 'grilled_cheese_sandwich',
 'grilled_salmon',
 'guacamole',
 'gyoza',
 'hamburger',
 'hot_and_sour_soup',
 'hot_dog',
 'huevos_rancheros',
 'hummus',
 'ice_cream',
 'lasagna',
 'lobster_bisque',
 'lobster_roll_sandwich',
 'macaroni_and_cheese',
 'macarons',
 'miso_soup',
 'mussels',
 'nachos',
 'omelette',
 'onion_rings',
 'oysters',
 'pad_thai',
 'paella',
 'pancakes',
 'panna_cotta',
 'papanasi',
 'peking_duck',
 'pho',
 'pizza',
 'pork_chop',
 'poutine',
 'prime_rib',
 'pulled_pork_sandwich',
 'ramen',
 'ravioli',
 'red_velvet_cake',
 'risotto',
 'samosa',
 'sarmale',
 'sashimi',
 'scallops',
 'seaweed_salad',
 'shrimp_and_grits',
 'spaghetti_bolognese',
 'spaghetti_carbonara',
 'spring_rolls',
 'steak',
 'strawberry_shortcake',
 'sushi',
 'tacos',
 'takoyaki',
 'tiramisu',
 'tuna_tartare',
 'waffles']

# print(len(Foods))
# print(len(class_labels))

# for food in Foods:
# 	print(food.name, food.check_values())