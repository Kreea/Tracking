rowi = 0
rowf = 7 
set term png size 1000,400
set output "circle_out.png"
filename = 'circle_me.csv'


set datafile separator ','
stats filename u 2 every ::rowi::rowf noout prefix "A"

rowf = (rowf-rowi > A_records -1 ? A_records + rowi - 1 : rowf)

angle(x) = x * 360/A_sum
percentage(x) = x * 100/A_sum

centerX = 0
centerY = 0
radius = 1

yposmin = 0.0
yposmax = 0.95*radius
xpos = 1.5*radius
ypos(i) = yposmax - i*(yposmax-yposmin)/(1.0*rowf-rowi)

set style fill solid 1
unset key
unset tics
unset border

set size ratio -1
set xrange [-radius:2*radius]
set yrange [-radius:radius]

pos = 0
colour = 0
plot filename u (centerX):(centerY):(radius):(pos):(pos=pos+angle($2)):(colour=colour+1) every ::rowi::rowf w circle lc var,\
	for [i=0:rowf-rowi] '+' u (xpos):(ypos(i)) w p pt 5 ps 4 lc i+1,\
	for [i=0:rowf-rowi] filename u (xpos):(ypos(i)):(sprintf('%05.2f%% %s', percentage($2), stringcolumn(1))) every ::i+rowi::i+rowi w labels left offset 3,0
