from pull_data import get_portfolio

def riskIndex(age, checked):
	def checker(checked):
		if checked["retirement"]:
			return .1
		if checked["college"]:
			return .25
		if checked["house"]:
			return .5
		if checked["car"]:
			return .75
		if checked["laptop"] or checked["other"]:
			return 1
	return (.5 * (1-(age/80))+(.5*checker(checked)))/10

def scope(checked):
	if checked["retirement"]:
		return "ten"
	if checked["college"]:
		return "ten"
	if checked["house"]:
		return "five"
	if checked["car"]:
		return "five"
	if checked["laptop"] or checked["other"]:
		return "one"


