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
    fsrc.write(os.path.join(output_dir, "out_files", ofile_name.replace(".root", "_"+script+".root")+" \n"))
    fsrc.write("output = " + os.path.join(output_dir, "out", ofile_name.replace(".root", "_"+script+".out")+" \n"))
    fsrc.write("error = " + os.path.join(output_dir, "err", ofile_name.replace(".root", "_"+script+".err")+" \n"))
    fsrc.write("log = " + os.path.join(output_dir, "log", ofile_name.replace(".root", "_"+script+".log")+" \n"))
    #fsrc.write('request_memory = 6000\n')
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
    ('isGB' , [
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191241/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191311/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191301/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191250/0000', 
]),
    ('isB' , [
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191241/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191311/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191301/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191250/0000', 
]),
    ('isC' , [
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191241/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191311/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191301/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191250/0000', 
]),
    ('isLight' , [
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191241/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191311/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191301/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191250/0000', 
]),
    ('isMatchOther' , [
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191241/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191311/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191301/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191250/0000', 
]),
    ('isOther' , [
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191241/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromTbar_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191311/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_SingleLeptFromT_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191301/0000',
               '/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/eschmitz/svTuples/deltaR_0p01_fixedother/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/crab_TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/200225_191250/0000', 
]),
])

    regions = [ 
                'b',
              ]
    files_per_job = 10

    background_list = process_the_samples(backgrounds, None, ['makeNtuples/svtree'])

    file_name_base = 'output_{}_regions_'+date+'_{}.root'
  
    working_dir = os.getcwd()

    output_dir = os.path.join(working_dir, 'output_condor_hists_b_0p01_'+date)
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


 
