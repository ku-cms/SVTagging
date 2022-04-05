#!/bin/bash

# setup env

export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh

source cmssw_setup_connect.sh

cmssw_setup sandbox-CMSSW_10_6_5-6403d6f.tar.bz2

cd cmssw-tmp/CMSSW_10_6_5/src/
eval `scramv1 runtime -sh`
cd -

echo "arg 1: $1"
echo "arg 2: $2"
echo "python make_b_eff_hists_batch.py --file_list $1 --out_file $2"

python make_b_eff_hists_batch.py --file_list $1 --out_file $2

