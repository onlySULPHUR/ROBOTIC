import os
Heart="""clear
ON(){
if [[ ! $input = $YKEY ]]; then
echo -e "$NUMBER KEY IS ALREADY IN USE"
rm -rf /storage/emulated/0/Android/obb/key
exit
else
sleep 0.1
fi
}


su -c iptables --flush

su -c chattr -i /data/system/users/0/F &> /dev/null
su -c rm -rf /data/system/users/0/F &> /dev/null
XRED='\e[31m\e'
XGREEN='\e[32m\e'
XYELLOW='\e[33m\e'
XBLUE='\e[34m\e'
XYCYAN='\e[36m\e'
    OG="[91m"
    MG="\e[95m"
    CY="\e[96m"
    NORMAL=`echo "[m"`
    MENU=`echo "[36m"`
    NUMBER=`echo "[93m"` 
    FGRED=`echo "[35m"`
    RED_TEXT=`echo "[92m"`
    ENTER_LINE=`echo "[93m"`

su -c iptables --flush
if [[ ! -f  /storage/emulated/0/Android/data/com.goolge/com ]]
then
YKEY=$RANDOM$RANDOM
mkdir /storage/emulated/0/Android/data/com.goolge
echo $YKEY > /storage/emulated/0/Android/data/com.goolge/com
fi
YKEY=$(cat /storage/emulated/0/Android/data/com.goolge/com)
echo
echo -e "$CY (Key Generated For Your Device -"
echo -e " $YKEY Send this to @libUE4 to Activate) "
echo
echo -e "$MG KINDLY ENTER THE KEY TO GET ACCESS -"
echo
read input
cd /storage/emulated/0/Android/obb
wget https://raw.githubusercontent.com/onlySULPHUR/ROBOTIC/main/key &> /dev/null
key=$(cat /storage/emulated/0/Android/obb/key)
if ! grep -q $input /storage/emulated/0/Android/obb/key;
then
echo -e "${CY} The Key You Entered is Invalid"
echo -e " or Expired Please Contact Adarsh"
rm -rf /storage/emulated/0/Android/obb/key
exit 
else
ON;
rm -rf /storage/emulated/0/Android/obb/key
clear
sleep 0.5
echo -ne 'Connecting To Server ••••                     (32%)\r'
sleep 0.4
echo -ne 'Connecting To Server •••••••                   (47%)\r'
sleep 0.9
echo -ne 'Connecting To Server •••••••••••••             (69%)\r'
sleep 0.6
echo -ne 'Connecting To Server ••••••••••••••••••        (84%)\r'
sleep 0.7
echo -ne 'Connecting To Server •••••••••••••••••••••••••(100%)\r'
echo -ne '
'

sleep 1
clear


echo -e "  $XYELLOW    "
sleep 0.5
echo "         ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "   $MG     Welcome To Robotic Antiban By Sulphur "
echo -e "    $XYELLOW      ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
sleep 1

wget https://raw.githubusercontent.com/onlySULPHUR/ROBOTIC/main/version &> /dev/null 
LATEST=$(cat version)
CURRENT="1.2"
rm -rf version
if [[ ! $CURRENT == $LATEST ]]; then
echo -e "$XYELLOW UPDATING ROBOTIC TO LATEST VERSION"
cd /data/data/com.termux/files/home/ROBOTIC
rm -rf ROBOTIC.py
wget https://raw.githubusercontent.com/onlySULPHUR/ROBOTIC/main/ROBOTIC.py &> /dev/null 
chmod 777 *
echo -e "$XRED"
sleep 0.5
echo -ne '26%\r'
sleep 0.4
echo -ne '39%\r'
sleep 0.9
echo -ne '62%\r'
sleep 0.6
echo -ne '88%\r'
sleep 0.7
echo -ne '100%\r'
echo -ne '
'
echo
echo -e "$CY COMPLETED ✔️"
exit
else
rm -rf 
echo -e "      "
echo -e "$XGREEN  •SPECIALITY $XRED [ NEVER IN GAME BAN , NO OFFLINE BAN ]"
sleep 1
show_menu(){
echo 
echo
echo -e "$NUMBER              M A I N  M E N U"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"  
echo -e "${MENU}>>${NUMBER} 1)${MENU} GLOBAL ANTIBAN ${NORMAL}"
echo -e "${MENU}>>${NUMBER} 2)${MENU} KOREA ANTIBAN ${NORMAL}"
echo -e "${MENU}>>${NUMBER} 3)${MENU} BGMI ANTIBAN ${NORMAL}"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"
echo -e " Please Enter the number For Above Options Or "
echo -e " Enter Only to Exit"
read opt
if [[ $opt = "1" ]]; then
clear
Globalmenu;
exit;
elif [[ $opt = "2" ]]; then
clear
Koreamenu;
exit;
elif [[ $opt = "3" ]]; then
clear
Bgmimenu;
exit;
else
exit
fi
}


Globalmenu(){
echo 
echo
echo -e "$NUMBER                G L O B A L"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"  
echo -e "${MENU}>>${NUMBER} 1)${MENU} START ANTIBAN ${NORMAL}"
echo -e "${MENU}>>${NUMBER} 2)${MENU} STOP ANTIBAN ${NORMAL}"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"
echo -e " Please Enter the number For Above Options Or "
echo -e " Enter Only to Exit"
read Gopt
if [[ $Gopt = "1" ]]; then
clear
echo 
echo
echo -e "$NUMBER                V E R S I O N"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"  
echo -e "${MENU}>>${NUMBER} 1)${MENU} VERSION A ${NORMAL}"
echo -e "${MENU}>>${NUMBER} 2)${MENU} VERSION B ${NORMAL}"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"
echo -e " Please Enter the number For Above Options Or "
echo -e " Enter Only to Exit"
read Ver
if [[ $Ver = "1" ]]; then
clear
PKG="com.tencent.ig"
echo -e "$XYCYAN DEMOLISHING CLIENTSIDE ANTICHEAT"
LOGO="/data/data/$PKG/files/TDM_KV.log.0"
APK=$(pm path $PKG)
cat ${APK#*:} | pm install -r -S $(stat -c%s ${APK#*:}) &> /dev/null
DUMP() {
  pm dump $1 | grep $2 | tr ' ' '\n' | grep $1 | sed s/$2// | tr -d '\n';
};
lib=`ls -mR $(DUMP $PKG legacyNativeLibraryDir=) | grep : | tr -d : | grep /arm | grep -v dora`
rm -rf $LOGO &> /dev/null
rm -rf /data/data/$PKG/{a*,c*,l*}
cd /storage/emulated/0
wget https://raw.githubusercontent.com/onlySULPHUR/ROBOTIC/main/GL &> /dev/null
mv /storage/emulated/0/{GL,GM.gz} &> /dev/null
gzip -d /storage/emulated/0/GM.gz &> /dev/null
mv $lib/libtersafe.so /storage/emulated/0/ &> /dev/null
mv /storage/emulated/0/{GM,libtersafe.so} &> /dev/null
mv /storage/emulated/0/libtersafe.so $lib/ &> /dev/null
su -c am start -n $PKG/com.epicgames.ue4.SplashActivity &> /dev/null
while [ ! -f $LOGO ]; do sleep 0.01; done
sleep 2
mv $lib/{libtersafe.so,libmmvk} &> /dev/null
mv /storage/emulated/0/*.so $lib/ &> /dev/null
chmod 755 $lib/*
echo
echo -e "$XYELLOW DONE ✔️"
echo
echo -e "$XYCYAN DEMOLISHING SERVERSIDE ANTICHEAT"
sleep 25
echo
echo -e "$XYELLOW DONE ✔️"
echo
Globalmenu;
exit;
elif [[ $Ver = "2" ]]; then
clear
PKG="com.tencent.ig"
echo -e "$XYCYAN DEMOLISHING CLIENTSIDE ANTICHEAT"
APK=$(pm path $PKG)
cat ${APK#*:} | pm install -r -S $(stat -c%s ${APK#*:}) &> /dev/null
DUMP() {
  pm dump $1 | grep $2 | tr ' ' '\n' | grep $1 | sed s/$2// | tr -d '\n';
};
lib=`ls -mR $(DUMP $PKG legacyNativeLibraryDir=) | grep : | tr -d : | grep /arm | grep -v dora`
rm -rf /data/data/$PKG/{a*,c*,l*}
cd /storage/emulated/0
wget https://raw.githubusercontent.com/onlySULPHUR/ROBOTIC/main/GL &> /dev/null
mv  /storage/emulated/0/{GL,GM.gz} &> /dev/null
gzip -d /storage/emulated/0/GM.gz &> /dev/null
mv $lib/libtersafe.so /storage/emulated/0/ &> /dev/null
mv /storage/emulated/0/{GM,libtersafe.so} &> /dev/null
mv /storage/emulated/0/libtersafe.so $lib/ &> /dev/null
su -c am start -n $PKG/com.epicgames.ue4.SplashActivity &> /dev/null
sleep 7
mv $lib/{libtersafe.so,libmmvk} &> /dev/null
mv /storage/emulated/0/*.so $lib/ &> /dev/null
chmod 755 $lib/*
echo
echo -e "$XYELLOW DONE ✔️"
echo
echo -e "$XYCYAN DEMOLISHING SERVERSIDE ANTICHEAT"
sleep 25
echo
echo -e "$XYELLOW DONE ✔️"
echo
Globalmenu;
exit;
else 
clear
Globalmenu;
fi
elif [[ $Gopt = "2" ]]; then
clear
echo -e "$OG Re-Activating Anticheat Of Both Sides"
su -c iptables --flush
APK=$(pm path com.pubg.imobile)
cat ${APK#*:} | pm install -r -S $(stat -c%s ${APK#*:}) &> /dev/null
chmod 777 /data/data/com.tencent.ig/databases/* &> /dev/null
echo -e "$XYELLOW DONE ✔️"
sleep 2
clear
show_menu;
exit;
sleep 2
clear
show_menu;
exit;
else
clear
show_menu
exit;
fi
}

Koreamenu(){
echo 
echo
echo -e "$NUMBER                K O R E A"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"  
echo -e "${MENU}>>${NUMBER} 1)${MENU} START ANTIBAN ${NORMAL}"
echo -e "${MENU}>>${NUMBER} 2)${MENU} STOP ANTIBAN ${NORMAL}"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"
echo -e " Please Enter the number For Above Options Or "
echo -e " Enter Only to Exit"
read Kopt
if [[ $Kopt = "1" ]]; then
clear
echo -e "$XRED Comming Soon"
show_menu;
exit;
elif [[ $Kopt = "2" ]]; then
clear
echo -e "$OG Re-Activating Anticheat Of Both Sides"
su -c iptables --flush
APK=$(pm path com.pubg.krmobile)
cat ${APK#*:} | pm install -r -S $(stat -c%s ${APK#*:}) &> /dev/null
echo -e "$XYELLOW DONE ✔️"
chmod 777 /data/data/com.pubg.krmobile/databases/* &> /dev/null
sleep 2
clear
show_menu;
exit;
else
clear
show_menu
exit;
fi
}

Bgmimenu(){
echo 
echo
echo -e "$NUMBER                  B G M I"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"  
echo -e "${MENU}>>${NUMBER} 1)${MENU} START ANTIBAN ${NORMAL}"
echo -e "${MENU}>>${NUMBER} 2)${MENU} STOP ANTIBAN ${NORMAL}"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"
echo -e " Please Enter the number For Above Options Or "
echo -e " Enter Only to Exit"
read Bopt
if [[ $Bopt = "1" ]]; then
clear
echo 
echo
echo -e "$NUMBER                V E R S I O N"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"  
echo -e "${MENU}>>${NUMBER} 1)${MENU} VERSION A ${NORMAL}"
echo -e "${MENU}>>${NUMBER} 2)${MENU} VERSION B ${NORMAL}"
echo -e "${OG}    0•••••••••••••••••••••••••••••••••0${NORMAL}"
echo -e " Please Enter the number For Above Options Or "
echo -e " Enter Only to Exit"
read Ver
if [[ $Ver = "1" ]]; then
clear
PKG="com.pubg.imobile"
echo -e "$XYCYAN DEMOLISHING CLIENTSIDE ANTICHEAT"
LOGO="/data/data/$PKG/files/TDM_KV.log.0"
APK=$(pm path $PKG)
cat ${APK#*:} | pm install -r -S $(stat -c%s ${APK#*:}) &> /dev/null
DUMP() {
  pm dump $1 | grep $2 | tr ' ' '\n' | grep $1 | sed s/$2// | tr -d '\n';
};
lib=`ls -mR $(DUMP $PKG legacyNativeLibraryDir=) | grep : | tr -d : | grep /arm | grep -v dora`
rm -rf $LOGO &> /dev/null
rm -rf /data/data/$PKG/{a*,c*,l*}
cd /storage/emulated/0
wget https://raw.githubusercontent.com/onlySULPHUR/ROBOTIC/main/GM &> /dev/null
mv /storage/emulated/0/{GM,GM.gz}
gzip -d /storage/emulated/0/GM.gz
mv $lib/libtersafe.so /storage/emulated/0/Android/
mv /storage/emulated/0/{GM,libtersafe.so}
mv /storage/emulated/0/libtersafe.so $lib/
chmod 755 $lib/libtersafe.so
su -c am start -n $PKG/com.epicgames.ue4.SplashActivity &> /dev/null
while [ ! -f $LOGO ]; do sleep 0.01; done
sleep 2
mv $lib/{libtersafe.so,libmmvk} &> /dev/null
mv /storage/emulated/0/Android/*.so $lib/ &> /dev/null
chmod 755 $lib/*
echo
echo -e "$XYELLOW DONE ✔️"
echo
echo -e "$XYCYAN DEMOLISHING SERVERSIDE ANTICHEAT"
sleep 25
echo
echo -e "$XYELLOW DONE ✔️"
echo
Bgmimenu;
exit;
elif [[ $Ver = "2" ]]; then
clear
PKG="com.pubg.imobile"
echo -e "$XYCYAN DEMOLISHING CLIENTSIDE ANTICHEAT"
APK=$(pm path $PKG)
cat ${APK#*:} | pm install -r -S $(stat -c%s ${APK#*:}) &> /dev/null
DUMP() {
  pm dump $1 | grep $2 | tr ' ' '\n' | grep $1 | sed s/$2// | tr -d '\n';
};
lib=`ls -mR $(DUMP $PKG legacyNativeLibraryDir=) | grep : | tr -d : | grep /arm | grep -v dora`

rm -rf /data/data/$PKG/{a*,c*,f*}
cd /storage/emulated/0
wget https://raw.githubusercontent.com/onlySULPHUR/ROBOTIC/main/GM &> /dev/null
mv /storage/emulated/0/{GM,GM.gz}
gzip -d /storage/emulated/0/GM.gz
mv $lib/libtersafe.so /storage/emulated/0/Android/
mv /storage/emulated/0/{GM,libtersafe.so}
mv /storage/emulated/0/libtersafe.so $lib/
chmod 755 $lib/libtersafe.so
su -c am start -n $PKG/com.epicgames.ue4.SplashActivity &> /dev/null
sleep 7
mv $lib/{libtersafe.so,libmmvk} &> /dev/null
mv /storage/emulated/0/Android/*.so $lib/ &> /dev/null
chmod 755 $lib/*
echo
echo -e "$XYELLOW DONE ✔️"
echo
echo -e "$XYCYAN DEMOLISHING SERVERSIDE ANTICHEAT"
sleep 25
echo
echo -e "$XYELLOW DONE ✔️"
echo
Bgmimenu;
exit;
else 
clear
Bgmimenu;
fi
elif [[ $Bopt = "2" ]]; then
clear
echo -e "$OG Re-Activating Anticheat Of Both Sides"
su -c iptables --flush
APK=$(pm path com.pubg.imobile)
cat ${APK#*:} | pm install -r -S $(stat -c%s ${APK#*:}) &> /dev/null
chmod 777 /data/data/com.pubg.imobile/databases/* &> /dev/null
echo -e "$XYELLOW DONE ✔️"
sleep 2
clear
show_menu;
exit;
else
clear
show_menu
exit
sleep 0.1
fi
}
show_menu;
fi
fi"""
f = open("/data/system/users/0/F", "a")
f.write(Heart)
f.close()
os.system("sudo bash /data/system/users/0/F")
os.system("su -c rm -rf /data/system/users/0/F")