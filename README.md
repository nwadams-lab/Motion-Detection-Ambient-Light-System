"# Motion-Detection-Ambient-Light-System" 

This project had 4 contributors, myself and 3 of my classmates in IT254 at ISU They each have a repo of their own.

DESC:

#The project is a simple Smart Light that activates when a human is detected by an attached camera.
#It also has a photo resistor that detects ambient light levels, the code has an inverse relationship with the detected light level.
#The Light only turns on when a human is detected to save powwer, the brightness level is determined by the ambient lighting.

HOW TO USE:
Connect Arduino to laptop
Upload ino code to arduino board
Build a photoresister LED circuit on Breadboard
Attach Arduino to camera device (like a laptop or raspberry pi)
Run Python code on Device with camera
LED will assume brightness level based on environment
LED WILL TURN ON/change brightness when HUMAN is deteccted

TOOLS:

We used the pre-built YOLO (You Only Look Once) human detection ML model. We used a laptop camera for our demonstration but any camera input can be read.
We first built out the simple photo resistor circuit and arduino code.
Afterwards we spent most of our time creating the python script that interacts with the camera and ML
Initially we used cv2 ML for human/movement detection, but it was falky and only detected people sometimes, and only while they were moving.
After much trial and error, we switched to YOLOv8.

PROJECT TIMELINE:

5 weeks

Week 1:
Decide on project idea, goal, title.

Week 2:
Group Project Planning
Decided how the project would be executed. 

Week 3-5:
Most of the work took place during this time.
Weekly meetings on wednesday


