#create a main function and the main function if to look up the distionary created.
def main():
# ask user for fruit wanted 
	fruit_wanted = input("enter fruit:\n").lower()
# using my own function get fruit to fetch the nutritional value of the fruit and print it.
	getfruit(fruit_wanted)

# defining getfruit function
def getfruit(x):
	fruits = {
		"apple": "120",
		"banana": "110",
		"avocado": "50",
		"cantaloupe": "50",
		"grapefruit": "60",
		"grapes": "90",
		"honeydew melon": "50",
		"kiwifruit": "90",
		"lemon": "15",
		"lime": "20",
		"nectarine": "60",
		"orange": "80",
		"peach": "60",
		"pear": "100",
		"pineapple": "50",
		"plums": "70",
		"stawberries": "50",
		"sweet cherries": "100",
		"tangerine": "50",
		"watermelon": "80"
	}
	for fruit in fruits:
		if fruit == x:
			print("Calories:", fruits[fruit])
main()
