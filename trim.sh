#!/bin/zsh

# 1320 - 400 = 920

# for i in `seq 160`
# do
# sec=`expr 2 + 5 \* $i`
# echo $sec
# sox masui.wav ./Voice/Masui/$i.wav trim $sec 5
# done


# TAKEFUJI
for i in `seq 180`
do
sec=`expr 400 + 5 \* $i`
echo $sec
sox takefuji.wav ./Voice/Takefuji/$i.wav trim $sec 5
done