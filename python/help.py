#!/usr/bin/env python

import ROOT, math

def fix(hin):
 nbins = hin.GetNbinsX();
 value1 = hin.GetBinContent(nbins+1);
 value2 = hin.GetBinContent(nbins);
 err1 = hin.GetBinError(nbins+1);
 err2 = hin.GetBinError(nbins);
 hin.SetBinContent(nbins+1, 0);
 hin.SetBinContent(nbins, value1 + value2);
 hin.SetBinError(nbins, math.sqrt(err1*err1 + err2*err2));

 #value3 = hin.GetBinContent(0)
 #value4 = hin.GetBinContent(1)
 #err3 = hin.GetBinError(0)
 #err4 = hin.GetBinError(1)
 #hin.SetBinContent(0,0)
 #hin.SetBinContent(1, value3 + value4)
 #hin.SetBinError(1, math.sqrt(err3*err3 + err4*err4))

def variableRebin(hin,hrebin) :
  for ii in range(1, hin.GetNbinsX()+1): 
    hrebin.Fill(ii, hin.GetBinContent(ii)) 
  fix(hrebin)

