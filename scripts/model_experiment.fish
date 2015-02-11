#!/usr/bin/fish

set code_dir ~/Repositories/thesis-code
set report_dir ~/Repositories/thesis-report
for k in 2 4 8 16 32 64 128 256 512 1024
        for j in (seq 5)
                eval $code_dir/release/experiments/model $report_dir/data/1000000.seq $report_dir/data/ $k > $report_dir/plot_data/model.data
        end
end
