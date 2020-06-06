# Read from the file file.txt and output the tenth line to stdout.
first_ten=`head -10 file.txt`
if [ 10 -le "`echo "$first_ten" | wc -l | awk '{print $1}'`" ]; then
    echo "$first_ten" | tail -1
fi
