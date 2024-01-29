import numpy as np

from geant4_pybind import *

from SensitiveDetector import SensitiveDetector

class DetectorConstruction(G4VUserDetectorConstruction):

    def __init__(self, opts):
        super().__init__()
        
        self._dimensions = np.empty(shape=(0),dtype=float)
        
        self.dimensions = opts.dimensions
        
        self.DefineMaterials()

    def DefineMaterials(self):
        man = G4NistManager.Instance()
        elH  = man.FindOrBuildElement("H", False)
        elO  = man.FindOrBuildElement("O", False)
        
        nelements = 2
        self.matWater = G4Material("Water", 1.0*g/cm3, nelements, kStateLiquid)
        self.matWater.AddElement(elH, 2)
        self.matWater.AddElement(elO, 1)
    
    @property
    def dimensions(self):
        return self._dimensions
        
    @dimensions.setter
    def dimensions(self, new_dimensions: np.array):
        self._dimensions = new_dimensions

    def Construct(self):
    
        matManager = G4NistManager.Instance()
        matWater = matManager.FindOrBuildMaterial("Water")
        
        solidWorld = G4Box("solidWorld", pX=self._dimensions[0], pY=self._dimensions[1], pZ=self._dimensions[2])
        logicWorld = G4LogicalVolume(solidWorld, matWater, "logicWorld")
        physWorld  = G4PVPlacement(None, G4ThreeVector(0.,0.,0.), logicWorld,"physWorld", None, False, 0, True)
  
        return physWorld
    
    def ConstructSDandField(self) -> None:
        SDman = G4SDManager.GetSDMpointer()
        sd = SensitiveDetector('SensitiveDetector')
        self.SetSensitiveDetector("logicWorld", sd, True)
        SDman.AddNewDetector(sd)