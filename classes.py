import pygame, random, math
import globalvars

class Force():
    def __init__(self, initial, direction, magnitude, color):
        self._initial = initial
        self._direction = math.radians(direction)
        self._magnitude = magnitude
        self.color = color

    def __repr__(self):
        return "Force:\n- Initial point: %s\n- Terminal point: %s\n- Direction: %s\n- Magnitude: %s\n" % (self.initial, self.terminal, self.direction, self.magnitude)

    # property functions
    @property
    def initial(self):
        return self._initial
    @initial.setter
    def initial(self, val):
        self._initial = val

    @property
    def direction(self):
        return math.degrees(self._direction)
    @direction.setter
    def direction(self, val):
        self._direction = math.radians(val)

    @property
    def magnitude(self):
        return self._magnitude
    @magnitude.setter
    def magnitude(self, val):
        if val <= 0:
            raise ValueError("A Force's magnitude must be greater than 0!")
        else:
            self._magnitude = val

    @property
    def terminal(self):
        x = self._initial[0] + math.cos(self._direction) * self._magnitude
        y = self._initial[1] + math.sin(self._direction) * self._magnitude
        return int(round(x)), int(round(y))
    @terminal.setter
    def terminal(self, val):
        if val == self._initial:
            # raise ValueError("A Force's terminal point cannot be equal to its initial point!")
            self._direction = 0
            self._magnitude = 0
        else:
            x = val[0] - self._initial[0]
            y = val[1] - self._initial[1]
            self._direction = math.atan2(y, x)
            self._magnitude = math.hypot(x, y)

    @property
    def width(self):
        return self.terminal[0] - self.initial[0]
    @property
    def height(self):
        return self.terminal[1] - self.initial[1]

    @property
    def initial_d(self):
        x = self._initial[0]
        y = globalvars.screensize[1] - self._initial[1]
        return (x, y)

    @property
    def terminal_d(self):
        pos = self.terminal
        x = pos[0]
        y = globalvars.screensize[1] - pos[1]
        return (x, y)

    # static methods
    @staticmethod
    def addforces(force1, force2):
        color = (255, 0, 255)
        if force1.initial != force2.initial:
            raise ValueError("Cannot add forces that don't have the same initial point!")
        else:
            endx = force1.terminal[0] + force2.width
            endy = force1.terminal[1] + force2.height
            f = Force(force1.initial, 45, 1, color)
            f.terminal = (endx, endy)
            return f

    # member functions
    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.initial_d, self.terminal_d)
        pygame.draw.circle(screen, self.color, self.terminal_d, 5)
