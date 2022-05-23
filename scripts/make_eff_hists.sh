#!/usr/bin/bash
# make_eff_hists.sh
# Caleb J. Smith
# May 23, 2022

input_dir=output_condor_hists_2D_proposal_23May22
output_dir=output_files_23May22

echo " - Running make_b_eff_hists_batch.py"
mkdir -p ${output_dir}
python python/make_b_eff_hists_batch.py --file_list output_condor_hists_2D_proposal_23May22/file_lists/TTJets_FastSim_2016_isB_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2016_isB.root
python python/make_b_eff_hists_batch.py --file_list output_condor_hists_2D_proposal_23May22/file_lists/TTJets_FastSim_2016_isC_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2016_isC.root
python python/make_b_eff_hists_batch.py --file_list output_condor_hists_2D_proposal_23May22/file_lists/TTJets_FastSim_2016_isLight_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2016_isLight.root
echo " - Running ahadd.py"
cd ${output_dir}
ahadd.py output_background_hist_b_eff_TTJets_FastSim_2016.root output_background_hist_b_eff_TTJets_FastSim_2016_*.root

