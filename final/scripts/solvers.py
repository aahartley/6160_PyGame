import pygame
class SmokeSolver:
    def __init__(self, state):
        self.state = state
        self.forces = []
        self.total_force = pygame.math.Vector2(0,0)

    def add_Force(self, f):
        self.forces.append(f)    
    
    def solve(self, dt):
        for f in self.forces:
            self.total_force += f
        for i in range(self.state.get_nb()):
            if self.state.lives[i] == True:
                self.state.velocities[i] += self.total_force * dt
                self.state.positions[i] += self.state.velocities[i] * dt
                self.state.ages[i] += dt
        

