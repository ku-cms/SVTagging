# makePlotsHistos.py

import os
import ROOT
import tools

# Make sure ROOT.TFile.Open(fileURL) does not seg fault when $ is in sys.argv (e.g. $ passed in as argument)
ROOT.PyConfig.IgnoreCommandLineOptions = True
# Make plots faster without displaying them
ROOT.gROOT.SetBatch(ROOT.kTRUE)
# Tell ROOT not to be in charge of memory, fix issue of histograms being deleted when ROOT file is closed:
ROOT.TH1.AddDirectory(False)

def plot(input_dir, plot_dir, input_files, eras, mc_type, variable, h_name, y_limits, setLogY):
    print("Plotting {0} - {1}".format(variable, mc_type))

    # xkcd colors: https://xkcd.com/color/rgb/
    #colors = ["red", "green", "blue"]
    colors = ["tomato", "kelly green", "azure"]

    # WARNING: must keep TFile open to use histograms; histograms are destroyed when TFile is closed
    open_files  = {}
    histos      = {}
    
    for era in eras:
        key         = "{0}-{1}".format(mc_type, era)
        input_file  = "{0}/{1}".format(input_dir, input_files[key])
        
        # check that input file exists
        if not os.path.isfile(input_file):
            print("ERROR: The input file \"{0}\" does not exist.".format(input_file))
            return
        
        open_files[era] = ROOT.TFile.Open(input_file)
        histos[era]     = open_files[era].Get(h_name)
    
    output_name = "{0}/{1}-{2}".format(plot_dir, variable, mc_type)
    
    c = ROOT.TCanvas("c", "c", 800, 800)
    c.SetLeftMargin(0.15)
    
    # legend: TLegend(x1,y1,x2,y2)
    legend_x1 = 0.70
    legend_x2 = 0.90
    legend_y1 = 0.70
    legend_y2 = 0.90
    legend = ROOT.TLegend(legend_x1, legend_y1, legend_x2, legend_y2)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetLineWidth(0)
    legend.SetNColumns(1)
    legend.SetTextFont(42)
    
    # draw histos
    for i, era in enumerate(eras):
        title   = "{0} ({1})".format(variable, mc_type)
        x_title = variable
        y_title = "Events"
        tools.setupHist(histos[era], title, x_title, y_title, y_limits[0], y_limits[1], colors[i], 3)
        histos[era].Draw("hist error same")
        legend.AddEntry(histos[era], era, "l")

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
    
    input_files = {
            "FullSim-2016" : "Histos-TTJets-DiLept-FullSim-2016-v1.root",
            "FullSim-2017" : "Histos-TTJets-DiLept-FullSim-2017-v1.root",
            "FullSim-2018" : "Histos-TTJets-DiLept-FullSim-2018-v1.root",
            "FastSim-2016" : "Histos-TTJets-DiLept-FastSim-2016-v1.root",
            "FastSim-2017" : "Histos-TTJets-DiLept-FastSim-2017-v1.root",
            "FastSim-2018" : "Histos-TTJets-DiLept-FastSim-2018-v1.root",
    }
    
    for mc_type in mc_types:
        plot(input_dir, plot_dir, input_files, eras, mc_type, variable, h_name, y_limits, setLogY)

def makePlots():
    print("Go make plots!")
    
    plot_dir_linear = "plots-histos-linear"
    plot_dir_log    = "plots-histos-log"
    input_dir       = "histos-v2"
    
    # y axis limits tuned for both linear and log scales
    histos = {
        "MET_pt"    : {"h_name" : "h_MET_pt",    "y_limits_linear" : [0, 5e4], "y_limits_log" : [1e-1, 1e10]},
        "nSV"       : {"h_name" : "h_nSV",       "y_limits_linear" : [0, 5e4], "y_limits_log" : [1e-1, 1e10]},
        "SV_ntrk"   : {"h_name" : "h_SV_ntrk",   "y_limits_linear" : [0, 2e5], "y_limits_log" : [1e-1, 1e10]},
        "SV_flavor" : {"h_name" : "h_SV_flavor", "y_limits_linear" : [0, 3e5], "y_limits_log" : [1e-1, 1e10]},
        "SV_pt_v1"  : {"h_name" : "h_SV_pt_v1",  "y_limits_linear" : [0, 1e5], "y_limits_log" : [1e-1, 1e10]},
        "SV_pt_v2"  : {"h_name" : "h_SV_pt_v2",  "y_limits_linear" : [0, 4e4], "y_limits_log" : [1e-1, 1e10]},
        "SV_eta"    : {"h_name" : "h_SV_eta",    "y_limits_linear" : [0, 5e4], "y_limits_log" : [1e-1, 1e10]},
    }
    
    tools.makeDir(plot_dir_linear)
    tools.makeDir(plot_dir_log)

    for key in histos:
        process(input_dir, plot_dir_linear, key, histos[key]["h_name"], histos[key]["y_limits_linear"], setLogY=False)
        process(input_dir, plot_dir_log, key, histos[key]["h_name"], histos[key]["y_limits_log"], setLogY=True)
    
def main():
    makePlots()

if __name__ == "__main__":
    main()

