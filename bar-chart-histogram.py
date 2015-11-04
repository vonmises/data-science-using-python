from collections import Counter
from matplotlib import pyplot as p

grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
def decile(grade): return grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

# shift each bar to the left by 4, give each bar its height, and a width of 8
p.bar([x - 4 for x in histogram.keys()], histogram.values(), 8)

# x-axis from -5 to 105, y-axis from 0 to 5
p.axis([-5, 105, 0, 5])

# x-axis labels from 0 to 10
p.xticks([i * 10 for i in range(11)])
p.xlabel("Decile")
p.ylabel("# of Students")
p.title("Distribution of Exam 1 Grades")
p.show()