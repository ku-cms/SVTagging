# quick_ratio.py

import ROOT
import numpy as np

# Make sure ROOT.TFile.Open(fileURL) does not seg fault when $ is in sys.argv (e.g. $ passed in as argument)
ROOT.PyConfig.IgnoreCommandLineOptions = True
# Make plots faster without displaying them
ROOT.gROOT.SetBatch(ROOT.kTRUE)
# Tell ROOT not to be in charge of memory, fix issue of histograms being deleted when ROOT file is closed:
ROOT.TH1.AddDirectory(False)

# TODO:
# - save output ROOT files of double ratio
# - save stats in text or csv file
# - add labels to plots (title, axis, name, etc)
# - use fixed x, y ranges in plots 
# DONE:
# - loop over plotting function instead of copy/paste
# - move input ROOT files to directory

# get bins values from histogram for a range of bins
# include values from start and end bins
def getBinValues(hist, start_bin, end_bin):
    values = []
    for i in range(start_bin, end_bin + 1, 1):
        values.append(hist.GetBinContent(i))
    return values

# given file names and histogram names, plot a ratio of histograms
def plotRatio(f_num_name, f_den_name, h_num_name, h_den_name, plot_name):
    plot_dir = "plots_FastOverFull"
    f_num = ROOT.TFile(f_num_name)
    f_den = ROOT.TFile(f_den_name)
    h_num = f_num.Get(h_num_name)
    h_den = f_den.Get(h_den_name)
    # check if histos loaded successfully
    print("h_num: {0}".format(h_num))
    print("h_den: {0}".format(h_den))
    quit = False
    if not h_num:
        print("ERROR: h_num does not exist.")
        quit = True
    if not h_den:
        print("ERROR: h_den does not exist.")
        quit = True
    if quit:
        print("Quitting now.")
        return
    # save num, den, and ratio histograms in a new root file

    # plot ratio; save as pdf
    c = ROOT.TCanvas("c", "c", 800, 800)
    h_ratio = h_num.Clone("h_ratio")
    h_ratio.Divide(h_den)
    h_ratio.Draw()
    # define start/end separated for PT, Eta
    start_bin = 1
    end_bin   = h_ratio.GetNbinsX()
    if "isC" in plot_name:
        start_bin = 1
        end_bin   = 18
    if "Eta" in plot_name:
        start_bin = 3
        end_bin   = 18
    values = getBinValues(h_ratio, start_bin, end_bin)
    print("name: {0}, n_values: {1}, mean: {2:.3f}, std dev: {3:.3f}".format(plot_name, len(values), np.mean(values), np.std(values)))
    c.SaveAs(plot_dir + "/" + plot_name + ".pdf")

# create plots for different years, flavors, and variables
def run(input_dir, years, flavors, variables):
    for year in years:
        for flavor in flavors:
            for variable in variables:
                # numerator:    FastSim SV eff.
                # denominator:  FullSim SV eff.
                plot_name  = "TTJets_{0}_FastOverFull_{1}_{2}".format(year, flavor, variable)
                f_num_name = "{0}/TTJets_FastSim_{1}_sv_eff.root".format(input_dir, year) 
                f_den_name = "{0}/TTJets_FullSim_{1}_sv_eff.root".format(input_dir, year)
                h_num_name = "{0}_discr_div_nojets_TTJets_FastSim_{1}_{2}_KUAnalysis".format(variable, year, flavor) 
                h_den_name = "{0}_discr_div_nojets_TTJets_FullSim_{1}_{2}_KUAnalysis".format(variable, year, flavor)
                plotRatio(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)

def main():
    # input directory with SV eff. ROOT files
    input_dir   = "sv_eff"
    years       = ["2016", "2017", "2018"]
    flavors     = ["isB", "isC", "isLight"]
    variables   = ["PT", "Eta"]
    
    run(input_dir, years, flavors, variables)

if __name__ == "__main__":
    main()

