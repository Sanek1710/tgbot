SYSSERVICEPATH="/lib/systemd/system"
SERVICENAME="tgbot-py.service"
SERVICEPATH="$SYSSERVICEPATH/$SERVICENAME"
MAINPATH=$(realpath ./../main.py)

PYTHONPATH=$(which python3)
if [ -z "$PYTHONPATH" ];
    then PYTHONPATH=$(which python);
    if [ -z "$PYTHONPATH" ];
        then PYTHONPATH=$(which python2);
    fi
fi

content="[Unit]
Description=Telegram Bot Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=\"$PYTHONPATH\" \"$MAINPATH\"
StandardInput=tty-force

[Install]
WantedBy=multi-user.target"

sudo echo "$content" > "$SERVICENAME"
sudo cp "$SERVICENAME" "$SERVICEPATH"
rm "$SERVICENAME"

sudo systemctl daemon-reload
