# University City, MO Crime
Crime info from University City, MO. Original data is [posted in XLSX files](http://www.ucitymo.org/482/Crime-Statistics-by-Region). This repo contains:
1. A mirror of that data.
2. Scripts to process those XLSX files into database tables.
3. The processed data (sqlite db and CSV). *Right now this contains 2015 data only*.

# Developing

* `pip install geocoder`
* `pip install sqlite3`
* `pip install openpyxl`

# Thanks

- https://github.com/geopy/geopy
- https://bitbucket.org/openpyxl/openpyxl