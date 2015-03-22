#!usr/bin/env bash

apt-get install python-pandas
chmod +x my_word_count.py
chmod +x my_running_median.py

python my_running_median.py 
python my_word_count.py