import FWCore.ParameterSet.Config as cms
from Configuration.Eras.Era_Run3_2025_cff import Run3_2025

# Define process
process = cms.Process("process", Run3_2025)

process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "auto:run3_data", "")

process.source = cms.Source('PoolSource',
                            fileNames = cms.untracked.vstring(
    #'/store/data/Run2018C/Charmonium/MINIAOD/17Sep2018-v1/00000/008E68B3-5B54-664C-8B0C-A3457A832E89.root'
    #'file:events_miniAOD.root'
    'file:GGtoNN_DisplacedVertexSignalSample.root'
    #'root://eospublic.cern.ch//eos/opendata/cms/Run2016H/JetHT/MINIAOD/UL2016_MiniAODv2-v2/130000/8D2050E5-0F24-544B-A0E3-B187539117D6.root'
    ))
  
from FWCore.MessageLogger.MessageLogger_cfi import *

process.add_(
    cms.Service('ISpyService',
    outputFileName = cms.untracked.string('miniAOD.ig'),
    outputIg = cms.untracked.bool(True),
    outputMaxEvents = cms.untracked.int32(25), # These are the number of events per ig file 
    debug = cms.untracked.bool(False)
    )
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(25) # These are the number of events to cycle through in the input root file
)

process.load('ISpy.Analyzers.ISpyEvent_cfi')
process.load('ISpy.Analyzers.ISpyEBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyEERecHit_cfi')
process.load('ISpy.Analyzers.ISpyESRecHit_cfi')

process.load('ISpy.Analyzers.ISpyHBRecHit_cfi')
process.load('ISpy.Analyzers.ISpyHERecHit_cfi')

process.load('ISpy.Analyzers.ISpyGenJet_cfi')

process.load('ISpy.Analyzers.ISpyPATMuon_cfi')
process.load('ISpy.Analyzers.ISpyPATElectron_cfi')
process.load('ISpy.Analyzers.ISpyPATJet_cfi')
process.load('ISpy.Analyzers.ISpyPATMET_cfi')
process.load('ISpy.Analyzers.ISpyPATPhoton_cfi')

process.load('ISpy.Analyzers.ISpyPackedCandidate_cfi')
process.load('ISpy.Analyzers.ISpyVertex_cfi')
process.load('ISpy.Analyzers.ISpyCaloTower_cfi')

process.ISpyEBRecHit.iSpyEBRecHitTag = cms.InputTag('reducedEgamma:reducedEBRecHits')
process.ISpyEERecHit.iSpyEERecHitTag = cms.InputTag('reducedEgamma:reducedEERecHits')
process.ISpyESRecHit.iSpyESRecHitTag = cms.InputTag('reducedEgamma:reducedESRecHits')

process.ISpyHBRecHit.iSpyHBRecHitTag = cms.InputTag('reducedEgamma:reducedHBHEHits')
process.ISpyHERecHit.iSpyHERecHitTag = cms.InputTag('reducedEgamma:reducedHBHEHits')

process.ISpyPATElectron.iSpyPATElectronTag = cms.InputTag('slimmedElectrons')
process.ISpyPATElectron.isAOD = cms.untracked.bool(True)

process.ISpyPackedCandidate.iSpyPackedCandidateTag = cms.InputTag('packedPFCandidates')
                                     
process.ISpyGenJet.iSpyGenJetTag = cms.InputTag('slimmedGenJetsAK8SoftDropSubJets')   
process.ISpyPATJet.iSpyPATJetTag = cms.InputTag('slimmedJets')
process.ISpyPATMET.iSpyPATMETTag = cms.InputTag('slimmedMETs')

process.ISpyPATMuon.iSpyPATMuonTag = cms.InputTag("slimmedMuons")

process.ISpyPATPhoton.iSpyPATPhotonTag = cms.InputTag('slimmedPhotons')

process.ISpyVertex.iSpyPriVertexTag = cms.InputTag('offlineSlimmedPrimaryVertices')
process.ISpyCaloTower.iSpyCaloTowerTag = cms.InputTag('towerMaker')

process.iSpy = cms.Path(process.ISpyEvent*
                        process.ISpyEBRecHit*
                        process.ISpyEERecHit*
                        process.ISpyESRecHit*
                        process.ISpyHBRecHit*
                        process.ISpyHERecHit*
                        process.ISpyCaloTower*
                        process.ISpyPATElectron*
                        process.ISpyPATJet*
                        process.ISpyPATMET*
                        process.ISpyPATMuon*
                        process.ISpyPATPhoton*
                        process.ISpyPackedCandidate*
                        process.ISpyVertex)

process.schedule = cms.Schedule(process.iSpy)

