# Timothy Vaculik
#  Code for plotting random walks
# I think is is difficulty of 9/10


from random import choice


class RandomWalk:
    """A class to generate random walks"""
    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def more_step(self):
        """Determine the distance and direction of one step."""
        distance = choice([1, -1])
        direction = choice([0, 1, 2, 3])
        return distance * direction

    def fill_walk(self):
        """Calculate points for the random walk."""
        while len(self.x_values) < self.num_points:

            x_step = self.more_step()
            y_step = self.more_step()

            if x_step == 0 and y_step == 0:
                continue

            (self.x_values[-1] + x_step)
            (self.y_values[-1] + y_step)

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)





    