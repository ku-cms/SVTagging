# SVTagging

SV Tagging for compressed SUSY search.

### Creating Custom NANO AOD

This section describes how to create custom NANO AOD from MINI AOD.
These commands are specific to submitting crab jobs from CMS LPC.

For bash users, if not already done, add these lines to your `~/.bash_profile`:
```
# CMS environment
source /cvmfs/cms.cern.ch/cmsset_default.sh
# CRAB environment
source /cvmfs/cms.cern.ch/common/crab-setup.sh
```
Then do 
```
source ~/.bash_profile
```

After setting up a working area, compile it:
```
cd <working-area>
cmsenv
scram b -j8
voms-proxy-init --valid 192:00 -voms cms
```

First, test that your code runs locally, for example:
```
cmsRun SUS-RunIISummer16NanoAODv7-cfg.py
```

Submit crab jobs with this script:
```
python submitTreesLPC.py -c <config> -d <dir> -f <datasets>
```
where <config> is a CMS config file, <dir> is a directory name for the crab submission, and <datasets> is a text file listing full dataset names with one dataset per line.

For example,
```
python submitTreesLPC.py -c SUS-RunIISummer16NanoAODv7-cfg.py -d TTJets-DiLept-FullSim-2016-Test -f Datasets-TTJets-DiLept-FullSim-2016.txt
```

