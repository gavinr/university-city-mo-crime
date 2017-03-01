# University City, MO Crime
Crime info from University City, MO. Original data is [posted in XLSX files](http://www.ucitymo.org/482/Crime-Statistics-by-Region). This repo contains:

1. A [mirror](https://github.com/gavinr/university-city-mo-crime/tree/master/original_data) of that data.
2. [Scripts](https://github.com/gavinr/university-city-mo-crime/tree/master/processor) to process those XLSX files into database tables.
3. The processed data (SQLite database and CSV mirror). *Right now this contains 2015 data only*.

# The Data

* Download: [SQLiteDB](https://github.com/gavinr/university-city-mo-crime/raw/master/data.sqlite) or [CSV](https://github.com/gavinr/university-city-mo-crime/blob/master/data.csv)
* Browse Data: [Browse the SQLite DB](http://inloop.github.io/sqlite-viewer/?url=https://cdn.rawgit.com/gavinr/university-city-mo-crime/master/data.sqlite) (2015 data only)
* Maps: (*coming soon!*)

# Developing

* `pip install geopy`
* `pip install geocoder`
* `pip install sqlite3`
* `pip install openpyxl`

# Thanks

- https://github.com/geopy/geopy
- https://bitbucket.org/openpyxl/openpyxl
