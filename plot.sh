#!/bin/bash
#Argument 1: determines hist file (default: history_out.csv)
#Argument 2: determines which of in/out/total to plot (line graph) (default: total_out.csv)
#	Note, circle graph always uses total_out.csv

if (( $# < 1 )); then
	python running_total.py
else
	python running_total.py $1
fi

if (( "$#" < 2 )); then
	cp total_out.csv plot_me.csv
else
	cp $2 plot_me.csv
fi

if (( "$#" < 1 )); then
	python circle_total.py > circle_me.csv
else
	python circle_total.py $1 > circle_me.csv
fi

gnuplot circle_plot.plt
gnuplot plot_total.plt
rm plot_me.csv
#rm circle_me.csv
feh graph_out.png&
feh circle_out.png&
