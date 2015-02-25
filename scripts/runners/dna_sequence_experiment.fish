#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
rm $report_dir/plot_data/dna_sequence.data
for i in 1024 2048 4096 8192 16384 32768 65536 131072
        for j in (seq -w 20)
                eval $code_dir/release/experiments/sequence $report_dir/data/16.hmm "$report_dir/data/chrI_$i.seq" $i 4 >> $report_dir/plot_data/dna_sequence.data
        end
end
