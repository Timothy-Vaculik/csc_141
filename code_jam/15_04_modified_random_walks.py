# Timothy Vaculik
#  Code for plotting random walks
# I think is is difficulty of 9/10


from random import RandomWalk

from random_walk import RandomWalk

while True:
rw = RandomWalk(5000)
rw.fill_walk()


plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))


ax.plot(rw.x_values, rw.y_values, edgecolor='none', s=15,linewidth=1)
ax.set_aspect('equal')

ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], edgecolors='none', s=100)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)



keep_running = input("Make another walk? (y/n): ")
if keep_running == 'n':
    break

    