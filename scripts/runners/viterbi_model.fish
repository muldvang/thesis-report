#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
set results_file $report_dir/plot_data/(basename (status -f) .fish).data
echo $results_file
rm $results_file
for j in (seq -w 10)
        echo $j
        for N in 2 3 4 6 8 12 16 24 32 48 64# 96 128 192 256 384 512
                eval $code_dir/release/experiments/bench_viterbi $report_dir/data/10000_{$j}.seq 10000 $report_dir/data/$N.hmm $N /dev/null
                eval $code_dir/release/experiments/bench_viterbi $report_dir/data/10000_{$j}.seq 10000 $report_dir/data/$N.hmm $N $results_file
        end
end
