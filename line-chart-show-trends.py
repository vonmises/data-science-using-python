from matplotlib import pyplot as p

variance = [2**x for x in range(9)] 
bias_squared = variance[::-1] # reverse the variance

total_error = [x+y for x, y in zip(variance, bias_squared)]
x = [i for i, _ in enumerate(variance)]

# we can make multiple calls to pyplot.plot to show multiple
# series on the same chart
p.plot(x, variance,     "g-",  label="variance")   # green dashed line
p.plot(x, bias_squared, "r-.", label="bias\u00B2") # red dot-dashed line
p.plot(x, total_error,  "b:",  label="total error")# blue dotted line

# because we've assigned labels to each series, a legend is also included
# loc=9 centers the legend
p.legend(loc=9)
p.xlabel("model complexity")
p.title("The Bias-Variance Tradeoff")
p.show()