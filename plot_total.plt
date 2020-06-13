set term png size 1400,500
set output "graph_out.png"
set datafile separator ","
set ylabel "Total ($)"
set xlabel "Time (Days)"
unset key
plot "plot_me.csv" using 1:2 with line
