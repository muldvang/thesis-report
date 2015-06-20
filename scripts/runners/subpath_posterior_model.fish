#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
set results_file $report_dir/plot_data/(basename -s .fish (status -f)).data
rm $results_file
for j in (seq -w 10)
        for N in 2 3 4 6 8 12 16 24 32 48 64# 96 128 192 256 384 512
                eval $code_dir/release/experiments/bench_subpath_posterior $report_dir/data/10000_{$j}.seq 10000 $report_dir/data/$N.hmm $N /dev/null 200
                eval $code_dir/release/experiments/bench_subpath_posterior $report_dir/data/10000_{$j}.seq 10000 $report_dir/data/$N.hmm $N $results_file 200
        end
end
