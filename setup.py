from distutils.core import setup
import py2exe
from glob import glob

data_filess = [("button.png", "buttonPressed.png", "buttonSquarePressed.png", "panel.png", "panelInset_brown.png", "victoria.wav")]
setup(
    console=[{
        "data_files":data_filess,
        "script": "p.py"
    }]
)