if [ -d "$HOME/T-DoS" ];
then
cd $HOME
rm -rf T-DoS
elif [ -d "$HOME/T-DoS" ];
then
cd $HOME
rm -rf T-DoS
else
echo
exit 1
fi
cd $HOME
sleep 1
echo -e "         \e[91mUPDATE IS GOING ON, PLEASE BE PATIENT...!\e[0m"
echo
printf "                     \e[96m["
# While process is running...
while git clone https://github.com/ParzivalHack/T-DoS 2> /dev/null; do 
    printf  "\e[91m▓▓▓▓▓▓▓▓▓▓▓▓▓\e[0m"
    sleep 1
done
printf "\e[91m]\e[0m"
echo
echo
echo
printf "\e[91m           UPDATED SUCCESSFULLY TO THE LATEST VERSION!\e[0m"
sleep 2.0
clear
cd $HOME
cd T-DoS
python T-DoS.py
