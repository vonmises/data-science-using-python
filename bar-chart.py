from matplotlib import pyplot as p

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
number_of_oscars = [5, 11, 3, 8, 10]

# bars are, by default, width 0.8, so we'll add 0.1 to the left co-ordinates
# so that each bar is centred.
x = [i + 0.1 for i, _ in enumerate(movies)]

# plot bars with left co-ordinates [x], heights [number_of_oscars]
p.bar(x, number_of_oscars)

p.ylabel("Number of Academy Awards")
p.title("My Favourite Movies")

# label x-axis with movie names at bar centres
p.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)

p.show()