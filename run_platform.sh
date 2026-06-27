#!/bin/bash

PROJECT="/home/rajat/Documents/Fred_Commodity_Yield"
PYTHON="/home/rajat/.pyenv/versions/3.12.3/bin/python3"

cd "$PROJECT" || exit 1

echo "========================================="
echo "Global Macro Intelligence Platform"
echo "Started: $(date)"
echo "========================================="

$PYTHON main.py

if [ $? -eq 0 ]; then
    git add .

    if ! git diff --cached --quiet; then
        git commit -m "Automated Update $(date '+%Y-%m-%d %H:%M')"

        if git push origin main; then
            echo "GitHub updated successfully."
        else
            echo "GitHub push failed."
        fi
    else
        echo "No changes detected."
    fi
else
    echo "main.py failed. Nothing committed."
fi

echo "Finished: $(date)"