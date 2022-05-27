# quick_ratio.py

import ROOT
import numpy as np
import tools
import csv

# Make sure ROOT.TFile.Open(fileURL) does not seg fault when $ is in sys.argv (e.g. $ passed in as argument)
ROOT.PyConfig.IgnoreCommandLineOptions = True
# Make plots faster without displaying them
ROOT.gROOT.SetBatch(ROOT.kTRUE)
# Tell ROOT not to be in charge of memory, fix issue of histograms being deleted when ROOT file is closed:
ROOT.TH1.AddDirectory(False)

# TODO:
# - save output ROOT files of double ratio
# - plot efficiencies for multiple years
# - plot (fast sim eff) / (full sim eff) for multiple years
# DONE:
# - loop over plotting function instead of copy/paste
# - move input ROOT files to directory
# - add labels to plots (title, axis, name, etc)
# - use fixed x, y ranges in plots 
# - save stats in a csv file

# get bins values from histogram for a range of bins
# include values from start and end bins
def getBinValues(hist, start_bin, end_bin):
    values = []
    for i in range(start_bin, end_bin + 1, 1):
        values.append(hist.GetBinContent(i))
    return values

# get row for csv output
def getRow(hist, plot_name, year, flavor, variable):
    # default: use all bins
    start_bin = 1
    end_bin   = hist.GetNbinsX()
    # use different start/end bins for isC (PT) and Eta (all flavors)
    if "isC" in plot_name:
        start_bin = 1
        end_bin   = 18
    if "Eta" in plot_name:
        start_bin = 3
        end_bin   = 18
    values = getBinValues(hist, start_bin, end_bin)
    n_values    = len(values)
    mean        = np.mean(values)
    std_dev     = np.std(values)
    mean_rnd    = round(mean, 3)
    std_dev_rnd = round(std_dev, 3)
    # output_column_titles = ["name", "year", "flavor", "variable", "n_values", "mean", "std_dev"]
    output_row = ["FastOverFull", year, flavor, variable, n_values, mean_rnd, std_dev_rnd]
    return output_row

# given file names and histogram names, plot a ratio of histograms
def plotRatio(plot_dir, plot_name, f_num_name, f_den_name, h_num_name, h_den_name, info, output_writer):
    # get info from info :-)
    year        = info["year"]
    flavor      = info["flavor"]
    variable    = info["variable"]
    
    # load files and histos
    f_num = ROOT.TFile(f_num_name)
    f_den = ROOT.TFile(f_den_name)
    h_num = f_num.Get(h_num_name)
    h_den = f_den.Get(h_den_name)
    
    # check if histos loaded successfully
    #print("h_num: {0}".format(h_num))
    #print("h_den: {0}".format(h_den))
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
    
    # TODO: save num, den, and ratio histograms in a new root file

    # axis labels
    labels = {
        "PT"    : "p_{T} [GeV]",
        "Eta"   : "#eta"
    }
    # plot ratio; save as pdf
    c = ROOT.TCanvas("c", "c", 800, 800)
    h_ratio = h_num.Clone("h_ratio")
    h_ratio.Divide(h_den)
    # setup
    title       = plot_name
    x_title     = labels[variable]
    y_title     = "(fast sim eff) / (full sim eff)" 
    y_min       = 0.0
    y_max       = 2.0
    color       = "black"
    lineWidth   = 3
    tools.setupHist(h_ratio, title, x_title, y_title, y_min, y_max, color, lineWidth)
    # draw
    h_ratio.Draw()
    
    # save stats to csv file
    output_row = getRow(h_ratio, plot_name, year, flavor, variable)
    output_writer.writerow(output_row)

    # save plot
    c.SaveAs(plot_dir + "/" + plot_name + ".pdf")

# create plots for different years, flavors, and variables
def run(input_dir, plot_dir, years, flavors, variables, output_writer):
    # make plot_dir if it does not exist
    tools.makeDir(plot_dir)
    # loop over years, flavors, and variables
    for year in years:
        for flavor in flavors:
            for variable in variables:
                # numerator:    FastSim SV eff.
                # denominator:  FullSim SV eff.
                info = {}
                info["year"]        = year
                info["flavor"]      = flavor
                info["variable"]    = variable
                plot_name  = "TTJets_{0}_FastOverFull_{1}_{2}".format(year, flavor, variable)
                f_num_name = "{0}/TTJets_FastSim_{1}_sv_eff.root".format(input_dir, year) 
                f_den_name = "{0}/TTJets_FullSim_{1}_sv_eff.root".format(input_dir, year)
                h_num_name = "{0}_discr_div_nojets_TTJets_FastSim_{1}_{2}_KUAnalysis".format(variable, year, flavor) 
                h_den_name = "{0}_discr_div_nojets_TTJets_FullSim_{1}_{2}_KUAnalysis".format(variable, year, flavor)
                plotRatio(plot_dir, plot_name, f_num_name, f_den_name, h_num_name, h_den_name, info, output_writer)

def main():
    # input_dir:        directory for input SV eff. ROOT files
    # plot_dir:         directory for output plots
    # csv_output_name:  name of output csv file with mean and std dev of scale factors
    input_dir       = "sv_eff"
    plot_dir        = "plots_FastOverFull"
    csv_output_name = "sv_FastOverFull.csv"
    years       = ["2016", "2017", "2018"]
    flavors     = ["isB", "isC", "isLight"]
    variables   = ["PT", "Eta"]

    output_column_titles = ["name", "year", "flavor", "variable", "n_values", "mean", "std_dev"]
    with open(csv_output_name, 'w') as output_csv:
        output_writer = csv.writer(output_csv)
        output_writer.writerow(output_column_titles)
        run(input_dir, plot_dir, years, flavors, variables, output_writer)

if __name__ == "__main__":
    main()

