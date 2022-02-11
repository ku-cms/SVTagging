# makeHistos.py

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
    max_event = 10
    
    # check that file exists
    if not os.path.isfile(input_file):
        print("ERROR: The input file \"{0}\" does not exist.".format(input_file))
        return
    
    tree_name   = "Events"
    
    # # attempt 1
    # 
    # # WARNING: Make sure to open file here, not within getTree() so that TFile stays open. 
    # #          If TFile closes, then TTree object is destroyed.
    # open_file   = ROOT.TFile.Open(input_file)
    # tree        = tools.getTree(open_file, tree_name)
    # reader      = ROOT.TTreeReader(tree_name, open_file)
    # #SV_pt       = ROOT.TTreeReaderValue(float)(reader, "SV_pt")
    # MET_pt      = ROOT.TTreeReaderValue(float)(reader, "MET_pt")

    # # loop over events
    # event_i = 0
    # while(reader.Next()):
    #     if max_event >= 0:
    #         if event_i >= max_event:
    #             break
    #     #print("SV_pt: {0}".format(SV_pt))
    #     print("MET_pt: {0}".format(MET_pt))
    #     event_i += 1

    # attempt 2
    # See python examples in https://github.com/alexpearce/Ntuple
    chain = ROOT.TChain(tree_name)
    chain.Add(input_file)
    entries = chain.GetEntries()
    print("entries: {0}".format(entries))
    for entry in range(entries):
        if max_event >= 0:
            if entry >= max_event:
                break
        chain.GetEntry(entry)
        SV_pt_list = [x for x in chain.SV_pt]
        print("{0}: MET_pt = {1:.3f}, nSV = {2}, SV_pt = {3}".format(entry, chain.MET_pt, chain.nSV, SV_pt_list))


def makeHistos():
    print("Go make histos!")
    input_dir   = "data"
    output_dir  = "histos"
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

