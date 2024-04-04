"""  Convenience file to easily get the full path of the project. """

import sys
from pathlib import Path

# Find module path
module_path = Path(__file__).parent
for _ in range(9):
    init = module_path / '.gitignore'
    if not init.exists():
        module_path = module_path.parent
    else:
        break

if module_path not in sys.path:
    sys.path.append(str(module_path))

