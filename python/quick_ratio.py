# quick_ratio.py

import ROOT

def getHisto(f_name, h_name):
    f = ROOT.TFile(f_name)
    h = f.Get(h_name)
    print("h: {0}".format(h))
    return h

def plot(h_num, h_den, plot_name):
    c = ROOT.TCanvas("c", "c", 800, 800)
    h_ratio = h_num.Clone("h_ratio")
    h_ratio.Divide(h_den)
    h_ratio.Draw()
    c.SaveAs(plot_name + ".pdf")

def plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name):
    plot_dir = "plots_FastOverFull"
    f_num = ROOT.TFile(f_num_name)
    f_den = ROOT.TFile(f_den_name)
    h_num = f_num.Get(h_num_name)
    h_den = f_den.Get(h_den_name)
    print("h_num: {0}".format(h_num))
    print("h_den: {0}".format(h_den))
    # save num, den, and ratio histograms in a new root file

    # plot ratio; save as pdf
    c = ROOT.TCanvas("c", "c", 800, 800)
    h_ratio = h_num.Clone("h_ratio")
    h_ratio.Divide(h_den)
    h_ratio.Draw()
    c.SaveAs(plot_dir + "/" + plot_name + ".pdf")

def main():
    #h_num = getHisto(f_num_name, h_num_name)
    #h_den = getHisto(f_den_name, h_den_name)
    #plot(h_num, h_den, plot_name)
    
    # --- 2016 --- #
    plot_name  = "TTJets_2016_FastOverFull_isB_PT"
    f_num_name = "TTJets_FastSim_2016.root"
    f_den_name = "TTJets_FullSim_2016.root"
    h_num_name = "PT_discr_div_nojets_TTJets_FastSim_2016_isB_KUAnalysis"
    h_den_name = "PT_discr_div_nojets_TTJets_FullSim_2016_isB_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2016_FastOverFull_isB_Eta"
    f_num_name = "TTJets_FastSim_2016.root"
    f_den_name = "TTJets_FullSim_2016.root"
    h_num_name = "Eta_discr_div_nojets_TTJets_FastSim_2016_isB_KUAnalysis"
    h_den_name = "Eta_discr_div_nojets_TTJets_FullSim_2016_isB_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2016_FastOverFull_isC_PT"
    f_num_name = "TTJets_FastSim_2016.root"
    f_den_name = "TTJets_FullSim_2016.root"
    h_num_name = "PT_discr_div_nojets_TTJets_FastSim_2016_isC_KUAnalysis"
    h_den_name = "PT_discr_div_nojets_TTJets_FullSim_2016_isC_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2016_FastOverFull_isC_Eta"
    f_num_name = "TTJets_FastSim_2016.root"
    f_den_name = "TTJets_FullSim_2016.root"
    h_num_name = "Eta_discr_div_nojets_TTJets_FastSim_2016_isC_KUAnalysis"
    h_den_name = "Eta_discr_div_nojets_TTJets_FullSim_2016_isC_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2016_FastOverFull_isLight_PT"
    f_num_name = "TTJets_FastSim_2016.root"
    f_den_name = "TTJets_FullSim_2016.root"
    h_num_name = "PT_discr_div_nojets_TTJets_FastSim_2016_isLight_KUAnalysis"
    h_den_name = "PT_discr_div_nojets_TTJets_FullSim_2016_isLight_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2016_FastOverFull_isLight_Eta"
    f_num_name = "TTJets_FastSim_2016.root"
    f_den_name = "TTJets_FullSim_2016.root"
    h_num_name = "Eta_discr_div_nojets_TTJets_FastSim_2016_isLight_KUAnalysis"
    h_den_name = "Eta_discr_div_nojets_TTJets_FullSim_2016_isLight_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    # --- 2017 --- #
    plot_name  = "TTJets_2017_FastOverFull_isB_PT"
    f_num_name = "TTJets_FastSim_2017.root"
    f_den_name = "TTJets_FullSim_2017.root"
    h_num_name = "PT_discr_div_nojets_TTJets_FastSim_2017_isB_KUAnalysis"
    h_den_name = "PT_discr_div_nojets_TTJets_FullSim_2017_isB_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2017_FastOverFull_isB_Eta"
    f_num_name = "TTJets_FastSim_2017.root"
    f_den_name = "TTJets_FullSim_2017.root"
    h_num_name = "Eta_discr_div_nojets_TTJets_FastSim_2017_isB_KUAnalysis"
    h_den_name = "Eta_discr_div_nojets_TTJets_FullSim_2017_isB_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2017_FastOverFull_isC_PT"
    f_num_name = "TTJets_FastSim_2017.root"
    f_den_name = "TTJets_FullSim_2017.root"
    h_num_name = "PT_discr_div_nojets_TTJets_FastSim_2017_isC_KUAnalysis"
    h_den_name = "PT_discr_div_nojets_TTJets_FullSim_2017_isC_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2017_FastOverFull_isC_Eta"
    f_num_name = "TTJets_FastSim_2017.root"
    f_den_name = "TTJets_FullSim_2017.root"
    h_num_name = "Eta_discr_div_nojets_TTJets_FastSim_2017_isC_KUAnalysis"
    h_den_name = "Eta_discr_div_nojets_TTJets_FullSim_2017_isC_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2017_FastOverFull_isLight_PT"
    f_num_name = "TTJets_FastSim_2017.root"
    f_den_name = "TTJets_FullSim_2017.root"
    h_num_name = "PT_discr_div_nojets_TTJets_FastSim_2017_isLight_KUAnalysis"
    h_den_name = "PT_discr_div_nojets_TTJets_FullSim_2017_isLight_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2017_FastOverFull_isLight_Eta"
    f_num_name = "TTJets_FastSim_2017.root"
    f_den_name = "TTJets_FullSim_2017.root"
    h_num_name = "Eta_discr_div_nojets_TTJets_FastSim_2017_isLight_KUAnalysis"
    h_den_name = "Eta_discr_div_nojets_TTJets_FullSim_2017_isLight_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    # --- 2018 --- #
    plot_name  = "TTJets_2018_FastOverFull_isB_PT"
    f_num_name = "TTJets_FastSim_2018.root"
    f_den_name = "TTJets_FullSim_2018.root"
    h_num_name = "PT_discr_div_nojets_TTJets_FastSim_2018_isB_KUAnalysis"
    h_den_name = "PT_discr_div_nojets_TTJets_FullSim_2018_isB_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2018_FastOverFull_isB_Eta"
    f_num_name = "TTJets_FastSim_2018.root"
    f_den_name = "TTJets_FullSim_2018.root"
    h_num_name = "Eta_discr_div_nojets_TTJets_FastSim_2018_isB_KUAnalysis"
    h_den_name = "Eta_discr_div_nojets_TTJets_FullSim_2018_isB_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2018_FastOverFull_isC_PT"
    f_num_name = "TTJets_FastSim_2018.root"
    f_den_name = "TTJets_FullSim_2018.root"
    h_num_name = "PT_discr_div_nojets_TTJets_FastSim_2018_isC_KUAnalysis"
    h_den_name = "PT_discr_div_nojets_TTJets_FullSim_2018_isC_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2018_FastOverFull_isC_Eta"
    f_num_name = "TTJets_FastSim_2018.root"
    f_den_name = "TTJets_FullSim_2018.root"
    h_num_name = "Eta_discr_div_nojets_TTJets_FastSim_2018_isC_KUAnalysis"
    h_den_name = "Eta_discr_div_nojets_TTJets_FullSim_2018_isC_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2018_FastOverFull_isLight_PT"
    f_num_name = "TTJets_FastSim_2018.root"
    f_den_name = "TTJets_FullSim_2018.root"
    h_num_name = "PT_discr_div_nojets_TTJets_FastSim_2018_isLight_KUAnalysis"
    h_den_name = "PT_discr_div_nojets_TTJets_FullSim_2018_isLight_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)
    
    plot_name  = "TTJets_2018_FastOverFull_isLight_Eta"
    f_num_name = "TTJets_FastSim_2018.root"
    f_den_name = "TTJets_FullSim_2018.root"
    h_num_name = "Eta_discr_div_nojets_TTJets_FastSim_2018_isLight_KUAnalysis"
    h_den_name = "Eta_discr_div_nojets_TTJets_FullSim_2018_isLight_KUAnalysis"
    plot_v2(f_num_name, f_den_name, h_num_name, h_den_name, plot_name)

if __name__ == "__main__":
    main()

