# tools.py

import os
import ROOT
import colors

# creates directory if it does not exist
def makeDir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# get tree from open file
# WARNING: Do not open TFile in getTree(); if you do, the returned TTree object will be destroyed when the TFile closes.
#          Pass open TFile to getTree().
def getTree(open_file, tree_name):
    tree     = open_file.Get(tree_name)
    n_events = tree.GetEntries()
    print("tree: {0}, number of events: {1}".format(tree_name, n_events))
    return tree

def setupHist(hist, color, lineWidth):
    hist.SetStats(ROOT.kFALSE)
    hist.SetLineColor(colors.getColorIndex(color))
    hist.SetLineWidth(lineWidth)

