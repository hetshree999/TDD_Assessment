class Craft:
    def __init__(self, initial_position, initial_direction):
        self.position = initial_position
        self.direction = initial_direction

    def move_forward(self):
        if(self.direction == 'N'):
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif(self.direction == 'S'):
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif(self.direction == 'E'):
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif(self.direction == 'W'):
            self.position = (self.position[0] - 1, self.position[1], self.position[2])

    def move_backward(self):
        if self.direction == 'N':
            self.position = (self.position[0], self.position[1] - 1, self.position[2])
        elif self.direction == 'S':
            self.position = (self.position[0], self.position[1] + 1, self.position[2])
        elif self.direction == 'E':
            self.position = (self.position[0] - 1, self.position[1], self.position[2])
        elif self.direction == 'W':
            self.position = (self.position[0] + 1, self.position[1], self.position[2])
        elif self.direction == 'U':
            self.position = (self.position[0], self.position[1], self.position[2]-1)
        elif self.direction == 'D':
            self.position = (self.position[0], self.position[1], self.position[2]+1)

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'U':
            self.direction = 'W'
        elif self.direction == 'D':
            self.direction = 'R'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'
        
    def turn_up(self):
        if self.direction in ('N', 'S', 'E', 'W'):
            self.direction = 'U'
        
    def turn_down(self):
        if self.direction in ('N', 'S', 'E', 'W'):
            self.direction = 'D'

def execute_commands(starting_position, initial_direction, commands):
    craft = Craft(starting_position, initial_direction)
    for command in commands:
        # if (command != 'f' or command != 'r' or command != 'b' or command != 'l' or command != 'u' or command != 'd' ):
        #     exit("Not possible")
        if command == 'f':
            craft.move_forward()
        elif command == 'b':
            craft.move_backward()
        elif command == 'l':
            craft.turn_left()
        elif command == 'r':
            craft.turn_right()
        elif command == 'u':
            craft.turn_up()
        elif command == 'd':
            craft.turn_down()
        else:
            exit("Not possible")
    return craft.position, craft.direction