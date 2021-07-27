./stop

SYSSERVICEPATH="/lib/systemd/system"
SERVICEPATH="$SYSSERVICEPATH/tgbot-py.service"

rm "$SERVICEPATH"

sudo systemctl daemon-reload