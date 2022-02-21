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

rt.gROOT.SetBatch()
rt.TH1.AddDirectory(rt.kFALSE)

date = strftime('%d%b%y', localtime())
########## get_histograms function template ############

########################################################

def get_histograms(list_of_files_, variable_list_, cuts_to_apply_=None):
    
    hist    = OrderedDict()
    counts  = OrderedDict()
    for sample in list_of_files_:
        hist[sample]    = OrderedDict()
        counts[sample]  = OrderedDict()
        for tree_name in list_of_files_[sample]['trees']:
            print '\nReserving Histograms for:', sample, tree_name 
            hist[sample][tree_name.replace('/', '_')]   = OrderedDict()
            counts[sample][tree_name.replace('/', '_')] = OrderedDict()
            # Reserve histograms

            selections_str = [
                                 'ntrk',
                                 'nojets',
                                 'all',
                                 'discr',
                                 'discr_ntrk',
            ]

            for sel in selections_str:
                hist[sample][tree_name.replace('/', '_')]['PT_'+sel]    = rt.TH1D('PT_'+sel+'_'+sample+'_'+tree_name.replace('/', '_'), '', 100, 2, 20)
                hist[sample][tree_name.replace('/', '_')]['Eta_'+sel]   = rt.TH1D('Eta_'+sel+'_'+sample+'_'+tree_name.replace('/', '_'), '', 100, -np.pi, np.pi)


        for ifile, in_file in enumerate(list_of_files_[sample]['files']):
            for tree_name in list_of_files_[sample]['trees']:
                sample_array = get_tree_info_singular(sample, in_file, tree_name, variable_list_, cuts_to_apply_)
                if sample_array is None:
                    continue

                print '\nGetting Histograms for:', sample, tree_name, in_file
                print 'file: ', ifile+1, ' / ', len(list_of_files_[sample]['files'])

                nsv         = np.array(sample_array['NSV'])
                sv_pt       = np.concatenate(np.array(sample_array['PT_SV']))
                sv_eta      = np.concatenate(np.array(sample_array['Eta_SV']))
                sv_m        = np.concatenate(np.array(sample_array['M_SV']))
                sv_probb    = np.concatenate(np.array(sample_array['ProbB_SV']))
                
                sv_d3d      = np.concatenate(np.array(sample_array['D3d_SV']))
                sv_d3dsig   = np.concatenate(np.array(sample_array['D3dSig_SV']))
                sv_ndof     = np.concatenate(np.array(sample_array['Ndof_SV']))
                sv_dxy      = np.concatenate(np.array(sample_array['Dxy_SV']))
                sv_cos      = np.concatenate(np.array(sample_array['CosTheta_SV']))
                sv_flavor   = np.concatenate(np.array(sample_array['Flavor_SV']))

                met     = np.array(sample_array['MET'])
                risr    = np.array(sample_array['RISR'])
                ptisr   = np.array(sample_array['PTISR'])

                met     = np.array([[m]*sv for m, sv in zip(met, nsv)])
                risr    = np.array([[m]*sv for m, sv in zip(risr, nsv)])
                ptisr   = np.array([[m]*sv for m, sv in zip(ptisr, nsv)])

                d3ds_g4     = sv_d3dsig > 4.
                d3ds_g3     = sv_d3dsig > 3.
                ndof_l1p8   = sv_ndof > 1.8 
                cos_g0p98   = sv_cos > 0.98        
                dxy_l3      = sv_dxy < 3.

                d3ds_g3     = sv_d3dsig > 3.
                cut_probb   = sv_probb > 0.3

                met_200     = met > 200
                ptisr_200   = ptisr > 200
     
                risr_0p5    = risr > 0.5
                risr_0p8    = risr > 0.8
                risr_0p95   = risr > 0.95

                all_b       = sv_flavor == 5
                is_c        = sv_flavor == 4
                is_light    = np.logical_not(all_b)*np.logical_not(is_c)
 
                sv_ntrk_selection_mask          = None
                sv_nojet_selection_mask         = None
                sv_all_selection_mask           = None
                sv_discr_selection_mask         = None
                sv_discr_ntrk_selection_mask    = None
                
                if 'isB' in sample:
                    sv_ntrk_selection_mask          = np.all([all_b, d3ds_g3, ndof_l1p8], axis=0)
                    sv_nojet_selection_mask         = np.all([all_b, d3ds_g3], axis=0)
                    sv_all_selection_mask           = np.all([all_b, ndof_l1p8, d3ds_g4, cos_g0p98, dxy_l3], axis=0)
                    sv_discr_selection_mask         = np.all([all_b, cut_probb, d3ds_g3], axis=0)
                    sv_discr_ntrk_selection_mask    = np.all([all_b, cut_probb, d3ds_g3, ndof_l1p8], axis=0)

                if 'isC' in sample:
                    sv_ntrk_selection_mask          = np.all([is_c, d3ds_g3, ndof_l1p8], axis=0)
                    sv_nojet_selection_mask         = np.all([is_c, d3ds_g3], axis=0)
                    sv_all_selection_mask           = np.all([is_c, ndof_l1p8, d3ds_g4, cos_g0p98, dxy_l3], axis=0)
                    sv_discr_selection_mask         = np.all([is_c, cut_probb, d3ds_g3], axis=0)
                    sv_discr_ntrk_selection_mask    = np.all([is_c, cut_probb, d3ds_g3, ndof_l1p8], axis=0)

                if 'isLight' in sample:
                    sv_ntrk_selection_mask          = np.all([is_light, d3ds_g3, ndof_l1p8], axis=0)
                    sv_nojet_selection_mask         = np.all([is_light, d3ds_g3], axis=0)
                    sv_all_selection_mask           = np.all([is_light, ndof_l1p8, d3ds_g4, cos_g0p98, dxy_l3], axis=0)
                    sv_discr_selection_mask         = np.all([is_light, cut_probb, d3ds_g3], axis=0)
                    sv_discr_ntrk_selection_mask    = np.all([is_light, cut_probb, d3ds_g3, ndof_l1p8], axis=0)

               
                selections_str = [
                                 'ntrk',
                                 'nojets',
                                 'all',
                                 'discr',
                                 'discr_ntrk',
                ]

                selections = [
                    sv_ntrk_selection_mask,
                    sv_nojet_selection_mask,
                    sv_all_selection_mask,
                    sv_discr_selection_mask,
                    sv_discr_ntrk_selection_mask,
                ]
          
                for sel, sel_str in zip(selections, selections_str): 
                    if np.any(sel):

                        pt_sel = sv_pt[sel]
                        eta_sel = sv_eta[sel]


                        rnp.fill_hist(hist[sample][tree_name.replace('/', '_')]['PT_'+sel_str], pt_sel) 
                        rnp.fill_hist(hist[sample][tree_name.replace('/', '_')]['Eta_'+sel_str], eta_sel) 
 
                    print 'finished filling: ' + sel_str
                print 'finished filling'
    return hist

def main():
    parser = arg.ArgumentParser(description='receiving file lists for batch jobs')
    parser.add_argument('-f', '--file_list', type=str)
    parser.add_argument('-o', '--out_file', type=str) 

    args = parser.parse_args()

    sample_file = args.file_list
    file_name   = args.out_file

    print "sample file: {0}".format(sample_file)

    # check that sample file was specified
    if not sample_file:
        print "ERROR: Please provide a file listing samples with the -f flag."
        return
    
    # check that sample file exists
    if not os.path.isfile(sample_file):
        print("ERROR: The sample file \"{0}\" does not exist.".format(sample_file))
        return

    sample_list = pickle.load( open(sample_file, "rb"))
    variables = ['MET', 'PTISR', 'RISR', 'NSV','PT_SV', 'Eta_SV', 'M_SV', 'Ndof_SV', 'ProbB_SV', 'D3d_SV', 'D3dSig_SV', 'Dxy_SV', 'CosTheta_SV', 'Flavor_SV']

    start_b = time.time()    

    hist_sample = get_histograms(sample_list, variables, None)

    write_hists_to_file(hist_sample, file_name) 
    stop_b = time.time()
    print "total:      ", stop_b - start_b

if __name__ == "__main__":
    main()

