"""
with help from: http://tillbergmann.com/blog/python-gradient-descent.html
"""


def simple_function(x_list):
    y_res = []
    for i in range(0, len(x_list)):
        y_res.append(- (x_list[i] ** 2 - 6 * x_list[i] + 5))
    return y_res


def f_derivative(arg):
    return 2 * arg - 6


def gradient_ascent(x_list):
    # algorithm 1
    alpha = 0.00001
    precision = 0.000000001
    old_x_max = 0
    x_max = min(x_list)
    maxs = []
    loss = []

    while abs(x_max - old_x_max) > precision:
        old_x_max = x_max
        gradient = f_derivative(old_x_max)
        move = gradient * alpha
        x_max = old_x_max - move
        loss.append((3 - x_max) ** 2)
        maxs.append(x_max)
    return max(maxs)


x = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
y = simple_function(x)

# plt.plot(x, y, linewidth=2)
# plt.show()

print(gradient_ascent(x))
print(simple_function([2.5, 2.99, 2.995, 2.995001677, 2.99950, 3, 4]))
