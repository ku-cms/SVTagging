# calc_ratio.py

import ROOT
import numpy as np
import tools
import csv
import colors
import json
import os

# Make sure ROOT.TFile.Open(fileURL) does not seg fault when $ is in sys.argv (e.g. $ passed in as argument)
ROOT.PyConfig.IgnoreCommandLineOptions = True
# Make plots faster without displaying them
ROOT.gROOT.SetBatch(ROOT.kTRUE)
# Tell ROOT not to be in charge of memory, fix issue of histograms being deleted when ROOT file is closed:
ROOT.TH1.AddDirectory(False)

# TODO:
# - change scale factor and unc. to be based on the total number of events (instead of weighted avg. across bins)
# - increase axis label sizes
# - save output ROOT files of double ratio
# DONE:
# - plot efficiencies for multiple years on the same plot
# - plot efficiencies for fast sim and full sim on the same plot
# - change color of central weighted avg. line
# - add weighted avg. and unc. to plots
# - remove extra eta bins
# - add error bars to eff. plots and eff. ratio plots
# - to get SFs, take weighted average over bins with weights w_i = 1/sig_i^2, where sig_i is the error on each bin
# - loop over plotting function instead of copy/paste
# - move input ROOT files to directory
# - add labels to plots (title, axis, name, etc)
# - use fixed x, y ranges in plots 
# - save stats in a csv file
# - plot (fast sim eff) / (full sim eff) for multiple years
# - invert ratio: use (full sim eff) / (fast sim eff)
# - use less bins: try 10 bins instead of 20
# NOTES:
# - Currently for errors on eff. histos, the average of high and low errors from TEfficiency are used. The double ratio has symmetric errors; could maintain asymmetric errors.
# - Currently for SF, std_dev is used; could instead propagate unc. through calc. of weighted average.

# check that file exists
def fileExists(file_name):
    if not os.path.isfile(file_name):
        print("ERROR: the file \"{0}\" does not exist.".format(file_name))
        return False
    else:
        return True

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

# get color based on a key
def getColor(key):
    # xkcd colors: https://xkcd.com/color/rgb/
    colors = {
        "2016" : "tomato red",
        "2017" : "kelly green",
        "2018" : "azure",
    }
    return colors[key]

# get x_min and x_max for hist
def getHistRange(hist):
    nbins   = hist.GetNbinsX()
    x_min   = hist.GetBinLowEdge(1)
    x_max   = hist.GetBinLowEdge(nbins) + hist.GetBinWidth(nbins)
    return [x_min, x_max]

# get empty dummy hist to draw
def getDummyFromHist(hist):
    nbins           = hist.GetNbinsX()
    x_min, x_max    = getHistRange(hist)
    dummy           = ROOT.TH1D("dummy", "dummy", nbins, x_min, x_max)
    return dummy

# get hist from TEfficiency object
def getHistFromEff(eff, name):
    verbose = False
    # assume constant bin widths
    # get number of bins, x_min, x_max
    h_total         = eff.GetTotalHistogram()
    nbins           = h_total.GetNbinsX()
    #x_min           = h_total.GetBinLowEdge(1)
    #x_max           = h_total.GetBinLowEdge(nbins) + h_total.GetBinWidth(nbins)
    x_min, x_max    = getHistRange(h_total) 
    new_name    = name + "_new" 
    if verbose:
        print("In getHistFromEff(): nbins = {0}, x_min = {1}, x_max = {2}".format(nbins, x_min, x_max))
    # new histogram
    h_new = ROOT.TH1D(new_name, new_name, nbins, x_min, x_max)
    for i in range(1, nbins+1):
        # get values
        val         = eff.GetEfficiency(i)
        err_low     = eff.GetEfficiencyErrorLow(i)
        err_high    = eff.GetEfficiencyErrorUp(i)
        ave_err     = np.mean([err_low, err_high])
        if verbose:
            print("val = {0:.5f}, err_low = {1:.5f}, err_high = {2:.5f}, ave_err = {3:.5f}".format(val, err_low, err_high, ave_err))
        # set values
        h_new.SetBinContent(i, val)
        h_new.SetBinError(i, ave_err)
    return h_new

# get names of files and hists for FastOverFull
def getNamesFastOverFull(input_dir, year, flavor, variable, use_eff):
    # If use_eff is true, then load TEfficiency objects instead of histograms.
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
    # If use_eff is true, then load TEfficiency objects instead of histograms.
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
    values = [hist.GetBinContent(i) for i in range(start_bin, end_bin + 1, 1)]
    return values

# get bins errors from histogram for a range of bins
# include errors from start and end bins
def getBinErrors(hist, start_bin, end_bin):
    errors = [hist.GetBinError(i) for i in range(start_bin, end_bin + 1, 1)]
    return errors

# get row for csv output
def getRow(hist, plot_name, ratio_name, year, flavor, variable, scale_factor):
    start_bin           = 1
    end_bin             = hist.GetNbinsX()
    values              = getBinValues(hist, start_bin, end_bin)
    errors              = getBinErrors(hist, start_bin, end_bin)
    weights             = [1/(err ** 2) for err in errors]
    n_values            = len(values)
    weighted_avg        = np.average(values, weights=weights)
    mean                = np.mean(values)
    std_dev             = np.std(values)
    scale_factor_rnd    = round(scale_factor, 3)
    weighted_avg_rnd    = round(weighted_avg, 3)
    mean_rnd            = round(mean, 3)
    std_dev_rnd         = round(std_dev, 3)
    # output_column_titles = ["name", "year", "flavor", "variable", "n_values", "scale_factor", "weighted_avg", "mean", "std_dev"]
    output_row = [ratio_name, year, flavor, variable, n_values, scale_factor_rnd, weighted_avg_rnd, mean_rnd, std_dev_rnd]
    return output_row

# given file names and histogram names, plot efficiencies (fullsim and fastsim)
def plotEff(ratio_name, input_dir, plot_dir, plot_name, info):
    use_eff = True
    num_legend_name = ""
    den_legend_name = ""
    # get info from info :-)
    year        = info["year"]
    flavor      = info["flavor"]
    variable    = info["variable"]
    # get file and hist names
    names = {}
    if ratio_name == "FastOverFull":
        names = getNamesFastOverFull(input_dir, year, flavor, variable, use_eff)
        num_legend_name = "fast sim"
        den_legend_name = "full sim"
    elif ratio_name == "FullOverFast":
        names = getNamesFullOverFast(input_dir, year, flavor, variable, use_eff)
        num_legend_name = "full sim"
        den_legend_name = "fast sim"
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
    h_num_eff = f_num.Get(h_num_name)
    h_den_eff = f_den.Get(h_den_name)
    
    # check that histos exist (loaded successfully)
    #print("h_num_name: {0}\nh_num_eff: {1}".format(h_num_name, h_num_eff))
    #print("h_den_name: {0}\nh_den_eff: {1}".format(h_den_name, h_den_eff))
    h_num_exists = histExists(h_num_name, h_num_eff) 
    h_den_exists = histExists(h_den_name, h_den_eff) 
    if not h_num_exists or not h_den_exists:
        print("The TEfficiency objects did not load properly. Quitting now.")
        return
    
    c = ROOT.TCanvas("c", "c", 800, 800)
    
    # legend
    legend_x1 = 0.70
    legend_x2 = 0.90
    legend_y1 = 0.70
    legend_y2 = 0.90
    # legend: TLegend(x1,y1,x2,y2)
    legend = ROOT.TLegend(legend_x1, legend_y1, legend_x2, legend_y2)
    tools.setupLegend(legend)
    
    # setup hists for plot
    h_num_total     = getHistFromEff(h_num_eff, h_num_name)
    dummy           = getDummyFromHist(h_num_total)
    title           = plot_name
    x_title         = getLabel(variable)
    y_title         = "Efficiency"
    x_min, x_max    = getHistRange(h_num_total) 
    y_min           = 0.0
    y_max           = 1.5
    h_dummy_color   = "black"
    h_num_eff_color = "tomato red"
    h_den_eff_color = "azure"
    h_line_width    = 3
    #print("x_min = {0}, x_max = {1}, y_min = {2}, y_max = {3}".format(x_min, x_max, y_min, y_max))
    tools.setupHist(dummy, title, x_title, y_title, y_min, y_max, h_dummy_color, 0)
    tools.setupEff(h_num_eff, h_num_eff_color, h_line_width)
    tools.setupEff(h_den_eff, h_den_eff_color, h_line_width)
        
    legend.AddEntry(h_num_eff, num_legend_name, "l")
    legend.AddEntry(h_den_eff, den_legend_name, "l")
    
    # draw dummy hist
    dummy.Draw()
    h_num_eff.Draw("same error")
    h_den_eff.Draw("same error")
    
    legend.Draw()
    
    # save plot
    c.Update()
    c.SaveAs("{0}/{1}.pdf".format(plot_dir, plot_name))

# given file names and histogram names, plot efficiencies (multiple years)
def plotEffMultiYear(ratio_name, input_dir, plot_dir, plot_name, years, info):
    use_eff = True
    # get info from info :-)
    flavor      = info["flavor"]
    variable    = info["variable"]
    
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
        # Only use numberator (only need to plot one set, either fullsim or fastim, not both)
        f_num_name = names["f_num_name"]
        h_num_name = names["h_num_name"]
        # load files and histos
        f_num = ROOT.TFile(f_num_name)
        if use_eff:
            h_num_eff = f_num.Get(h_num_name)
            histos[year] = getHistFromEff(h_num_eff, h_num_name)
            h_num = histos[year]
        else:
            histos[year] = f_num.Get(h_num_name)
            h_num = histos[year]
        
        # check that histos exist (loaded successfully)
        #print("h_num_name: {0}\nh_num: {1}".format(h_num_name, h_num))
        h_num_exists = histExists(h_num_name, h_num) 
        if not h_num_exists:
            print("The histogram(s) did not load properly. Quitting now.")
            return
        
        # setup hist for plot
        title       = plot_name
        x_title     = getLabel(variable)
        y_title     = "Efficiency"
        y_min       = 0.0
        y_max       = 1.5
        color       = getColor(year)
        line_width  = 3
        tools.setupHist(h_num, title, x_title, y_title, y_min, y_max, color, line_width)
        # draw
        h_num.Draw("same error")
        legend.AddEntry(h_num, year, "l")
    
    legend.Draw()
    
    # save plot
    c.Update()
    c.SaveAs("{0}/{1}.pdf".format(plot_dir, plot_name))

# given file names and histogram names, plot a ratio of histograms
def plotRatio(ratio_name, input_dir, plot_dir, plot_name, info, output_writer, eff_map, use_eff, draw_err, draw_w_avg):
    # TODO: save num, den, and ratio histograms in a new root file
    # get info from info :-)
    year        = info["year"]
    flavor      = info["flavor"]
    variable    = info["variable"]
    # get efficiencies
    eff_key_fastsim = "TTJets_FastSim_{0}".format(year)
    eff_key_fullsim = "TTJets_FullSim_{0}".format(year)
    eff_fastsim     = eff_map[eff_key_fastsim]["ratio"]
    eff_fullsim     = eff_map[eff_key_fullsim]["ratio"]
    scale_factor    = -1
    # get file and hist names
    names = {}
    if ratio_name == "FastOverFull":
        names = getNamesFastOverFull(input_dir, year, flavor, variable, use_eff)
        scale_factor = eff_fastsim / eff_fullsim
    elif ratio_name == "FullOverFast":
        names = getNamesFullOverFast(input_dir, year, flavor, variable, use_eff)
        scale_factor = eff_fullsim / eff_fastsim
    else:
        # print error and quit if ratio name is not supported
        print("ERROR: The ratio_name \"{0}\" is not supported. Quitting now!".format(ratio_name))
        return
    
    print("ratio_name: {0}, year: {1}, scale_factor: {2}".format(ratio_name, year, scale_factor))
    
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
    dummy = getDummyFromHist(h_ratio)
    # setup hists for plot
    title           = plot_name
    x_title         = getLabel(variable)
    y_title         = getLabel(ratio_name)
    x_min, x_max    = getHistRange(h_ratio) 
    #y_min           = 0.0
    #y_max           = 2.0
    y_min           = 0.5
    y_max           = 1.5
    h_color         = "black"
    h_line_width    = 3
    tools.setupHist(h_ratio, title, x_title, y_title, y_min, y_max, h_color, h_line_width)
    tools.setupHist(dummy, title, x_title, y_title, y_min, y_max, h_color, 0)
    # save stats to csv file
    output_row = getRow(h_ratio, plot_name, ratio_name, year, flavor, variable, scale_factor)
    output_writer.writerow(output_row)
    # draw dummy hist
    dummy.Draw()
    
    # draw weighted avg. with unc.
    if draw_w_avg:
        # WARNING: hardcoded row indices... needs to match positions of values in row
        # output_column_titles = ["name", "year", "flavor", "variable", "n_values", "scale_factor", "weighted_avg", "mean", "std_dev"]
        w_avg       = output_row[-3]
        std_dev     = output_row[-1]
        w_avg_up    = w_avg + std_dev
        w_avg_down  = w_avg - std_dev
        # TLine (Double_t x1, Double_t y1, Double_t x2, Double_t y2)
        line_w_avg      = ROOT.TLine(x_min, w_avg,      x_max, w_avg)
        line_w_avg_up   = ROOT.TLine(x_min, w_avg_up,   x_max, w_avg_up)
        line_w_avg_down = ROOT.TLine(x_min, w_avg_down, x_max, w_avg_down)
        # setup lines
        mean_color  = "tomato red"
        unc_color   = "azure"
        line_width  = 3
        line_style  = 7
        tools.setupLine(line_w_avg,         mean_color, line_width, line_style)
        tools.setupLine(line_w_avg_up,      unc_color,  line_width, line_style)
        tools.setupLine(line_w_avg_down,    unc_color,  line_width, line_style)
        # draw lines
        line_w_avg.Draw()
        line_w_avg_up.Draw()
        line_w_avg_down.Draw()
        
        # legend
        legend_x1 = 0.70
        legend_x2 = 0.90
        legend_y1 = 0.70
        legend_y2 = 0.90
        # legend: TLegend(x1,y1,x2,y2)
        legend = ROOT.TLegend(legend_x1, legend_y1, legend_x2, legend_y2)
        tools.setupLegend(legend)
        
        legend.AddEntry(h_ratio,        "eff. ratio",       "l")
        legend.AddEntry(line_w_avg,     "#mu",              "l")
        legend.AddEntry(line_w_avg_up,  "#mu #pm #sigma",   "l")
        legend.Draw()
    
    # draw
    if draw_err:
        h_ratio.Draw("same error")
    else:
        h_ratio.Draw("same")

    # text
    if draw_w_avg:
        text_x = x_min + 0.10 * (x_max - x_min)
        text_y = y_min + 0.90 * (y_max - y_min)
        #print("x_min = {0:.3f}, x_max = {1:.3f}, text_x = {2:.3f}".format(x_min, x_max, text_x))
        #print("y_min = {0:.3f}, y_max = {1:.3f}, text_y = {2:.3f}".format(y_min, y_max, text_y))
        text = ROOT.TLatex()
        text.SetTextAlign(11) # left aligned
        text.SetTextFont(42)
        text.SetTextSize(0.05)
        content = "#mu #pm #sigma = {0:.3f} #pm {1:.3f}".format(w_avg, std_dev)
        text.DrawLatex(text_x, text_y, content)
    
    # save plot
    c.Update()
    c.SaveAs("{0}/{1}.pdf".format(plot_dir, plot_name))

# plot ratio of histograms for multiple years on one plot
def plotRatioMultiYear(ratio_name, input_dir, plot_dir, plot_name, years, info, use_eff, draw_err):
    # TODO: save num, den, and ratio histograms in a new root file
    # get info from info :-)
    flavor      = info["flavor"]
    variable    = info["variable"]
    
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
        #y_min       = 0.0
        #y_max       = 2.0
        y_min       = 0.5
        y_max       = 1.5
        color       = getColor(year)
        line_width  = 3
        tools.setupHist(h_ratio, title, x_title, y_title, y_min, y_max, color, line_width)
        # draw
        if draw_err:
            h_ratio.Draw("same error")
        else:
            h_ratio.Draw("same")
        legend.AddEntry(h_ratio, year, "l")
    
    legend.Draw()
    
    # save plot
    c.Update()
    c.SaveAs("{0}/{1}.pdf".format(plot_dir, plot_name))

# create plots for different years, flavors, and variables
def run(ratio_name, input_dir, plot_dir, years, flavors, variables, output_writer, eff_map):
    use_eff     = True
    draw_err    = True
    draw_w_avg  = True
    # make plot_dir if it does not exist
    tools.makeDir(plot_dir)
    # loop over years, flavors, and variables
    for year in years:
        for flavor in flavors:
            for variable in variables:
                info = {}
                info["year"]            = year
                info["flavor"]          = flavor
                info["variable"]        = variable
                plot_name_eff           = "TTJets_{0}_{1}_{2}_{3}_eff".format(ratio_name, year, flavor, variable)
                plot_name_eff_ratios    = "TTJets_{0}_{1}_{2}_{3}_eff_ratios".format(ratio_name, year, flavor, variable)
                # plot efficiencies (fullsim and fastsim)
                plotEff(ratio_name, input_dir, plot_dir, plot_name_eff, info)
                # plot ratio of efficiencies
                plotRatio(ratio_name, input_dir, plot_dir, plot_name_eff_ratios, info, output_writer, eff_map, use_eff, draw_err, draw_w_avg)
    
    # loop over flavors and variables 
    for flavor in flavors:
        for variable in variables:
            # determine MC name for multi year plot (use numerator) 
            mc_name = ""
            if ratio_name == "FastOverFull":
                mc_name = "FastSim"
            elif ratio_name == "FullOverFast":
                mc_name = "FullSim"
            else:
                # print error and quit if ratio name is not supported
                print("ERROR: The ratio_name \"{0}\" is not supported. Quitting now!".format(ratio_name))
                return
            info = {}
            info["flavor"]          = flavor
            info["variable"]        = variable
            plot_name_eff           = "TTJets_{0}_AllYears_{1}_{2}_eff".format(mc_name, flavor, variable)
            plot_name_eff_ratios    = "TTJets_{0}_AllYears_{1}_{2}_eff_ratios".format(ratio_name, flavor, variable)
            # plot efficiencies for multiple years
            plotEffMultiYear(ratio_name, input_dir, plot_dir, plot_name_eff, years, info)
            # plot ratio of efficiencies for multiple years
            plotRatioMultiYear(ratio_name, input_dir, plot_dir, plot_name_eff_ratios, years, info, use_eff, draw_err)

def main():
    # --------------------------------------------------------------------------------- #
    # ratio_name:       name of ratio (e.g. FastOverFull, FullOverFast);                #
    #                   determines numerator and denominator for ratio                  #
    # input_dir:        directory for input SV eff. ROOT files                          #
    # years:            data-taking years                                               #
    # flavors:          quark flavors from gen matching                                 #
    # variables:        kinematic variables used to bin histograms                      #
    # plot_dir:         directory for output plots                                      #
    # csv_output_name:  name of output csv file with mean and std dev of scale factors  #
    # --------------------------------------------------------------------------------- #
    ratio_names     = ["FastOverFull", "FullOverFast"]
    input_dir       = "sv_eff"
    years           = ["2016", "2017", "2018"]
    flavors         = ["isB", "isC", "isLight"]
    variables       = ["PT", "Eta"]

    eff_map     = {}
    json_file   = "sv_eff/sv_eff.json"
    json_exists = fileExists(json_file)
    
    if json_exists:
        with open(json_file, 'r') as input_file:
            eff_map = json.load(input_file)
    else:
        return
    
    for ratio_name in ratio_names:
        plot_dir        = "plots_{0}".format(ratio_name)
        csv_output_name = "sv_{0}.csv".format(ratio_name)
        output_column_titles = ["name", "year", "flavor", "variable", "n_values", "scale_factor", "weighted_avg", "mean", "std_dev"]
        with open(csv_output_name, 'w') as output_csv:
            output_writer = csv.writer(output_csv)
            output_writer.writerow(output_column_titles)
            run(ratio_name, input_dir, plot_dir, years, flavors, variables, output_writer, eff_map)

if __name__ == "__main__":
    main()

