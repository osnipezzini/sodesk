set sh1 to "launchctl unload -w /Library/LaunchDaemons/xyz.sotech.SODesk_service.plist;"
set sh2 to "/bin/rm /Library/LaunchDaemons/xyz.sotech.SODesk_service.plist;"
set sh3 to "/bin/rm /Library/LaunchAgents/xyz.sotech.SODesk_server.plist;"

set sh to sh1 & sh2 & sh3
do shell script sh with prompt "SODesk want to unload daemon" with administrator privileges