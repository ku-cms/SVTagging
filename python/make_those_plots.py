from datetime import datetime
from collections import OrderedDict
from plotting_susy_cff import plot_configurables as pc
from plotting_susy_cff import sample_configurables as sc
import ROOT as rt
import imp, os
import tools
import re
import json

date = datetime.today().strftime('%Y_%m_%d')

rt.gROOT.SetBatch()
rt.gROOT.SetStyle('Plain')
rt.gStyle.SetOptTitle(0)
rt.gStyle.SetOptStat(0000)
rt.gStyle.SetOptFit(0111)
rt.gStyle.SetPalette(rt.kBlueRedYellow)
rt.TH1.SetDefaultSumw2()
rt.TH1.AddDirectory(rt.kFALSE)

helper   = imp.load_source('fix'     , './python/help.py')
tdrstyle = imp.load_source('tdrstyle', './python/tdrstyle.py')
CMS_lumi = imp.load_source('CMS_lumi', './python/CMS_lumi.py') 

CMS_extraText = "Simulation"

#tdrstyle.setTDRStyle()

def getIntegral(hist):
    bin1 = 1
    bin2 = hist.GetNbinsX()
    return hist.Integral(bin1, bin2)

def make_me_a_canvas():
   can = rt.TCanvas('canvas', 'canvas', 800, 600)
   can.SetLeftMargin(0.15)
   can.SetRightMargin(0.18)
   #can.SetTopMargin(0.05)
   can.SetBottomMargin(0.15)
   #can.SetGridx()
   #can.SetGridy()
   can.SetLogz()
   return can

def make_2D_plots(hists_, suffix_):
    tdrstyle.setTDRStyle()
    rt.gROOT.SetBatch()
    rt.gROOT.SetStyle('Plain')
    rt.gStyle.SetOptTitle(0)
    rt.gStyle.SetOptStat(0000)
    rt.gStyle.SetOptFit(0111)
    rt.gStyle.SetPalette(rt.kBlueRedYellow)
    if not (os.path.isdir('./plots_'+date)): os.mkdir('./plots_'+date)
    for sample in hists_:
        if not (os.path.isdir('./plots_'+date+'/'+sample)): os.mkdir('./plots_'+date+'/'+sample)
        for tree in hists_[sample]:
            if not (os.path.isdir('./plots_'+date+'/'+sample+'/'+tree)): os.mkdir(os.path.join('./plots_'+date, sample, tree))
            out_dir = os.path.join('./plots_'+date, sample, tree)
            for hist_name, hist in hists_[sample][tree].items():
                if not hist.InheritsFrom(rt.TH2.Class()):
                    continue
                if not hist.GetEntries() > 0.:
                    continue                 
                if hist_name not in pc:
                    continue
                can = make_me_a_canvas()
                can.cd() 
                #if 'N' not in hist_name.split('_')[0]: hist.RebinX(2)
                #if 'N' not in hist_name.split('_')[1]: hist.RebinY(2)
                hist.Draw("COLZ")
                hist.GetXaxis().CenterTitle()
                hist.GetXaxis().SetTitleFont(42)
                hist.GetXaxis().SetTitleSize(0.06)
                hist.GetXaxis().SetTitleOffset(1.06)
                hist.GetXaxis().SetLabelFont(42)
                hist.GetXaxis().SetLabelSize(0.05)
                hist.GetXaxis().SetTitle(pc[hist_name]['xlabel'])
                hist.GetYaxis().CenterTitle()
                hist.GetYaxis().SetTitleFont(42)
                hist.GetYaxis().SetTitleSize(0.06)
                hist.GetYaxis().SetTitleOffset(1.12)
                hist.GetYaxis().SetLabelFont(42)
                hist.GetYaxis().SetLabelSize(0.05)
                hist.GetYaxis().SetTitle(pc[hist_name]['ylabel'])
                hist.GetZaxis().CenterTitle()
                hist.GetZaxis().SetTitleFont(42)
                hist.GetZaxis().SetTitleSize(0.06)
                hist.GetZaxis().SetTitleOffset(1.1)
                hist.GetZaxis().SetLabelFont(42)
                hist.GetZaxis().SetLabelSize(0.05)
                hist.GetZaxis().SetTitle("a. u.")
                if pc[hist_name]['xmax'] is not None: 
                    xmin = pc[hist_name]['xmin']
                    xmax = pc[hist_name]['xmax']
                    hist.GetXaxis().SetRangeUser(xmin, xmax) 
                if pc[hist_name]['ymax'] is not None: 
                    ymin = pc[hist_name]['ymin']
                    ymax = pc[hist_name]['ymax']
                    hist.GetYaxis().SetRangeUser(ymin, ymax) 
                #hist.GetZaxis().SetRangeUser(0.9*hist.GetMinimum(0.0),1.1*hist.GetMaximum())
                hist.GetZaxis().SetRangeUser(0.001,1.1*hist.GetMaximum())
                CMS_lumi.writeExtraText = 1
                CMS_lumi.extraText = CMS_extraText
                #CMS_lumi.CMS_lumi(can, 0, 10)
                CMS_lumi.CMS_lumi(can, 0, 0)
                l = rt.TLatex()
                l.SetTextFont(42)
                l.SetNDC()
                l.SetTextSize(0.055)
                l.SetTextFont(42)
                if 'SMS' in sample:
                    l.DrawLatex(0.45,0.943,' '.join(sc[sample]['legend'].split('-')[-2:])+' '+tree)
                else:
                    l.DrawLatex(0.6,0.943,sc[sample]['legend'])
                can.SetLogz()
                can.Update()
                can.SaveAs(out_dir+'/h_'+hist.GetName()+'_'+suffix_+'.root')
                can.SaveAs(out_dir+'/h_'+hist.GetName()+'_'+suffix_+'.pdf')


# main efficiency plot
def make_overlay_plot(hists_, suffix_, output_name_):
    debug = True
    if debug:
        print("make_overlay_plot(): start")
        print(" - hists_: {0}".format(hists_))
        print(" - suffix_: {0}".format(suffix_))
        print(" - output_name_: {0}".format(output_name_))
    
    title = output_name_
    hists_tmp = OrderedDict()
    
    plot_dir = './plots_' + output_name_ + '_' + date
    
    if debug:
        print("plot_dir: {0}".format(plot_dir))
    
    if not (os.path.isdir(plot_dir)):
        os.mkdir(plot_dir)
    
    out_dir = os.path.join(plot_dir)
    
    if debug:
        print("out_dir: {0}".format(out_dir))

    for sample in hists_:
        print("sample: {0} at location 1".format(sample))
        for tree in hists_[sample]:
            print("tree: {0} at location 1".format(tree))
            for hist_name, hist in hists_[sample][tree].items():
                print("hist_name: {0} at location 1".format(hist_name))
                if hist_name not in pc:
                    print("WARNING: The hist_name {0} is not in pc at location 1.".format(hist_name))
                    continue
                if not hist.InheritsFrom(rt.TH1.Class()):
                    continue                    
                if hist.InheritsFrom(rt.TH2.Class()):
                    continue                    
                hists_tmp[hist_name] = OrderedDict()

    for sample in hists_:
        print("sample: {0} at location 2".format(sample))
        for tree in hists_[sample]:
            print("tree: {0} at location 2".format(tree))
            for hist_name, hist in hists_[sample][tree].items():
                print("hist_name: {0} at location 2".format(hist_name))
                if hist_name not in pc:
                    print("WARNING: The hist_name {0} is not in pc at location 2.".format(hist_name))
                    continue
                if not hist.InheritsFrom(rt.TH1.Class()):
                    continue                    
                if hist.InheritsFrom(rt.TH2.Class()):
                    continue
                hists_tmp[hist_name][sample] = OrderedDict()
    
    for sample in hists_:
        print("sample: {0} at location 3".format(sample))
        for tree in hists_[sample]:
            print("tree: {0} at location 3".format(tree))
            for hist_name, hist in hists_[sample][tree].items():
                print("hist_name: {0} at location 3".format(hist_name))
                if hist_name not in pc:
                    print("WARNING: The hist_name {0} is not in pc at location 3.".format(hist_name))
                    continue
                if not hist.InheritsFrom(rt.TH1.Class()):
                    continue
                if hist.InheritsFrom(rt.TH2.Class()):
                    continue
                #if '500_490' not in tree: continue 
                hists_tmp[hist_name][sample][tree] = hist
    
    if debug:
        print("hists_tmp: {0}".format(hists_tmp))
    
    for hist in hists_tmp:
        if debug:
            print("hist: {0}".format(hist))
        can = make_me_a_canvas()
        can.cd() 
        #leg = rt.TLegend(0.2,0.73,0.75,0.93,'','brNDC') 
        leg = rt.TLegend(0.3,0.80,0.8,0.88,'','brNDC') 
        leg.SetBorderSize(0)
        leg.SetNColumns(1)
        leg.SetTextSize(0.02)
        leg.SetMargin(0.2)
        leg.SetFillStyle(0)
        for sample in hists_tmp[hist]:
            for itr, tree in enumerate(hists_tmp[hist][sample]):
                if int(hists_tmp[hist][sample][tree].GetEntries()) == 0:
                    continue
                hists_tmp[hist][sample][tree].SetLineColor(sc[sample]['color']+itr*2)
                hists_tmp[hist][sample][tree].SetLineStyle(sc[sample]['style'])
                hists_tmp[hist][sample][tree].SetLineWidth(sc[sample]['width'])
                if sc[sample]['fill']: hists_tmp[hist][sample][tree].SetFillColor(sc[sample]['fill'])
                if sc[sample]['fill_style']: hists_tmp[hist][sample][tree].SetFillStyle(sc[sample]['fill_style'])
                #print hist, sample, tree
                if 'SMS' in sample:
                    stop_m = tree.split('_')[1]
                    neut_m = tree.split('_')[2]
                    leg.AddEntry(hists_tmp[hist][sample][tree], sc[sample]['legend']+' M(#tilde{t})='+stop_m+', M(#tilde{#chi}_{1}^{0})='+neut_m, 'fl')
                else:
                    leg.AddEntry(hists_tmp[hist][sample][tree], sc[sample]['legend'], 'fl')

                #if 'N' not in hist:
                #    print("TRUE: 'N' not in hist '{0}'".format(hist))
                #    hists_tmp[hist][sample][tree].Rebin(1)

                #hists_tmp[hist][sample][tree].Scale(1/hists_tmp[hist][sample][tree].Integral())

                nbins = hists_tmp[hist][sample][tree].GetNbinsX()
                #print("NBINS: output_name_: {0}, hist: {1}, number of bins: {2}".format(output_name_, hist, nbins))
   
                hists_tmp[hist][sample][tree].SetTitle(title)
                hists_tmp[hist][sample][tree].GetXaxis().SetTitle(pc[hist]['xlabel'])
                hists_tmp[hist][sample][tree].GetXaxis().CenterTitle()
                hists_tmp[hist][sample][tree].GetXaxis().SetTitleFont(42)
                hists_tmp[hist][sample][tree].GetXaxis().SetTitleSize(0.06)
                hists_tmp[hist][sample][tree].GetXaxis().SetTitleOffset(1.06)
                hists_tmp[hist][sample][tree].GetXaxis().SetLabelFont(42)
                hists_tmp[hist][sample][tree].GetXaxis().SetLabelSize(0.05)
                hists_tmp[hist][sample][tree].GetYaxis().SetTitle(pc[hist]['ylabel'])
                hists_tmp[hist][sample][tree].GetYaxis().CenterTitle()
                hists_tmp[hist][sample][tree].GetYaxis().SetTitleFont(42)
                hists_tmp[hist][sample][tree].GetYaxis().SetTitleSize(0.06)
                hists_tmp[hist][sample][tree].GetYaxis().SetTitleOffset(1.12)
                hists_tmp[hist][sample][tree].GetYaxis().SetLabelFont(42)
                hists_tmp[hist][sample][tree].GetYaxis().SetLabelSize(0.05)

                ymax = hists_tmp[hist][sample][tree].GetMaximum()
                #hists_tmp[hist][sample][tree].SetMinimum(0.01)
                #hists_tmp[hist][sample][tree].SetMaximum(250*ymax)
                if pc[hist_name]['xmax'] is not None: 
                    xmin = pc[hist_name]['xmin']
                    xmax = pc[hist_name]['xmax']
                    hist.GetXaxis().SetRangeUser(xmin, xmax) 

                hists_tmp[hist][sample][tree].SetMinimum(0.0)
                hists_tmp[hist][sample][tree].SetMaximum(1.25)

                hists_tmp[hist][sample][tree].Draw('histsame')
                
                # Draw title
                title_x = -999
                title_y = 1.1
                if "PT" in hist:
                    title_x = 13.0
                elif "Eta" in hist:
                    title_x = 0.5
                mark = rt.TLatex()
                mark.SetTextSize(0.03)
                mark.DrawLatex(title_x, title_y, title)

        can.cd()
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = CMS_extraText
        CMS_lumi.CMS_lumi(can, 0, 0)
        leg.Draw()
        #can.SetLogy()
        #can.Update()
        #can.SaveAs(out_dir+'/hoverlay_log_'+hist+'_'+suffix_+'.root')
        #can.SaveAs(out_dir+'/hoverlay_log_'+hist+'_'+suffix_+'.pdf')
        can.SetLogy(0)
        can.Update()
        can.SaveAs(out_dir+'/hoverlay_'+hist+'_'+suffix_+'.root')
        can.SaveAs(out_dir+'/hoverlay_'+hist+'_'+suffix_+'.pdf')
    
    if debug:
        print("make_overlay_plot(): end")

def make_plots(hists_, sig_hists_ = None, print_plots = True, suffix_=''):
    '''
    Makes plots wihtout stacking the hists, following the samples that are given in the histogram dictionary
    '''
    tdrstyle.setTDRStyle()
    if print_plots:
        if not (os.path.isdir('./plots_'+date)): os.mkdir('./plots_'+date)
    
    n_entries = OrderedDict()
    hists_tmp = OrderedDict()
    if sig_hists_:
        sig_hists_tmp = OrderedDict()
    out_dir = os.path.join('./plots_'+date)
    for sample in hists_:
        for tree in hists_[sample]:
            for hist_name, hist in hists_[sample][tree].items():
                if hist_name not in pc: continue
                if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                if hist.InheritsFrom(rt.TH2.Class()): continue                    
                n_entries[hist_name] = OrderedDict()
                hists_tmp[hist_name] = OrderedDict()
    for sample in hists_:
        for tree in hists_[sample]:
            for hist_name, hist in hists_[sample][tree].items():
                if hist_name not in pc: continue
                if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                if hist.InheritsFrom(rt.TH2.Class()): continue           
                nevts = hist.Integral(0,1000)
                if nevts == 0: continue        
                n_entries[hist_name][sample] = hist.Integral(0,10000)
                hists_tmp[hist_name][sample] = hist
    if sig_hists_:
        for sample in sig_hists_:
            for tree in sig_hists_[sample]:
                for hist_name, hist in sig_hists_[sample][tree].items():
                    if hist_name not in pc: continue
                    if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                    if hist.InheritsFrom(rt.TH2.Class()): continue                    
                    sig_hists_tmp[hist_name] = OrderedDict()
        for sample in sig_hists_:
            for tree in sig_hists_[sample]:
                for hist_name, hist in sig_hists_[sample][tree].items():
                    if hist_name not in pc: continue
                    if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                    if hist.InheritsFrom(rt.TH2.Class()): continue                    
                    sig_hists_tmp[hist_name][sample] = OrderedDict()
        for sample in sig_hists_:
            for tree in sig_hists_[sample]:
                for hist_name, hist in sig_hists_[sample][tree].items():
                    if hist_name not in pc: continue
                    if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                    if hist.InheritsFrom(rt.TH2.Class()): continue  
                    if not hist.GetEntries() > 0.: continue                 
                    if 'TChi' in sample and ('190' not in tree or '170' not in tree or '240' not in tree): continue 
                    if 'TSlep' in sample and ('190' not in tree or '170' not in tree or '195' not in tree): continue 
                    if 'T2' in sample and ('490' not in tree or '460' not in tree or '420' not in tree): continue 
                    sig_hists_tmp[hist_name][sample][tree] = hist
    for hist in n_entries:
        n_entries[hist] = OrderedDict(sorted(n_entries[hist].items(), key=lambda x: x[1]))
        can = make_me_a_canvas()
        can.cd() 
        leg = rt.TLegend(0.45,0.86,0.8,0.92,'','brNDC') 
        leg.SetBorderSize(0)
        leg.SetNColumns(2)
        leg.SetTextSize(0.024)
        leg.SetMargin(0.2)
        #leg.SetFillStyle(0)
        leg2 = rt.TLegend(0.45,0.58,0.80,0.86,'','brNDC') 
        leg2.SetBorderSize(0)
        leg2.SetEntrySeparation(0.5)
        leg2.SetNColumns(1)
        leg2.SetTextSize(0.024)
        leg2.SetMargin(0.2)
        #leg2.SetFillStyle(0)
        for sample in n_entries[hist]:
            if 'N' not in hist: hists_tmp[hist][sample].Rebin(1)
            hists_tmp[hist][sample].Scale(1./n_entries[hist][sample])
            hists_tmp[hist][sample].SetLineColor(sc[sample]['color'])
            hists_tmp[hist][sample].SetLineStyle(sc[sample]['style'])
            hists_tmp[hist][sample].SetLineWidth(sc[sample]['width'])
            if sc[sample]['fill']: hists_tmp[hist][sample].SetFillColor(sc[sample]['fill'])
            if sc[sample]['fill_style']: hists_tmp[hist][sample].SetFillStyle(sc[sample]['fill_style'])
            #print hist, sample
            leg.AddEntry(hists_tmp[hist][sample], sc[sample]['legend'], 'fl')
        if sig_hists_:
            for sample in sig_hists_tmp[hist]:
                for itr, tree in enumerate(sig_hists_tmp[hist][sample]):
                    if not sig_hists_tmp[hist][sample][tree].Integral() > 0. : continue
                    sig_hists_tmp[hist][sample][tree].Scale(1/sig_hists_tmp[hist][sample][tree].Integral())
                    sig_hists_tmp[hist][sample][tree].SetLineColor(sc[sample]['color']+itr+2)
                    sig_hists_tmp[hist][sample][tree].SetLineStyle(sc[sample]['style'])
                    sig_hists_tmp[hist][sample][tree].SetLineWidth(sc[sample]['width'])
                    if sc[sample]['fill']: sig_hists_tmp[hist][sample][tree].SetFillColor(sc[sample]['fill'])
                    if sc[sample]['fill_style']: sig_hists_tmp[hist][sample][tree].SetFillStyle(sc[sample]['fill_style'])
                    #print hist, sample, tree
                    if 'Events' in tree:
                        stop_m = '500'
                        neut_m = sample.split('_')[-1]
                        if 'T2bW' in sample:
                            sample_n = '-'.join(sample.split('_')[:2])
                        else:
                            sample_n = '-'.join(sample.split('_')[:3])
                            
                        #leg2.AddEntry(sig_hists_tmp[hist][sample][tree], '#splitline{'+sc[sample]['legend'] + ';}{#kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m+'}', 'fl')
                        leg2.AddEntry(sig_hists_tmp[hist][sample][tree], sc[sample]['legend']+'; #kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m, 'fl')
                    else:
                        stop_m = tree.split('_')[1]
                        neut_m = tree.split('_')[2]
                        sample_n = sample.split('_')[0]                
                        #leg2.AddEntry(sig_hists_tmp[hist][sample][tree], '#splitline{'+sc[sample]['legend'] + ';}{#kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m+'}', 'fl')
                        leg2.AddEntry(sig_hists_tmp[hist][sample][tree], sc[sample]['legend']+'; #kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m, 'fl')
        can.cd()
        for isam, sample in enumerate(reversed(hists_tmp[hist])):
            hists_tmp[hist][sample].Draw('histsame')
            hists_tmp[hist][sample].GetXaxis().SetTitle(pc[hist]['xlabel'])
            hists_tmp[hist][sample].GetXaxis().CenterTitle()
            hists_tmp[hist][sample].GetXaxis().SetTitleFont(42)
            hists_tmp[hist][sample].GetXaxis().SetTitleSize(0.048)
            hists_tmp[hist][sample].GetXaxis().SetTitleOffset(1.15)
            hists_tmp[hist][sample].GetXaxis().SetLabelFont(42)
            hists_tmp[hist][sample].GetXaxis().SetLabelSize(0.05)
            hists_tmp[hist][sample].GetYaxis().SetTitle(pc[hist]['ylabel'])
            hists_tmp[hist][sample].GetYaxis().CenterTitle()
            hists_tmp[hist][sample].GetYaxis().SetTitleFont(42)
            hists_tmp[hist][sample].GetYaxis().SetTitleSize(0.048)
            hists_tmp[hist][sample].GetYaxis().SetTitleOffset(1.2)
            hists_tmp[hist][sample].GetYaxis().SetLabelFont(42)
            hists_tmp[hist][sample].GetYaxis().SetLabelSize(0.05)
            can.Update()
            if pc[hist]['xmax'] is not None and isam == 0: 
                xmin = pc[hist]['xmin']
                xmax = pc[hist]['xmax']
                hists_tmp[hist][sample].GetXaxis().SetRangeUser(xmin, xmax) 
                can.Update()
        # if pc[hist]['ymax'] is not None: 
        #     ymin = pc[hist]['ymin']
        #     ymax = pc[hist]['ymax']
        #     stack[hist].GetYaxis().SetRangeUser(ymin, ymax) 
        # stack[hist].SetMinimum(0.00001)
        if sig_hists_:
            for sample in sig_hists_tmp[hist]:
                for tree in sig_hists_tmp[hist][sample]:
                    if 'N' not in hist: sig_hists_tmp[hist][sample][tree].Rebin(1)
                    sig_hists_tmp[hist][sample][tree].Draw('histsame')
        can.Update()
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = CMS_extraText
        CMS_lumi.CMS_lumi(can, 4, 0)
        #CMS_lumi.CMS_lumi(can, 0, 10)
        #l = rt.TLine(20., 0., 20., 0.2)
        #l.SetLineColor(13)
        #l.SetLineStyle(9)
        #l.SetLineWidth(1)
        #l.Draw()
        leg.Draw()
        leg2.Draw()
        can.Update()
        rt.gPad.RedrawAxis()
        if print_plots:
            if hists_tmp[hist]:
                can.SetLogy()
                first_hist = next(reversed(hists_tmp[hist]))
                ymax = hists_tmp[hist][first_hist].GetMaximum()
                hists_tmp[hist][first_hist].SetMinimum(0.001)
                hists_tmp[hist][first_hist].SetMinimum(0.001)
                #hists_tmp[hist][first_hist].SetMaximum(250*ymax)
                hists_tmp[hist][first_hist].SetMaximum(500)
                can.Update()
                can.SaveAs(out_dir+'/hoverlay_log_'+hist+'_'+suffix_+'.root')
                can.SaveAs(out_dir+'/hoverlay_log_'+hist+'_'+suffix_+'.pdf')
                can.SetLogy(0)
                hists_tmp[hist][first_hist].SetMinimum(0.001)
                hists_tmp[hist][first_hist].SetMaximum(2.0*ymax)
                #hists_tmp[hist][first_hist].SetMaximum(0.3)
                can.Update()
                can.SaveAs(out_dir+'/hoverlay_'+hist+'_'+suffix_+'.root')
                can.SaveAs(out_dir+'/hoverlay_'+hist+'_'+suffix_+'.pdf')
            else:
                can.SetLogy()
                first_sig = next(iter(sig_hists_tmp[hist]))
                first_hist = next(iter(sig_hists_tmp[hist][first_sig]))
                ymax = sig_hists_tmp[hist][first_sig][first_hist].GetMaximum()
                sig_hists_tmp[hist][first_sig][first_hist].SetMinimum(0.001)
                sig_hists_tmp[hist][first_sig][first_hist].SetMinimum(0.001)
                #sig_hists_tmp[hist][first_sig][first_hist].SetMaximum(250*ymax)
                sig_hists_tmp[hist][first_sig][first_hist].SetMaximum(1)
                can.Update()
                can.SaveAs(out_dir+'/hoverlay_log_'+hist+'_'+suffix_+'.root')
                can.SaveAs(out_dir+'/hoverlay_log_'+hist+'_'+suffix_+'.pdf')
                can.SetLogy(0)
                sig_hists_tmp[hist][first_sig][first_hist].SetMinimum(0.001)
                # sig_hists_tmp[hist][first_sig][first_hist].SetMaximum(1.5*ymax)
                sig_hists_tmp[hist][first_sig][first_hist].SetMaximum(0.3)
                can.Update()
                can.SaveAs(out_dir+'/hoverlay_'+hist+'_'+suffix_+'.root')
                can.SaveAs(out_dir+'/hoverlay_'+hist+'_'+suffix_+'.pdf')

    #return stack, leg

def make_stacked_plots(hists_, sig_hists_ = None, print_plots = True, suffix_=''):
    '''
    Makes stacked plots following the samples that are given in the histogram dictionary
    '''
    tdrstyle.setTDRStyle()
    if print_plots:
        if not (os.path.isdir('./plots_'+date)): os.mkdir('./plots_'+date)
    stack = OrderedDict()
    
    n_entries = OrderedDict()
    hists_tmp = OrderedDict()
    if sig_hists_:
        sig_hists_tmp = OrderedDict()
    out_dir = os.path.join('./plots_'+date)
    for sample in hists_:
        for tree in hists_[sample]:
            for hist_name, hist in hists_[sample][tree].items():
                if hist_name not in pc: continue
                if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                if hist.InheritsFrom(rt.TH2.Class()): continue                    
                stack[hist_name] = rt.THStack('stack','')
                n_entries[hist_name] = OrderedDict()
                hists_tmp[hist_name] = OrderedDict()
    for sample in hists_:
        for tree in hists_[sample]:
            for hist_name, hist in hists_[sample][tree].items():
                if hist_name not in pc: continue
                if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                if hist.InheritsFrom(rt.TH2.Class()): continue                    
                n_entries[hist_name][sample] = hist.Integral(0,10000)
                hists_tmp[hist_name][sample] = hist
    if sig_hists_:
        for sample in sig_hists_:
            for tree in sig_hists_[sample]:
                for hist_name, hist in sig_hists_[sample][tree].items():
                    if hist_name not in pc: continue
                    if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                    if hist.InheritsFrom(rt.TH2.Class()): continue                    
                    sig_hists_tmp[hist_name] = OrderedDict()
        for sample in sig_hists_:
            for tree in sig_hists_[sample]:
                for hist_name, hist in sig_hists_[sample][tree].items():
                    if hist_name not in pc: continue
                    if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                    if hist.InheritsFrom(rt.TH2.Class()): continue                    
                    sig_hists_tmp[hist_name][sample] = OrderedDict()
        for sample in sig_hists_:
            for tree in sig_hists_[sample]:
                for hist_name, hist in sig_hists_[sample][tree].items():
                    if hist_name not in pc: continue
                    if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                    if hist.InheritsFrom(rt.TH2.Class()): continue  
                    #if not hist.GetEntries() > 0.: continue
                    #if 'SMS' not in sample: continue                 
                    #if 'TChi' in sample and ('240' not in tree): continue 
                    #if 'TSlep' in sample and ('195' not in tree): continue
                    if 'SMST2' in sample and ('500_490' not in tree and '500_480' not in tree and '500_420' not in tree): continue 
                    sig_hists_tmp[hist_name][sample][tree] = hist
    for hist in n_entries:
        n_entries[hist] = OrderedDict(sorted(n_entries[hist].items(), key=lambda x: x[1]))
        can = make_me_a_canvas()
        can.cd() 
        leg = rt.TLegend(0.45,0.86,0.8,0.92,'','brNDC') 
        leg.SetBorderSize(0)
        leg.SetNColumns(2)
        leg.SetTextSize(0.024)
        leg.SetMargin(0.2)
        #leg.SetFillStyle(0)
        leg2 = rt.TLegend(0.45,0.72,0.80,0.86,'','brNDC') 
        leg2.SetBorderSize(0)
        leg2.SetNColumns(1)
        leg2.SetTextSize(0.024)
        leg2.SetMargin(0.2)
        #leg2.SetFillStyle(0)
        for sample in n_entries[hist]:
            if 'N' not in hist: hists_tmp[hist][sample].Rebin(1)
            # hists_tmp[hist][sample].Scale(1./n_entries[hist][sample])
            hists_tmp[hist][sample].SetLineColor(sc[sample]['color'])
            hists_tmp[hist][sample].SetLineStyle(sc[sample]['style'])
            if sc[sample]['fill']: hists_tmp[hist][sample].SetFillColor(sc[sample]['fill'])
            if sc[sample]['fill_style']: hists_tmp[hist][sample].SetFillStyle(1001)
            #print hist, sample
            stack[hist].Add(hists_tmp[hist][sample])
            leg.AddEntry(hists_tmp[hist][sample], sc[sample]['legend'], 'fl')
        if sig_hists_:
            for sample in sig_hists_tmp[hist]:
                for itr, tree in enumerate(sig_hists_tmp[hist][sample]):
                    # sig_hists_tmp[hist][sample][tree].Scale(1/sig_hists_tmp[hist][sample][tree].Integral())
                    sig_hists_tmp[hist][sample][tree].SetLineColor(sc[sample]['color']+itr)
                    sig_hists_tmp[hist][sample][tree].SetLineStyle(sc[sample]['style'])
                    sig_hists_tmp[hist][sample][tree].SetLineWidth(sc[sample]['width'])
                    if sc[sample]['fill']: sig_hists_tmp[hist][sample][tree].SetFillColor(sc[sample]['fill'])
                    if sc[sample]['fill_style']: sig_hists_tmp[hist][sample][tree].SetFillStyle(sc[sample]['fill_style'])
                    #print hist, sample, tree
                    if 'Events' in tree:
                        stop_m = '500'
                        neut_m = sample.split('_')[-1]
                        if 'T2bW' in sample:
                            sample_n = '-'.join(sample.split('_')[:2])
                        else:
                            sample_n = '-'.join(sample.split('_')[:3])
                            
                        #leg2.AddEntry(sig_hists_tmp[hist][sample][tree], '#splitline{'+sc[sample]['legend'] + ';}{#kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m+'}', 'fl')
                        leg2.AddEntry(sig_hists_tmp[hist][sample][tree], sc[sample]['legend']+'; #kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m, 'fl')
                    else:
                        stop_m = tree.split('_')[1]
                        neut_m = tree.split('_')[2]
                        sample_n = sample.split('_')[0]                
                        #leg2.AddEntry(sig_hists_tmp[hist][sample][tree], '#splitline{'+sc[sample]['legend'] + ';}{#kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m+'}', 'fl')
                        leg2.AddEntry(sig_hists_tmp[hist][sample][tree], sc[sample]['legend']+'; #kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m, 'fl')
        can.cd()
        stack[hist].Draw('hist')
        stack[hist].GetXaxis().SetTitle(pc[hist]['xlabel'])
        stack[hist].GetXaxis().CenterTitle()
        stack[hist].GetXaxis().SetTitleFont(42)
        stack[hist].GetXaxis().SetTitleSize(0.06)
        stack[hist].GetXaxis().SetTitleOffset(1.06)
        stack[hist].GetXaxis().SetLabelFont(42)
        stack[hist].GetXaxis().SetLabelSize(0.05)
        stack[hist].GetYaxis().SetTitle(pc[hist]['ylabel'])
        stack[hist].GetYaxis().CenterTitle()
        stack[hist].GetYaxis().SetTitleFont(42)
        stack[hist].GetYaxis().SetTitleSize(0.06)
        stack[hist].GetYaxis().SetTitleOffset(1.12)
        stack[hist].GetYaxis().SetLabelFont(42)
        stack[hist].GetYaxis().SetLabelSize(0.05)
        can.Update()
        if pc[hist]['xmax'] is not None: 
            xmin = pc[hist]['xmin']
            xmax = pc[hist]['xmax']
            stack[hist].GetXaxis().SetRangeUser(xmin, xmax) 
            can.Update()
        # if pc[hist]['ymax'] is not None: 
        #     ymin = pc[hist]['ymin']
        #     ymax = pc[hist]['ymax']
        #     stack[hist].GetYaxis().SetRangeUser(ymin, ymax) 
        # stack[hist].SetMinimum(0.00001)
        if sig_hists_:
            for sample in sig_hists_tmp[hist]:
                for tree in sig_hists_tmp[hist][sample]:
                    if 'N' not in hist: sig_hists_tmp[hist][sample][tree].Rebin(1)
                    sig_hists_tmp[hist][sample][tree].Draw('histsame')
        can.Update()
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = CMS_extraText
        CMS_lumi.CMS_lumi(can, 4, 0)
        leg.Draw()
        leg2.Draw()
        can.Update()
        if print_plots:
            can.SetLogy()
            ymax = stack[hist].GetMaximum()
            stack[hist].SetMinimum(0.001)
            stack[hist].SetMaximum(2000*ymax)
            #stack[hist].SetMaximum(1.0)
            can.Update()
            can.SaveAs(out_dir+'/hstack_log_'+hist+'_'+suffix_+'.root')
            can.SaveAs(out_dir+'/hstack_log_'+hist+'_'+suffix_+'.pdf')
            can.SetLogy(0)
            stack[hist].SetMinimum(0.001)
            stack[hist].SetMaximum(2.0*ymax)
            can.Update()
            can.SaveAs(out_dir+'/hstack_'+hist+'_'+suffix_+'.root')
            can.SaveAs(out_dir+'/hstack_'+hist+'_'+suffix_+'.pdf')

    #return stack, leg


def make_data_stacked_plots(data_, hists_, sig_hists_ = None, print_plots = True, suffix_=''):
    '''
    Makes stacked plots following the samples that are given in the histogram dictionary
    '''
    tdrstyle.setTDRStyle()
    if print_plots:
        if not (os.path.isdir('./plots_'+date)): os.mkdir('./plots_'+date)
    stack = OrderedDict()
    
    n_entries = OrderedDict()
    data_tmp = OrderedDict()
    hists_tmp = OrderedDict()
    bkg_tot = OrderedDict()
    if sig_hists_:
        sig_hists_tmp = OrderedDict()
    out_dir = os.path.join('./plots_'+date)
    for sample in data_:
        for tree in data_[sample]:
            for hist_name, hist in data_[sample][tree].items():
                if hist_name not in pc: continue
                if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                if hist.InheritsFrom(rt.TH2.Class()): continue                    
                data_tmp[hist_name] = hist
                bkg_tot[hist_name] = hist.Clone("bkg_tot")
                bkg_tot[hist_name].Reset()
    for sample in hists_:
        for tree in hists_[sample]:
            for hist_name, hist in hists_[sample][tree].items():
                if hist_name not in pc: continue
                if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                if hist.InheritsFrom(rt.TH2.Class()): continue                    
                stack[hist_name] = rt.THStack('stack','')
                n_entries[hist_name] = OrderedDict()
                hists_tmp[hist_name] = OrderedDict()
    for sample in hists_:
        for tree in hists_[sample]:
            for hist_name, hist in hists_[sample][tree].items():
                if hist_name not in pc: continue
                if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                if hist.InheritsFrom(rt.TH2.Class()): continue                    
                n_entries[hist_name][sample] = hist.Integral(0,10000)
                if 'TTJets' in sample:
                    hist.Scale(1.199)
                hists_tmp[hist_name][sample] = hist
                bkg_tot[hist_name].Add(hist)
    if sig_hists_:
        for sample in sig_hists_:
            for tree in sig_hists_[sample]:
                for hist_name, hist in sig_hists_[sample][tree].items():
                    if hist_name not in pc: continue
                    if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                    if hist.InheritsFrom(rt.TH2.Class()): continue                    
                    sig_hists_tmp[hist_name] = OrderedDict()
        for sample in sig_hists_:
            for tree in sig_hists_[sample]:
                for hist_name, hist in sig_hists_[sample][tree].items():
                    if hist_name not in pc: continue
                    if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                    if hist.InheritsFrom(rt.TH2.Class()): continue                    
                    sig_hists_tmp[hist_name][sample] = OrderedDict()
        for sample in sig_hists_:
            for tree in sig_hists_[sample]:
                for hist_name, hist in sig_hists_[sample][tree].items():
                    if hist_name not in pc: continue
                    if not hist.InheritsFrom(rt.TH1.Class()): continue                    
                    if hist.InheritsFrom(rt.TH2.Class()): continue  
                    #if not hist.GetEntries() > 0.: continue
                    #if 'SMS' not in sample: continue                 
                    #if 'TChi' in sample and ('240' not in tree): continue 
                    #if 'TSlep' in sample and ('195' not in tree): continue
                    if 'SMST2' in sample and ('500_490' not in tree and '500_480' not in tree and '500_420' not in tree): continue 
                    sig_hists_tmp[hist_name][sample][tree] = hist
    for hist in n_entries:
        n_entries[hist] = OrderedDict(sorted(n_entries[hist].items(), key=lambda x: x[1]))
        can = make_me_a_canvas()
        can.cd()
        rt.SetOwnership(can,False)

    
        leg = rt.TLegend(0.45,0.82,0.8,0.92,'','brNDC') 
        leg.SetBorderSize(0)
        leg.SetNColumns(2)
        leg.SetTextSize(0.024)
        leg.SetMargin(0.2)
        #leg.SetFillStyle(0)
        leg2 = rt.TLegend(0.45,0.72,0.80,0.82,'','brNDC') 
        leg2.SetBorderSize(0)
        leg2.SetNColumns(1)
        leg2.SetTextSize(0.024)
        leg2.SetMargin(0.2)
        #leg2.SetFillStyle(0)
        leg.AddEntry(data_tmp[hist], sc['data']['legend'], 'fl')

        scale = data_tmp[hist].Integral(0,1000) / bkg_tot[hist].Integral(0,1000)
        #print scale
        for sample in n_entries[hist]:
            #if 'N' not in hist: hists_tmp[hist][sample].Rebin(2)
            hists_tmp[hist][sample].Rebin(2)
            hists_tmp[hist][sample].SetLineColor(sc[sample]['color'])
            hists_tmp[hist][sample].SetLineStyle(sc[sample]['style'])
            if sc[sample]['fill']: hists_tmp[hist][sample].SetFillColor(sc[sample]['fill'])
            if sc[sample]['fill_style']: hists_tmp[hist][sample].SetFillStyle(1001)
            #print hist, sample
            stack[hist].Add(hists_tmp[hist][sample])
            leg.AddEntry(hists_tmp[hist][sample], sc[sample]['legend'], 'fl')
        if sig_hists_:
            for sample in sig_hists_tmp[hist]:
                for itr, tree in enumerate(sig_hists_tmp[hist][sample]):
                    # sig_hists_tmp[hist][sample][tree].Scale(1/sig_hists_tmp[hist][sample][tree].Integral())
                    sig_hists_tmp[hist][sample][tree].SetLineColor(sc[sample]['color']+itr)
                    sig_hists_tmp[hist][sample][tree].SetLineStyle(sc[sample]['style'])
                    sig_hists_tmp[hist][sample][tree].SetLineWidth(sc[sample]['width'])
                    if sc[sample]['fill']: sig_hists_tmp[hist][sample][tree].SetFillColor(sc[sample]['fill'])
                    if sc[sample]['fill_style']: sig_hists_tmp[hist][sample][tree].SetFillStyle(sc[sample]['fill_style'])
                    #print hist, sample, tree
                    if 'Events' in tree:
                        stop_m = '500'
                        neut_m = sample.split('_')[-1]
                        if 'T2bW' in sample:
                            sample_n = '-'.join(sample.split('_')[:2])
                        else:
                            sample_n = '-'.join(sample.split('_')[:3])
                            
                        #leg2.AddEntry(sig_hists_tmp[hist][sample][tree], '#splitline{'+sc[sample]['legend'] + ';}{#kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m+'}', 'fl')
                        leg2.AddEntry(sig_hists_tmp[hist][sample][tree], sc[sample]['legend']+'; #kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m, 'fl')
                    else:
                        stop_m = tree.split('_')[1]
                        neut_m = tree.split('_')[2]
                        sample_n = sample.split('_')[0]                
                        #leg2.AddEntry(sig_hists_tmp[hist][sample][tree], '#splitline{'+sc[sample]['legend'] + ';}{#kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m+'}', 'fl')
                        leg2.AddEntry(sig_hists_tmp[hist][sample][tree], sc[sample]['legend']+'; #kern[-0.1]{M}#lower[-0.05]{#kern[-0.1]{(}#lower[0.3]{#tilde{#lower[-0.1]{t}}}#kern[0.1]{)}}='+stop_m+', M(#tilde{#chi}#lower[-0.1]{_{1}}#kern[-0.7]{#lower[0.3]{^{0}}})='+neut_m, 'fl')


        can.cd()
        pad0 = rt.TPad("pad0", "", 0.0, 0.3, 1.0, 1.0)
        pad1 = rt.TPad("pad1", "", 0.0, 0.0, 1.0, 0.3)
        pad0.Draw()
        pad1.Draw()

        pad0.cd()
        pad0.SetBottomMargin(0.05)
        stack[hist].Draw('hist')
        stack[hist].GetXaxis().SetTitle(pc[hist]['xlabel'])
        stack[hist].GetXaxis().CenterTitle()
        stack[hist].GetXaxis().SetTitleFont(42)
        stack[hist].GetXaxis().SetTitleSize(0)
        stack[hist].GetXaxis().SetTitleOffset(1.06)
        stack[hist].GetXaxis().SetLabelFont(42)
        stack[hist].GetXaxis().SetLabelSize(0)
        stack[hist].GetYaxis().SetTitle(pc[hist]['ylabel'])
        stack[hist].GetYaxis().CenterTitle()
        stack[hist].GetYaxis().SetTitleFont(42)
        stack[hist].GetYaxis().SetTitleSize(0.06)
        stack[hist].GetYaxis().SetTitleOffset(1.12)
        stack[hist].GetYaxis().SetLabelFont(42)
        stack[hist].GetYaxis().SetLabelSize(0.05)
        data_tmp[hist].Rebin(2)
        data_tmp[hist].Draw('e1same')
        if pc[hist]['xmax'] is not None: 
            xmin = pc[hist]['xmin']
            xmax = pc[hist]['xmax']
            stack[hist].GetXaxis().SetRangeUser(xmin, xmax) 
            data_tmp[hist].GetXaxis().SetRangeUser(xmin, xmax) 
            bkg_tot[hist].GetXaxis().SetRangeUser(xmin, xmax) 
        # if pc[hist]['ymax'] is not None: 
        #     ymin = pc[hist]['ymin']
        #     ymax = pc[hist]['ymax']
        #     stack[hist].GetYaxis().SetRangeUser(ymin, ymax) 
        # stack[hist].SetMinimum(0.00001)
        if sig_hists_:
            for sample in sig_hists_tmp[hist]:
                for tree in sig_hists_tmp[hist][sample]:
                    if 'N' not in hist: sig_hists_tmp[hist][sample][tree].Rebin(1)
                    sig_hists_tmp[hist][sample][tree].Draw('histsame')
        leg.Draw()
        leg2.Draw()
        pad0.RedrawAxis()
        pad0.Update()

        pad1.cd()
        pad1.SetTopMargin(0.05)
        pad1.SetBottomMargin(0.4)
        ######### making ratio plot and other datay things ############# 
        hratio = data_tmp[hist].Clone('hratio')
        bkg_tot[hist].Rebin(2)
        hratio.Divide(bkg_tot[hist])
        hratio.SetMarkerStyle(20)
        hratio.SetLineStyle(1)
        hratio.SetLineWidth(2)
        hratio.SetLineColor(1)
        hratio.GetXaxis().SetTitle(pc[hist]['xlabel'])
        hratio.GetXaxis().SetTitleSize(0.14)
        hratio.GetXaxis().SetLabelSize(0.14)
        hratio.GetXaxis().SetTickLength(stack[hist].GetXaxis().GetTickLength())
        hratio.GetXaxis().SetTitleOffset(1.20)
        hratio.GetXaxis().SetNdivisions(510)
     
        hratio.GetYaxis().SetTitle("Data/MC")
        hratio.GetYaxis().SetTitleSize(0.14)
        hratio.GetYaxis().SetLabelSize(0.14)
        hratio.GetYaxis().SetTickLength(stack[hist].GetYaxis().GetTickLength())
        hratio.GetYaxis().SetTitleOffset(0.35)
        hratio.GetYaxis().SetNdivisions(504)
        
        hratio.Draw("e0")
        hratio.SetMinimum(0.0)
        hratio.SetMaximum(2.0)
 
        line = rt.TLine(stack[hist].GetXaxis().GetXmin(),1.,stack[hist].GetXaxis().GetXmax(),1.)
        line.Draw()
        pad1.RedrawAxis()

        pad0.cd()
        CMS_lumi.lumi_13TeV = "41.5 fb^{-1}"
        CMS_lumi.writeExtraText = 1
        CMS_lumi.extraText = CMS_extraText
        CMS_lumi.CMS_lumi(pad0, 4, 0)
        can.Update()
        if print_plots:
            pad0.SetLogy()
            ymax = stack[hist].GetMaximum()
            stack[hist].SetMinimum(0.001)
            stack[hist].SetMaximum(800*ymax)
            #stack[hist].SetMaximum(1.0)
            can.Update()
            can.SaveAs(out_dir+'/hstack_log_'+hist+'_'+suffix_+'.root')
            can.SaveAs(out_dir+'/hstack_log_'+hist+'_'+suffix_+'.pdf')
            pad0.SetLogy(0)
            stack[hist].SetMinimum(0.001)
            stack[hist].SetMaximum(1.5*ymax)
            can.Update()
            can.SaveAs(out_dir+'/hstack_'+hist+'_'+suffix_+'.root')
            can.SaveAs(out_dir+'/hstack_'+hist+'_'+suffix_+'.pdf')

    #return stack, leg


def make_1D_plots(hists_, suffix_):
    #print("make_1D_plots(): start")
    tdrstyle.setTDRStyle()
    if not (os.path.isdir('./plots_'+date)): os.mkdir('./plots_'+date)
    for sample in hists_:
        if not (os.path.isdir('./plots_'+date+'/'+sample)): os.mkdir('./plots_'+date+'/'+sample)
        for tree in hists_[sample]:
            if not (os.path.isdir('./plots_'+date+'/'+sample+'/'+tree)): os.mkdir(os.path.join('./plots_'+date, sample, tree))
            out_dir = os.path.join('./plots_'+date, sample, tree)
            for hist_name, hist in hists_[sample][tree].items():
                #print hist_name, sample
                if not hist.InheritsFrom(rt.TH1.Class()): continue                   
                if hist.InheritsFrom(rt.TH2.Class()): continue 
                if hist_name not in pc: continue
                can = make_me_a_canvas()
                can.cd()
                hist.Draw('hist')
                if 'N' not in hist_name: hist.Rebin(2) 
                hist.SetLineColor(sc[sample]['color'])
                hist.SetLineStyle(sc[sample]['style'])
                hist.SetLineWidth(sc[sample]['width'])
                if sc[sample]['fill']: hist.SetFillColor(sc[sample]['fill'])
                if sc[sample]['fill_style']: hist.SetFillStyle(sc[sample]['fill_style'])
                hist.GetXaxis().CenterTitle()
                hist.GetXaxis().SetTitleFont(42)
                hist.GetXaxis().SetTitleSize(0.06)
                hist.GetXaxis().SetTitleOffset(1.06)
                hist.GetXaxis().SetLabelFont(42)
                hist.GetXaxis().SetLabelSize(0.05)
                hist.GetXaxis().SetTitle(pc[hist_name]['xlabel'])
                hist.GetYaxis().CenterTitle()
                hist.GetYaxis().SetTitleFont(42)
                hist.GetYaxis().SetTitleSize(0.06)
                hist.GetYaxis().SetTitleOffset(1.12)
                hist.GetYaxis().SetLabelFont(42)
                hist.GetYaxis().SetLabelSize(0.05)
                hist.GetYaxis().SetTitle(pc[hist_name]['ylabel'])
                hist.GetYaxis().SetRangeUser(0.001,1.2*hist.GetMaximum())
                CMS_lumi.writeExtraText = 1
                CMS_lumi.extraText = CMS_extraText
                CMS_lumi.CMS_lumi(can, 0, 10)
                l = rt.TLatex()
                l.SetTextFont(42)
                l.SetNDC()
                l.SetTextSize(0.055)
                l.SetTextFont(42)
                l.DrawLatex(0.41,0.943,sc[sample]['legend'])
      
                can.Update()
                can.SaveAs(out_dir+'/h_'+hist.GetName()+'_'+suffix_+'.root')
                can.SaveAs(out_dir+'/h_'+hist.GetName()+'_'+suffix_+'.pdf')

def read_in_hists(in_file_):
    print("read_in_hists(): start")
    
    # Use old 2017 version
    USE_OLD_VERSION = True
    
    in_file = rt.TFile(in_file_, 'r')
    hists = OrderedDict()
    for key in in_file.GetListOfKeys():
        #print key.GetName()
        key_name = key.GetName()
        # WARNING: key_name is skipped if it is not in sc
        if key_name not in sc:
            print("The key_name '{0}' is not in 'sc'. Skipping!".format(key_name))
            continue
        sample_dir = in_file.Get(key.GetName())
        hists[key_name] = OrderedDict()
        for tree_key in sample_dir.GetListOfKeys():
            #print tree_key.GetName()
            tree_name = tree_key.GetName()
            tree_dir = sample_dir.Get(tree_key.GetName())
            hists[key_name][tree_name] = OrderedDict()
            for hist_key in tree_dir.GetListOfKeys():
                #print hist_key.GetName()
                hist_name = hist_key.GetName()
                hist = tree_dir.Get(hist_key.GetName())
                # debugging
                #print("key_name: {0}".format(key_name))
                #print("tree_name: {0}".format(tree_name))
                #print("hist_name: {0}".format(hist_name))
                #print("split: {0}".format(hist_name.split('_')))
                #print("start: {0}".format(hist_name.split('_')[:-5]))
                #print("joined: {0}".format('_'.join(hist_name.split('_')[:-5])))
                if 'SMST2bW' in key_name or 'SMST2tt' in key_name:
                    hists[key_name][tree_name]['_'.join(hist_name.split('_')[:-4])] = hist
                elif 'SMS_T2_' in key_name:
                    hists[key_name][tree_name]['_'.join(hist_name.split('_')[:-7])] = hist
                elif 'SMS_TSlep' in key_name:
                    hists[key_name][tree_name]['_'.join(hist_name.split('_')[:-5])] = hist
                elif 'SMS_TChiWZ_mZMin' in key_name:
                    hists[key_name][tree_name]['_'.join(hist_name.split('_')[:-6])] = hist
                elif 'SMS_TChiWZ' in key_name:
                    hists[key_name][tree_name]['_'.join(hist_name.split('_')[:-5])] = hist
                elif 'SMS' in key_name:
                    hists[key_name][tree_name]['_'.join(hist_name.split('_')[:-5])] = hist
                #elif 'DY' in key_name:
                #    hists[key_name][tree_name]['_'.join(hist_name.split('_')[:-2])] = hist
                # old 2017 version
                # WARNING: [:-3] required for old version
                elif USE_OLD_VERSION and '2017' in key_name:
                    hists[key_name][tree_name]['_'.join(hist_name.split('_')[:-3])] = hist
                # current version for run 2:
                # WARNING: [:-5] required for new version
                else:
                    hists[key_name][tree_name]['_'.join(hist_name.split('_')[:-5])] = hist
    # debugging
    print("--- hists ---")
    for key in hists:
        print(" - {0}: {1}".format(key, len(hists[key])))
    print("-------------")
    print("read_in_hists(): end")
    return hists 

# TODO:
# Fix error: Error in <TH1D::Divide>: Cannot divide histograms with different number of bins
# Fix rebinning (works for some ratios, but breaks others)
def make_new_hists(hists_, output_root_file_name, process, results):
    print("make_new_hists(): start")
    output_file = rt.TFile(output_root_file_name, "RECREATE")
    DO_REBIN  = True
    REBIN_NUM = 10
    temp_new = OrderedDict()
    for sample in hists_:
        temp_new[sample] = OrderedDict()
        for tree in hists_[sample]:
            if '4bd' in sample and sample.split('_')[1] not in tree:
                continue
            temp_new[sample][tree] = OrderedDict()
            for hist_name, hist in hists_[sample][tree].items():
                new_hist = None
                if 'all' in hist_name:
                    #print sample, tree, hist_name
                    
                    new_hist = hist_name.replace('all', 'all_div_nojets')
                    temp_new[sample][tree][new_hist] = hist.Clone(hist.GetName().replace('all', 'all_div_nojets'))
                    # rebin hists before dividing
                    #if DO_REBIN:
                    #    temp_new[sample][tree][new_hist].Rebin(REBIN_NUM)
                    #    hists_[sample][tree][hist_name.replace('all','nojets')].Rebin(REBIN_NUM)
                    temp_new[sample][tree][new_hist].Divide(hists_[sample][tree][hist_name.replace('all','nojets')])
                    
                    new_hist_2 = hist_name.replace('all', 'all_div_ntrk')
                    temp_new[sample][tree][new_hist_2] = hist.Clone(hist.GetName().replace('all', 'all_div_ntrk'))
                    # rebin hists before dividing
                    #if DO_REBIN:
                    #    temp_new[sample][tree][new_hist_2].Rebin(REBIN_NUM)
                    #    hists_[sample][tree][hist_name.replace('all','ntrk')].Rebin(REBIN_NUM)
                    temp_new[sample][tree][new_hist_2].Divide(hists_[sample][tree][hist_name.replace('all','ntrk')])
                    
                    #zero_value = temp_new[sample][tree][new_hist].GetBinContent(1)
                    #temp_new[sample][tree][new_hist].Scale(1./zero_value)
                    #for ibin in xrange(temp_new[sample][tree][new_hist].GetNbinsX()):
                    #    bin_val = temp_new[sample][tree][new_hist].GetBinContent(ibin)
                    #    temp_new[sample][tree][new_hist].SetBinContent(ibin, bin_val / zero_value)
                elif 'discr' in hist_name:
                    if 'ntrk' in hist_name:
                        new_hist = hist_name.replace('discr_ntrk', 'discr_ntrk_div_nojets')
                        temp_new[sample][tree][new_hist] = hist.Clone(hist.GetName().replace('discr_ntrk','discr_ntrk_div_nojets'))
                        # rebin hists before dividing
                        #if DO_REBIN:
                        #    temp_new[sample][tree][new_hist].Rebin(REBIN_NUM)
                        #    hists_[sample][tree][hist_name.replace('discr_ntrk','nojets')].Rebin(REBIN_NUM)
                        temp_new[sample][tree][new_hist].Divide(hists_[sample][tree][hist_name.replace('discr_ntrk','nojets')])

                        new_hist_2 = hist_name.replace('discr_ntrk', 'discr_ntrk_div_ntrk')
                        temp_new[sample][tree][new_hist_2] = hist.Clone(hist.GetName().replace('discr_ntrk','discr_ntrk_div_ntrk'))
                        # rebin hists before dividing
                        #if DO_REBIN:
                        #    temp_new[sample][tree][new_hist_2].Rebin(REBIN_NUM)
                        #    hists_[sample][tree][hist_name.replace('discr_ntrk','ntrk')].Rebin(REBIN_NUM)
                        temp_new[sample][tree][new_hist_2].Divide(hists_[sample][tree][hist_name.replace('discr_ntrk','ntrk')])
                    else:
                        den_name        = hist_name.replace('discr','nojets')
                        ratio_name      = hist_name.replace('discr', 'discr_div_nojets')
                        long_name       = hist.GetName()
                        new_long_name   = hist.GetName().replace('discr','discr_div_nojets') 
                        # print names:
                        #print("# --------------------------------------- #")
                        #print("hist_name: {0}".format(hist_name))
                        #print("den_name: {0}".format(den_name))
                        #print("ratio_name: {0}".format(ratio_name))
                        #print("long_name: {0}".format(long_name))
                        #print("new_long_name: {0}".format(new_long_name))
                        #print("# --------------------------------------- #")
                        temp_new[sample][tree][ratio_name] = hist.Clone(new_long_name)
                        # rebin hists before dividing
                        if DO_REBIN:
                            temp_new[sample][tree][ratio_name].Rebin(REBIN_NUM)
                            hists_[sample][tree][den_name].Rebin(REBIN_NUM)
                        # number of bins:
                        #print("{0}: n_bins = {1}".format(ratio_name, temp_new[sample][tree][ratio_name].GetNbinsX()))
                        #print("{0}: n_bins = {1}".format(den_name,   hists_[sample][tree][den_name].GetNbinsX()))
                        # calc eff for isB
                        if "isB" in new_long_name:
                            # number of events:
                            num_events  = getIntegral(temp_new[sample][tree][ratio_name])
                            den_events  = getIntegral(hists_[sample][tree][den_name])
                            ratio       = num_events / den_events
                            #print("CALC: number of events (numerator) = {0}".format(num_events))
                            #print("CALC: number of events (denominator) = {0}".format(den_events))
                            #print("CALC: ratio = {0:.3f}".format(ratio))
                            results[process]["num_events"]  = num_events
                            results[process]["den_events"]  = den_events
                            results[process]["ratio"]       = ratio
                        # efficiency: do this before taking ratio!!
                        # TEfficiency::CheckConsistency(h_pass,h_total)
                        if rt.TEfficiency.CheckConsistency(temp_new[sample][tree][ratio_name], hists_[sample][tree][den_name]):
                            #print("PASS CheckConsistency: {0} and {1}".format(ratio_name, den_name))
                            h_eff = rt.TEfficiency(temp_new[sample][tree][ratio_name], hists_[sample][tree][den_name])
                            #print("(1) h_eff.GetName(): {0}".format(h_eff.GetName()))
                            h_eff_name = new_long_name + "_eff"  
                            h_eff.SetName(h_eff_name)
                            #print("(2) h_eff.GetName(): {0}".format(h_eff.GetName()))
                            h_eff.Write()
                        # ratio
                        temp_new[sample][tree][ratio_name].Divide(hists_[sample][tree][den_name])
                        # save ratio to file
                        temp_new[sample][tree][ratio_name].Write()

                    #zero_value = temp_new[sample][tree][new_hist].GetBinContent(1)
                    #temp_new[sample][tree][new_hist].Scale(1./zero_value)
                    #for ibin in xrange(temp_new[sample][tree][new_hist].GetNbinsX()):
                    #    bin_val = temp_new[sample][tree][new_hist].GetBinContent(ibin)
                    #    temp_new[sample][tree][new_hist].SetBinContent(ibin, bin_val / zero_value)
    hists_.update(temp_new)
    print("make_new_hists(): end")
    return hists_

def read_in_hists_opt(in_file_):
    in_file = rt.TFile(in_file_, 'r')
    hists = OrderedDict()
    for key in in_file.GetListOfKeys():
        key_name = key.GetName()
        #print key_name
        key_split = key_name.split('__')
        sample = key_split[0]
        tree = key_split[1]
        hist_name = key_split[2]
        
        if sample not in hists.keys():
            hists[sample] = OrderedDict()
        if tree not in hists[sample].keys():
            hists[sample][tree] = OrderedDict()

        hists[sample][tree][hist_name] = in_file.Get(key_name)
    return hists

if __name__ == "__main__":
    #data_file = 'output_data_hist_sv_check_0p3_upperMet_18Nov20.root'
    #data_hists = read_in_hists(data_file)
    
    #signal_file = './output_signal_risr_95_mixed_10Jan20.root'
    #signal_file = 'output_signal_hist_1l_regions_2Dec20.root'
    #signal_file = 'output_signal_hist_2D_region_vars_21sam_14Jan21.root'
      
    #signal_file = 'output_signal_hist_sv_eff_06Dec20.root'
    #sig_hists = read_in_hists(signal_file)
    #suffix = '0p95'
    #suffix = 'sigs'
    #sig_hists_new = make_new_hists(sig_hists)
    #print sig_hists_new
    #make_1D_plots(sig_hists, suffix)

    #background_file = './output_background_risr_95_mixed_10Jan20.root'
    #background_file = 'output_background_1l_10Feb20.root'
    #background_file = 'output_background_hist_sv_2D_flav_3Jan20.root'
    #background_file = 'output_background_hist_2D_region_vars_21sam_14Jan21_tot.root'
    #background_file = 'output_background_hist_1l_regions_2Dec20.root'
    #background_file = 'output_background_hist_dphimetv_3Dec20.root'
    #background_file = 'output_background_hist_sv_b_eff_09Dec20.root'
    
    #print b_hists
    #make_1D_plots(b_hists, suffix)
    #make_stacked_plots(b_hists, sig_hists, True, suffix)
    #make_data_stacked_plots(data_hists, b_hists, sig_hists, True, suffix)
    #make_overlay_plot(sig_hists_new, suffix)
    #make_overlay_plot(b_hists_new, suffix)
    #make_2D_plots(sig_hists, suffix)
    #make_2D_plots(b_hists, suffix)
    
    # old 2017 version
    #background_file = 'data/output_background_hist_sv_b_eff_09Dec20.root'
    
    #background_file = 'output_background_hist_b_eff_TTJets_FastSim_2016_17May22.root'
    #output_name = "TTJets_FastSim_2016"
    #suffix = 'regions'
    
    suffix = 'eff'
    # old input from Erich (full sim 2017, all backgrounds)
    file_map_v1 = {
        "Old_Tot2017" : "data/output_background_hist_sv_b_eff_09Dec20.root",
    }
    # new inputs from Caleb (fast/full sim, 2016, 2017, 2018, only TTJets DiLepton)
    # v5 ntuples
    file_map_v5 = {
        "TTJets_FastSim_2016" : "output_files_23May22/output_background_hist_b_eff_TTJets_FastSim_2016.root",
        "TTJets_FastSim_2017" : "output_files_23May22/output_background_hist_b_eff_TTJets_FastSim_2017.root",
        "TTJets_FastSim_2018" : "output_files_23May22/output_background_hist_b_eff_TTJets_FastSim_2018.root",
        "TTJets_FullSim_2016" : "output_files_23May22/output_background_hist_b_eff_TTJets_FullSim_2016.root",
        "TTJets_FullSim_2017" : "output_files_23May22/output_background_hist_b_eff_TTJets_FullSim_2017.root",
        "TTJets_FullSim_2018" : "output_files_23May22/output_background_hist_b_eff_TTJets_FullSim_2018.root",
    }
    # v6 ntuples
    file_map_v6p0 = {
        "TTJets_FastSim_2016" : "output_files_24May22/output_background_hist_b_eff_TTJets_FastSim_2016.root",
        "TTJets_FastSim_2017" : "output_files_24May22/output_background_hist_b_eff_TTJets_FastSim_2017.root",
        "TTJets_FastSim_2018" : "output_files_24May22/output_background_hist_b_eff_TTJets_FastSim_2018.root",
        "TTJets_FullSim_2016" : "output_files_24May22/output_background_hist_b_eff_TTJets_FullSim_2016.root",
        "TTJets_FullSim_2017" : "output_files_24May22/output_background_hist_b_eff_TTJets_FullSim_2017.root",
        "TTJets_FullSim_2018" : "output_files_24May22/output_background_hist_b_eff_TTJets_FullSim_2018.root",
    }
    file_map_v6p1 = {
        "TTJets_FastSim_2016" : "output_files_2022_07_13/output_background_hist_b_eff_TTJets_FastSim_2016.root",
        "TTJets_FastSim_2017" : "output_files_2022_07_13/output_background_hist_b_eff_TTJets_FastSim_2017.root",
        "TTJets_FastSim_2018" : "output_files_2022_07_13/output_background_hist_b_eff_TTJets_FastSim_2018.root",
        "TTJets_FullSim_2016" : "output_files_2022_07_13/output_background_hist_b_eff_TTJets_FullSim_2016.root",
        "TTJets_FullSim_2017" : "output_files_2022_07_13/output_background_hist_b_eff_TTJets_FullSim_2017.root",
        "TTJets_FullSim_2018" : "output_files_2022_07_13/output_background_hist_b_eff_TTJets_FullSim_2018.root",
    }

    input_file_map          = file_map_v1
    #input_file_map          = file_map_v6p1
    output_dir              = "sv_eff"
    output_json_file_name   = "{0}/sv_eff.json".format(output_dir)
    tools.makeDir(output_dir)

    results = {}
    
    for process in input_file_map:
        print(" - Process {0}".format(process))
        results[process]        = {}
        background_file         = input_file_map[process]
        output_root_file_name   = "{0}/{1}_sv_eff.root".format(output_dir, process)
        b_hists                 = read_in_hists(background_file)
        b_hists_new             = make_new_hists(b_hists, output_root_file_name, process, results)
        make_overlay_plot(b_hists_new, suffix, process)

    with open(output_json_file_name, 'w') as output_json:
        json.dump(results, output_json, indent=4, sort_keys=True)

