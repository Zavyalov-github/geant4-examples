from geant4_pybind import *

class RunAction(G4UserRunAction):
    
    def __init__(self, file_name):
        super().__init__()
        analysisManager = G4AnalysisManager.Instance()
        print(f'Using {analysisManager.GetType()}')
        analysisManager.CreateNtuple('NTuple', 'Example simple tree')
        analysisManager.CreateNtupleDColumn('EnergyDeposit')
        analysisManager.CreateNtupleDColumn('Momentum')
        analysisManager.CreateNtupleDColumn('StepLength')
        
        self.file_name = file_name
    
    def BeginOfRunAction(self, aRun):
        analysisManager = G4AnalysisManager.Instance()
        analysisManager.OpenFile(self.file_name)

        print(f'### Run {aRun.GetRunID()} start.')
    
    def EndOfRunAction(self, _):
        analysisManager = G4AnalysisManager.Instance()
        analysisManager.Write()
        analysisManager.CloseFile()