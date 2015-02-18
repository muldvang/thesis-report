#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
rm $report_dir/plot_data/posterior_model.data
for k in 2 3 4 6 8 12 16 24 32 48 64 96 128 192 256 384 512 768 1024
        for j in (seq 5)
                eval $code_dir/release/experiments/posterior_model $report_dir/data/100000.seq $report_dir/data/ $k >> $report_dir/plot_data/posterior_model.data
        end
end
