
class SmokeState:
    def __init__(self):
        self.positions = []
        self.velocities = []
        self.colors = []
        self.radi = []
        self.lives = []
        self.ages = []
        self.inactive_particles = []
        self.inactive_count = 0
        self.default_radius = 2
        self.default_age = 10
        self.default_radius_decrement = 2
        self.alpha_decay = 5
    
    def get_nb(self):
        return len(self.positions) 

    def get_active_nb(self):
        return len(self.positions) - self.inactive_count

    
    def update_state(self, dt):
        for i in range(self.get_nb()):
            if(self.lives[i] == True):
                self.colors[i][3] -= self.alpha_decay * dt
                if(self.colors[i][3] <= 0):
                    self.colors[i][3] = 0
                self.radi[i] += self.default_radius_decrement * dt

                if(self.ages[i] > self.default_age or self.colors[i][3] == 0):
                    self.lives[i] = False
                    self.inactive_particles.append(i)
                    self.inactive_count += 1
    
    
    def add_particle(self, P, V ,C):
        if(self.inactive_count > 0):
            index = self.inactive_particles.pop()
            self.inactive_count -= 1
            self.positions[index]= P
            self.velocities[index]= V
            self.colors[index] =C
            self.lives[index]= True
            self.ages[index] =0
            self.radi[index] = self.default_radius
        else:
            self.positions.append(P)
            self.velocities.append(V)
            self.colors.append(C)
            self.lives.append(True)
            self.ages.append(0)
            self.radi.append(self.default_radius)

