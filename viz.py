import matplotlib.pyplot as plt
import numpy as np
import itertools
from matplotlib import patches
import imageio
from collections import OrderedDict
from matplotlib import cm
colors = cm.get_cmap('tab20')

figure_size=(8,8)

def plot_vec(x, y, c, label, ep = 0.1):
    ax.quiver(0, 0, x, y, angles='xy', color=colors.colors[c], scale_units='xy', scale=1,  width=0.01,)
    ax.annotate(label, (x+2*ep, y+ep))

num = 6
data = list(range(0, num))
pairs = itertools.product(data, repeat=2)
x, y = list(map(list, zip(*pairs)))
pairs = itertools.product(data, repeat=2)
#each equivalence class is a different color
z = [x - y for (x, y) in pairs]

#setting up the plot
plt.figure(figsize=figure_size)
ax = plt.subplot(111)
plt.title("N x N")
plt.ylabel("N")
plt.xlabel("N")
plt.xticks(data)
plt.yticks(data)
plt.scatter(x, y,  c=z, cmap='tab20')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# scatter
plt.savefig('output/NxN.png', bbox_inches='tight')

plt.title("Z: Equivalence classes of N x N")
old_axis = ax.get_xlim(), ax.get_ylim()
#plotting the integers
for i in range(-5, 6, 1):
    x_vals = np.array(ax.get_xlim())
    y_vals = -i + x_vals
    ax.plot(x_vals, y_vals, '--') 
    ax.annotate(str(-i), ((i+5.2)/2,  (num-i-1)/2))

ax.set_xlim(old_axis[0])
ax.set_ylim(old_axis[1])
plt.savefig("output/Zaxis.png", bbox_inches='tight')

plt.title("Arithmetic in Z: 1  + -2 = -1 = 2 - 3")
#too lazy to figure out matplotlib animation
images =[imageio.imread('output/NxN.png')]
vectors = [ (0, 1, 8, '1 = (0, 1)'),
            (2, 0, 14, '-2 = (2, 0)'),
            (2, 1, 12, '1 + -2 = (0+2, 1+0) = -1'),
            (1, 3, 6, '2 = (1, 3)'),
            (0, 3, 4, '3 = (0, 3)'),
            (4, 3, 12, '2-3 = (1+3, 3+0) = -1')]

for i, (_, _, _, title) in enumerate(vectors):
    for j in range(i+1):
        plot_vec(*vectors[j])
    filename = 'output/addition_{}.png'.format(i)
    plt.title(title)
    plt.savefig(filename, bbox_inches='tight')
    images.append(imageio.imread(filename))

#hold result for a bit
images.append(images[-1])
imageio.mimsave('output/additionZ.gif', images, duration=2)  


# now for the rationals
num = 3
data = list(range(-num, num+1))
no_zero = list(data)
no_zero.remove(0)
pairs = itertools.product(data, no_zero)
x, y = list(map(list, zip(*pairs)))
pairs = itertools.product(data,no_zero)
scaled = [6 * x / y for i, (x, y) in enumerate(pairs)]
vals = list(sorted(set(scaled)))
# slow but whatever
z = [vals.index(i) for i in scaled]
print(scaled)
print(z)

plt.figure(figsize=figure_size)
ax = plt.subplot(111)
plt.title("Z x Z \ {0}")
plt.xticks(data)
plt.yticks(no_zero)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_position('center')
# plot dots
plt.scatter(x, y,  c=z, cmap='tab20')
plt.savefig("output/ZxZ.png", bbox_inches='tight')

#plot equivalence classes
old_axis = ax.get_xlim(), ax.get_ylim()
ordered_s, ordered_c = list(OrderedDict.fromkeys(scaled)), [15, 16, 19, 0, 2, 4, 14, 18, 1, 5, 11, 12, 7, 8 , 6]
for (m, c) in zip(ordered_s, ordered_c):
    x_vals = np.array(ax.get_xlim())
    if m == 0:
        plt.plot([0,0], [10,-10], '--', color=colors.colors[10])
    else:
        y_vals = 6/m * x_vals
        print(6/m, c)
        plt.plot(x_vals, y_vals, '--', color=colors.colors[c])

ax.set_xlim(old_axis[0])
ax.set_ylim(old_axis[1])
plt.savefig("output/Qaxis.png", bbox_inches='tight')

#arithmetic
plt.title("Arithmetic in Z:  -3 / 2 = -1 + -(1/2)")
plt.savefig("output/start.png", bbox_inches='tight')

#too lazy to figure out matplotlib animation
images =[imageio.imread('output/start.png')]
vectors = [ (-3, 1, 0, '-3 = (-3, 1)'),
            (2, 1, 18, '2 = (2, 1)'),
            (-3, 2, 2, '-3 / 2  = (-3*1, 1*2)'),
            (-1, 1, 4, '-1 = (-1, 1)'),
            (-2, 1, 1, '-1/2 = (1, -2)'),
            (3, -2, 2, '-1 + -1/2 = (-1*-2 + 1*1, -2*1) = -3/2')]

for i, (_, _, _, title) in enumerate(vectors):
    for j in range(i+1):
        plot_vec(*vectors[j], ep=-0.1)
    filename = 'output/qarithmetic{}.png'.format(i)
    plt.title(title)
    plt.savefig(filename, bbox_inches='tight')
    images.append(imageio.imread(filename))

#hold result for a bit
images.append(images[-1])
imageio.mimsave('output/arithmeticQ.gif', images, duration=2)  
    
### REALS 
#data = data[1:-1]
# plt.figure(figsize=(figure_size[0], 1))
# ax = plt.subplot(111)
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['bottom'].set_position('center')
# ax.get_yaxis().set_visible(False)
# ax.axvspan(min(data), 1, alpha=0.5, color='red')
# plt.title("R: (1)")
# plt.xlabel("Q")
# plt.xticks(data)
# plt.savefig('output/R1.png', bbox_inches='tight')
# plt.figure(figsize=(figure_size[0], 1))
# ax = plt.subplot(111)
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['bottom'].set_position('center')
# ax.get_yaxis().set_visible(False)
# ax.axvspan(min(data), 1.41, alpha=0.5, color='blue')
# plt.title("R: sqrt(2)")
# plt.xticks(data)
# plt.xlabel("Q")
# plt.savefig('output/Rroot2.png', bbox_inches='tight')
# plt.figure(figsize=(figure_size[0], 1))
# ax = plt.subplot(111)
# ax.spines['right'].set_visible(False)
# ax.spines['top'].set_visible(False)
# ax.spines['left'].set_visible(False)
# ax.spines['bottom'].set_position('center')
# ax.get_yaxis().set_visible(False)
# ax.axvspan(-3, 1, alpha=0.60, color='red')
# ax.axvspan(-3, 2.41, alpha=0.40, color='blue')
# plt.title("R: 1 + sqrt(2)")
# plt.xticks(range(-3, 4))
# plt.xlabel("Q")
# plt.savefig('output/Raddition.png', bbox_inches='tight')

