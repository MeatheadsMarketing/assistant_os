#!/bin/bash

cd ~/Desktop/assistant-os-raycast

# Git identity
git config user.name "MeatheadsMarketing"
git config user.email "mmshopify2024@gmail.com"

# Initialize and commit
git init
git add .
git commit -m "📦 Initial commit: Finalized Assistant OS snapshot"
git branch -M main
git remote add origin https://github.com/MeatheadsMarketing/assistant_os.git
git push -u origin main