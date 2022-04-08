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
config.General.requestName = 'TTJets-DiLept-FullSim-2018-v2'
config.General.transferOutputs = True
config.General.transferLogs = True

config.section_('JobType')
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TOP-RunIIAutumn18NanoAODv7-cfg.py'
config.JobType.outputFiles = ['TTJets-DiLept-FullSim-2018.root']
config.JobType.allowUndistributedCMSSW = True
config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxJobRuntimeMin = 2750
config.JobType.maxMemoryMB = 2500

# Note: slash required after <user-name> if <output-directory> is not provided
#config.Data.outLFNDirBase = '/store/user/<user-name>/<output-directory>'
#config.Data.outLFNDirBase = '/store/group/<group-name>/<output-directory>'
config.section_('Data')
config.Data.inputDataset = '/TTJets_DiLept_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM'
config.Data.outLFNDirBase = '/store/group/lpcsusylep/NANO_SVSF_v2'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = False
config.Data.ignoreLocality = False

# Make sure you have write access to the config.Site.storageSite that you specify 
# voms-proxy-init --valid 192:00 -voms cms
# crab checkwrite --site T3_US_FNALLPC
# crab checkwrite --site=T3_US_FNALLPC --lfn=/store/group/lpcsusylep
config.section_('Site')
config.Site.storageSite = 'T3_US_FNALLPC'

