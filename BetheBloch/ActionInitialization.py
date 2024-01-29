from geant4_pybind import *

from ParticleGenerator import ParticleGenerator
from RunAction import RunAction

class ActionInitialization(G4VUserActionInitialization):
    
    def __init__(self, app, opts):
        super().__init__()
        self.particle_pdgid = opts.particle_pdgid
        self.tot_energy_MeV = opts.tot_energy_MeV
        self.position_m = opts.position_m
        self.direction = opts.direction
        self.file_name = opts.o
        
        self.app = app

    def Build(self):
        self.ParticleGenerator = ParticleGenerator()
        self.RunAction = RunAction(self.file_name)
        self.ParticleGenerator.particle_pdgid = self.particle_pdgid
        self.ParticleGenerator.tot_energy_MeV = self.tot_energy_MeV
        self.ParticleGenerator.position_m = self.position_m
        self.ParticleGenerator.direction = self.direction
        self.SetUserAction(self.ParticleGenerator)
        self.SetUserAction(self.RunAction)
        