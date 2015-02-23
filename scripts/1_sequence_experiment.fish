#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
rm $report_dir/plot_data/1_sequence.data
for i in 1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576 2097152 4194304 8388608 16777216
        for j in (seq -w 20)
                eval $code_dir/release/experiments/sequence $report_dir/data/16.hmm "$report_dir/data/1_$i\_$j.seq" $i 4 >> $report_dir/plot_data/1_sequence.data
        end
end
