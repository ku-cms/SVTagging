# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SUS-RunIISummer16NanoAODv7-cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:TTJets-DiLept-FullSim-2016.root --conditions 102X_mcRun2_asymptotic_v8 --step NANO --filein dbs:/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM --era Run2_2016,run2_nanoAOD_94X2016 --no_exec --mc -n -1
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANO',eras.Run2_2016,eras.run2_nanoAOD_94X2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/5ABB0EC9-FCE9-E811-B517-0CC47A6C1056.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1ACFEC66-F8E9-E811-B2A8-0025901D08D6.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/46EE82F3-FDE9-E811-8A71-1C6A7A21B74D.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/FC6DABCB-FEE9-E811-A459-1C6A7A26BFE7.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/B228EE6E-F8E9-E811-BE25-002590E3A0EE.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3AC2AB46-FBE9-E811-BEA1-002590E3A2D6.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/88A37EA0-FEE9-E811-9073-0CC47A2B0744.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1AA5D307-FFE9-E811-9CA9-0CC47AD98F74.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/80009115-FFE9-E811-9125-0CC47AD98C8A.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/58D93131-FBE9-E811-AB01-90B11C282313.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A2792F16-FCE9-E811-9507-1C6A7A26BB7D.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3CB2555D-FDE9-E811-9361-90B11C26815F.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/C44B534E-FCE9-E811-B4F4-90B11C27F89E.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/849DC691-F7E9-E811-B225-002590E3A2D6.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/62F12C3E-FEE9-E811-852B-002590E3A212.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/AE52D448-FEE9-E811-BC84-90B11C2C93C9.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/984791C6-FDE9-E811-8413-002590E3A0D4.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0EB34C25-FDE9-E811-9862-002590E39DF4.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/82946FA5-FFE9-E811-BA85-002590E3A222.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/601768FF-FBE9-E811-89BE-002590491AE4.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/18D24627-00EA-E811-8E9D-0025904A8ECC.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/6A71A876-FEE9-E811-B7F4-0025904A8EC8.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/382BBCD7-FCE9-E811-A73B-0025901D0C4E.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A0741189-FEE9-E811-BEFF-0025901D1668.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1A77724A-73EA-E811-A80E-0CC47A6C06C2.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/72756D56-07EA-E811-AD6F-0025904897C2.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/86DB3AB0-0BEA-E811-82BE-1C6A7A267085.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1C7D69BA-13EA-E811-9EC0-0CC47AD98F78.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/BEDD716C-1AEA-E811-B907-0CC47AD98C86.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3E250943-F9E9-E811-8C4B-0CC47AD98BC6.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/9CEC7C00-F8E9-E811-B139-0025907254BC.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/04D5809A-FAE9-E811-BAC6-0CC47AA98B8E.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/0C14222B-FAE9-E811-AF5C-0CC47AA9906E.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/4E3C3C8F-F8E9-E811-B81E-0CC47AD99144.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/64A39C31-FBE9-E811-8443-90B11C27F89E.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/3474BF6C-F7E9-E811-BE18-90B11C27F383.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/128E328C-F9E9-E811-A7C7-0CC47AD98F64.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/CA6E7025-F8E9-E811-BD2C-0CC47A6C1866.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/363EA1AA-F7E9-E811-957F-0CC47AA989CA.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/A8E1F7A7-F7E9-E811-AC35-0CC47A6B5B20.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/5C9009BB-F7E9-E811-8589-0CC47A2B0214.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/1AE957EC-F7E9-E811-A0AE-0CC47A13D0F2.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/845ED930-FDE9-E811-8C73-0CC47A2B04CC.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/00D134FC-FBE9-E811-AF6C-1C6A7A26C53B.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/28910E6C-FCE9-E811-83C1-0CC47A6C186C.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/404BEE11-FFE9-E811-96B7-0CC47AD98D12.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/E00C2E9C-FBE9-E811-9BC4-0CC47AD98B90.root', 
        '/store/mc/RunIISummer16MiniAODv3/TTJets_DiLept_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUMoriond17_94X_mcRun2_asymptotic_v3-v2/270000/9A4AE0D8-FBE9-E811-A405-0CC47AD98CEA.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('--python_filename nevts:-1'),
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
    fileName = cms.untracked.string('file:TTJets-DiLept-FullSim-2016.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_mcRun2_asymptotic_v8', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequenceMC)
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

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
