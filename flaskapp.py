from flask import Flask, render_template
import os
import csv
import json
app = Flask(__name__,template_folder='static')

@app.route('/')
def plot1():
	directory = os.path.abspath(os.path.join(os.path.split(__file__)[0], ''))
	
	f = open(directory + "/output/test.csv")
	csv_file = csv.reader(f)
	l = []
	current = None
	value = 0
	for row in csv_file :
		d = {}
		if row[0] == current :
			value += int(row[2].replace("\t",""))
		else :
			if current :
				d["x"] = row[0]
				d["y"] = value
				l.append(d)
			current = row[0]
			value += int(row[2].replace("\t",""))
	d["x"] = row[0]
	d["y"] = value
	l.append(d)	
	json_data = json.dumps(l, sort_keys=False)
	return render_template('BarPlot.html',data = json_data)

if __name__ == '__main__':
	app.run()
