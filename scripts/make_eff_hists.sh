#!/usr/bin/bash
# make_eff_hists.sh
# Caleb J. Smith
# May 23, 2022

input_dir=output_condor_hists_2D_proposal_23May22
output_dir=output_files_23May22

# delete directory if it exists
if [ -d ${output_dir} ]; then
    echo "Removing the directory ${output_dir}"
    rm -r ${output_dir}
fi

echo " - Running make_b_eff_hists_batch.py"
mkdir -p ${output_dir}
# FastSim
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FastSim_2016_isB_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2016_isB.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FastSim_2016_isC_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2016_isC.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FastSim_2016_isLight_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2016_isLight.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FastSim_2017_isB_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2017_isB.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FastSim_2017_isC_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2017_isC.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FastSim_2017_isLight_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2017_isLight.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FastSim_2018_isB_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2018_isB.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FastSim_2018_isC_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2018_isC.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FastSim_2018_isLight_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FastSim_2018_isLight.root
# FullSim
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FullSim_2016_isB_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FullSim_2016_isB.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FullSim_2016_isC_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FullSim_2016_isC.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FullSim_2016_isLight_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FullSim_2016_isLight.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FullSim_2017_isB_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FullSim_2017_isB.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FullSim_2017_isC_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FullSim_2017_isC.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FullSim_2017_isLight_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FullSim_2017_isLight.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FullSim_2018_isB_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FullSim_2018_isB.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FullSim_2018_isC_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FullSim_2018_isC.root
python python/make_b_eff_hists_batch.py --file_list ${input_dir}/file_lists/TTJets_FullSim_2018_isLight_files_0.pkl --out_file ${output_dir}/output_background_hist_b_eff_TTJets_FullSim_2018_isLight.root

echo " - Running ahadd.py"
cd ${output_dir}
# FastSim
ahadd.py output_background_hist_b_eff_TTJets_FastSim_2016.root output_background_hist_b_eff_TTJets_FastSim_2016_*.root
ahadd.py output_background_hist_b_eff_TTJets_FastSim_2017.root output_background_hist_b_eff_TTJets_FastSim_2017_*.root
ahadd.py output_background_hist_b_eff_TTJets_FastSim_2018.root output_background_hist_b_eff_TTJets_FastSim_2018_*.root
# FullSim
ahadd.py output_background_hist_b_eff_TTJets_FullSim_2016.root output_background_hist_b_eff_TTJets_FullSim_2016_*.root
ahadd.py output_background_hist_b_eff_TTJets_FullSim_2017.root output_background_hist_b_eff_TTJets_FullSim_2017_*.root
ahadd.py output_background_hist_b_eff_TTJets_FullSim_2018.root output_background_hist_b_eff_TTJets_FullSim_2018_*.root

