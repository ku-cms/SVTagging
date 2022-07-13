# calc_ratio.py

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
# - plot efficiencies for multiple years on the same plot
# - plot efficiencies for fast sim and full sim on the same plot
# - add error bars to eff. plots and eff. ratio plots
# - to get SFs, take weighted average over bins with weights w_i = 1/sig_i^2, where sig_i is the error on each bin
# - remove extra eta bins
# - save output ROOT files of double ratio
# DONE:
# - loop over plotting function instead of copy/paste
# - move input ROOT files to directory
# - add labels to plots (title, axis, name, etc)
# - use fixed x, y ranges in plots 
# - save stats in a csv file
# - plot (fast sim eff) / (full sim eff) for multiple years
# - invert ratio: use (full sim eff) / (fast sim eff)
# - use less bins: try 10 bins instead of 20

# check that histogram exists
def histExists(hist_name, hist):
    if not hist:
        print("ERROR: the histogram \"{0}\" does not exist.".format(hist_name))
        return False
    else:
        return True

# get label based on a key
def getLabel(key):
    labels = {
        "PT"            : "p_{T} [GeV]",
        "Eta"           : "#eta",
        "FastOverFull"  : "(fast sim eff) / (full sim eff)",
        "FullOverFast"  : "(full sim eff) / (fast sim eff)"
    }
    return labels[key]

# get hist from TEfficiency object
def getHistFromEff(eff, name):
    # assume constant bin widths
    # get number of bins, x_min, x_max
    h_total     = eff.GetTotalHistogram()
    nbins       = h_total.GetNbinsX()
    x_min       = h_total.GetBinLowEdge(1)
    x_max       = h_total.GetBinLowEdge(nbins) + h_total.GetBinWidth(nbins)
    new_name    = name + "_new" 
    print("In getHistFromEff(): nbins = {0}, x_min = {1}, x_max = {2}".format(nbins, x_min, x_max))
    # new histogram
    h_new = ROOT.TH1D(new_name, new_name, nbins, x_min, x_max)
    for i in range(1, nbins+1):
        # get values
        val         = eff.GetEfficiency(i)
        err_low     = eff.GetEfficiencyErrorLow(i)
        err_high    = eff.GetEfficiencyErrorUp(i)
        ave_err     = np.mean([err_low, err_high])
        print("val = {0:.5f}, err_low = {1:.5f}, err_high = {2:.5f}, ave_err = {3:.5f}".format(val, err_low, err_high, ave_err))
        # set values
        h_new.SetBinContent(i, val)
        h_new.SetBinError(i, ave_err)
    return h_new

# get names of files and hists for FastOverFull
def getNamesFastOverFull(input_dir, year, flavor, variable, use_eff):
    tag = ""
    if use_eff:
        tag = "_eff"
    names = {}
    names["f_num_name"] = "{0}/TTJets_FastSim_{1}_sv_eff.root".format(input_dir, year) 
    names["f_den_name"] = "{0}/TTJets_FullSim_{1}_sv_eff.root".format(input_dir, year)
    names["h_num_name"] = "{0}_discr_div_nojets_TTJets_FastSim_{1}_{2}_KUAnalysis{3}".format(variable, year, flavor, tag) 
    names["h_den_name"] = "{0}_discr_div_nojets_TTJets_FullSim_{1}_{2}_KUAnalysis{3}".format(variable, year, flavor, tag)
    return names

# get names of files and hists for FullOverFast
def getNamesFullOverFast(input_dir, year, flavor, variable, use_eff):
    tag = ""
    if use_eff:
        tag = "_eff"
    names = {}
    names["f_num_name"] = "{0}/TTJets_FullSim_{1}_sv_eff.root".format(input_dir, year) 
    names["f_den_name"] = "{0}/TTJets_FastSim_{1}_sv_eff.root".format(input_dir, year)
    names["h_num_name"] = "{0}_discr_div_nojets_TTJets_FullSim_{1}_{2}_KUAnalysis{3}".format(variable, year, flavor, tag) 
    names["h_den_name"] = "{0}_discr_div_nojets_TTJets_FastSim_{1}_{2}_KUAnalysis{3}".format(variable, year, flavor, tag)
    return names

# get bins values from histogram for a range of bins
# include values from start and end bins
def getBinValues(hist, start_bin, end_bin):
    values = []
    for i in range(start_bin, end_bin + 1, 1):
        values.append(hist.GetBinContent(i))
    return values

# get row for csv output
def getRow(hist, plot_name, ratio_name, year, flavor, variable):
    # default: use all bins
    start_bin = 1
    end_bin   = hist.GetNbinsX()
    
    # use different start/end bins for isC (PT) and Eta (all flavors)
    
    # old binning
    # if "isC" in plot_name:
    #     start_bin = 1
    #     end_bin   = 18
    # if "Eta" in plot_name:
    #     start_bin = 3
    #     end_bin   = 18
    
    # new binning
    if "Eta" in plot_name:
        start_bin += 1
        end_bin   -= 1

    values = getBinValues(hist, start_bin, end_bin)
    n_values    = len(values)
    mean        = np.mean(values)
    std_dev     = np.std(values)
    mean_rnd    = round(mean, 3)
    std_dev_rnd = round(std_dev, 3)
    # output_column_titles = ["name", "year", "flavor", "variable", "n_values", "mean", "std_dev"]
    output_row = [ratio_name, year, flavor, variable, n_values, mean_rnd, std_dev_rnd]
    return output_row

# given file names and histogram names, plot a ratio of histograms
def plotRatio(ratio_name, input_dir, plot_dir, plot_name, info, output_writer, use_eff, draw_err):
    # TODO: save num, den, and ratio histograms in a new root file
    # get info from info :-)
    year        = info["year"]
    flavor      = info["flavor"]
    variable    = info["variable"]
    # get file and hist names
    names = {}
    if ratio_name == "FastOverFull":
        names = getNamesFastOverFull(input_dir, year, flavor, variable, use_eff)
    elif ratio_name == "FullOverFast":
        names = getNamesFullOverFast(input_dir, year, flavor, variable, use_eff)
    else:
        # print error and quit if ratio name is not supported
        print("ERROR: The ratio_name \"{0}\" is not supported. Quitting now!".format(ratio_name))
        return
    f_num_name = names["f_num_name"]
    f_den_name = names["f_den_name"]
    h_num_name = names["h_num_name"]
    h_den_name = names["h_den_name"]
    
    # load files and histos
    f_num = ROOT.TFile(f_num_name)
    f_den = ROOT.TFile(f_den_name)
    if use_eff:
        h_num_eff = f_num.Get(h_num_name)
        h_den_eff = f_den.Get(h_den_name)
        h_num = getHistFromEff(h_num_eff, h_num_name)
        h_den = getHistFromEff(h_den_eff, h_den_name)
    else:
        h_num = f_num.Get(h_num_name)
        h_den = f_den.Get(h_den_name)
    
    # check that histos exist (loaded successfully)
    #print("h_num_name: {0}\nh_num: {1}".format(h_num_name, h_num))
    #print("h_den_name: {0}\nh_den: {1}".format(h_den_name, h_den))
    h_num_exists = histExists(h_num_name, h_num) 
    h_den_exists = histExists(h_den_name, h_den) 
    if not h_num_exists or not h_den_exists:
        print("The histogram(s) did not load properly. Quitting now.")
        return
    
    # plot ratio; save as pdf
    c = ROOT.TCanvas("c", "c", 800, 800)
    h_ratio = h_num.Clone("h_ratio")
    h_ratio.Divide(h_den)
    # setup hist for plot
    title       = plot_name
    x_title     = getLabel(variable)
    y_title     = getLabel(ratio_name)
    y_min       = 0.0
    y_max       = 2.0
    color       = "black"
    lineWidth   = 3
    tools.setupHist(h_ratio, title, x_title, y_title, y_min, y_max, color, lineWidth)
    # draw
    if draw_err:
        h_ratio.Draw("error")
    else:
        h_ratio.Draw()
    # save plot
    c.SaveAs(plot_dir + "/" + plot_name + ".pdf")
    
    # save stats to csv file
    output_row = getRow(h_ratio, plot_name, ratio_name, year, flavor, variable)
    output_writer.writerow(output_row)

# plot ratio of histograms for multiple years on one plot
def plotRatioMultiYear(ratio_name, input_dir, plot_dir, plot_name, years, info, use_eff, draw_err):
    # TODO: save num, den, and ratio histograms in a new root file
    # get info from info :-)
    flavor      = info["flavor"]
    variable    = info["variable"]
    # xkcd colors: https://xkcd.com/color/rgb/
    colors = {
        "2016" : "tomato",
        "2017" : "kelly green",
        "2018" : "azure",
    }
    
    # plot ratio; save as pdf
    c = ROOT.TCanvas("c", "c", 800, 800)
    
    # legend
    legend_x1 = 0.70
    legend_x2 = 0.90
    legend_y1 = 0.70
    legend_y2 = 0.90
    # legend: TLegend(x1,y1,x2,y2)
    legend = ROOT.TLegend(legend_x1, legend_y1, legend_x2, legend_y2)
    tools.setupLegend(legend)
    
    # loop over years
    # store histos in map so that they are not overwritten 
    histos = {}
    for year in years:
        histos[year] = {}
        # get file and hist names
        names = {}
        if ratio_name == "FastOverFull":
            names = getNamesFastOverFull(input_dir, year, flavor, variable, use_eff)
        elif ratio_name == "FullOverFast":
            names = getNamesFullOverFast(input_dir, year, flavor, variable, use_eff)
        else:
            # print error and quit if ratio name is not supported
            print("ERROR: The ratio_name \"{0}\" is not supported. Quitting now!".format(ratio_name))
            return
        f_num_name = names["f_num_name"]
        f_den_name = names["f_den_name"]
        h_num_name = names["h_num_name"]
        h_den_name = names["h_den_name"]
    
        # load files and histos
        f_num = ROOT.TFile(f_num_name)
        f_den = ROOT.TFile(f_den_name)
        if use_eff:
            h_num_eff = f_num.Get(h_num_name)
            h_den_eff = f_den.Get(h_den_name)
            histos[year]["h_num"] = getHistFromEff(h_num_eff, h_num_name)
            histos[year]["h_den"] = getHistFromEff(h_den_eff, h_den_name)
            h_num = histos[year]["h_num"]
            h_den = histos[year]["h_den"]
        else:
            histos[year]["h_num"] = f_num.Get(h_num_name)
            histos[year]["h_den"] = f_den.Get(h_den_name)
            h_num = histos[year]["h_num"]
            h_den = histos[year]["h_den"]
        
        # check that histos exist (loaded successfully)
        #print("h_num_name: {0}\nh_num: {1}".format(h_num_name, h_num))
        #print("h_den_name: {0}\nh_den: {1}".format(h_den_name, h_den))
        h_num_exists = histExists(h_num_name, h_num) 
        h_den_exists = histExists(h_den_name, h_den) 
        if not h_num_exists or not h_den_exists:
            print("The histogram(s) did not load properly. Quitting now.")
            return
    
        histos[year]["h_ratio"] = h_num.Clone("h_ratio")
        h_ratio = histos[year]["h_ratio"]
        h_ratio.Divide(h_den)
        # setup hist for plot
        title       = plot_name
        x_title     = getLabel(variable)
        y_title     = getLabel(ratio_name)
        y_min       = 0.0
        y_max       = 2.0
        color       = colors[year]
        lineWidth   = 3
        tools.setupHist(h_ratio, title, x_title, y_title, y_min, y_max, color, lineWidth)
        # draw
        if draw_err:
            h_ratio.Draw("same error")
        else:
            h_ratio.Draw("same")
        legend.AddEntry(h_ratio, year, "l")
    
    legend.Draw()
    
    # save plot
    c.Update()
    c.SaveAs(plot_dir + "/" + plot_name + ".pdf")

# create plots for different years, flavors, and variables
def run(ratio_name, input_dir, plot_dir, years, flavors, variables, output_writer):
    use_eff  = True
    draw_err = True
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
                plot_name  = "TTJets_{0}_{1}_{2}_{3}".format(ratio_name, year, flavor, variable)
                plotRatio(ratio_name, input_dir, plot_dir, plot_name, info, output_writer, use_eff, draw_err)
    
    # loop over flavors and variables 
    for flavor in flavors:
        for variable in variables:
            info = {}
            info["flavor"]      = flavor
            info["variable"]    = variable
            plot_name  = "TTJets_{0}_AllYears_{1}_{2}".format(ratio_name, flavor, variable)
            plotRatioMultiYear(ratio_name, input_dir, plot_dir, plot_name, years, info, use_eff, draw_err)

def main():
    # ratio_name:       name of ratio (e.g. FastOverFull, FullOverFast)
    # input_dir:        directory for input SV eff. ROOT files
    # plot_dir:         directory for output plots
    # csv_output_name:  name of output csv file with mean and std dev of scale factors
    
    ratio_names     = ["FastOverFull", "FullOverFast"]
    input_dir       = "sv_eff"
    years           = ["2016", "2017", "2018"]
    flavors         = ["isB", "isC", "isLight"]
    variables       = ["PT", "Eta"]
    
    for ratio_name in ratio_names:
        plot_dir        = "plots_{0}".format(ratio_name)
        csv_output_name = "sv_{0}.csv".format(ratio_name)

        output_column_titles = ["name", "year", "flavor", "variable", "n_values", "mean", "std_dev"]
        with open(csv_output_name, 'w') as output_csv:
            output_writer = csv.writer(output_csv)
            output_writer.writerow(output_column_titles)
            run(ratio_name, input_dir, plot_dir, years, flavors, variables, output_writer)

if __name__ == "__main__":
    main()

