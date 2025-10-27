# From: https://cms-pdmv-prod.web.cern.ch/mcm/public/restapi/requests/get_fragment/PPD-Phase2Spring24wmLHEGS-00005/0

import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc630/14TeV/powheg/V2/TT_hvq/TT_hdamp_NNPDF31_NNLO.tgz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh'),
    generateConcurrently = cms.untracked.bool(True)
)

#Link to datacards:
#https://github.com/cms-sw/genproductions/blob/master/bin/Powheg/production/TT_hdamp_TuneT4_NNPDF30_13TeV_powheg/TT_hdamp_TuneT4_NNPDF30_13TeV_powheg.input

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
	maxEventsToPrint = cms.untracked.int32(1),
	pythiaPylistVerbosity = cms.untracked.int32(1),
	pythiaHepMCVerbosity = cms.untracked.bool(False),
	comEnergy = cms.double(14000.),
	PythiaParameters = cms.PSet(
		pythia8CommonSettingsBlock,
		pythia8CP5SettingsBlock,
		pythia8PowhegEmissionVetoSettingsBlock,
		processParameters = cms.vstring(
        	'POWHEG:nFinal = 2', ## Number of final state particles
        	## (BEFORE THE DECAYS) in the LHE
        	## other than emitted extra parton
        	'TimeShower:mMaxGamma = 1.0',#cutting off lepton-pair production
        	##in the electromagnetic shower
        	##to not overlap with ttZ/gamma* samples
   		),
		parameterSets = cms.vstring('pythia8CommonSettings',
			'pythia8CP5Settings',
			'pythia8PowhegEmissionVetoSettings',
			'processParameters'
		)
	)
)
