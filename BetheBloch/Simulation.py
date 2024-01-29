import configargparse
import sys

from geant4_pybind import *

from DetectorConstruction import DetectorConstruction
from ActionInitialization import ActionInitialization
from PhysicsList import PhysicsList

def parse_arguments():
    
    p = configargparse.get_argument_parser()
    p.add_argument('-n', type=int, default=1, help='')
    p.add_argument('-o', type=str, default='proton_230MeV.csv', help="output file name")
    p.add_argument('--particle_pdgid', type=int, default=2212, help='')
    p.add_argument('--tot_energy_MeV', type=float, default=230, help='')
    p.add_argument('--position_m', nargs=3, type=float, default=[0, 0, 0], help='')
    p.add_argument('--direction', nargs=3, type=float, default=[0, 0, 1], help='')
    p.add_argument('--dimensions', nargs=3, type=float, default=[100, 100, 10000], help='')

    opts = p.parse_args()

    return opts

class Simulation:
    
    def __init__(self, opts):
        self.runManager = G4RunManagerFactory.CreateRunManager(G4RunManagerType.Serial)
        
        self.DetectorConstruction = DetectorConstruction(opts)
        self.PhysicsList = PhysicsList()
        
        self.ActionInitialization = ActionInitialization(self, opts)
        
        self.n_events = opts.n
    
    def configure(self):
        self.runManager.SetUserInitialization(self.DetectorConstruction)
        self.runManager.SetUserInitialization(self.PhysicsList)
        
        self.runManager.SetUserInitialization(self.ActionInitialization)
        UImanager = G4UImanager.GetUIpointer()
        UImanager.ApplyCommand('/process/eLoss/StepFunctionMuHad 0.01 0.001 mm')
        self.runManager.Initialize()
        
        self.runManager.BeamOn(self.n_events)
        
        self.applyGeant4Command('/tracking/verbose', [0])
    
    def applyGeant4Command(self, command, arguments=[]):
        arg_string = ""
        for arg in arguments:
            arg_string += f" {arg}"
        UImanager = G4UImanager.GetUIpointer()
        UImanager.ApplyCommand(command + arg_string)

opts = parse_arguments()

app = Simulation(opts)
app.configure()