import csv
import matplotlib.pyplot as plt

Men = []
Women = []

categories = []

with open('gender.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("first row")
			categories.append(row)
			line_count += 1

		else:
			if row[5] == "Men":
				print("is a man")
				Men.append(row[5])
			elif row[5] == "Women":
				print("is a woman")
				Women.append(row[5])

			print(line_count)
			line_count += 1

print(len(Men))
print(len(Women))

labels = ["Men", "Women"]
sizes = [len(Men), len(Women)]
colors = ['lightblue', 'pink']
explode = (0.1, 0.1, 0.1)

plt.pie(sizes, colors=colors, autopct='%1.f%%', shadow=False, startangle=140)

plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Medal Gender Distribution (Italy)")
plt.show()


