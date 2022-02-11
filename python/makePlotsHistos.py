# makePlotsHistos.py

import os
import ROOT
import tools

def plot():
    pass

def process(input_file, plot_dir):
    print("Processing {0}".format(input_file))
    
    # check that input file exists
    if not os.path.isfile(input_file):
        print("ERROR: The input file \"{0}\" does not exist.".format(input_file))
        return
    
    open_file = ROOT.TFile.Open(input_file)

    histo_names = ["h_MET_pt", "h_nSV", "h_SV_ntrk", "h_SV_flavor", "h_SV_pt_v1", "h_SV_pt_v2", "h_SV_eta"]

    for h_name in histo_names:
        h = open_file.Get(h_name)

def makePlots():
    print("Go make plots!")
    plot_dir    = "plots-histos"
    input_dir   = "histos-v2"
    info = {
            "FullSim-2016" : {"input" : "Histos-TTJets-DiLept-FullSim-2016-v1.root"},
            "FullSim-2017" : {"input" : "Histos-TTJets-DiLept-FullSim-2017-v1.root"},
            "FullSim-2018" : {"input" : "Histos-TTJets-DiLept-FullSim-2018-v1.root"},
            "FastSim-2016" : {"input" : "Histos-TTJets-DiLept-FastSim-2016-v1.root"},
            "FastSim-2017" : {"input" : "Histos-TTJets-DiLept-FastSim-2017-v1.root"},
            "FastSim-2018" : {"input" : "Histos-TTJets-DiLept-FastSim-2018-v1.root"},
    }
    
    tools.makeDir(plot_dir)
    
    for key in info:
        input_file  = "{0}/{1}".format(input_dir,  info[key]["input"])
        process(input_file, plot_dir)

def main():
    makePlots()

if __name__ == "__main__":
    main()

