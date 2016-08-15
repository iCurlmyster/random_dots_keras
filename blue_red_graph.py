import matplotlib.pyplot as plt
import csv
import sys

file_name = "./blue_red_sample.csv"
if len(sys.argv) > 1:
	file_name = sys.argv[1]

with open(file_name,newline="") as csvReader:
	f_read= csv.reader(csvReader, delimiter=",")
	br_data = []
	for row in f_read:
		br_data.append(row)


with open("./br_results.txt",newline="") as br_file:
	f_read = csv.reader(br_file)
	predict_data = []
	for row in f_read:
		predict_data.append(row)

b_x = []
b_y = []
r_x = []
r_y = []
m_x = []
m_y = []
y_x = []
y_y = []

total_num = len(predict_data)
sum_num = 0

print("Threshold at 70% for deciding blue or red. Above 70% is blue otherwise red.")
for val in range(len(predict_data)):
	if float(predict_data[val][0]) > 0.70:
		if "blue" in br_data[val][0]:
			b_x.append(br_data[val][1])
			b_y.append(br_data[val][2])
			sum_num += 1
		else:
			m_x.append(br_data[val][1])
			m_y.append(br_data[val][2])
	else:
		if "red" in br_data[val][0]:
			r_x.append(br_data[val][1])
			r_y.append(br_data[val][2])
			sum_num += 1
		else:
			y_x.append(br_data[val][1])
			y_y.append(br_data[val][2])

print("Blue dots: Correctly labeled blue dots.\nRed dots: Correctly labeled red dots.")
print("Magenta dots: Dots that should be labeled red but were identified as blue.")
print("Yellow dots: Dots that should be labeled blue but were identified as red.")

print("\nAccuracy based on threshold at 70%% is: %f\n" % ( ((sum_num/total_num)*100) ) )

plt.plot(b_x, b_y, 'bo')
plt.plot(r_x, r_y, 'ro')
plt.plot(m_x, m_y, 'mo')
plt.plot(y_x, y_y, 'yo')
plt.show()
