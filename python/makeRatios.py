# makeRatios.py

import os
import ROOT
import tools
import makePlotsHistos

# Make sure ROOT.TFile.Open(fileURL) does not seg fault when $ is in sys.argv (e.g. $ passed in as argument)
ROOT.PyConfig.IgnoreCommandLineOptions = True
# Make plots faster without displaying them
ROOT.gROOT.SetBatch(ROOT.kTRUE)
# Tell ROOT not to be in charge of memory, fix issue of histograms being deleted when ROOT file is closed:
ROOT.TH1.AddDirectory(False)

# plot ratio (full sim / fast sim) 
def plotRatio(input_dir, plot_dir, input_files, mc_types, era, variable, h_name, y_limits, setLogY):
    print("Plotting {0} - {1}".format(variable, era))
    
    # xkcd colors: https://xkcd.com/color/rgb/
    colors = ["tomato", "kelly green", "azure"]
    
    # WARNING: must keep TFile open to use histograms; histograms are destroyed when TFile is closed
    open_files  = {}
    histos      = {}
    
    for mc_type in mc_types:
        key         = "{0}-{1}".format(mc_type, era)
        input_file  = "{0}/{1}".format(input_dir, input_files[key])
        
        # check that input file exists
        if not os.path.isfile(input_file):
            print("ERROR: The input file \"{0}\" does not exist.".format(input_file))
            return
        
        open_files[mc_type] = ROOT.TFile.Open(input_file)
        histos[mc_type]     = open_files[mc_type].Get(h_name)
    
    output_name = "{0}/{1}-{2}".format(plot_dir, variable, era)
    
    c = ROOT.TCanvas("c", "c", 800, 800)
    c.SetLeftMargin(0.15)
    
    # legend
    legend_x1 = 0.70
    legend_x2 = 0.90
    legend_y1 = 0.70
    legend_y2 = 0.90
    # legend: TLegend(x1,y1,x2,y2)
    legend = ROOT.TLegend(legend_x1, legend_y1, legend_x2, legend_y2)

    tools.setupLegend(legend)
    
    # draw histos
    for i, mc_type in enumerate(mc_types):
        title   = "{0} ({1})".format(variable, era)
        x_title = variable
        y_title = "Events"
        tools.setupHist(histos[mc_type], title, x_title, y_title, y_limits[0], y_limits[1], colors[i], 3)
        histos[mc_type].Draw("hist error same")
        legend.AddEntry(histos[mc_type], mc_type, "l")

    legend.Draw()
    
    if setLogY:
        c.SetLogy(1) 
    
    # save plots
    c.Update()
    c.SaveAs(output_name + ".pdf")
    c.SaveAs(output_name + ".png")

def process(input_dir, plot_dir, variable, h_name, y_limits, setLogY):
    eras        = ["2016", "2017", "2018"]
    mc_types    = ["FullSim", "FastSim"]

    input_files = makePlotsHistos.getInputFiles()
    
    #for mc_type in mc_types:
    #    plotEras(input_dir, plot_dir, input_files, eras, mc_type, variable, h_name, y_limits, setLogY)
    #
    #for era in eras:
    #    plotSim(input_dir, plot_dir, input_files, mc_types, era, variable, h_name, y_limits, setLogY)
    
    for era in eras:
        plotRatio(input_dir, plot_dir, input_files, mc_types, era, variable, h_name, y_limits, setLogY)
    
def makeRaiots():
    print("Go make ratios!")
    plot_dir  = "plots-FullSimVsFastSim"
    input_dir = "histos-v2"
    
    # y axis limits tuned for both linear and log scales
    histos = {
        "SV_pt_v2"  : {"h_name" : "h_SV_pt_v2",  "y_limits_linear" : [0, 4e4], "y_limits_log" : [1e-1, 1e10]},
        "SV_eta"    : {"h_name" : "h_SV_eta",    "y_limits_linear" : [0, 5e4], "y_limits_log" : [1e-1, 1e10]},
    }
    
    tools.makeDir(plot_dir)
    
    for key in histos:
        process(input_dir, plot_dir, key, histos[key]["h_name"], histos[key]["y_limits_linear"], setLogY=False)

def main():
    makeRaiots()

if __name__ == "__main__":
    main()

