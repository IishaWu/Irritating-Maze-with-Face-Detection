# Irritating-Maze-with-Face-Detection
Use face detection to control the circle to arrive the destination
# Installation
- OpenCV 安裝 ----> Ubuntu[安裝教學](https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/)  
- Raspberry[安裝教學](https://paper.dropbox.com/doc/Raspi-install-opencv-IHaVgymS9tRgfhnCaCSGv)
# How to
- Please notice which the directory you install the opencv and modify the code in face_game.py

  # Load prebuilt model for Frontal Face
	cascadePath = "/home/nicole/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt.xml"
- python face_game.py
- Use trackbar to swith 'Start' bar 0 to 1, therefore, you can start the game.
- You can also switch the 'Level' bar 1 to 5, the width of path would be changed to more small.
- When you want to restart the game, switch the 'Start' bar 1 to 0 and then swith the 'Start' bar 0 to 1,it would re-locate your start point.
- Use 'q' to end the program.
- You can also conbine the Face-Recognition, all you need are in Source/.
![pic](http://ms15.voip.edu.tw/~nicole/photo1.png)
![pic](http://ms15.voip.edu.tw/~nicole/photo2.jpg)
# Source
- [Raspberry-Face-Recognition](https://github.com/trieutuanvnu/Raspberry-Face-Recognition)
