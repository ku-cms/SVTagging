import ROOT
import os

# Make sure ROOT.TFile.Open(fileURL) does not seg fault when $ is in sys.argv (e.g. $ passed in as argument)
ROOT.PyConfig.IgnoreCommandLineOptions = True
# Make plots faster without displaying them
ROOT.gROOT.SetBatch(ROOT.kTRUE)
# Tell ROOT not to be in charge of memory, fix issue of histograms being deleted when ROOT file is closed:
ROOT.TH1.AddDirectory(False)

# create directory if it does not exist
def makeDir(dir_name):
    if not os.path.exists(dir_name):
       os.makedirs(dir_name)

# analyze root file
def analyze(filename, variable, cuts = ""):
    makeDir("plots")
    
    # load tree from root file
    treename = "Events"
    chain = ROOT.TChain(treename)
    chain.Add(filename)
    
    # plot histogram
    c = ROOT.TCanvas("c", "c", 800, 800)
    chain.Draw(variable, cuts)
    
    # save plot
    if cuts:
        plotname = "plots/{0}_{1}.pdf".format(variable, cuts)
    else:
        plotname = "plots/{0}.pdf".format(variable)
    
    c.Update()
    c.SaveAs(plotname)

def main():
    filename = "TTJets-DiLept-FastSim-2016-v1.root"
    analyze(filename, "Electron_pt")
    analyze(filename, "Electron_pt", "Electron_pt>50")
    
if __name__ == "__main__":
    main()

