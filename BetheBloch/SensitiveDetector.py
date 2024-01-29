from geant4_pybind import *

class SensitiveDetector(G4VSensitiveDetector):

    def __init__(self, name: str):
        super().__init__(name)
        
        self.track_length = 0.
    
    def ProcessHits(self, step, _):
        
        track = step.GetTrack()
        
        depe         = step.GetTotalEnergyDeposit()
        steplength   = step.GetStepLength()
        process_name = step.GetPostStepPoint().GetProcessDefinedStep().GetProcessName()
        energy_kin   = track.GetKineticEnergy()

        analysisManager = G4AnalysisManager.Instance()
        
        self.track_length += steplength/cm
        
        if (track.GetTrackID() == 1 and process_name == "hIoni"):
            analysisManager.FillNtupleDColumn(0, depe/MeV/(steplength/cm))
            analysisManager.FillNtupleDColumn(1, energy_kin/MeV)
            analysisManager.FillNtupleDColumn(2, self.track_length)
            analysisManager.AddNtupleRow()
        
        return True
    
    def EndOfEvent(self, _):
        self.track_length = 0.