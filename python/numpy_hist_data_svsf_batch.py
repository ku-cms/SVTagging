from time import strftime, localtime
import argparse as arg
import os, re
from file_table_functions import *
import ROOT as rt
import numpy as np
import root_numpy as rnp
from collections import OrderedDict
import pickle

date = strftime('%d%b%y', localtime())


def write_sub(output_dir, src_file, script, file_list, ofile_name, queue_num):
    fsrc = open(os.path.join(output_dir, "submit", src_file+'_'+script+'.submit'), 'w')
    fsrc.write("universe = vanilla \n")
    fsrc.write("executable = " + os.path.join(output_dir, "exe", "run_"+script+"_python_on_condor.sh")+" \n")
    fsrc.write("input = file_table_functions.py\n")
    fsrc.write("getenv = True \n")
    fsrc.write("Arguments = ");
    fsrc.write(os.path.join(output_dir, "file_lists", file_list+"_$(Process).pkl") + " ")
    fsrc.write(os.path.join(output_dir, "out_files", script, ofile_name.replace(".root", "_"+script+".root")+" \n"))
    fsrc.write("output = " + os.path.join(output_dir, "out", ofile_name.replace(".root", "_"+script+".out")+" \n"))
    fsrc.write("error = " + os.path.join(output_dir, "err", ofile_name.replace(".root", "_"+script+".err")+" \n"))
    fsrc.write("log = " + os.path.join(output_dir, "log", ofile_name.replace(".root", "_"+script+".log")+" \n"))
    fsrc.write('request_memory = 10000\n')
    fsrc.write("Requirements = (Machine != \"red-node000.unl.edu\")\n")
    fsrc.write("queue "+ str(queue_num) + " \n")
    #fsrc.write("cd "+RUN_DIR+" \n")
    #fsrc.write("source ../RestFrames/setup_RestFrames.sh \n")
    fsrc.close()

def write_sh(work_dir, out_dir, script):
    script_template = '''#!/bin/bash

workdir=WORKDIR
rundir=$(pwd)

cd ${workdir}
eval `scramv1 runtime -sh`
cd ${rundir}

python ${workdir}/make_SCRIPT_hists_batch.py --file_list $1 --out_file $2
'''
    out_script = re.sub('WORKDIR', work_dir, script_template)
    out_script = re.sub('SCRIPT', script, out_script)

    with open(os.path.join(out_dir, 'exe', 'run_'+script+'_python_on_condor.sh'), 'w') as f:
        f.write(out_script)
    os.system('chmod a+x ' + os.path.join(out_dir, 'exe', 'run_'+script+'_python_on_condor.sh'))



if __name__ == "__main__":
    backgrounds = OrderedDict([ 
#    ('data_muoneg'   , [
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MuonEG_SVSF/MuonEG_Run2017B-02Apr2020-v1_2017_Fall17_102X',
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MuonEG_SVSF/MuonEG_Run2017C-02Apr2020-v1_2017_Fall17_102X',
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MuonEG_SVSF/MuonEG_Run2017D-02Apr2020-v1_2017_Fall17_102X',
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MuonEG_SVSF/MuonEG_Run2017E-02Apr2020-v1_2017_Fall17_102X',
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MuonEG_SVSF/MuonEG_Run2017F-02Apr2020-v1_2017_Fall17_102X',
#                    ]),
#    ('data_met'   , [
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MET/MET_Run2017B-02Apr2020-v1_2017_Fall17_102X',
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MET/MET_Run2017C-02Apr2020-v1_2017_Fall17_102X',
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MET/MET_Run2017D-02Apr2020-v1_2017_Fall17_102X',
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MET/MET_Run2017E-02Apr2020-v1_2017_Fall17_102X',
#                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_Data_MET/MET_Run2017F-02Apr2020-v1_2017_Fall17_102X',
#                    ]),
    ('Tot2017' , [
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-100To200_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-200To400_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-400To600_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-600To800_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-800To1200_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Nu_13TeV_powheg_pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo4L_13TeV_powheg_pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WZ_TuneCP5_13TeV-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWG_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Fall17_102X',
]),
##    ('Tot2017_isB' , [
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-100To200_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-200To400_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-400To600_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-600To800_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-800To1200_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Nu_13TeV_powheg_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo4L_13TeV_powheg_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WZ_TuneCP5_13TeV-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWG_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Fall17_102X',
##]),
##    ('Tot2017_isC' , [
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-100To200_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-200To400_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-400To600_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-600To800_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-800To1200_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Nu_13TeV_powheg_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo4L_13TeV_powheg_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WZ_TuneCP5_13TeV-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWG_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Fall17_102X',
##]),
##    ('Tot2017_isLight' , [
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-100To200_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-200To400_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-400To600_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-600To800_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-800To1200_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Nu_13TeV_powheg_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo4L_13TeV_powheg_pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WZ_TuneCP5_13TeV-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWG_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
##                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Fall17_102X',
##]),
    ('TTJets2017' , [
#                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
#                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTTT_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
]),
    ('TTV2017' , [
                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8_Fall17_102X',
                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
                     '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
]),
    ('WJets2017' , [
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
]),
    ('VV2017', [ 
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWTo4Q_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Nu_13TeV_powheg_pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo2Q2Nu_TuneCP5_13TeV_amcatnloFXFX_madspin_pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZTo4L_13TeV_powheg_pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WZ_TuneCP5_13TeV-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWG_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
]),
    ('ST2017', [
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_hadronicDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_antitop_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_t-channel_top_4f_inclusiveDecays_TuneCP5_13TeV-powhegV2-madspin-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_top_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8_Fall17_102X',
]),
    ('ZDY2017' , [
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-100to200_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-4to50_HT-600toInf_TuneCP5_13TeV-madgraphMLM-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-100To200_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-200To400_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-400To600_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-600To800_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-800To1200_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-1200To2500_13TeV-madgraph_Fall17_102X',
                    '/home/t3-ku/erichjs/work/Ewkinos/NTUPLES/Fall17_102X_SVSF/ZJetsToNuNu_HT-2500ToInf_13TeV-madgraph_Fall17_102X',
])
])

    #regions = [
    #            # 'b_eff', 
    #            # 'sv',
    #            # 'sv_forward',
    #            # 'sv_central',
    #]
    
    #regions = ['b_eff']
    regions = ['sv']
    
    files_per_job = 50

    background_list = process_the_samples(backgrounds, None, None)
    #signal_list = process_the_samples(signals, None, None)

    file_name_base = 'output_{}_regions_'+date+'_{}.root'
  
    working_dir = os.getcwd()

    #output_dir = os.path.join(working_dir, 'output_condor_hists_b_eff_2D_proposal_'+date)
    output_dir = os.path.join(working_dir, 'output_condor_hists_sv_2D_proposal_'+date)
    
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
        os.mkdir(os.path.join(output_dir, 'out'))
        os.mkdir(os.path.join(output_dir, 'err'))
        os.mkdir(os.path.join(output_dir, 'log'))
        os.mkdir(os.path.join(output_dir, 'out_files'))
        os.mkdir(os.path.join(output_dir, 'file_lists'))
        os.mkdir(os.path.join(output_dir, 'submit'))
        os.mkdir(os.path.join(output_dir, 'exe'))
    for r in regions:
        if not os.path.isdir(os.path.join(output_dir, 'out_files', r)):
            os.mkdir(os.path.join(output_dir, 'out_files', r))

    for r in regions:
        write_sh(working_dir, output_dir, r)

    list_of_bkg_files = OrderedDict()
    for sample in background_list:
        list_of_bkg_files[sample] = []
        tmp_list = background_list[sample]['files']

        for i in xrange(0, len(tmp_list), files_per_job):
            list_of_bkg_files[sample].append(tmp_list[i:i+files_per_job])
        #if 'data' in sample: list_of_bkg_files[sample].append(tmp_list)
    
    for sample in list_of_bkg_files:
        submit_list = OrderedDict()
        submit_list[sample] = OrderedDict()
        submit_list[sample]['trees'] = background_list[sample]['trees']
        submit_list[sample]['files'] = None

        src_file = 'hists_{}'.format(sample)
        file_list = '{}_files'.format(sample)

        submit_name = file_name_base.format('background_'+sample, '$(Process)')

        queue_num = len(list_of_bkg_files[sample])

        for r in regions:
            write_sub(output_dir, src_file, r, file_list, submit_name, queue_num)

        for i_set, file_set in enumerate(list_of_bkg_files[sample]):
            submit_list[sample]['files'] = file_set

            with open(os.path.join(output_dir, "file_lists", file_list+"_"+str(i_set)+".pkl"), "wb") as f:
                pickle.dump(submit_list, f)
                f.close()


