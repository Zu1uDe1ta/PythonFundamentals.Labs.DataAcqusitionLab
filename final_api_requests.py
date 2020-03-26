import json
import urllib.request
import urllib.parse
import requests

file_counter = 39
offset_count = 1
token = "INSERT_TOKEN_HERE"
url_base = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset='
header = {"token": token, 'Content-Type': 'application/json'}

while file_counter <= 1:
	create_file(build_file_name(file_counter),make_request(build_url(url_base,offset_count),header))
	file_counter = file_counter + 1
	offset_count = offset_count + 1000

def url(url_base, offset_count):
	url = url_base + str(offset_count)
	return url

def build_file(file_counter):
	y = ("location_" + str(file_counter))
	return y

def request_response(url , header):
	data = requests.get(url, headers = header)
	return data.json()

def create_file(name, data):
	with open ((name+".json"), 'w') as outfile:
		json.dump(data, outfile)
