# --------------------------------- #
# Dataset: SingleKLongGun_E0p2To200 #
# --------------------------------- #
# DAS: https://cmsweb.cern.ch/das/request?input=dataset%3D%2FSingleKLongGun_E0p2To200%2FRun3Winter23Reco-EpsilonPUGTv3_GTv3_126X_mcRun3_2023_forPU65_v3-v2%2FGEN-SIM-RECO&instance=prod/global

# PPD-Run3Winter23Reco-00015
# PPD-chain_Run3Winter23GS_flowRun3Winter23DigiEpsilonPU-00002
# Fragment taken from: PPD-Run3Winter23GS-00005

import FWCore.ParameterSet.Config as cms

generator = cms.EDProducer("FlatRandomEGunProducer",
    PGunParameters = cms.PSet(
        PartID = cms.vint32(130),
        MaxEta = cms.double(3.0),
        MaxPhi = cms.double(3.14159265359),
        MinEta = cms.double(-3.0),
        MinE = cms.double(0.2),
        MinPhi = cms.double(-3.14159265359),
        MaxE = cms.double(200)
    ),
    Verbosity = cms.untracked.int32(0),
    psethack = cms.string('single klong0 E 0.2-200'),
    AddAntiParticle = cms.bool(False),
    firstRun = cms.untracked.uint32(1)
)
