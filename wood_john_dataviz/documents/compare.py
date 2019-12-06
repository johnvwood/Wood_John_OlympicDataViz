import csv
import matplotlib.pyplot as plt

FRA = []
FIN = []
SWE = []

categories = []

with open('compare.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("first row")
			categories.append(row)
			line_count += 1

		else:
			if row[4] == "FRA":
				print("is french")
				FRA.append(row[4])
			elif row[4] == "FIN":
				print("is finnish")
				FIN.append(row[4])
			elif row[4] == "SWE":
				print("is sweden")
				SWE.append(row[4])

			print(line_count)
			line_count += 1

print(len(FRA))
print(len(FIN))
print(len(SWE))

labels = ["FRA", "FIN", "SWE"]
sizes = [len(FRA), len(FIN), len(SWE)]
colors = ['blue', 'lightblue', 'yellow']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, colors=colors, autopct='%1.f%%', shadow=False, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("France, Finland and Sweden Total Medal Distribution")
plt.show()


