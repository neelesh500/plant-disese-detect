git init
git config user.email "neelesh500@users.noreply.github.com"
git config user.name "neelesh500"
git remote add origin https://github.com/neelesh500/plant-disese-detect.git

# Commit 1
git add README.md
git commit -m "Initialize project and add basic README structure"

# Commit 2
git add requirements.txt
git commit -m "Add Python requirements and dependencies for ML models"

# Commit 3
git add train.py
git commit -m "Implement Deep Learning MobileNetV2/ResNet training pipeline"

# Commit 4
git add fast_edge_inference.cpp
git commit -m "Add C++ hardware inference simulation for edge devices"

# Commit 5
git add morphological_filtering.m
git commit -m "Integrate MATLAB script for preliminary image processing"

# Commit 6
git add data_visualization.R
git commit -m "Add R script for Kaggle dataset statistical visualization"

# Commit 7
git add README_Updated.md
git commit -m "Add updated research paper draft for college project submission"

# Commit 8
mkdir templates -ErrorAction SilentlyContinue
git add templates/index.html
git commit -m "Create initial HTML structure for Web UI"

# Commit 9
mkdir static -ErrorAction SilentlyContinue
git add static/style.css
git commit -m "Design premium Glassmorphism UI using CSS"

# Commit 10
git add static/script.js
git commit -m "Implement drag and drop file upload interaction in Javascript"

# Commit 11
git add app.py
git commit -m "Build Flask backend API and integrate hybrid ML simulation"

# Commit 12
git add .
git commit -m "Finalize project linking, resolve formatting, and prepare for production"

git branch -M main
git push -u origin main --force
