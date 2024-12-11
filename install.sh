#!/bin/bash

clear
echo -e "\033[0m                                                 "
echo -e "\033[0;31m███████╗███████╗ ██████╗██████╗ ███████╗████████╗"
echo -e "\033[0;31m██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝╚══██╔══╝"
echo -e "\033[0;31m███████╗█████╗  ██║     ██████╔╝█████╗     ██║   "
echo -e "\033[0;31m╚════██║██╔══╝  ██║     ██╔══██╗██╔══╝     ██║   "
echo -e "\033[0;31m███████║███████╗╚██████╗██║  ██║███████╗   ██║   "
echo -e "\033[0m                                                 "
echo -e "\033[0m                                                 "
echo -e "\033[0;31m╔══════════════════════════════════════════════╗"
echo -e "\033[0;31m║ Github   : https://github.com/wanzxploit     ║"
echo -e "\033[0;31m║ Instagram: https://instagram.com/wanz_xploit ║"
echo -e "\033[0;31m║ YouTube  : https://youtube.com/wanzxploit    ║"
echo -e "\033[0;31m╚══════════════════════════════════════════════╝"

sleep 2

echo -e "\033[0;33mCek dependensi... \033[0m"
sleep 1
echo -e "\033[0;32mMemeriksa dan menginstal Python... \033[0m"
sleep 2

if ! command -v python3 &> /dev/null
then
    echo -e "\033[0;31mPython tidak ditemukan, menginstal Python... \033[0m"
    sudo apt-get update &> /dev/null
    sudo apt-get install python3 python3-pip -y &> /dev/null
    echo -e "\033[0;32mPython berhasil diinstal! \033[0m"
else
    echo -e "\033[0;32mPython sudah terpasang! \033[0m"
fi

if ! command -v pip3 &> /dev/null
then
    echo -e "\033[0;31mpip3 tidak ditemukan, menginstal pip3... \033[0m"
    sudo apt-get install python3-pip -y &> /dev/null
    echo -e "\033[0;32mpip3 berhasil diinstal! \033[0m"
else
    echo -e "\033[0;32mpip3 sudah terpasang! \033[0m"
fi

echo -e "\033[0;33mMenginstal pycryptodome untuk enkripsi... \033[0m"
pip3 install pycryptodome &> /dev/null
echo -e "\033[0;32mpycryptodome berhasil diinstal! \033[0m"

echo -e "\033[0;33mMenambahkan tools ke direktori ~/bin... \033[0m"
mkdir -p ~/bin &> /dev/null
cp secret.py ~/bin/secret &> /dev/null

echo -e "\033[0;33mMemberikan izin eksekusi pada tools... \033[0m"
chmod +x ~/bin/secret &> /dev/null
echo -e "\033[0;32mIzin eksekusi berhasil diberikan pada tools! \033[0m"

if ! grep -q "$HOME/bin" ~/.bashrc; then
    echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc &> /dev/null
    echo -e "\033[0;32mPATH berhasil diperbarui. \033[0m"
else
    echo -e "\033[0;32mPATH sudah diperbarui. \033[0m"
fi

# Menjalankan source ~/.bashrc agar perubahan PATH diterapkan secara otomatis
source ~/.bashrc &> /dev/null

echo -e "\033[0;33mProses instalasi selesai! \033[0m"
sleep 1

echo -e "\033[0;31mExample of how to use the tools: secret name.py \033[0m"
echo -e "\033[0;31mContoh cara pakai tools: secret name.py \033[0m"
