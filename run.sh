#!/bin/bash

if [[ $# -ne 3 ]]; then
	echo "Usage: run.sh [Directory Name] [min/average] [LSE/Linear]"
	exit
fi

directory=$1
min_average=$2
trilateration_method=$3

if [ ! -d "$directory" ]; then
    echo "$directory does not exists"
else 
	cd "$directory"
	if [ -f "vision.txt" -a -f "wifi.txt" -a -f "appositions.txt" -a -f "groundtruth.txt"]; then
		echo "One of the vision.txt, wifi.txt, appositions.txt or groundtruth.txt does not exist"
		cd ..
		exit
	else
		python3 ../parse_allwifiresults.py wifi.txt wifiaverage.txt wifiminimum.txt
		if [[ "$min_average" == "average" && "$trilateration_method" == "Linear" ]]; then
			python3 ../trilaterate_wholefile.py wifiaverage.txt averagetrilateration.txt appositions.txt $trilateration_method
			python3 ../process_vision_readings.py vision.txt averagetrilateration.txt groundtruth.txt
		elif [[ "$min_average" == "average" && "$trilateration_method" == "LSE" ]]; then
			python3 ../trilaterate_wholefile.py wifiaverage.txt averagetrilateration.txt appositions.txt $trilateration_method
			python3 ../process_vision_readings.py vision.txt averagetrilateration.txt groundtruth.txt
		elif [[ "$min_average" == "min" && "$trilateration_method" == "Linear" ]]; then
			python3 ../trilaterate_wholefile.py wifiminimum.txt minimumtrilateration.txt appositions.txt $trilateration_method
			python3 ../process_vision_readings.py vision.txt minimumtrilateration.txt groundtruth.txt
		elif [[ "$min_average" == "min" && "$trilateration_method" == "LSE" ]]; then
			python3 ../trilaterate_wholefile.py wifiminimum.txt minimumtrilateration.txt appositions.txt $trilateration_method
			python3 ../process_vision_readings.py vision.txt minimumtrilateration.txt groundtruth.txt
		fi
		cd ..
	fi

fi
