import subprocess
import os


def Main():
    CurrentDir = os.path.dirname(os.path.abspath(__file__))
    PyCacheDir = os.path.join(CurrentDir, "__pycache__")

    if os.path.exists(PyCacheDir):
        subprocess.run(["attrib", "+h", PyCacheDir], shell=True)

if __name__ == "__main__":
    Main()