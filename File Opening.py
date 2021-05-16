Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('hello')
hello
>>> for i in range(1, 100)
SyntaxError: invalid syntax
>>> for i in range(1, 100):
	print("hello World!")

hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
hello World!
>>> clear
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> import os
>>> os.startfile('C:\Users\Aditya\Pictures')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> os.startfile('C:/Users/Aditya/Pictures/')
>>> os.startfile('C:/Users/Aditya/Pictures/Do it.jpg')
>>> os.startfile('rC:\Users\Aditya\Pictures/Do it.jpg')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 3-4: truncated \UXXXXXXXX escape
>>> os.startfile(r'C:\Users\Aditya\Pictures/Do it.jpg')
>>> os.chdir(r'C:\Users\Aditya\Pictures')
>>> os.listdir
<built-in function listdir>
>>> os.listdir()
['2cb27571a5d731effda5401e536780a0.jpg', '3f8d650085742f7905a8451a83a8eee8--negative-people-quotes-live-and-learn.jpg', '9f9a88799eac3437664e94df173e8c1d.png', 'Amazing-Batman-v-Superman-Movie-4K-Wallpaper.jpg', 'Arduino-Projects-Volume-1.jpg', 'Backup', 'Banking ER Model.svg', 'Camera Roll', 'cool-pictures-for-profile-pic-best-whatsapp-profile-picture.jpg', 'CyberLink Cloud', 'desktop.ini', 'Do it.jpg', 'DSLqkLIXUAIe_ig.jpg', 'Instructions Of Zerodha.png', 'Motivational-Wallpaper-02-2560x1600.jpg', 'Motivational-Wallpaper-03-1920x1080.jpg', 'Only Goku', 'PICS', 'Pointer Basics in C - GeeksQuiz.html', 'Pointer Basics in C - GeeksQuiz_files', 'Saved Pictures', 'square-linkedin-512.png', 'Things', 'wp1859212-the-ninja-h2r-wallpapers.jpg', 'wp1859212.jpg', 'wp1859230-the-ninja-h2r-wallpapers.jpg', 'wp1859258-the-ninja-h2r-wallpapers.jpg', '_27721_table145.jpg.gif']
>>> pic = os.listdir()
>>> import random
>>> random.choice(pic)
'Motivational-Wallpaper-02-2560x1600.jpg'
>>> print(random.choice(pic))
Arduino-Projects-Volume-1.jpg
>>> pic = random.choice(pic)
>>> os.start(pic)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    os.start(pic)
AttributeError: module 'os' has no attribute 'start'
>>> os.startdfile(pic)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    os.startdfile(pic)
AttributeError: module 'os' has no attribute 'startdfile'
>>> os.startfile(pic)
>>> pic
'CyberLink Cloud'
>>> import glob
>>> glob.glob('*.mp3')
[]
>>> glob.glob('*.jpg')
['2cb27571a5d731effda5401e536780a0.jpg', '3f8d650085742f7905a8451a83a8eee8--negative-people-quotes-live-and-learn.jpg', 'Amazing-Batman-v-Superman-Movie-4K-Wallpaper.jpg', 'Arduino-Projects-Volume-1.jpg', 'cool-pictures-for-profile-pic-best-whatsapp-profile-picture.jpg', 'Do it.jpg', 'DSLqkLIXUAIe_ig.jpg', 'Motivational-Wallpaper-02-2560x1600.jpg', 'Motivational-Wallpaper-03-1920x1080.jpg', 'wp1859212-the-ninja-h2r-wallpapers.jpg', 'wp1859212.jpg', 'wp1859230-the-ninja-h2r-wallpapers.jpg', 'wp1859258-the-ninja-h2r-wallpapers.jpg']
>>> songs = glob.glob('*.jpg')
>>> songs
['2cb27571a5d731effda5401e536780a0.jpg', '3f8d650085742f7905a8451a83a8eee8--negative-people-quotes-live-and-learn.jpg', 'Amazing-Batman-v-Superman-Movie-4K-Wallpaper.jpg', 'Arduino-Projects-Volume-1.jpg', 'cool-pictures-for-profile-pic-best-whatsapp-profile-picture.jpg', 'Do it.jpg', 'DSLqkLIXUAIe_ig.jpg', 'Motivational-Wallpaper-02-2560x1600.jpg', 'Motivational-Wallpaper-03-1920x1080.jpg', 'wp1859212-the-ninja-h2r-wallpapers.jpg', 'wp1859212.jpg', 'wp1859230-the-ninja-h2r-wallpapers.jpg', 'wp1859258-the-ninja-h2r-wallpapers.jpg']
>>> del songs
>>> jpg = glob.glob('*.jpg')
>>> import system
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    import system
ModuleNotFoundError: No module named 'system' >>>
