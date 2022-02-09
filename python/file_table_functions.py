#!/usr/bin/env python

"""
Creator: Erich Schmitz
Date: Feb 22, 2019
"""

import ROOT as rt
import numpy as np
import root_numpy as rnp
import numpy.lib.recfunctions as rfc
import os
from collections import OrderedDict

rt.gROOT.SetBatch()
rt.TH1.AddDirectory(rt.kFALSE)


def get_tree_info_singular(sample_, file_name_, tree_name_, variable_list_, cuts_to_apply_=None):
    """
    Same as get_tree_info_plural, but runs over a single file
    returns structured array containing the list of variables
    """
    tmp_f = rt.TFile.Open(file_name_, 'r')
    
    tmp_t = tmp_f.Get(tree_name_)
    tmp_array = None
    if bool(tmp_t) and tmp_t.InheritsFrom(rt.TTree.Class()): 
        tmp_array = rnp.tree2array(tmp_t, branches=variable_list_, selection=cuts_to_apply_)
    else:
        print('tree: ' + tree_name_ + ' is not a tree, skipping')
    
    return tmp_array


def get_tree_info_singular_deprecated(sample_, file_name_, tree_names_, variable_list_, cuts_to_apply_=None):
    """
    Same as get_tree_info_plural, but runs over a single file
    returns structured array containing the list of variables
    """
    tmp_array = {}
    tmp_array[sample_] = OrderedDict()
    for tree in tree_names_:
        tmp_f = rt.TFile.Open(file_name_, 'r')
        tmp_t = tmp_f.Get(tree)
        if bool(tmp_t) and tmp_t.InheritsFrom(rt.TTree.Class()):
            if variable_list_: 
                tmp_array[sample_][tree] = rnp.tree2array(tmp_t, branches=variable_list_, selection=cuts_to_apply_)
            else:
                tmp_array[sample_][tree] = rnp.tree2array(tmp_t, selection=cuts_to_apply_)
        else:
            print('tree: ' + tree + ' is not a tree, skipping')
    
    return tmp_array

def reduce_and_condense(file_list_of_file_lists, variable_list):
    print('for posterity')

    tree_chain = rt.TChain('deepntuplizer/tree')
    for file_list in file_list_of_file_lists:
        files = open(file_list).readlines()
        files = [f.replace('\n','') for f in files]
        for file_name in files:
            tree_chain.Add(file_name)
        branches = [b.GetName() for b in tree_chain.GetListOfBranches()]
    for branch in branches:
        if branch not in variable_list:
            tree_chain.SetBranchStatus(branch, 0)
    file_out = rt.TFile.Open('output_condensed.root', 'recreate')
    reduced_tree = tree_chain.CloneTree()
    reduced_tree.Write()
    file_out.Close()


def reduce_singular(in_file_name_, out_file_name_, variable_list_):
    tmp_f = rt.TFile(int_file_name_, 'r')
    tmp_t = tmp_f.Get('deepntuplizer/tree')

    branches = [b.GetName() for b in tmp_t.GetListOfBranches()]        
    for branch in branches:
        if branch not in variable_list:
            tmp_t.SetBranchStatus(branch, 0)

    out_file = rt.TFile(out_file_name_, 'recreate')
    reduced_tree = tmp_t.CloneTree()
    reduced_tree.Write()
    file_out.Close()

def process_the_samples(input_sample_list_, truncate_file_ = None, tree_in_dir_ = None):
    list_of_files = OrderedDict()

    for sample, list_of_folders in input_sample_list_.items():
        print(sample)
        file_list = []
        for folder in list_of_folders:
            print('->', folder)
            if '.root' in folder:
                file_list.append(folder)
            else:
                file_list_tmp = [os.path.join(folder, f) for f in os.listdir(folder) if (os.path.isfile(os.path.join(folder, f)) and ('.root' in f))]
                file_list.append(file_list_tmp)
        need_to_concat = [True if type(x) == list else False for x in file_list]
        if np.any(need_to_concat):
            file_list = np.concatenate(file_list)
        # Get file structure, in case there is a grid of mass points
        print(file_list)
        if 'data' in sample:
            #f_struct_tmp = None
            f_struct_tmp = rt.TFile.Open(file_list[0], 'r')
        elif 'SMS' not in sample:
            f_struct_tmp = rt.TFile.Open(file_list[0], 'r')
        tree_list = []
        if tree_in_dir_ is not None and 'SMS' not in sample:
            for tree in tree_in_dir_:
                tree_list.append(tree)
        else:
            if 'data' in sample:
                #tree_list.append('Fake')
                tree_list = [tree.GetName() for tree in f_struct_tmp.GetListOfKeys() if 'EventCount' not in tree.GetName() and 'Histograms' not in tree.GetName()]
            elif 'SMS' not in sample:
                tree_list = [tree.GetName() for tree in f_struct_tmp.GetListOfKeys() if 'EventCount' not in tree.GetName() and 'Histograms' not in tree.GetName()]

        if truncate_file_ is not None:
            file_list = file_list[:truncate_file_]
        if 'SMS' in sample:
            if tree_in_dir_ is not None:
                trees_to_keep = [tree for tree in tree_in_dir_]
            else:
                #trees_to_keep = ['SMS_700_690', 'SMS_700_680', 'SMS_700_660', 'SMS_700_640', 'SMS_700_620', 'SMS_600_590', 'SMS_600_580', 'SMS_600_560', 'SMS_600_540', 'SMS_600_520', 'SMS_500_490', 'SMS_500_480', 'SMS_500_460', 'SMS_500_440', 'SMS_500_420', 'SMS_300_295', 'SMS_300_293', 'SMS_300_290', 'SMS_300_280', 'SMS_300_260', 'SMS_300_220', 'SMS_250_245', 'SMS_250_243', 'SMS_250_240', 'SMS_250_230', 'SMS_250_210', 'SMS_250_170', 'SMS_200_199', 'SMS_200_195', 'SMS_200_193', 'SMS_200_190']
                trees_to_keep = ['SMS_700_690', 'SMS_700_680', 'SMS_700_660', 'SMS_700_640', 'SMS_700_620', 'SMS_600_590', 'SMS_600_580', 'SMS_600_560', 'SMS_600_540', 'SMS_600_520', 'SMS_500_490', 'SMS_500_480', 'SMS_500_460', 'SMS_500_440', 'SMS_500_420', 'SMS_550_325', 'SMS_550_375', 'SMS_658_475', 'SMS_558_375', 'SMS_518_350', 'SMS_550_400', 'SMS_525_400', 'SMS_550_425', 'SMS_550_450', 'SMS_550_475', 'SMS_550_350', 'SMS_200_120', 'SMS_250_170']
            #trees_to_keep = ['SMS_700_690', 'SMS_600_590', 'SMS_500_490', 'SMS_500_480', 'SMS_500_460', 'SMS_500_440', 'SMS_500_420']
            #trees_to_keep = ['Events']
                #trees_to_keep = []
            if trees_to_keep:
                #tmp_tree_list = []
                #for tree in trees_to_keep:
                #    if tree in tree_list:
                #        tmp_tree_list.append(tree)
                tree_list = trees_to_keep
            else:
                tree_name_mass = [(int(mass.split('_')[1]), int(mass.split('_')[2])) for mass in tree_list]
                tree_name_mass.sort(key=lambda x: int(x[0]))
                tree_list = ['SMS_'+str(mom) + '_' + str(child) for mom, child in tree_name_mass]
        if not 'data' in sample and 'SMS' not in sample:
            f_struct_tmp.Close()
        list_of_files[sample] = OrderedDict([('files', file_list), ('trees', tree_list)])
    return list_of_files


def write_hists_to_template_file(hists_, out_file_name_):

    out_file = rt.TFile.Open(out_file_name_, "recreate")
    print('writing histograms to: ', out_file.GetName())
    out_file.cd()
    for sample in hists_:
        for tree in hists_[sample]:
            for hist in hists_[sample][tree].values():
                hist.Write()
    out_file.Close()
    print('finished writing')

def write_hists_to_file(hists_, out_file_name_):

    out_file = rt.TFile.Open(out_file_name_, "recreate")
    print('writing histograms to: ', out_file.GetName())
    out_file.cd()
    for sample in hists_:
        sample_dir = out_file.mkdir(sample)
        for tree in hists_[sample]:
            sample_dir.cd()
            tmp_dir = sample_dir.mkdir(tree)
            tmp_dir.cd()
            for hist in hists_[sample][tree].values():
                hist.Write()
    out_file.Close()
    print('finished writing')

def write_arrays_to_file(arrays_, out_file_name_):
    """
    save ndarray to .npy file
    """
    if '.npy' in out_file_name_:
        np.save(out_file_name_, arrays_)
    else:
        raise ValueError(out_file_name_.split('.')[-1] + ' is the wrong file type, please use npy')


def evaluateZbi(Nsig, Nbkg,sys):
    Nobs = rt.Double(Nsig+Nbkg)
    tau = rt.Double(1./Nbkg/(sys*sys/10000.))
    aux = rt.Double(Nbkg*tau)
    Pvalue = rt.TMath.BetaIncomplete(1./(1.+tau),Nobs,aux+1.)
    return rt.TMath.Sqrt(2.)*rt.TMath.ErfcInverse(Pvalue*2)


def write_table(table_array_, reference_, table_name_):

    out_lines = []
    out_w_lines = []
    out_lines_zbi = []
    background = OrderedDict()
    new_signal_array = OrderedDict()
    is_background = False

    for factor, sample in enumerate(table_array_):
        if factor == 0:
            out_lines.append('{:^60}'.format(' '))
        for itree, tree in enumerate(table_array_[sample]):
            if table_array_[sample][tree][0] == 0: continue
            row_string = '{:<30} {:<30}'.format(sample, tree)
            out_lines.append(row_string)
            row_index = out_lines.index(row_string)
            for icol, name in enumerate(reference_):
                if '_w' in name: continue
                if factor == 0 and itree == 0:
                    out_lines[factor] += '{:^60}'.format(name)
                    out_lines[row_index] += '{:^60.4f}'.format(table_array_[sample][tree][icol])
                else:
                    out_lines[row_index] += '{:^60.4f}'.format(table_array_[sample][tree][icol])
    
    for factor, sample in enumerate(table_array_):
        if 'SMS' not in sample and 'Tot' not in sample:
            is_background = True
        if factor == 0:
            out_w_lines.append('{:^60}'.format(' '))
        for itree, tree in enumerate(table_array_[sample]):
            if table_array_[sample][tree][0] == 0: continue
            row_string = '{:<30} {:<30}'.format(sample, tree)
            out_w_lines.append(row_string)
            row_index = out_w_lines.index(row_string)
            for icol, name in enumerate(reference_):
                if '_w' not in name: continue
                if is_background:
                    if name not in background:
                        background[name] = 0.
                    background[name] += table_array_[sample][tree][icol] 
                if factor == 0 and itree == 0:
                    out_w_lines[factor] += '{:^60}'.format(name)
                    out_w_lines[row_index] += '{:^60.4f}'.format(table_array_[sample][tree][icol])
                else:
                    out_w_lines[row_index] += '{:^60.4f}'.format(table_array_[sample][tree][icol])
            if not is_background:
                new_signal_array[sample+'_'+tree] = table_array_[sample][tree]
        is_background = False
    if background:
        for factor, sample in enumerate(new_signal_array):
            if factor == 0:
                out_lines_zbi.append('{:^60}'.format(' '))
            row_string = '{:^60}'.format(sample)
            out_lines_zbi.append(row_string)
            row_index = out_lines_zbi.index(row_string)
            for icol, name in enumerate(reference_):
                if '_w' not in name: continue
                val_zbi = evaluateZbi(new_signal_array[sample][icol], background[name], 10)
                if factor == 0:
                    out_lines_zbi[factor] += '{:^60}'.format(name)
                    out_lines_zbi[row_index] += '{:^60.4f}'.format(val_zbi)
                else:
                    out_lines_zbi[row_index] += '{:^60.4f}'.format(val_zbi)

    for iline in xrange(len(out_lines)):
        out_lines[iline] += '\n'
    for iline in xrange(len(out_w_lines)):
        out_w_lines[iline] += '\n'
    for iline in xrange(len(out_lines_zbi)):
        out_lines_zbi[iline] += '\n'

    with open(table_name_, 'w') as t:
        t.writelines(out_lines)
        t.write('\n')
        t.writelines(out_w_lines)
        t.write('\n')
        t.writelines(out_lines_zbi)
        t.close()


def write_table_deperecated(table_array_, table_w_array_, table_name_):

    out_lines = []
    out_w_lines = []
    for factor, sample in enumerate(table_array_):
        if factor == 0:
            out_lines.append('{:^30}'.format(' '))
        for itree, tree in enumerate(table_array_[sample]):
            row_string = '{:<15} {:<15}'.format(sample, tree)
            out_lines.append(row_string)
            row_index = out_lines.index(row_string)
            for icol, name_value in enumerate(table_array_[sample][tree].items()):
                if factor == 0 and itree == 0:
                    out_lines[factor] += '{:^30}'.format(name_value[0])
                    out_lines[row_index] += '{:^30.4f}'.format(name_value[1])
                else:
                    out_lines[row_index] += '{:^30.4f}'.format(name_value[1])
    
    for factor, sample in enumerate(table_w_array_):
        if factor == 0:
            out_w_lines.append('{:^30}'.format(' '))
        for itree, tree in enumerate(table_w_array_[sample]):
            row_string = '{:<15} {:<15}'.format(sample, tree)
            out_w_lines.append(row_string)
            row_index = out_w_lines.index(row_string)
            for icol, name_value in enumerate(table_w_array_[sample][tree].items()):
                if factor == 0 and itree == 0:
                    out_w_lines[factor] += '{:^30}'.format(name_value[0])
                    out_w_lines[row_index] += '{:^30.4f}'.format(name_value[1])
                else:
                    out_w_lines[row_index] += '{:^30.4f}'.format(name_value[1])

    for iline in xrange(len(out_lines)):
        out_lines[iline] += '\n'
    for iline in xrange(len(out_w_lines)):
        out_w_lines[iline] += '\n'
    with open(table_name_, 'w') as t:
        t.writelines(out_lines)
        t.write('\n')
        t.writelines(out_w_lines)
        t.close()



        
     


