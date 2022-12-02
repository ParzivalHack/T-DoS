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
echo -e "         Updating T-DoS..."
echo
printf "                     \e[96m["
# While process is running...
while git clone https://github.com/ParzivalHack/T-DoS 2> /dev/null; do 
    printf  "▓▓▓▓▓▓▓▓▓▓▓▓▓"
    sleep 1
done
printf " "
echo
echo
echo
printf "           Successfully updated to the latest version!"
sleep 2.0
clear
cd $HOME
cd T-DoS
python T-DoS.py
