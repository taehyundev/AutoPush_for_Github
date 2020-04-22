  
echo ""
echo ""
echo "#######################################################################################"
echo "#################################### run test #########################################"
echo "#######################################################################################"
echo ""
echo ""

cd autoPushList
dir


git init
git add .
git commit -m "auto push TEST"
git remote add origin https://github.com/taehyundev/AutoPush_for_Github
git push -f origin master


echo "[Message] auto commit and push fin"

function pause(){
   read -p "$*"
}

pause 'Press [Enter] key to continue...'
