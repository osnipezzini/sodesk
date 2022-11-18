on run {daemon_file, agent_file, user}

  set sh1 to "echo " & quoted form of daemon_file & " > /Library/LaunchDaemons/xyz.sotech.SODesk_service.plist && chown root:wheel /Library/LaunchDaemons/xyz.sotech.SODesk_service.plist;"

  set sh2 to "echo " & quoted form of agent_file & " > /Library/LaunchAgents/xyz.sotech.SODesk_server.plist && chown root:wheel /Library/LaunchAgents/xyz.sotech.SODesk_server.plist;"

  set sh3 to "cp -rf /Users/" & user & "/Library/Preferences/xyz.sotech.SODesk/SODesk.toml /var/root/Library/Preferences/xyz.sotech.SODesk/;"

  set sh4 to "cp -rf /Users/" & user & "/Library/Preferences/xyz.sotech.SODesk/SODesk2.toml /var/root/Library/Preferences/xyz.sotech.SODesk/;"

  set sh5 to "launchctl load -w /Library/LaunchDaemons/xyz.sotech.SODesk_service.plist;"

  set sh to sh1 & sh2 & sh3 & sh4 & sh5

  do shell script sh with prompt "SODesk want to install daemon and agent" with administrator privileges
end run
