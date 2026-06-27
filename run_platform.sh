#!/bin/bash

PROJECT="$HOME/Documents/Fred_Commodity_Yield"

cd "$PROJECT" || exit 1

echo "========================================="
echo "Global Macro Intelligence Platform"
echo "Started: $(date)"
echo "========================================="

# Activate virtual environment (if you have one)
# source venv/bin/activate

# Run the platform
python3 main.py

# Commit and push only if there are changes
git add .

if ! git diff --cached --quiet; then
    git commit -m "Automated Update $(date '+%Y-%m-%d %H:%M')"
    git push origin main
    echo "GitHub updated."
else
    echo "No changes detected."
fi

echo "Finished: $(date)"