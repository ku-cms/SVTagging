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
    # check that file exists
    if not os.path.isfile(input_file):
        print("ERROR: The input file \"{0}\" does not exist.".format(input_file))
        return

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

