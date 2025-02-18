#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
set results_file $report_dir/plot_data/(basename -s .fish (status -f)).data
rm $results_file
for i in (seq 15 32)
        set T (math (wc -c < $report_dir/data/fib$i.seq) / 2)
        eval $code_dir/release/experiments/bench_viterbi $report_dir/data/fib{$i}.seq $T $report_dir/data/16.hmm 16 /dev/null
        for j in (seq 5)
                eval $code_dir/release/experiments/bench_viterbi $report_dir/data/fib{$i}.seq $T $report_dir/data/16.hmm 16 $results_file
        end
end
