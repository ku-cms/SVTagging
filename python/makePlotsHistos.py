# makePlotsHistos.py

import os
import ROOT
import tools

def plot(input_dir, plot_dir, input_files, eras, mc_type, variable, h_name):
    print("Plotting {0} - {1}".format(variable, mc_type))

    # WARNING: must keep TFile open to use histograms; histograms are destroyed when TFile is closed
    open_files  = {}
    histos      = {}
    
    print("first loop")
    for era in eras:
        key         = "{0}-{1}".format(mc_type, era)
        input_file  = "{0}/{1}".format(input_dir, input_files[key])
        
        # check that input file exists
        if not os.path.isfile(input_file):
            print("ERROR: The input file \"{0}\" does not exist.".format(input_file))
            return
        
        open_files[era] = ROOT.TFile.Open(input_file)
        histos[era]     = open_files[era].Get(h_name)
        print("era: {0}, h: {1}".format(era, histos[era]))
    
    print("second loop")
    for era in eras:
        print("era: {0}, h: {1}".format(era, histos[era]))

def process(input_dir, plot_dir, variable, h_name):
    eras        = ["2016", "2017", "2018"]
    mc_types    = ["FullSim", "FastSim"]
    
    input_files = {
            "FullSim-2016" : "Histos-TTJets-DiLept-FullSim-2016-v1.root",
            "FullSim-2017" : "Histos-TTJets-DiLept-FullSim-2017-v1.root",
            "FullSim-2018" : "Histos-TTJets-DiLept-FullSim-2018-v1.root",
            "FastSim-2016" : "Histos-TTJets-DiLept-FastSim-2016-v1.root",
            "FastSim-2017" : "Histos-TTJets-DiLept-FastSim-2017-v1.root",
            "FastSim-2018" : "Histos-TTJets-DiLept-FastSim-2018-v1.root",
    }
    
    for mc_type in mc_types:
        plot(input_dir, plot_dir, input_files, eras, mc_type, variable, h_name)

def makePlots():
    print("Go make plots!")
    plot_dir    = "plots-histos"
    input_dir   = "histos-v2"
    histos = {
        "MET_pt"    : "h_MET_pt",
        "nSV"       : "h_nSV",
        "SV_ntrk"   : "h_SV_ntrk",
        "SV_flavor" : "h_SV_flavor",
        "SV_pt_v1"  : "h_SV_pt_v1",
        "SV_pt_v2"  : "h_SV_pt_v2",
        "SV_eta"    : "h_SV_eta",
    }
    
    tools.makeDir(plot_dir)

    for key in histos:
        process(input_dir, plot_dir, key, histos[key])
    
def main():
    makePlots()

if __name__ == "__main__":
    main()

