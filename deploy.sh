final=$(ifconfig | grep '192.' | awk '{print $2}') 
timestamp=$(date +"%Y-%m-%d--%H:%M:%S")
batteryper=$(termux-battery-status | grep 'percentage' | awk '{print $2}')

cp ./dispTemplate.txt ./index.htm
sed -i "s/__IP__/"$final"/g" ./index.htm
sed -i "s/__TIME__/"$timestamp"/g" ./index.htm
sed -i "s/__BATTERY__/"$batteryper"/g" ./index.htm

lftp martinogg.com -u serverstatus_martinogg.com:martin -p 21 -e 'put ./index.htm; bye'
