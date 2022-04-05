#!/usr/bin/env python
"""
This is a small script that submits a config over many datasets
"""
import os
from optparse import OptionParser
from CRABAPI.RawCommand import crabCommand
from httplib import HTTPException
from WMCore.Configuration import Configuration
from multiprocessing import Process

def getOptions() :
    """
    Parse and return the arguments provided by the user.
    """
    usage = ('usage: python submitTreesLPC.py -c <config> -d <dir> -f <datasets>')

    parser = OptionParser(usage=usage)    
    parser.add_option("-c", "--config",   dest="config",   help=("The crab script you want to submit "), metavar="CONFIG")
    parser.add_option("-d", "--dir",      dest="dir",      help=("The crab directory you want to use "), metavar="DIR")
    parser.add_option("-f", "--datasets", dest="datasets", help=("File listing datasets to run over"),   metavar="DATASETS")
    (options, args) = parser.parse_args()

    if options.config == None or options.dir == None or options.datasets == None:
        parser.error(usage)
    
    return options

def main():
    options = getOptions()

    config = Configuration()

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.section_("General")
    config.General.workArea = options.dir
    config.General.transferLogs = True

    config.section_("JobType")
    config.JobType.pluginName = 'Analysis'
    config.JobType.psetName = options.config
    config.JobType.pyCfgParams = None 
    config.JobType.maxMemoryMB = 2500
    config.JobType.allowUndistributedCMSSW = True

    config.section_("Data")
    config.Data.inputDataset = None
    config.Data.splitting = 'FileBased'
    config.Data.unitsPerJob = 2
    config.Data.ignoreLocality = False
    config.Data.publication = False     
    config.Data.outLFNDirBase = '/store/group/lpcsusylep/NANO_SVSF'
    
    config.section_("Site")
    config.Site.storageSite = 'T3_US_FNALLPC'

    print 'Using config ' + options.config
    print 'Writing to directory ' + options.dir
    print 'Using datasets listed in ' + options.datasets
    
    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException, hte:
            print 'Cannot execute commend'
            print hte.headers

    #############################################################################################
    ## From now on that's what users should modify: this is the a-la-CRAB2 configuration part. ##
    #############################################################################################

    datasetsFile = open(options.datasets)
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

        config.Data.inputDataset = job
        print 'Submitting ' + config.General.requestName + ', dataset = ' + job
        print 'Configuration :'
        print config
        try :
            p = Process(target=submit, args=(config,))
            p.start()
            p.join()
            #submit(config)
        except :
            print 'Not submitted.'

if __name__ == '__main__':
    main()            

