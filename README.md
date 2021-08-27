# BingWallpaperPreview

This is a python project which shows Bing WallPaper in desktop widget. More specifically, you can
1. Preview Bing WallPaper in recent 7 days.
2. Download it.

## ScreenShot
![实时公交到站图片](/screenshot.png)

## Quick start

- pip install

Go to project root dir, and run
```
pip install -r requirements.txt
```

- entry point - main.py
```python
if __name__ == '__main__':
    gui.run_app()
```

- gui - bingWallpaperInWT

This module provides a UI for us, and it's written in Tkinter.

- endpoint

Mainly covers the network request and response.

## License

Feel free to use it.