import numpy as np

from geant4_pybind import *

class ParticleGenerator(G4VUserPrimaryGeneratorAction):
    
    def __init__(self):
        super().__init__()
        self.ParticleGun = G4ParticleGun(1)
        
        self._particle_pdgid: int = 1
        self._tot_energy_MeV: float = 1.
        self._position_m: np.array = np.empty(shape=(0),dtype=float)
        self._direction: np.array = np.empty(shape=(0),dtype=float)
        
    @property
    def particle_pdgid(self):
        return self._particle_pdgid
        
    @particle_pdgid.setter
    def particle_pdgid(self, new_particle_pdgid: int):
        self._particle_pdgid = new_particle_pdgid
    
    @property
    def tot_energy_MeV(self):
        return self._tot_energy_MeV
        
    @tot_energy_MeV.setter
    def tot_energy_MeV(self, new_tot_energy_MeV: float):
        self._tot_energy_MeV = new_tot_energy_MeV
    
    @property
    def position_m(self):
        return self._position_m
        
    @position_m.setter
    def position_m(self, new_position_m: np.array):
        self._position_m = new_position_m
    
    @property
    def direction(self):
        return self._direction
        
    @direction.setter
    def direction(self, new_direction: np.array):
        self._direction = new_direction

    def GeneratePrimaries(self, anEvent):
        # default particle kinematic
        particleTable = G4ParticleTable.GetParticleTable()
        particle = particleTable.FindParticle(int(self.particle_pdgid))
        self.ParticleGun.SetParticleDefinition(particle)
        self.ParticleGun.SetParticlePosition(G4ThreeVector(*self.position_m))
        self.ParticleGun.SetParticleMomentumDirection(G4ThreeVector(*self.direction))
#        self.ParticleGun.SetParticleMomentum(self.tot_energy_MeV*MeV)
        self.ParticleGun.SetParticleEnergy(self.tot_energy_MeV*MeV)
        # This function is called at the begining of event
        self.ParticleGun.GeneratePrimaryVertex(anEvent)