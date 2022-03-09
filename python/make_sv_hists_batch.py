#!/usr/bin/env python

"""
New thing to try out, doing analysis with numpy, converting back to ROOT to do histogramming
Creator: Erich Schmitz
Date: Feb 22, 2019
"""

from time import strftime, localtime
import argparse as arg
import ROOT as rt
import numpy as np
import root_numpy as rnp
import numpy.lib.recfunctions as rfc
import os
from file_table_functions import *
from collections import OrderedDict
import time
import pickle
from array import array

rt.gROOT.SetBatch()
rt.TH1.SetDefaultSumw2()
rt.TH1.AddDirectory(rt.kFALSE)
date = strftime('%d%b%y', localtime())
########## get_histograms function template ############

########################################################

selections_str = [
        'base',
        'base_sv',
        'base_pre',
        'base_pre_sv',
        #'emu_lowmet',
        #'emu_lowmet_sv',
        #'emu_highmet',
        #'emu_highmet_sv',
        #'2lep',
        #'2lep_sv',
        #'1lep',
        #'1lep_sv',
        #'1lep_l0p8',
        #'1lep_l0p8_sv',
        #'0lep',
        #'0lep_sv',
    ]

def get_histograms(list_of_files_, variable_list_, cuts_to_apply_=None):
    
    hist = OrderedDict()
    counts = OrderedDict()
    for sample in list_of_files_:
        hist[sample] = OrderedDict()
        counts[sample] = OrderedDict()
        for tree_name in list_of_files_[sample]['trees']:
            print '\nReserving Histograms for:', sample, tree_name 
            hist[sample][tree_name] = OrderedDict()
            counts[sample][tree_name] = OrderedDict()
            # Reserve histograms

            for sel in selections_str:
                hist[sample][tree_name]['RISR_MPE_'+sel]    = rt.TH2D('_'.join(['RISR_MPE', sel, sample, tree_name]), '', 100, 0, 1.5, 100, 0, 100)
                hist[sample][tree_name]['MET_'+sel]         = rt.TH1D('_'.join(['MET', sel, sample, tree_name]), '', 100, 50, 500)
                hist[sample][tree_name]['MET_1bin'+sel]     = rt.TH1D('_'.join(['MET_1bin', sel, sample, tree_name]), '', 1, 50, 500)
                #hist[sample][tree_name]['PT_Eta_'+sel] = rt.TH2D('_'.join(['PT_Eta', sel, sample, tree_name]), '', 18, 2, 20, 2, -2.4, 2.4)
                #hist[sample][tree_name]['PT_SV_'+sel] = rt.TH1D('_'.join(['PT_SV', sel, sample, tree_name]), '', 50, 2, 20)
                #hist[sample][tree_name]['PT_SV_1GeV_'+sel] = rt.TH1D('_'.join(['PT_SV_1GeV', sel, sample, tree_name]), '', 18, 2, 20)
                #hist[sample][tree_name]['PT_SV_1bin_'+sel] = rt.TH1D('_'.join(['PT_SV_1bin', sel, sample, tree_name]), '', 1, 2, 20)
                #hist[sample][tree_name]['Eta_SV_'+sel] = rt.TH1D('_'.join(['Eta_SV', sel, sample, tree_name]), '', 50, -2.4, 2.4)
                #hist[sample][tree_name]['Eta_SV_2bin_'+sel] = rt.TH1D('_'.join(['Eta_SV_2bin', sel, sample, tree_name]), '', 2, -2.4, 2.4)
                #hist[sample][tree_name]['Eta_SV_1bin_'+sel] = rt.TH1D('_'.join(['Eta_SV_1bin', sel, sample, tree_name]), '', 2, -2.4, 2.4)
                #hist[sample][tree_name]['Eta_SV_2binV2_'+sel] = rt.TH1D('_'.join(['Eta_SV_2binV2', sel, sample, tree_name]), '', 2, 0, 3)
                #hist[sample][tree_name]['M_SV_'+sel] = rt.TH1D('_'.join(['M_SV', sel, sample, tree_name]), '', 50, 0, 5)
                #hist[sample][tree_name]['Ndof_SV_'+sel] = rt.TH1D('_'.join(['Ndof_SV', sel, sample, tree_name]), '', 50, 0, 20)
                #hist[sample][tree_name]['Dxy_SV_'+sel] = rt.TH1D('_'.join(['Dxy_SV', sel, sample, tree_name]), '', 50, 0, 10)
                #hist[sample][tree_name]['DxySig_SV_'+sel] = rt.TH1D('_'.join(['DxySig_SV', sel, sample, tree_name]), '', 50, 0, 10)
                #hist[sample][tree_name]['D3d_SV_'+sel] = rt.TH1D('_'.join(['D3d_SV', sel, sample, tree_name]), '', 50, 0, 5)
                #hist[sample][tree_name]['D3dSig_SV_'+sel] = rt.TH1D('_'.join(['D3dSig_SV', sel, sample, tree_name]), '', 50, 0, 30)
                #hist[sample][tree_name]['CosTheta_SV_'+sel] = rt.TH1D('_'.join(['CosTheta_SV', sel, sample, tree_name]), '', 50, 0.95, 1)
                #hist[sample][tree_name]['ProbB_SV_'+sel] = rt.TH1D('_'.join(['ProbB_SV', sel, sample, tree_name]), '', 50, 0, 1)
                #hist[sample][tree_name]['Ndof_PT_'+sel] = rt.TH2D('_'.join(['Ndof_PT', sel, sample, tree_name]), '', 50, 0, 20, 50, 2, 20)
                #hist[sample][tree_name]['Ndof_Eta_'+sel] = rt.TH2D('_'.join(['Ndof_Eta', sel, sample, tree_name]), '', 50, 0, 20, 50, -2.4, 2.4)
                #hist[sample][tree_name]['Dxy_PT_'+sel] = rt.TH2D('_'.join(['Dxy_PT', sel, sample, tree_name]), '', 50, 0, 10, 50, 2, 20)
                #hist[sample][tree_name]['Dxy_Eta_'+sel] = rt.TH2D('_'.join(['Dxy_Eta', sel, sample, tree_name]), '', 50, 0, 10, 50, -2.4, 2.4)
                #hist[sample][tree_name]['D3d_PT_'+sel] = rt.TH2D('_'.join(['D3d_PT', sel, sample, tree_name]), '', 50, 0, 5, 50, 2, 20)
                #hist[sample][tree_name]['D3d_Eta_'+sel] = rt.TH2D('_'.join(['D3d_Eta', sel, sample, tree_name]), '', 50, 0, 5, 50, -2.4, 2.4)
                #hist[sample][tree_name]['D3dSig_PT_'+sel] = rt.TH2D('_'.join(['D3dSig_PT', sel, sample, tree_name]), '', 50, 0, 30, 50, 2, 20)
                #hist[sample][tree_name]['D3dSig_Eta_'+sel] = rt.TH2D('_'.join(['D3dSig_Eta', sel, sample, tree_name]), '', 50, 0, 30, 50, -2.4, 2.4)
                #hist[sample][tree_name]['CosTheta_PT_'+sel] = rt.TH2D('_'.join(['CosTheta_PT', sel, sample, tree_name]), '', 50, 0.95, 1.0, 50, 2, 20)
                #hist[sample][tree_name]['CosTheta_Eta_'+sel] = rt.TH2D('_'.join(['CosTheta_Eta', sel, sample, tree_name]), '', 50, 0.95, 1.0, 50, -2.4, 2.4)
                #hist[sample][tree_name]['M_PT_'+sel] = rt.TH2D('_'.join(['M_PT', sel, sample, tree_name]), '', 50, 0, 5, 50, 2, 20)
                #hist[sample][tree_name]['M_Eta_'+sel] = rt.TH2D('_'.join(['M_Eta', sel, sample, tree_name]), '', 50, 0, 5, 50, -2.4, 2.4)
 

        for ifile, in_file in enumerate(list_of_files_[sample]['files']):
            for tree_name in list_of_files_[sample]['trees']:
                sample_array = get_tree_info_singular(sample, in_file, tree_name, variable_list_, cuts_to_apply_)
                if sample_array is None: continue

                print '\nGetting Histograms for:', sample, tree_name, in_file
                print 'file: ', ifile+1, ' / ', len(list_of_files_[sample]['files'])

                met         = np.array(sample_array['MET'])
                risr        = np.array(sample_array['RISR'])
                ptisr       = np.array(sample_array['PTISR'])
                ptcm        = np.array(sample_array['PTCM'])
                dphicmi     = np.array(sample_array['dphiCMI'])
                dphimetv    = np.array(sample_array['dphiMET_V'])
                mxpa        = np.array(sample_array['MX3a_BoostT'])
                mxpb        = np.array(sample_array['MX3b_BoostT'])
                
                if len(met) == 0:
                    continue 

                #emu_trig = np.array(sample_array['EMutrigger'])
                met_trig = np.array(sample_array['METtrigger'])

                nsv             = np.array(sample_array['NSV'])
                nsv_s           = np.array(sample_array['NSV_S'])
                nsv_isr         = np.array(sample_array['NSV_ISR'])
                pt_sv           = np.array(sample_array['PT_SV'])
                eta_sv          = np.array(sample_array['Eta_SV'])
                #probb_sv       = np.array(sample_array['ProbB_SV'])
                #flav_sv        = np.array(sample_array['Flavor_SV'])
                #flav_sv        = np.array([pt<0 for pt in pt_sv])
                #matched_sv     = np.array(sample_array['MatchedJetID_SV'])
                #matched_sv     = np.array([pt<0 for pt in pt_sv])
                #ndof_sv        = np.array(sample_array['Ndof_SV'])
                #mass_sv        = np.array(sample_array['M_SV'])
                #dxy_sv         = np.array(sample_array['Dxy_SV'])
                #dxysig_sv      = np.array(sample_array['DxySig_SV'])
                #d3d_sv         = np.array(sample_array['D3d_SV'])
                #d3dsig_sv      = np.array(sample_array['D3dSig_SV'])
                #cos_sv         = np.array(sample_array['CosTheta_SV'])

                nbjet       = np.array(sample_array['Nbjet'])
                nbjet_isr   = np.array(sample_array['Nbjet_ISR'])
                nbjet_s     = np.array(sample_array['Nbjet_S'])

                njet        = np.array(sample_array['Njet'])
                pt_jet      = np.array(sample_array['PT_jet'])
                eta_jet     = np.array(sample_array['Eta_jet'])
                btag_jet    = np.array(sample_array['Btag_jet'])

                weight      = np.array(sample_array['weight'])

                nlep        = np.array(sample_array['Nlep'])
                phi_lep     = np.array(sample_array['Phi_lep'])
                id_lep      = np.array(sample_array['ID_lep'])
                pt_lep      = np.array(sample_array['PT_lep'])
                mini_lep    = np.array(sample_array['MiniIso_lep'])
                pf_lep      = np.array(sample_array['RelIso_lep'])
                sip3d_lep   = np.array(sample_array['SIP3D_lep'])
                pdgid_lep   = np.array(sample_array['PDGID_lep'])
                ch_lep      = np.array(sample_array['Charge_lep'])
                
                #if 'SMS_T2_4bd_490' in sample:
                #    weight = np.array([(137000 * 0.51848) / 1207007. for w in weight])
                
                if 'data' in sample:
                    weight = np.ones(len(weight))
                elif '2016' in sample:
                    weight = 35.922 * weight
                elif '2017' in sample:
                    weight = 41.529 * weight
                elif '2018' in sample:
                    weight = 59.74 * weight
                else:
                    weight = 41.529 * weight
  
                mpe = np.sqrt( (mxpa**2 + mxpb**2) / 2)

                #discr_0p3_pt8 = np.array([(prob>0.3)*(pt<8) for prob, pt in zip(probb_sv, pt_sv)])
                #discr_0p3_20_pt8 = np.array([(prob>0.3)*(pt>=8) for prob, pt in zip(probb_sv, pt_sv)])
                #eta_g1p5 = np.array([np.abs(eta)>=1.5 for eta in eta_sv])
                #eta_l1p5 = np.array([np.abs(eta)>=1.5 for eta in eta_sv])
                #keep_sv = ((discr_0p3_20_pt8)+(discr_0p3_pt8))
                #keep_sv_etag1p5 = ((discr_0p3_20_pt8)+(discr_0p3_pt8))*eta_g1p5
                #keep_sv_etal1p5 = ((discr_0p3_20_pt8)+(discr_0p3_pt8))*eta_l1p5
                #keep_step = ((discr_0p3_20_pt8)+(discr_0p3_pt8))*(discr_ndof_g1p8)

                #nsv_anti_eta = np.array([len(eta[(np.abs(eta)>=1.5)*(keep)]) for eta, keep in zip(eta_sv, keep_sv)])
                #nsv = np.array([len(match[(match<2)*(keep)*(pt>2)]) for match, keep, pt in zip(matched_sv, keep_sv, pt_sv)])

                #flav_sv = np.array([flav[(match<2)*(keep)*(pt>2)] for flav, match, keep, pt in zip(flav_sv, matched_sv, keep_sv, pt_sv)])
                #ndof_sv = np.array([ndof[(match<2)*(keep)*(pt>2)] for ndof, match, keep, pt in zip(ndof_sv, matched_sv, keep_sv, pt_sv)])
                #eta_sv = np.array([eta[(match<2)*(keep)*(pt>2)] for eta, match, keep, pt in zip(eta_sv, matched_sv, keep_sv, pt_sv)])
                #mass_sv = np.array([mass[(match<2)*(keep)*(pt>2)] for mass, match, keep, pt in zip(mass_sv, matched_sv, keep_sv, pt_sv)])
                #probb_sv = np.array([probb[(match<2)*(keep)*(pt>2)] for probb, match, keep, pt in zip(probb_sv, matched_sv, keep_sv, pt_sv)])
                #dxy_sv = np.array([dxy[(match<2)*(keep)*(pt>2)] for dxy, match, keep, pt in zip(dxy_sv, matched_sv, keep_sv, pt_sv)])
                ##dxysig_sv = np.array([dxysig[(match<2)*(keep)*(pt>2)] for dxysig, match, keep, pt in zip(dxysig_sv, matched_sv, keep_sv, pt_sv)])
                #d3d_sv = np.array([d3d[(match<2)*(keep)*(pt>2)] for d3d, match, keep, pt in zip(d3d_sv, matched_sv, keep_sv, pt_sv)])
                #d3dsig_sv = np.array([d3dsig[(match<2)*(keep)*(pt>2)] for d3dsig, match, keep, pt in zip(d3dsig_sv, matched_sv, keep_sv, pt_sv)])
                #cos_sv = np.array([cos[(match<2)*(keep)*(pt>2)] for cos, match, keep, pt in zip(cos_sv, matched_sv, keep_sv, pt_sv)])
                #pt_sv = np.array([pt[(match<2)*(keep)*(pt>2)] for match, keep, pt in zip(matched_sv, keep_sv, pt_sv)])


                zero_lep = nlep == 0 
                one_lep  = nlep == 1 
                two_lep  = nlep >= 2 
                ################        Medium       #####################
                id_lep      = np.array([lep[::2] for lep in id_lep])                
                mini_lep    = np.array([mini[lid>=3]*pt[lid>=3] for mini, lid, pt in zip(mini_lep, id_lep, pt_lep)])
                pf_lep      = np.array([pf[lid>=3]*pt[lid>=3] for pf, lid, pt in zip(pf_lep, id_lep, pt_lep)])
                sip3d_lep   = np.array([ips[lid>=3] for ips, lid in zip(sip3d_lep, id_lep)])
                pt_lep      = np.array([ips[lid>=3] for ips, lid in zip(pt_lep, id_lep)])
                pdgid_lep   = np.array([ips[lid>=3] for ips, lid in zip(pdgid_lep, id_lep)])
                ch_lep      = np.array([ips[lid>=3] for ips, lid in zip(ch_lep, id_lep)])

                iso_sip_check = np.array([(mini<4)*(pf<4)*(sip<2) for mini, pf, sip in zip(mini_lep, pf_lep, sip3d_lep)])

                gold_2_mask  = np.array([ True if len(pt[iso*(pt>24)]) == 2 and two else False for iso, two, pt in zip(iso_sip_check, two_lep, pt_lep)])
                gold_22_mask = np.array([ True if len(pt[iso]) == 2 and two else False for iso, two, pt in zip(iso_sip_check, two_lep, pt_lep)])
                gold_1_mask  = np.array([ True if len(iso[iso]) == 1 and one else False for iso, one in zip(iso_sip_check, one_lep)])
              
                n_mu  = np.array([len(lep[(np.abs(lep) == 13)*iso*(pt>25)]) for iso, lep, pt in zip(iso_sip_check, pdgid_lep, pt_lep)])
                n_el  = np.array([len(lep[(np.abs(lep) == 11)*iso*(pt>24)]) for iso, lep, pt in zip(iso_sip_check, pdgid_lep, pt_lep)])
                n_pos = np.array([len(lep[(lep > 0)*iso*(pt>24)]) for iso, lep, pt in zip(iso_sip_check, ch_lep, pt_lep)])
                n_neg = np.array([len(lep[(lep < 0)*iso*(pt>24)]) for iso, lep, pt in zip(iso_sip_check, ch_lep, pt_lep)])

                #b_sv = np.array([np.abs(sv)==5 for sv in flav_sv])
                #c_sv = np.array([np.abs(sv)==4 for sv in flav_sv])
                #light_sv = np.array([(np.abs(sv)!=5)*(np.abs(sv)!=4) for sv in flav_sv])                

                risr_0p5    = risr > 0.5 
                met_50      = met > 50.
                met_l175    = met <= 175.
                met_150     = met > 150.
                met_175     = met > 175.
                met_0       = met > 0.
                ptisr_250   = ptisr > 250
                metv        = np.abs(dphimetv) < np.pi/2.
                risr_l0p8   = risr < 0.8
                one_el      = n_el >= 1
                one_mu      = n_mu >= 1
                one_pos     = n_pos >= 1
                one_neg     = n_neg >= 1

                no_isrb     = nbjet_isr < 1
                one_bjet    = nbjet == 1
                jet_veto    = nbjet = njet

                ge_one_sv   = nsv >= 1

                #pass_di_trig = emu_trig > 0
                pass_met_trig = met_trig > 0

                dphi_cut_75     = (ptcm<75)  * (dphicmi<=np.pi/4)  # 400x - 400x^2 - y
                dphi_cut_100    = (ptcm<100) * (dphicmi>(3*np.pi)/4)  # 400x - 400x^2 - y
                dphi_cut_other  = (ptcm>0)   * ((dphicmi > np.pi/4) * (dphicmi <= (3*np.pi)/4))

                dphicmi_ptcm_cut = dphi_cut_100 + dphi_cut_75 + dphi_cut_other

                evt_base_selection_mask = np.all([met_150], axis=0)
                evt_base_sv_selection_mask = np.all([met_150, ge_one_sv], axis=0)
                evt_base_pre_selection_mask = np.all([met_150, risr_0p5, ptisr_250, dphicmi_ptcm_cut, metv], axis=0)
                evt_base_pre_sv_selection_mask = np.all([met_150, risr_0p5, ptisr_250, dphicmi_ptcm_cut, metv, ge_one_sv], axis=0)
                #evt_emu_lowmet_selection_mask = np.all([met_50, met_l175, gold_2_mask, one_el, one_mu, one_pos, one_neg, one_bjet, jet_veto, pass_di_trig], axis=0)
                #evt_emu_lowmet_sv_selection_mask = np.all([met_50, met_l175, gold_2_mask, one_el, one_mu, one_pos, one_neg, one_bjet, jet_veto, ge_one_sv, pass_di_trig], axis=0)
                #evt_emu_highmet_selection_mask = np.all([met_175, gold_2_mask, one_el, one_mu, one_pos, one_neg, one_bjet, jet_veto, pass_di_trig], axis=0)
                #evt_emu_highmet_sv_selection_mask = np.all([met_175, gold_2_mask, one_el, one_mu, one_pos, one_neg, one_bjet, jet_veto, ge_one_sv, pass_di_trig], axis=0)

                #evt_2lep_selection_mask = np.all([met_175, risr_0p5, gold_22_mask, pass_met_trig], axis=0)
                #evt_2lep_sv_selection_mask = np.all([met_175, gold_22_mask, ge_one_sv, pass_met_trig], axis=0)
                #evt_1lep_l0p8_selection_mask = np.all([met_175, gold_1_mask, risr_l0p8, no_isrb, pass_met_trig], axis=0)
                #evt_1lep_l0p8_sv_selection_mask = np.all([met_175, gold_1_mask, risr_l0p8, no_isrb, ge_one_sv, pass_met_trig], axis=0)
                #evt_1lep_selection_mask = np.all([met_175, risr_0p5, gold_1_mask, pass_met_trig], axis=0)
                #evt_1lep_sv_selection_mask = np.all([met_175, gold_1_mask, no_isrb, ge_one_sv, pass_met_trig], axis=0)
                #evt_0lep_selection_mask = np.all([met_175, zero_lep, no_isrb, pass_met_trig], axis=0)
                #evt_0lep_sv_selection_mask = np.all([met_175, zero_lep, no_isrb, ge_one_sv, pass_met_trig], axis=0)

                selections = [
                    evt_base_selection_mask,
                    evt_base_sv_selection_mask,
                    evt_base_pre_selection_mask,
                    evt_base_pre_sv_selection_mask,
                    #evt_emu_lowmet_selection_mask,
                    #evt_emu_lowmet_sv_selection_mask,
                    #evt_emu_highmet_selection_mask,
                    #evt_emu_highmet_sv_selection_mask,
                    #evt_2lep_selection_mask,
                    #evt_2lep_sv_selection_mask,
                    #evt_1lep_selection_mask,
                    #evt_1lep_sv_selection_mask,
                    #evt_1lep_l0p8_selection_mask,
                    #evt_1lep_l0p8_sv_selection_mask,
                    #evt_0lep_selection_mask,
                    #evt_0lep_sv_selection_mask,
                ]
          
                for sel, sel_str in zip(selections, selections_str): 
                    if np.any(sel):

                        met_sel = met[sel]
                        risr_sel = risr[sel]
                        mpe_sel = mpe[sel]

                        #if 'data' in sample:
                        #    probb_sel = np.array([prob for prob, s in zip(probb_sv, sel) if s])
                        #    pt_sel = np.array([pt for pt, s in zip(pt_sv, sel) if s])
                        #    eta_sel = np.array([eta for eta, s in zip(eta_sv, sel) if s])
                        #    mass_sel = np.array([mass for mass, s in zip(mass_sv, sel) if s])
                        #    ndof_sel = np.array([ndof for ndof, s in zip(ndof_sv, sel) if s])
                        #    dxy_sel = np.array([dxy for dxy, s in zip(dxy_sv, sel) if s])
                        #    #dxysig_sel = np.array([dxysig for dxysig, s in zip(dxysig_sv, sel) if s])
                        #    d3d_sel = np.array([d3d for d3d, s in zip(d3d_sv, sel) if s])
                        #    d3dsig_sel = np.array([d3dsig for d3dsig, s in zip(d3dsig_sv, sel) if s])
                        #    cos_sel = np.array([cos for cos, s in zip(cos_sv, sel) if s])
                        #if 'isB' in sample:
                        #    probb_sel = np.array([prob[fl] for prob, fl, s in zip(probb_sv, b_sv, sel) if s])
                        #    pt_sel = np.array([pt[fl] for pt, fl, s in zip(pt_sv, b_sv, sel) if s])
                        #    eta_sel = np.array([eta[fl] for eta, fl, s in zip(eta_sv, b_sv, sel) if s])
                        #    mass_sel = np.array([mass[fl] for mass, fl, s in zip(mass_sv, b_sv, sel) if s])
                        #    ndof_sel = np.array([ndof[fl] for ndof, fl, s in zip(ndof_sv, b_sv, sel) if s])
                        #    dxy_sel = np.array([dxy[fl] for dxy, fl, s in zip(dxy_sv, b_sv, sel) if s])
                        #    #dxysig_sel = np.array([dxysig[fl] for dxysig, fl, s in zip(dxysig_sv, b_sv, sel) if s])
                        #    d3d_sel = np.array([d3d[fl] for d3d, fl, s in zip(d3d_sv, b_sv, sel) if s])
                        #    d3dsig_sel = np.array([d3dsig[fl] for d3dsig, fl, s in zip(d3dsig_sv, b_sv, sel) if s])
                        #    cos_sel = np.array([cos[fl] for cos, fl, s in zip(cos_sv, b_sv, sel) if s])
                        #if 'isC' in sample:
                        #    probb_sel = np.array([prob[fl] for prob, fl, s in zip(probb_sv, c_sv, sel) if s])
                        #    pt_sel = np.array([pt[fl] for pt, fl, s in zip(pt_sv, c_sv, sel) if s])
                        #    eta_sel = np.array([eta[fl] for eta, fl, s in zip(eta_sv, c_sv, sel) if s])
                        #    mass_sel = np.array([mass[fl] for mass, fl, s in zip(mass_sv, c_sv, sel) if s])
                        #    ndof_sel = np.array([ndof[fl] for ndof, fl, s in zip(ndof_sv, c_sv, sel) if s])
                        #    dxy_sel = np.array([dxy[fl] for dxy, fl, s in zip(dxy_sv, c_sv, sel) if s])
                        #    #dxysig_sel = np.array([dxysig[fl] for dxysig, fl, s in zip(dxysig_sv, c_sv, sel) if s])
                        #    d3d_sel = np.array([d3d[fl] for d3d, fl, s in zip(d3d_sv, c_sv, sel) if s])
                        #    d3dsig_sel = np.array([d3dsig[fl] for d3dsig, fl, s in zip(d3dsig_sv, c_sv, sel) if s])
                        #    cos_sel = np.array([cos[fl] for cos, fl, s in zip(cos_sv, c_sv, sel) if s])
                        #if 'isLight' in sample:
                        #    probb_sel = np.array([prob[fl] for prob, fl, s in zip(probb_sv, light_sv, sel) if s])
                        #    pt_sel = np.array([pt[fl] for pt, fl, s in zip(pt_sv, light_sv, sel) if s])
                        #    eta_sel = np.array([eta[fl] for eta, fl, s in zip(eta_sv, light_sv, sel) if s])
                        #    mass_sel = np.array([mass[fl] for mass, fl, s in zip(mass_sv, light_sv, sel) if s])
                        #    ndof_sel = np.array([ndof[fl] for ndof, fl, s in zip(ndof_sv, light_sv, sel) if s])
                        #    dxy_sel = np.array([dxy[fl] for dxy, fl, s in zip(dxy_sv, light_sv, sel) if s])
                        #    #dxysig_sel = np.array([dxysig[fl] for dxysig, fl, s in zip(dxysig_sv, light_sv, sel) if s])
                        #    d3d_sel = np.array([d3d[fl] for d3d, fl, s in zip(d3d_sv, light_sv, sel) if s])
                        #    d3dsig_sel = np.array([d3dsig[fl] for d3dsig, fl, s in zip(d3dsig_sv, light_sv, sel) if s])
                        #    cos_sel = np.array([cos[fl] for cos, fl, s in zip(cos_sv, light_sv, sel) if s])
                        #else:
                        #    probb_sel = np.array([prob for prob, s in zip(probb_sv, sel) if s])
                        #    pt_sel = np.array([pt for pt, s in zip(pt_sv, sel) if s])
                        #    eta_sel = np.array([eta for eta, s in zip(eta_sv, sel) if s])
                        #    mass_sel = np.array([mass for mass, s in zip(mass_sv, sel) if s])
                        #    ndof_sel = np.array([ndof for ndof, s in zip(ndof_sv, sel) if s])
                        #    dxy_sel = np.array([dxy for dxy, s in zip(dxy_sv, sel) if s])
                        #    #dxysig_sel = np.array([dxysig for dxysig, s in zip(dxysig_sv, sel) if s])
                        #    d3d_sel = np.array([d3d for d3d, s in zip(d3d_sv, sel) if s])
                        #    d3dsig_sel = np.array([d3dsig for d3dsig, s in zip(d3dsig_sv, sel) if s])
                        #    cos_sel = np.array([cos for cos, s in zip(cos_sv, sel) if s])


                        tmp_weight = weight[sel]
                        #tmp_weight_sv = np.array([[w]*len(sv) for w, sv in zip(tmp_weight, pt_sel)])

                        #pt_sel = np.concatenate(pt_sel)
                        #eta_sel = np.concatenate(eta_sel)
                        #mass_sel = np.concatenate(mass_sel)
                        #ndof_sel = np.concatenate(ndof_sel)
                        #dxy_sel = np.concatenate(dxy_sel)
                        ##dxysig_sel = np.concatenate(dxysig_sel)
                        #d3d_sel = np.concatenate(d3d_sel)
                        #d3dsig_sel = np.concatenate(d3dsig_sel)
                        #cos_sel = np.concatenate(cos_sel)
                        #probb_sel = np.concatenate(probb_sel)
                        #tmp_weight_sv = np.concatenate(tmp_weight_sv)

                        rnp.fill_hist(hist[sample][tree_name]['MET_'+sel_str], met_sel, tmp_weight) 
                        rnp.fill_hist(hist[sample][tree_name]['RISR_MPE_'+sel_str], np.swapaxes([risr_sel, mpe_sel], 0, 1), tmp_weight) 
                        rnp.fill_hist(hist[sample][tree_name]['MET_1bin'+sel_str], met_sel, tmp_weight) 
                        #rnp.fill_hist(hist[sample][tree_name]['PT_Eta_'+sel_str], np.swapaxes([pt_sel, eta_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['PT_SV_'+sel_str], pt_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['PT_SV_1GeV_'+sel_str], pt_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['PT_SV_1bin_'+sel_str], pt_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['ProbB_SV_'+sel_str], probb_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Eta_SV_'+sel_str], eta_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Eta_SV_2bin_'+sel_str], eta_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Eta_SV_1bin_'+sel_str], eta_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Eta_SV_2binV2_'+sel_str], np.abs(eta_sel), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['M_SV_'+sel_str], mass_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Ndof_SV_'+sel_str], ndof_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Dxy_SV_'+sel_str], dxy_sel, tmp_weight_sv) 
                        ##rnp.fill_hist(hist[sample][tree_name]['DxySig_SV_'+sel_str], dxysig_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['D3d_SV_'+sel_str], d3d_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['D3dSig_SV_'+sel_str], d3dsig_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['CosTheta_SV_'+sel_str], cos_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['CosTheta_SV_'+sel_str], cos_sel, tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Ndof_PT_'+sel_str], np.swapaxes([ndof_sel, pt_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Ndof_Eta_'+sel_str], np.swapaxes([ndof_sel, eta_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Dxy_PT_'+sel_str], np.swapaxes([dxy_sel, pt_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['Dxy_Eta_'+sel_str], np.swapaxes([dxy_sel, eta_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['D3d_PT_'+sel_str], np.swapaxes([d3d_sel, pt_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['D3d_Eta_'+sel_str], np.swapaxes([d3d_sel, eta_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['D3dSig_PT_'+sel_str], np.swapaxes([d3dsig_sel, pt_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['D3dSig_Eta_'+sel_str], np.swapaxes([d3dsig_sel, eta_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['CosTheta_PT_'+sel_str], np.swapaxes([cos_sel, pt_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['CosTheta_Eta_'+sel_str], np.swapaxes([cos_sel, eta_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['M_PT_'+sel_str], np.swapaxes([mass_sel, pt_sel], 0, 1), tmp_weight_sv) 
                        #rnp.fill_hist(hist[sample][tree_name]['M_Eta_'+sel_str], np.swapaxes([mass_sel, eta_sel], 0, 1), tmp_weight_sv) 

                    print 'finished filling: ' + sel_str
                print 'finished filling'
    return hist

def main():
    parser = arg.ArgumentParser(description='receiving file lists for batch jobs')
    parser.add_argument('-f', '--file_list', type=str)
    parser.add_argument('-o', '--out_file',  type=str) 

    args = parser.parse_args()

    sample_file = args.file_list
    file_name   = args.out_file
    
    print "sample file: {0}".format(sample_file)

    # check that sample file was specified
    if not sample_file:
        print "ERROR: Please provide a file listing samples with the -f flag."
        return
    
    # check that output file was specified
    if not file_name:
        print "ERROR: Please provide an output file with the -o flag."
        return
    
    # check that sample file exists
    if not os.path.isfile(sample_file):
        print("ERROR: The sample file \"{0}\" does not exist.".format(sample_file))
        return

    sample_list = pickle.load(open(sample_file, "rb"))
    
    #variables = ['MET', 'MET_phi', 'PT_lep', 'Phi_lep', 'MiniIso_lep', 'ID_lep', 'Nbjet','Nbjet_ISR', 'Nbjet_S', 'weight', 'NSV', 'NSV_S', 'NSV_ISR', 'Nlep', 'PT_SV', 'Eta_SV', 'PT_jet', 'Eta_jet', 'SIP3D_lep', 'Njet', 'Btag_jet', 'ProbB_SV', 'Ndof_SV', 'M_SV', 'Dxy_SV', 'D3d_SV', 'D3dSig_SV', 'CosTheta_SV', 'PDGID_lep', 'Charge_lep', 'DxySig_SV', 'MX3a_BoostT','MX3b_BoostT', 'RISR', 'METtrigger', 'RelIso_lep']
    #variables = ['MET', 'MET_phi', 'PT_lep', 'Phi_lep', 'MiniIso_lep', 'ID_lep', 'Nbjet','Nbjet_ISR', 'Nbjet_S', 'weight', 'NSV', 'NSV_S', 'NSV_ISR', 'Nlep', 'PT_SV', 'Eta_SV', 'PT_jet', 'Eta_jet', 'SIP3D_lep', 'Njet', 'Btag_jet', 'ProbB_SV', 'Ndof_SV', 'M_SV', 'Dxy_SV', 'D3d_SV', 'D3dSig_SV', 'CosTheta_SV', 'EMutrigger', 'PDGID_lep', 'Charge_lep', 'MatchedJetID_SV', 'MX3a_BoostT','MX3b_BoostT', 'RISR', 'METtrigger', 'RelIso_lep', 'Flavor_SV']
    variables = ['MET', 'MET_phi', 'PT_lep', 'Phi_lep', 'MiniIso_lep', 'ID_lep', 'Nbjet','Nbjet_ISR', 'Nbjet_S', 'weight', 'NSV', 'NSV_S', 'NSV_ISR', 'Nlep', 'PT_SV', 'Eta_SV', 'PT_jet', 'Eta_jet', 'SIP3D_lep', 'Njet', 'Btag_jet', 'PDGID_lep', 'Charge_lep', 'MX3a_BoostT','MX3b_BoostT', 'RISR', 'METtrigger', 'RelIso_lep', 'PTISR', 'PTCM', 'dphiCMI', 'dphiMET_V']

    start_b = time.time()    

    hist_sample = get_histograms(sample_list, variables, None)

    write_hists_to_file(hist_sample, file_name) 
    stop_b = time.time()
    print "total:      ", stop_b - start_b

if __name__ == "__main__":
    main()

