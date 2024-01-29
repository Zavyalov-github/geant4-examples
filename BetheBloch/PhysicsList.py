from geant4_pybind import *

class PhysicsList(G4VModularPhysicsList):

    def __init__(self):
        super().__init__()
    
        self.RegisterPhysics(G4EmStandardPhysics())
        stepLimitPhys = G4StepLimiterPhysics()
        stepLimitPhys.SetApplyToAll(True)
        self.RegisterPhysics(stepLimitPhys)