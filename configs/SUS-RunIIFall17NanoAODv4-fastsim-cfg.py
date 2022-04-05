# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SUS-RunIIFall17NanoAODv4-fastsim-cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --processName 14Dec2018 --fileout file:TTJets-DiLept-FastSim-2017.root --conditions 102X_mc2017_realistic_v6 --customise_commands process.particleLevelSequence.remove(process.genParticles2HepMCHiggsVtx);process.particleLevelSequence.remove(process.rivetProducerHTXS);process.particleLevelTables.remove(process.HTXSCategoryTable) --step NANO --filein dbs:/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIFall17MiniAODv2-PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/MINIAODSIM --era Run2_2017,run2_nanoAOD_94XMiniAODv2 --fast --no_exec --mc -n -1
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('14Dec2018',eras.Run2_2017,eras.run2_nanoAOD_94XMiniAODv2,eras.fastSim)

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
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/62DEE342-7E20-E911-9031-901B0E542974.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/18FA0A8D-0D21-E911-8BE3-00259021A4C2.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/66E7A506-DE23-E911-899F-509A4C8339A0.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/82C5B6D4-DC23-E911-8C09-EC0D9A8222E6.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/C45635BB-D01F-E911-A2E5-6CC2173D6E60.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/52A95096-C120-E911-9501-002481DE47D0.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/6CADBECE-0B21-E911-8F47-1866DA87931C.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/54F7F798-0D21-E911-84D1-0242AC1C0501.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/1C9609D6-DC23-E911-9705-008CFAC91834.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/AAD63849-FC1F-E911-956A-3417EBE51E7D.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/B2D156AB-1321-E911-88EF-003048CF3EF0.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/C63C2199-D81F-E911-A75A-008CFA000BF0.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/40A5DF5E-0C21-E911-805E-3417EBE70003.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/810000/AA30CAD1-2A23-E911-87A5-FA163E7D2619.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/1287D126-CC20-E911-AD70-0CC47AFCC3CE.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/2E89CDCA-0D21-E911-848B-0CC47AFCC3CA.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/3681C190-DD23-E911-8016-A0369FC5E49C.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/4A54AC5A-DD23-E911-BF69-001C23BED7E1.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/AC0A8637-B81F-E911-A894-008CFAC93C1C.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/C473B6D2-1020-E911-9DF5-008CFAC91B68.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/7C2EB5F6-ED20-E911-8ADD-008CFA56D64C.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/606BAF15-0020-E911-B657-0CC47A6C06C4.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/02086B72-C620-E911-82B7-0CC47A2B0940.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/0CC5123D-3D20-E911-AD5D-6C3BE5B5B340.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/5CAF2CA5-C120-E911-9A03-B499BAAC04E6.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/E4AA145F-1E21-E911-98B2-0242AC1C0501.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/3C1AA7D0-DC23-E911-940F-A0369FE2C142.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/42C5469A-B71F-E911-9656-FA163ED92AEB.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/92500FA2-D41F-E911-91A2-A0369FC5DCBC.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/0A459B38-D71F-E911-B88E-008CFA0514E0.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/B2EDBABC-1920-E911-8EA8-008CFA197D2C.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/5EA129D1-E020-E911-ABCA-A0369FF8841A.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/EA4EDB1A-8920-E911-86E6-90E2BACBAD64.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/E28826C7-0E21-E911-9F96-68B59972C37E.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/AE450880-B01F-E911-903A-FA163E756B33.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/B8BCBCF3-B61F-E911-87F4-FA163EE4A297.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/3E1C7332-BE1F-E911-B61A-FA163E01B425.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/10AC2839-BE1F-E911-8BDE-02163E019FC6.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/5CE51930-C41F-E911-B4B2-FA163ED8FB28.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/746BF5D4-E61F-E911-BDD9-FA163ED0947A.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/36F04CC3-B320-E911-935F-02163E01A0CC.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/70383889-DC23-E911-A9D4-001517F7F524.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/3CF37CA4-1621-E911-A10D-44A842B4210B.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/847E3A4B-5523-E911-9603-AC1F6B1E3074.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/0E4C8E59-5523-E911-9226-6CC2173BC120.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/3CA8E656-3423-E911-8B3C-FA163EE49D4F.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/628580E8-DC23-E911-87E7-0CC47A5FC619.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/BAE41BE0-DD23-E911-99EC-0CC47AA99436.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/32CAB655-A520-E911-9F4B-0025909077C6.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/CCE56512-1A21-E911-8B47-00259007C36E.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/FCBE1AB0-B920-E911-8070-0CC47A1E0478.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/3471E958-0C21-E911-8BB9-B0262814DF44.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/6AFA2FB9-2E20-E911-AF03-24BE05C656A1.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/78730EE8-DC23-E911-840A-AC1F6B4D546A.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/DE78D73E-B51F-E911-9268-0242AC130002.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/9221BC72-F91F-E911-A580-0242AC130002.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/B889580B-FF1F-E911-BDA6-0242AC130002.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/86932197-CC20-E911-AD56-0242AC130002.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/A482B37A-9520-E911-93D8-001E67A3FBAA.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/E87B747C-0D21-E911-A114-001E67A4202B.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/86716DB6-2E20-E911-B0C2-9CDC715F87E0.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/C48C54B7-2E20-E911-B684-24BE05CEEB31.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/5C5D5B1E-F320-E911-9E83-506B4BB16AE6.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/0E7ED9E4-B320-E911-AA68-0CC47AC08816.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/F8576379-BE1F-E911-B809-0025905B858C.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/BC0125B6-E31F-E911-AEB1-001E6779262C.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/08C83757-AE20-E911-9F19-001E67E6F5AD.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/0441AF11-D11F-E911-8F5E-AC1F6BAC7C16.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/9A63D5CB-A020-E911-AA05-AC1F6BAC7C16.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/5024F7CF-0D21-E911-B48B-002590A3C954.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/34F4E29F-D61F-E911-8187-AC1F6B0DE13A.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/AED97539-3323-E911-AA9C-0CC47A4D76D0.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/68717B4F-A020-E911-9280-509A4C78134B.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/E699F0C4-0E21-E911-B1A8-3417EBE669D4.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/701DC25F-8620-E911-A2BE-008CFAF21F34.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/70B457F3-1A21-E911-920D-509A4C83EF80.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/5000FB11-0B20-E911-909C-A0369FE2C19A.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/C2CCE17A-0D21-E911-999D-D0946626135C.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/8A86FFD0-0D21-E911-BA11-1866DAEA6BC4.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/160F9DD4-DC23-E911-ACCB-0025904CF93C.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/D0AD150D-DD23-E911-9412-0242AC1C0501.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/80000/90F6511D-DD23-E911-B2E4-FA163E35307D.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/388082DD-C31F-E911-8B14-001C23C0B77F.root', 
        '/store/mc/RunIIFall17MiniAODv2/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall17Fast_lhe_94X_mc2017_realistic_v15-v1/10000/E6CA67AC-8E20-E911-942D-549F3525BF58.root'
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
    fileName = cms.untracked.string('file:TTJets-DiLept-FastSim-2017.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_mc2017_realistic_v6', '')

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
