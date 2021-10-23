
#Expected portfolio return 

#Takes two arguments
#First in how many asset classes or a list of weiht corressponding returns. ie [25,75] for 25% corperate bonds , 75% s&p index fund
#Second is a list of expected returns on those assets ie [4, 9 ] for 4% and 9%

def weightedReturn(assets, list_returns):
	expected_return =0

	# Calculate return for even weighting among assets
	if type(assets) == int:
		even_weight = 100/assets*.01	

		if assets == len(list_returns):
			for returns in list_returns:
				expected_return +=even_weight* (returns*.01)
			return expected_return
		
		else:
			pass
	
	# Calculate return for uneven weighting of assets
	if type(assets) == list:
		list_weights= list(map(lambda g : g*.01, assets))
		print(list_weights)
		list_returns =list( map(lambda g : g*.01, list_returns))
		print(list_returns)
		
		
		if len(assets) == len(list_returns):
			for a, r in zip(list_weights, list_returns):
				expected_return +=(a*r)

			return expected_return	


		else:
			pass




#print(weightedReturn(4,[4,6,10,14]))
#print(weightedReturn([25,25,25,25], [4,6,10,14]))









