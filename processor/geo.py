import geocoder
import sqlite3

def findAddress(conn, address, city, state):
	# first look up in the cache
	c = conn.cursor()
	addressString = address + ", " + city + ", " + state
	print("\n" + addressString)
	t = (addressString,)
	c.execute('SELECT * FROM addressCache WHERE address=?', t)
	cacheHit = c.fetchone()

	if(cacheHit):
		print('CACHE HIT')
		return [cacheHit[1], cacheHit[2]]
	else:
		# no cache hit, do the geocode.
		print('GEOCODING')
		g = geocoder.google(address + ", " + city + ", " + state)
		conn.execute('INSERT INTO addressCache VALUES (?,?,?,?)', (addressString, g.json['lat'], g.json['lng'], None))
		conn.commit()
		return [g.json['lat'], g.json['lng']]
