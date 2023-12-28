import json
import csv

data_from_csv = []

with open('data_set.txt', 'r') as txt:
	data_from_txt = json.loads(txt.read())

field_names = ['throttle', 'steer']
csvfilestore = open('p227.csv', 'w', newline='')
writer = csv.DictWriter(csvfilestore, fieldnames=field_names)
writer.writeHeader()
csv.writerows(data_from_txt)

with open('p227.csv', 'r') as csv:
	reader = csv.reader(file)

	for row in reader:
		data_from_csv.append(row)

print(data_from_csv)
