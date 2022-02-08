# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: --python_filename SUS-RunIIAutumn18NanoAODv7-fastsim-cfg.py --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --fileout file:TTJets-DiLept-FastSim-2018-v1.root --conditions 102X_upgrade2018_realistic_v21 --step NANO --filein dbs:/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/RunIIAutumn18MiniAOD-PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/MINIAODSIM --era Run2_2018,run2_nanoAOD_102Xv1 --fast --no_exec --mc -n 100000
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('NANO',eras.Run2_2018,eras.run2_nanoAOD_102Xv1,eras.fastSim)

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
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/B622677C-31FB-9D46-AF8B-A31BC148EFC1.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/7B06B3F6-48C1-694D-8040-573643ED3458.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/E90AE9CF-A57F-BD45-B555-923EEE5F14C3.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/9A565BE4-B916-5B49-A660-001ECE3EAB11.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/49338D7A-9BD2-0F4E-81A6-0E1DFDA248C4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/5B07A8FC-2CF1-0D46-BD0D-64106597D4F7.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/9729EEB5-315A-004B-9938-16C2CCBC161B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/6E9E9F50-4FBA-2340-AC97-B5ED975BA749.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/EED8FBB2-36CB-8F42-879B-BF37203CFB20.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/72581F5A-6076-6340-A06C-19D7611DE3EC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/074B95FE-84B0-C84A-9FB7-52FC28D92272.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/27FC0A41-316C-BA48-8D93-826F25C41736.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/C8670E9A-420D-0343-95CC-1402750013D8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/36930AB0-56F7-994E-A26D-735EDF39358E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/50F9AF11-013D-C84A-8B83-2579A9E09D34.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/F87C93ED-9A98-A743-9C7A-EE2211FA134D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/3A4BC460-00BB-2049-8B07-C483CDC3BE42.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/71AC1925-F66A-AD4A-AB40-7C2A56922E23.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/B86E71F0-1A23-8E49-8F47-2E906DFF5D15.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/EA1EC52C-CBAB-E04F-8E1F-ACF4A59CD270.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/6F1601E4-D5EA-BB46-86EE-17BA2E656B53.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/1CDBF3F8-B6FD-3645-8DD9-39203588C4BB.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/8E6CC2DD-6DFC-1C4B-8ABD-2A5068E0E31A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/63A347E0-7B95-574A-B3AC-AA15D4A8AC56.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/EE6D9EA4-C9A1-404F-A5D3-F35926BBB92D.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/EA06A561-AF72-5945-8D31-018C2EEA6327.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/A0CD4C2C-2C13-434B-816A-8044180901D8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/E6F57A50-073A-4445-AC69-B01340F47FD8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/78B61B91-4635-304A-A023-40070E66E85A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/2B6F10E2-5C55-804D-B833-9A852F2773CC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/ACF32515-7597-9146-ACE3-F8FB49B21E2C.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/ED82AF53-93A6-F749-B961-DD0D60C1F13E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/AB7FFAE3-7C9C-6C48-9614-35C5BF776EE9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/2D649412-4C45-F743-88B8-C3BF2CD8D6B0.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/BDCBC4D8-4ACF-B84D-A921-5AC0D459A7E8.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/14854AD7-4F14-B64B-A519-A51E25DC1FAA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/D06ADFCC-B101-3E4A-BDAB-4EFDBEFA8681.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/5600DE95-B854-544D-A65E-A379C9CCFF59.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/E2CF08B8-2327-E044-AA2D-0F6B96F608E5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/5EAB1A4F-30D1-B544-93B0-3542DBD6A4CA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/05EE9D9F-BB0D-BE40-8286-A314DDA1025F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/48A96CDD-1C01-3749-8950-29EA4E6C7750.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/3140C0CE-235A-5C4B-8784-553A8823827A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/DA7056F2-F0D5-E64D-ADAC-F6FD34BF4C0E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/6FC9A72C-D314-EB4C-9711-F880890EE2DB.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/F3EE8918-683F-9E48-9CB8-518771E02201.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/49F3ADFC-68AE-6442-956E-A3293A46EA60.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/EAD39D58-2EB0-AD46-9756-E63C706DE483.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/14144BE7-D5C3-6642-AD0F-FAE63230250A.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/D4B39536-E2C5-F041-81C4-ABE9E8B3E416.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/B2D2934B-1CDA-074B-933D-7CAC28CC6635.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/505AA27C-258C-F64A-8C08-4970247E5DE5.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/4A45313F-C18E-0F4C-9F20-E0F4C4BC5166.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/831DF1EE-291A-1B46-BBA9-D0F0578ACB93.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/1C0E2FBB-F02C-1E4C-9549-22936856F65F.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/D49B9D3F-2086-384E-A01F-5BCA83562F48.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/D98EF990-0AD1-9E47-B45F-5D09ECCDF443.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/7195A9B2-DDF4-9E48-B8EF-8C133A58C5DA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/0CD2A29C-7B33-144F-AF25-ED38BA55AF42.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/C84F1AA2-F741-534D-B661-AB1E4D30D58B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/53E3E0C2-BA8D-3546-A91E-43451D9C7389.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/7B8F0345-50C3-CA45-BBBF-B6791CD4E76B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/F704DA70-F119-8A49-9BAB-0ABDCF5C1CD4.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/8894CD76-3CF6-8642-A40F-93E01BD54AB9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/7AAE1714-424D-9240-82B1-A92DB80B3867.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/F179799C-AE5C-F04C-8116-4EA05A17AC83.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/B57EDCF8-6384-B240-AA55-535BE6BDB6EC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/F60E94C7-DC3E-0A42-BECA-86165E7F7AEC.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/1D84C39D-8017-7F40-B430-D6F2758FF0EE.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/D2F8AA7D-E78F-364A-A4B4-3749105E2CAA.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/E8F6F4C2-96F3-C346-A2D9-1C53646B4B37.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/ED9E550D-9188-6F4A-ABFA-D233CF13E86B.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/5077C309-8026-0C4A-9C9A-6605BCC21E96.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/537D6416-4EB5-D94C-B5F0-41DE5AF57FFF.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/4201BC09-8652-0B4B-A9A4-216B581A6054.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/9DE3E592-B496-6744-B735-DE8C82B092D9.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/621094C6-6EE2-204A-A2A4-280146022C33.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/20997191-0861-0246-ABE5-99C87F7D0B8E.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/EDB5EF6A-6224-1748-BD01-20BDB167DB85.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/553F6036-F5F5-F946-AB57-659176BF8321.root', 
        '/store/mc/RunIIAutumn18MiniAOD/TTJets_DiLept_TuneCP2_13TeV-madgraphMLM-pythia8/MINIAODSIM/PUFall18Fast_lhe_102X_upgrade2018_realistic_v15-v2/20000/312B8B9B-92A2-8D4B-80C5-C80D15F3989B.root'
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
    fileName = cms.untracked.string('file:TTJets-DiLept-FastSim-2018-v1.root'),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v21', '')

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

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
