import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronzes = []

categories = []

with open('canadamedals.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("this is the first row")
			categories.append(row)
			line_count += 1

		else:
			if row[7] == "Gold":
				print("won a gold and got the epic dub")
				golds.append(row[7])
			elif row[7] == "Silver":
				print("won a silver medal")
				silvers.append(row[7])
			elif row[7] == "Bronze":
				print("won a bronze")
				bronzes.append(row[7])

			print(line_count)
			line_count += 1

print(len(golds))
print(len(silvers))
print(len(bronzes))

labels = ["Gold", "Silver", "Bronze"]
sizes = [len(golds), len(silvers), len(bronzes)]
colors = ['gold', 'silver', 'darkgoldenrod']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, colors=colors, autopct='%1.f%%', shadow=False, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Canadian Medals 1924-2014")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.show()


