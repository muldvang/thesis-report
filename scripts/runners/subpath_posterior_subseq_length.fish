#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
set results_file $report_dir/plot_data/(basename -s .fish (status -f)).data
rm $results_file
for j in (seq -w 10)
        for subseq_length in 2 4 8 16 32 64 128 256 512 1024 2048 4096 8192
                eval $code_dir/release/experiments/bench_indexed_posterior $report_dir/data/10000_{$j}.seq 10000 $report_dir/data/16.hmm 16 /dev/null $subseq_length
                for k in (seq 5)
                        eval $code_dir/release/experiments/bench_indexed_posterior $report_dir/data/10000_{$j}.seq 10000 $report_dir/data/16.hmm 16 $results_file $subseq_length
                end
        end
end
