#!/usr/bin/env python
"""
This is a small script that submits a config over many datasets
"""
import os
from optparse import OptionParser

def getOptions() :
    """
    Parse and return the arguments provided by the user.
    """
    usage = ('usage: python submit_all.py -c CONFIG -d DIR ')

    parser = OptionParser(usage=usage)    
    #parser.add_option("-c", "--config", dest="config",
    #    help=("The crab script you want to submit "),
    #    metavar="CONFIG")
    #parser.add_option("-d", "--dir", dest="dir",
    #    help=("The crab directory you want to use "),
    #    metavar="DIR")
    parser.add_option("-f", "--datasets", dest="datasets",
        help=("File listing datasets to run over"),
        metavar="FILE")
    (options, args) = parser.parse_args()


    #if options.config == None or options.dir == None:
     #   parser.error(usage)
    
    return options
    

def main():
    options = getOptions()

    from CRABAPI.RawCommand import crabCommand
    from httplib import HTTPException
    from WMCore.Configuration import Configuration
    config = Configuration()


    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.section_("General")
    config.General.workArea = 'crab_sv_NANO_SMS_v2'
    config.General.transferLogs = True

    config.section_("JobType")
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = 'myNanoProdMc2017_FAST_NANO.py' 
    config.JobType.pyCfgParams = None 
    config.JobType.maxMemoryMB = 2500
    config.JobType.allowUndistributedCMSSW = True

    config.section_("Data")
    config.Data.inputDataset = None
    config.Data.splitting = 'FileBased'
    config.Data.unitsPerJob = 2
    config.Data.ignoreLocality = False
    config.Data.publication = False     
    config.Data.outLFNDirBase = '/store/user/eschmitz/NANO/'
    
    config.section_("Site")
    config.Site.storageSite = 'T2_US_Nebraska'
    #config.Site.whitelist = ['T2_US_*']

    #print 'Using config ' + options.config
    #print 'Writing to directory ' + options.dir
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print 'Cannot execute commend'
            print hte.headers

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    datasetsFile = open( options.datasets )
    jobsLines = datasetsFile.readlines()
    jobs = []
    for ijob in jobsLines :
        s = ijob.rstrip()
        if (len(s)==0 or s[0][0]=='#'): continue
        jobs.append( s )
        print '  --> added ' + s
        
    for ijob, job in enumerate(jobs) :

        print "-->  ", job
        pd = job.split('/')[1] #+ job.split('/')[2].split('-')[0]
        processing = (job.split('/')[2]).split('-')[0] + (job.split('/')[2]).split('-')[1] #+ (job.split('/')[2]).split('-')[2] # (job.split('/')[2]).split('-')[0] #for data
        if (len(pd + '_' + processing)<=100): 
          config.General.requestName = pd + '_' + processing
        else:
          config.General.requestName = pd
        if 'SMS' in job:
            pyCfgParams = ['version=v15']
        else:
            pyCfgParams = ['version=v14']

        #if 'Fast' in job:
        #    pyCfgParams = ['mcInfo=1', 'GlobalTag=80X_mcRun2_asymptotic_2016_miniAODv2_v0', 'specialFix=JEC', 'jecDBname=Fall17_17Nov2017_V8_MC', 'fastsim=1']
        #    inputFiles = ['Fall17_17Nov2017_V8_MC.db']
        #else:
        #    if 'Summer16' in job:
        #        pyCfgParams = ['mcInfo=1', 'GlobalTag=80X_mcRun2_asymptotic_2016_TrancheIV_v6', 'specialFix=JEC', 'jecDBname=Summer16_23Sep2016V4_MC']
        #        inputFiles = ['Summer16_23Sep2016V4_MC.db']
        #    elif 'Fall17' in job:
        #        pyCfgParams = ['mcInfo=1', 'GlobalTag=94X_mc2017_realistic_v14', 'specialFix=JEC', 'jecDBname=Fall17_17Nov2017_V8_MC']
        #        inputFiles = ['Fall17_17Nov2017_V8_MC.db']
                
        #config.JobType.pyCfgParams = pyCfgParams
        #config.JobType.inputFiles = inputFiles
        config.Data.inputDataset = job
        print 'Submitting ' + config.General.requestName + ', dataset = ' + job
        print 'Configuration :'
        print config
        try :
            from multiprocessing import Process
            p = Process(target=submit, args=(config,))
            p.start()
            p.join()
            #submit(config)
        except :
            print 'Not submitted.'

if __name__ == '__main__':
    main()            
