def rent_album(album):
	'''(str) -> (str)'''

	renting = """
	Michael Jackson - Dangerous - Released in 1991 ------------ 15.00
	Ray Charles - The Birth of Soul - Released in 1991 -----------15.00
	Lil Wayne - The Carter V - Released in 2017 --------------------20.00
	Eminem - Encore - Released in 2004 ------------------------------20.00
	Akon - Stadium - Released in 2015 ---------------------------------20.00

	Which album do you want to rent?: {}
	""".format(album)
	return renting

def test_rent_album():
	assert rent_album("Dangerous") == """
	Michael Jackson - Dangerous - Released in 1991 ------------ 15.00
	Ray Charles - The Birth of Soul - Released in 1991 -----------15.00
	Lil Wayne - The Carter V - Released in 2017 --------------------20.00
	Eminem - Encore - Released in 2004 ------------------------------20.00
	Akon - Stadium - Released in 2015 ---------------------------------20.00

	Which album do you want to rent?: Dangerous
	"""
	
	assert rent_album("The Birth of Soul") == """
	Michael Jackson - Dangerous - Released in 1991 ------------ 15.00
	Ray Charles - The Birth of Soul - Released in 1991 -----------15.00
	Lil Wayne - The Carter V - Released in 2017 --------------------20.00
	Eminem - Encore - Released in 2004 ------------------------------20.00
	Akon - Stadium - Released in 2015 ---------------------------------20.00

	Which album do you want to rent?: The Birth of Soul
	"""
	assert rent_album("The Carter V") == """
	Michael Jackson - Dangerous - Released in 1991 ------------ 15.00
	Ray Charles - The Birth of Soul - Released in 1991 -----------15.00
	Lil Wayne - The Carter V - Released in 2017 --------------------20.00
	Eminem - Encore - Released in 2004 ------------------------------20.00
	Akon - Stadium - Released in 2015 ---------------------------------20.00

	Which album do you want to rent?: The Carter V
	"""
	assert rent_album("Encore") == """
	Michael Jackson - Dangerous - Released in 1991 ------------ 15.00
	Ray Charles - The Birth of Soul - Released in 1991 -----------15.00
	Lil Wayne - The Carter V - Released in 2017 --------------------20.00
	Eminem - Encore - Released in 2004 ------------------------------20.00
	Akon - Stadium - Released in 2015 ---------------------------------20.00

	Which album do you want to rent?: Encore
	"""
	assert rent_album("Stadium") == """
	Michael Jackson - Dangerous - Released in 1991 ------------ 15.00
	Ray Charles - The Birth of Soul - Released in 1991 -----------15.00
	Lil Wayne - The Carter V - Released in 2017 --------------------20.00
	Eminem - Encore - Released in 2004 ------------------------------20.00
	Akon - Stadium - Released in 2015 ---------------------------------20.00

	Which album do you want to rent?: Stadium
	"""