SYSSERVICEPATH="/lib/systemd/system"
SERVICEPATH="$SYSSERVICEPATH/tgbot-py.service"
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

sudo echo "$content" > "$SERVICEPATH"

sudo systemctl daemon-reload
