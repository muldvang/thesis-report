#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
set results_file $report_dir/plot_data/model.data
rm $results_file
for N in 2 3 4 6 8 12 16 24 32 48 64 96 128 192 256 384 512 768 1024
        for j in (seq -w 5)
                eval $code_dir/release/experiments/bench_viterbi $report_dir/data/100000.seq 100000 $report_dir/data/$N.hmm $N >> $results_file
        end
end
