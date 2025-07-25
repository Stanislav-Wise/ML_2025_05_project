python3 -m venv .venv

source ./.venv/bin/activate
deactivate

pip install -r requirements.txt


import pandas as pd
print(pd.__version__)