import scripts.states as states
import scripts.solvers as solvers
import scripts.particle_emitters as pe
import pygame
class SmokeSim:
    def __init__(self, state, solver):
        self.state = state
        self.solver = solver
        self.run = True
        self.emitters = []

    def add_emitter(self, emitter):
        self.emitters.append(emitter)

    def change_emitter_rate(self, index, rate):
        self.emitters[index].rate = rate

    def get_nb(self):
        return self.state.get_nb()
    
    def get_active_nb(self):
        return self.state.get_active_nb()

    def add_particles(self):
        for e in self.emitters:
            for i in range(e.rate):
                P = pygame.math.Vector2()
                V = pygame.math.Vector2()
                C = []
                e.emit(P, V, C)
                self.state.add_particle(P, V, C)
       

    def update(self, dt):
        self.add_particles()
        self.solver.solve(dt)
        self.state.update_state(dt)

    def draw(self, screen):
        for i in range(self.get_nb()):
            if(self.state.lives[i] == True):
                pygame.draw.circle(screen, self.state.colors[i], self.state.positions[i], self.state.radi[i] )

def create_smoke_sim():
    state = states.SmokeState()
    solver = solvers.SmokeSolver(state)
    return SmokeSim(state, solver)
