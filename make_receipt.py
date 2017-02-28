def make_receipt(album, artist, price, year, days_renting):
	''' (str, str, float, int, int) --> (str)'''
	# receipt = open('receipt.py', 'a')
	receipt = """\t\tMiTunes Music Rental Shop\

	\t\tAlbum Name......................{}
	\t\tArtist Name.........................{}
	\t\tAlbum Renting Price.........{}
	\t\tYear Released/Releasing.....{}
	\t\tDays Renting.......................{}
	""".format(album, artist, price, year, days_renting)
	return receipt


def test_make_receipt():
	assert make_receipt("Dangerous" , "Michael Jackson", "15.00", "1991", "6")  ==  """\t\tMiTunes Music Rental Shop\

	\t\tAlbum Name......................Dangerous
	\t\tArtist Name.........................Michael Jackson
	\t\tAlbum Renting Price.........15.00
	\t\tYear Released/Releasing.....1991
	\t\tDays Renting.......................6
	"""
	assert make_receipt("The Birth of Soul" , "Ray Charles", "15.00", "1991", "6")  == """\t\tMiTunes Music Rental Shop\

	\t\tAlbum Name......................The Birth of Soul
	\t\tArtist Name.........................Ray Charles
	\t\tAlbum Renting Price.........15.00
	\t\tYear Released/Releasing.....1991
	\t\tDays Renting.......................6
	"""
	assert make_receipt("Encore" , "Eminem", "20.00", "2004", "6")  == """\t\tMiTunes Music Rental Shop\

	\t\tAlbum Name......................Encore
	\t\tArtist Name.........................Eminem
	\t\tAlbum Renting Price.........20.00
	\t\tYear Released/Releasing.....2004
	\t\tDays Renting.......................6
	"""
	assert make_receipt("The Carter V" , "Lil Wayne", "20.00", "2017", "6")  == """\t\tMiTunes Music Rental Shop\

	\t\tAlbum Name......................The Carter V
	\t\tArtist Name.........................Lil Wayne
	\t\tAlbum Renting Price.........20.00
	\t\tYear Released/Releasing.....2017
	\t\tDays Renting.......................6
	"""
	assert make_receipt("Stadium" , "Akon", "20.00", "2015", "6")  == """\t\tMiTunes Music Rental Shop\

	\t\tAlbum Name......................Stadium
	\t\tArtist Name.........................Akon
	\t\tAlbum Renting Price.........20.00
	\t\tYear Released/Releasing.....2015
	\t\tDays Renting.......................6
	"""

