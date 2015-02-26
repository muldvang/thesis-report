#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
set results_file $report_dir/plot_data/(basename -s .fish (status -f)).data
rm $results_file
for T in 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576 2097152 4194304 8388608
        for j in (seq -w 20)
                eval $code_dir/release/experiments/bench_viterbi $report_dir/data/2_{$T}_{$j}.seq $T $report_dir/data/16.hmm 16 $results_file
        end
end
