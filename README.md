# My Server Map

## Setup

### 1. Export your Xaero map
- Open Minecraft → press M → Export as PNG
- Save it as `bigmap.png`

### 2. Install gdal2tiles
Open Command Prompt and run:
```
pip install gdal2tiles
```

### 3. Convert PNG to tiles
```
gdal2tiles --zoom=0-5 --webviewer=none bigmap.png tiles
```
This fills the `tiles/` folder automatically.

### 4. Upload to GitHub Pages
```
git init
git add .
git commit -m "first upload"
git branch -M main
git remote add origin https://github.com/YOURUSERNAME/mymap.git
git push -u origin main
```
Then go to repo Settings → Pages → select main branch → Save.

Your map will be live at: https://YOURUSERNAME.github.io/mymap

## Customise
- Edit the server name in `index.html` line with "My Anarchy Server"
- Use the coord search box (top right) to jump to any X, Z
- Mouse over the map to see coordinates
