import PyInstaller.__main__

PyInstaller.__main__.run([
    'app.py',
    '--onefile',
    '--windowed',
    '--clean',
])

print("--- DONE! Your app is now in the 'dist' folder ---")