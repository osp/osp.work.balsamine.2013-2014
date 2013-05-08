# the separated pdf as input
# convert input-green.pdf -density 3003300 -quality 100.png 
# convert input-pink.pdf -density 300x300 -quality 100.png

# generating color gradient that will be used to colorize
# change the color if needed
convert -size 10x256 gradient:'#00aa5a'-white a-gradient-green.png
convert -size 10x256 gradient:'rgb(255, 0, 82)'-white a-gradient-pink.png

#loop for managing filenames
for (( i=1; i<=`find g-*.png | wc -l`; i++ ))
do

# colorizing
convert g-${i}.png a-gradient-green.png -clut cg-${i}.png
echo cg-${i}.png # to follow the action
convert p-${i}.png a-gradient-pink.png -clut cp-${i}.png
echo cp-${i}.png # to follow the action
# compositing
composite cg-${i}.png -compose Multiply cp-${i}.png composite-${i}.png
echo composite-${i}.png # to follow the action

done

# merge in a pdf - dirty but working
convert composite-1.png composite-2.png composite-3.png composite-4.png composite-5.png composite-6.png composite-7.png composite-8.png composite-9.png composite-10.png composite-11.png composite-12.png composite-13.png composite-14.png composite-15.png composite-16.png composite-17.png composite-18.png composite-19.png composite-20.png composite-21.png composite-22.png composite-23.png composite-24.png composite-25.png composite-26.png composite-27.png composite-28.png composite-29.png composite-30.png composite-31.png composite-32.png composite-33.png composite-34.png composite-35.png composite-36.png composite-37.png composite-38.png composite-39.png composite-40.png composite-41.png composite-42.png composite-43.png composite-44.png composite-45.png composite-46.png composite-47.png composite-48.png a-output.pdf

rm c*.png # clean up