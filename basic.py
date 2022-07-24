import os
select=1
print("""

     ___      .______    _______  _______          ___    __  
    /   \     |   _  \  |   ____||       \        / _ \  /_ | 
   /  ^  \    |  |_)  | |  |__   |  .--.  |______| | | |  | | 
  /  /_\  \   |   _  <  |   __|  |  |  |  |______| | | |  | | 
 /  _____  \  |  |_)  | |  |____ |  '--'  |      | |_| |  | | 
/__/     \__\ |______/  |_______||_______/        \___/   |_| 
                                                             
____________________________(+)________________________________
  
  Owner       :  MD MAZHARUL ISLAM ABED
 
  Github       :  Abed-01

  Facebook  : MD MAZHARUL ISLAM
  
  Page          :   ABED
  
  Youtube     : A B E D
  
  Contact     : +8801841268478
______________________________(+)_________________________________
******************************************************************
1.Start Installation
2.exit
****************************************************************** """)
selection=int(input("select your choice :"))
if selection==select:
	os.system("pkg update -y &&  pkg upgrade -y &&  pkg install python -y &&  pkg install python2 -y &&  pkg install fish -y && pkg install ruby -y && pkg install git -y &&  pkg install php -y &&  pkg install perl -y && pkg install nmap -y && pkg install bash -y && pkg install clang -y ")
	os.system("pkg install python3 && pkg install python-pip && pip2 install wget && pip install bs4 && pip2 install bs4 && pip install requests && pip2 install requests && pip install mechanize && pip2 install mechanize && pip install php && pip2 install php && pkg install wget")
	os.system("pkg install openssl -y && pkg install cmatrix -y && pkg install openssh -y && pkg install wireshark -y && pkg install toilet && pkg install sl && pkg install vim && pkg install tch && pkg install zsh && pkg install fortune && pkg install zsh && apt update && apt upgrad")
	os.system("pkg install nano -y && pkg install w3m -y && pkg install hydra -y && pkg install figlet -y && pkg install cowsay -y && pkg install curl -y&& pkg install tar -y && pkg install zip -y && pkg install unzip -y && pkg install tor -y && pkg install wget -y && pkg install wcalc -y && pkg install bmon -y && pkg install golang -y")
	os.system("pkg install git && pkg install php && pkg install parallel && pkg install bash && pkg install nano && pkg install curl && pkg install tar && pkg install zip && pkg install unzip && pkg install net-tools && pkg install tor -y && pkg install sudo -y && pkg install file && pkg install python-pip && termux-setup-storage")
	print("installation complete")
	print("Now you can enjoy the termux app")
else :
	print("Try Again")
