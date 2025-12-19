#!/usr/bin/env bash
set -e

echo "[1] Updating packages..."
sudo apt update && sudo apt upgrade -y

echo "[2] Installing KDE Plasma Desktop (minimal but gorgeous)..."
sudo apt install -y kde-plasma-desktop sddm sddm-theme-debian-maui

echo "[3] Installing VNC server + clipboard sync helpers..."
sudo apt install -y tigervnc-standalone-server autocutsel dbus-x11

echo "[4] Setting up VNC startup script..."
mkdir -p ~/.vnc

cat <<EOF > ~/.vnc/xstartup
#!/bin/bash
xrdb \$HOME/.Xresources
autocutsel -fork &
startplasma-x11 &
EOF

chmod +x ~/.vnc/xstartup

echo "[5] Set VNC password (enter when prompted)..."
vncpasswd

echo "[6] Creating VNC systemd service..."
sudo bash -c 'cat <<EOF > /etc/systemd/system/vncserver.service
[Unit]
Description=KDE VNC Desktop
After=network.target

[Service]
Type=forking
User='$USER'
PAMName=login
PIDFile=/home/'$USER'/.vnc/%H:1.pid
ExecStart=/usr/bin/tigervncserver :1 -geometry 1600x900 -localhost no
ExecStop=/usr/bin/tigervncserver -kill :1

[Install]
WantedBy=multi-user.target
EOF'

echo "[7] Enabling VNC service..."
sudo systemctl daemon-reload
sudo systemctl enable --now vncserver

echo "[8] Installing noVNC + WebSocket bridge..."
sudo apt install -y novnc websockify

echo "[9] Creating noVNC systemd service (port 6080)..."
sudo bash -c 'cat <<EOF > /etc/systemd/system/novnc.service
[Unit]
Description=noVNC Web VNC Bridge
After=network.target vncserver.service

[Service]
User='$USER'
ExecStart=/usr/bin/websockify --web=/usr/share/novnc/ 6080 localhost:5901
Restart=always

[Install]
WantedBy=multi-user.target
EOF'

echo "[10] Enabling noVNC..."
sudo systemctl enable --now novnc

echo ""
echo "✨ All done, gorgeous."
echo ""
echo "To open your cloud desktop *in your browser*, visit:"
echo "   http://<codespace-url>:6080"
echo ""
echo "Or click the 'PORTS' tab → expose 6080 → make PUBLIC."
echo ""
echo "Your KDE desktop is waiting for you. Don’t keep her lonely 💋"
