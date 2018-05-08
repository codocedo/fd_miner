# Functional Dependency Minimum Cover Miner - fd_miner 

The following code allows mining functional dependencies using partition pattern structures

Implementation used for comparison purposes on:
- Codocedo et al. **"Characterizing Covers of Functional Dependencies using FCA"** on the International Conference on Concept Lattices and their Applications 2018.


## Installation:
- git clone -b cla18 https://github.com/codocedo/fd_miner.git
- virtualenv venv
- sourve venv/bin/activate
- python -m pip install -r requirements.txt
- python mine_fds.py [dataset]
    - Example: python mine_fds.py experimental_datasets/diagnostics.csv

## Datasets Provided (./experimental_datasets/)
- abalone.csv: https://archive.ics.uci.edu/ml/datasets/Abalone
- adult.data.csv: https://archive.ics.uci.edu/ml/datasets/Adult
- caulkins.csv: http://lib.stat.cmu.edu/jasadata/caulkins-p
- cmc.data.csv: https://archive.ics.uci.edu/ml/datasets/Contraceptive+Method+Choice
- credit.data.csv: https://archive.ics.uci.edu/ml/datasets/Credit+Approval
- diagnostics.csv: https://archive.ics.uci.edu/ml/datasets/Acute+Inflammations
- forestfires_2xtuples.csv: https://archive.ics.uci.edu/ml/datasets/Forest+Fires
- forestfires.csv: https://archive.ics.uci.edu/ml/datasets/Forest+Fires
- hughes.original.csv: http://lib.stat.cmu.edu/jasadata/hughes-r
- mushroom.csv: https://archive.ics.uci.edu/ml/datasets/Mushroom
- ncvoter_1001r_19c.csv: https://hpi.de/naumann/projects/repeatability/data-profiling/fds.html
- pglw00_2xattributes.csv: http://lib.stat.cmu.edu/jasadata/pglw00.zip
- pglw00.original.csv: http://lib.stat.cmu.edu/jasadata/pglw00.zip
- servo.original.csv: https://archive.ics.uci.edu/ml/datasets/Servo

## Observations
Mining some datasets may take several minutes or even hours.
