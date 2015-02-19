#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
rm $report_dir/plot_data/fib_sequence.data
for i in (seq 32)
        eval $code_dir/release/experiments/sequence $report_dir/data/16.hmm "$report_dir/data/fib$i.seq" (math (wc -c < "$report_dir/data/fib$i.seq") / 2) >> $report_dir/plot_data/fib_sequence.data
end
