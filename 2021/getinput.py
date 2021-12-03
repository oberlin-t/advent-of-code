from sys import argv
import requests

script, year, day, cookie = argv

sessionCookie = {"session": cookie }

url = "https://adventofcode.com/{}/day/{}/input".format(year,day)

r = requests.get(url, cookies=sessionCookie)
open('input.txt', 'wb').write(r.content)
