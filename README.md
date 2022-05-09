# SVTagging

SV Tagging for compressed SUSY search.

## Workflow

1. Produce custom NANO AOD from MINI AOD (with extra SV variables)
2. Produce reduced ntuples from NANO AOD (with extra SV variables)
3. Produce efficiency input file (on condor)
4. Create efficiency plot

### Produce Custom NANO AOD

This section describes how to produce custom NANO AOD from MINI AOD.
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

Copy the following working area on CMS LPC:
```
# Working are on cmslpc for producing NANO AOD samples:
# /uscms/home/caleb/nobackup/KU_Compressed_SUSY/SV_Tagging/erichjs/cms_nano/CMSSW_10_2_22/src

mkdir ~/nobackup/SV_Tagging
cd ~/nobackup/SV_Tagging
rsync -az /uscms/home/caleb/nobackup/KU_Compressed_SUSY/SV_Tagging/erichjs/cms_nano/CMSSW_10_2_22 .
```

After setting up a working area, compile it:
```
cd ~/nobackup/SV_Tagging/CMSSW_10_2_22/src
cmsenv
scram b -j8
voms-proxy-init --valid 192:00 -voms cms
```

First, test that the code runs locally, for example:
```
cmsRun SUS-RunIISummer16NanoAODv7-cfg.py
```

If the code works locally, then you can submit to crab, for example:
```
crab submit -c crab-TTJets-DiLept-FullSim-2016.py
```

To check the status of crab jobs:
```
crab status -d <directory>
```

If there are failed jobs, they can be resubmitted like this:
```
crab resubmit -d <directory>
```

<details>
<summary>Crab Submit Script</summary>

You may use this crab submit script... though it should be tested first.
```
python submitTreesLPC.py -c <config> -d <dir> -f <datasets>
```
where `<config>` is a CMS config file, `<dir>` is a directory name for the crab submission, and `<datasets>` is a text file listing full dataset names with one dataset per line.

For example,
```
python submitTreesLPC.py -c SUS-RunIISummer16NanoAODv7-cfg.py -d TTJets-DiLept-FullSim-2016-Test -f Datasets-TTJets-DiLept-FullSim-2016.txt
```

</details>
