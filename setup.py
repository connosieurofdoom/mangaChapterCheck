import subprocess
import sys
def setup():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], stdout=subprocess.DEVNULL)
    except Exception as e:
        print(e)
    return True