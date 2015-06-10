#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
set results_file $report_dir/plot_data/(basename -s .fish (status -f)).data
echo $results_file
rm $results_file
for T in 16777216 33554432 67108864 134217728
        for j in (seq -w 02)
                eval $code_dir/release/experiments/bench_viterbi_extended $report_dir/data/{$T}_{$j}.seq $T $report_dir/data/16.hmm 16 $results_file
        end
end
