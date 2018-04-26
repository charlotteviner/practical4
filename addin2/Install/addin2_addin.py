import arcpy
import pythonaddins

class RiskButton(object):
    """Implementation for addin2_addin.riskbutton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog("M:/Programming/practical1/albertsurface/Models.tbx", "TraffordModelScript")