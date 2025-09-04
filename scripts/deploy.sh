#!/bin/bash
cd /home/ec2-user/weather-app

# Kill old Flask process if running
pkill -f "python3 app.py" || true

# Start new Flask app in background
nohup python3 app.py > app.log 2>&1 &
