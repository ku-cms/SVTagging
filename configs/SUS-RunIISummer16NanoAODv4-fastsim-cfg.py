# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SUS-RunIISummer16NanoAODv4-fastsim-cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --processName 14Dec2018 --fileout file:TTJets-DiLept-FastSim-2016-v1.root --conditions 102X_mcRun2_asymptotic_v6 --customise_commands process.particleLevelSequence.remove(process.genParticles2HepMCHiggsVtx);process.particleLevelSequence.remove(process.rivetProducerHTXS);process.particleLevelTables.remove(process.HTXSCategoryTable) --step NANO --filein dbs:/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM --era Run2_2016,run2_nanoAOD_94X2016 --fast --no_exec --mc -n 100000
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('14Dec2018',eras.Run2_2016,eras.run2_nanoAOD_94X2016,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/52278B3D-0C21-E911-A22C-0242AC1C0504.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/921D837A-1E21-E911-8481-0242AC1C0502.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/2E936A00-5421-E911-AF97-0242AC1C0504.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/78F290EE-5921-E911-B844-0242AC1C0502.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/020C00FC-6121-E911-8689-0242AC1C0503.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/46580C86-A921-E911-A726-0242AC1C0500.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/4A811591-8F22-E911-BE71-0242AC1C0500.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/CADD1E70-4921-E911-80C2-0002C9A0C4C1.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/404ECC9D-B921-E911-8959-0CC47A57D168.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/E031E85E-7221-E911-BCB6-AC1F6B0F7B08.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/7CB0C213-7821-E911-927D-AC1F6B0DE3F8.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/2C447AAA-1321-E911-8B06-AC1F6B0DE3F4.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/7C07E417-5621-E911-BABA-AC1F6B0DE45A.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/8AC37DE8-9D22-E911-AFD3-AC1F6B0DE2E8.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/7A3D1281-DE22-E911-B122-001E67E33C01.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/986F8725-AC22-E911-AFA2-001E67792444.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/50BB1618-B322-E911-883E-001E677924FC.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/C69F5F98-DF22-E911-A106-001E67E6F85F.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/229C7481-DE22-E911-B697-001E67E6F7BA.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/3857B794-DF22-E911-B04A-A4BF011257E0.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/A232DC80-DE22-E911-B91F-001E67E33C01.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/6E455794-DF22-E911-AA94-001E67792596.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/2CAFE4F2-4A21-E911-B82C-20040FE8E8A0.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/549C889E-4A21-E911-B88F-549F3525D084.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/7251D091-2D21-E911-877F-141877411970.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/BE567AF1-3121-E911-9BD6-20040FE9AD80.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/6A98FFAF-5021-E911-AA41-549F3525AE18.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/36BA8219-5321-E911-B9A2-B083FED00117.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/90A48786-5621-E911-9C93-20040FE9CF74.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/CEB5EB02-5921-E911-9702-20040FEABE68.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUSummer16v3Fast_lhe_94X_mcRun2_asymptotic_v3-v1/30000/B89E6404-B621-E911-BDA8-90B11C0BCBD6.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:100000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:TTJets-DiLept-FastSim-2016-v1.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_mcRun2_asymptotic_v6', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceFS)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

process.particleLevelSequence.remove(process.genParticles2HepMCHiggsVtx);process.particleLevelSequence.remove(process.rivetProducerHTXS);process.particleLevelTables.remove(process.HTXSCategoryTable)
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
