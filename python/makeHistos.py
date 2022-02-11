# makeHistos.py

import numpy as np
import os
import ROOT
import tools

# Make sure ROOT.TFile.Open(fileURL) does not seg fault when $ is in sys.argv (e.g. $ passed in as argument)
ROOT.PyConfig.IgnoreCommandLineOptions = True
# Make plots faster without displaying them
ROOT.gROOT.SetBatch(ROOT.kTRUE)
# Tell ROOT not to be in charge of memory, fix issue of histograms being deleted when ROOT file is closed:
ROOT.TH1.AddDirectory(False)

def process(input_file, output_file):
    print("Processing {0} to create {1}".format(input_file, output_file))
    
    # check that input file exists
    if not os.path.isfile(input_file):
        print("ERROR: The input file \"{0}\" does not exist.".format(input_file))
        return

    # histos
    h_MET_pt    = ROOT.TH1F("h_MET_pt",     "h_MET_pt",     10, 0, 500)
    h_nSV       = ROOT.TH1F("h_nSV",        "h_nSV",        10, 0, 10)
    h_SV_ntrk   = ROOT.TH1F("h_SV_ntrk",    "h_SV_ntrk",    15, 0, 15)
    h_SV_flavor = ROOT.TH1F("h_SV_flavor",  "h_SV_flavor",  6,  1, 7)
    h_SV_pt_v1  = ROOT.TH1F("h_SV_pt_v1",   "h_SV_pt_v1",   20, 0, 100)
    h_SV_pt_v2  = ROOT.TH1F("h_SV_pt_v2",   "h_SV_pt_v2",   18, 2, 20)
    h_SV_eta    = ROOT.TH1F("h_SV_eta",     "h_SV_eta",     20, -np.pi, np.pi)
    
    # See python examples in https://github.com/alexpearce/Ntuple
    max_event   = -1
    tree_name   = "Events"
    chain = ROOT.TChain(tree_name)
    chain.Add(input_file)
    entries = chain.GetEntries()
    
    print("entries: {0}, max_event: {1}".format(entries, max_event))
    
    for entry in range(entries):
        # skip if max event is >= 0
        if max_event >= 0:
            if entry >= max_event:
                break
        if entry % 1000 == 0:
            print("Processing entry {0}".format(entry))
        
        chain.GetEntry(entry)
        
        SV_ntrk_list    = [x for x in chain.SV_ntrk]
        SV_flavor_list  = [x for x in chain.SV_flavor]
        SV_pt_list      = [x for x in chain.SV_pt]
        SV_eta_list     = [x for x in chain.SV_eta]
        
        #print("{0}: MET_pt = {1:.3f}, nSV = {2}, SV_pt = {3}".format(entry, chain.MET_pt, chain.nSV, SV_pt_list))
        
        # Fill histos
        h_MET_pt.Fill(chain.MET_pt)
        h_nSV.Fill(chain.nSV)
        for sv in range(chain.nSV):
            h_SV_ntrk.Fill(SV_ntrk_list[sv])
            h_SV_flavor.Fill(SV_flavor_list[sv])
            h_SV_pt_v1.Fill(SV_pt_list[sv])
            h_SV_pt_v2.Fill(SV_pt_list[sv])
            h_SV_eta.Fill(SV_eta_list[sv])

    # save histos to output file
    file_out = ROOT.TFile(output_file, "RECREATE")
    h_MET_pt.Write()
    h_nSV.Write()
    h_SV_ntrk.Write()
    h_SV_flavor.Write()
    h_SV_pt_v1.Write()
    h_SV_pt_v2.Write()
    h_SV_eta.Write()
    file_out.Close()

def makeHistos():
    print("Go make histos!")
    input_dir   = "data"
    output_dir  = "histos-v2"
    info = {
            "FullSim-2016" : {"input" : "TTJets-DiLept-FullSim-2016-v1.root", "output" : "Histos-TTJets-DiLept-FullSim-2016-v1.root"},
            "FullSim-2017" : {"input" : "TTJets-DiLept-FullSim-2017-v1.root", "output" : "Histos-TTJets-DiLept-FullSim-2017-v1.root"},
            "FullSim-2018" : {"input" : "TTJets-DiLept-FullSim-2018-v1.root", "output" : "Histos-TTJets-DiLept-FullSim-2018-v1.root"},
            "FastSim-2016" : {"input" : "TTJets-DiLept-FastSim-2016-v1.root", "output" : "Histos-TTJets-DiLept-FastSim-2016-v1.root"},
            "FastSim-2017" : {"input" : "TTJets-DiLept-FastSim-2017-v1.root", "output" : "Histos-TTJets-DiLept-FastSim-2017-v1.root"},
            "FastSim-2018" : {"input" : "TTJets-DiLept-FastSim-2018-v1.root", "output" : "Histos-TTJets-DiLept-FastSim-2018-v1.root"},
    }
    
    tools.makeDir(output_dir)
    for key in info:
        input_file  = "{0}/{1}".format(input_dir,  info[key]["input"])
        output_file = "{0}/{1}".format(output_dir, info[key]["output"])
        process(input_file, output_file)

def main():
    makeHistos()

if __name__ == "__main__":
    main()

