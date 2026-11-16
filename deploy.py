import shutil
import sys
from pathlib import Path


destination = Path(sys.argv[1])
destination.mkdir(parents=True, exist_ok=True)
shutil.copy2("app.py", destination / "app.py")
print(f"Deployed app.py to {destination}")
