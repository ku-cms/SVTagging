import os                                                                                                              
import glob                                                                                                            

from WMCore.Configuration import Configuration
config = Configuration()

# To submit crab jobs:
# crab submit -c <config_file>

# To check crab write permissions: 
# crab checkwrite --site <site>

# Documentation:
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/CRAB3ConfigurationFile

# Automatic splitting: config.Data.splitting = 'Automatic'
# The 'maxJobRuntimeMin' parameter is not compatible with the 'Automatic' splitting mode (default).
# In case of Automatic splitting, the Data.unitsPerJob parameter must be in the [180, 2700] minutes range.
# When Data.splitting = 'Automatic', Data.unitsPerJob represents the jobs target runtime in minutes,
# and its minimum allowed value is 180 (i.e. 3 hours).

config.section_('General')
config.General.transferOutputs = True
config.General.transferLogs = True
config.General.requestName = 'TTJets-DiLept-FullSim-2016'

config.section_('JobType')
config.JobType.allowUndistributedCMSSW = True
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'SUS-RunIISummer16NanoAODv7-cfg.py'
config.JobType.outputFiles = ['TTJets-DiLept-FullSim-2016.root']
config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxJobRuntimeMin = 2750
config.JobType.maxMemoryMB = 2500

# Note: slash required after <CERN-username> if <output-directory> is not provided
#config.Data.outLFNDirBase = '/store/user/<CERN-username>/<output-directory>'
config.section_('Data')
config.Data.inputDataset = '/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM'
config.Data.outLFNDirBase = '/store/group/lpcsusylep/NANO_SVSF'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.publication = False
config.Data.ignoreLocality = False

# Storage sites: T3_US_FNALLPC
# Fermilab: T1_US_FNAL: Fermilab
# FNAL CMS LPC: T3_US_FNALLPC is up to speed, but you have to have a cmslpc account to run jobs there
# Whitelist: don't include 'T3_US_*' as many of them are not up to speed 

# Make sure you have write access to the config.Site.storageSite that you specify 
# voms-proxy-init --valid 192:00 -voms cms
# crab checkwrite --site T3_US_FNALLPC

config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'

