final=$(ifconfig | grep '192' | cut -d ' ' -f 2) 
timestamp=$(date +"%Y-%m-%d--%H:%M:%S")
cp ./dispTemplate.txt ./index.htm
sed -i .del "s/__IP__/"$final"/g" ./index.htm
sed -i .del "s/__TIME__/"$timestamp"/g" ./index.htm
lftp martinogg.com -u serverstatus_martinogg.com:martin -p 21 -e 'put ./index.htm; bye'
