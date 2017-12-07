# Functional dependency miner - fd_miner 
The following code allows mining functional dependencies using partition pattern structures

## Installation:
- git clone https://github.com/codocedo/fd_miner.git
- virtualenv venv
- sourve venv/bin/activate
- python -m pip install -r requirements.txt
- python mine_fds.py [dataset]
    - Example: python mine_fds.py diag.txt

## Datasets provided (folder data)
- adult.data.csv
- diag.txt
- xyzw.csv
- forestfires.csv
- digits.csv

## Observations
Mining some datasets may take several minutes or even hours.
