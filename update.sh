#!/bin/bash

# Check if the T-DoS directory exists in the user's home directory
if [ -d "$HOME/T-DoS" ]; then
    echo "Removing old T-DoS directory..."
    rm -rf "$HOME/T-DoS"
fi

# Change to the user's home directory and create a new T-DoS directory
cd "$HOME" || exit
mkdir "$HOME/T-DoS" || { echo "Failed to create T-DoS directory"; exit 1; }

# Clone the T-DoS repository from GitHub
echo "Updating T-DoS..."
printf "                    [\033[0;36m"
git clone https://github.com/ParzivalHack/T-DoS "$HOME/T-DoS" >/dev/null 2>&1 &
while kill -0 $! >/dev/null 2>&1; do
    printf "▓"
    sleep 1
done
wait $!

# Check if the clone was successful
if [ $? -ne 0 ]; then
    echo -e "\033[0;31m ERROR\033[0m]"
    echo "Failed to update T-DoS, please check your internet connection and try again."
    exit 1
fi

# Display success message and run T-DoS script
echo -e "\033[0;32m DONE\033[0m]"
echo "T-DoS has been updated to the latest version!"
cd "$HOME/T-DoS" || exit
python T-DoS.py
