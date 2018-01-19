# Import OpenCV2 for image processing
import cv2

# Import numpy for matrices calculations
import numpy as np
def nothing(x):
    pass

def drawmap(image,level):
	cv2.line(image,(0,200),(300,200),(255,0,0),5)
	cv2.line(image,(300,200),(300,400),(255,0,0),5)
	cv2.line(image,(300,400),(800,400),(255,0,0),5)
	#cv2.line(image,(800,400),(800,100),(255,0,0),5)
	#cv2.line(image,(800,100),(1200,100),(255,0,0),5)

	cv2.line(image,(0,200+level),(300-level,200+level),(255,0,0),5)
	cv2.line(image,(300-level,200+level),(300-level,400+level),(255,0,0),5)
	cv2.line(image,(300-level,400+level),(800+level,400+level),(255,0,0),5)
	#cv2.line(image,(800+level,400+level),(800+level,100+level),(255,0,0),5)
	#cv2.line(image,(800+level,100+level),(1200,100+level),(255,0,0),5)

def main():
	# Create Local Binary Patterns Histograms for face recognization


	recognizer = cv2.face.createLBPHFaceRecognizer()

	# Load the trained mode
	recognizer.load('trainer/trainer.yml')

	# Load prebuilt model for Frontal Face
	cascadePath = "/home/nicole/opencv-3.2.0/data/haarcascades/haarcascade_frontalface_alt.xml"

	# Create classifier from prebuilt model
	faceCascade = cv2.CascadeClassifier(cascadePath);

	# Set the font style
	font = cv2.FONT_HERSHEY_SIMPLEX

	# Initialize and start the video frame capture
	cam = cv2.VideoCapture(0)

	cv2.namedWindow('game')
	# Read the video frame
	ret, im =cam.read()
	cv2.createTrackbar('Level','game',1,5,nothing)
	#cv2.createButton('Start', callbackButton2, s, CV_PUSH_BUTTON, 0)
	# create switch for ON/OFF functionality
	switch = '0 : OFF \n1 : ON'
	cv2.createTrackbar(switch, 'game',0,1,nothing)
	# Convert the captured frame into grayscale
	gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

	# Get all face from the video frame
	faces = faceCascade.detectMultiScale(gray, 1.2,5)
	fx,fy,fw,fh=0,0,0,0
	try:
		fx,fy,fw,fh = faces[0]
	except:
		pass	
	c=0
	sc=1
	s=0	
	# Loop
	while True:
		# Read the video frame
		ret, im =cam.read()
		
		image = cv2.imread('map.jpg')
		# Convert the captured frame into grayscale
		gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

		# Get all face from the video frame
		faces = faceCascade.detectMultiScale(gray, 1.2,5)
		
		print(faces)
		# For each face in faces
		level=100+5//cv2.getTrackbarPos('Level','game')*20
		s = cv2.getTrackbarPos(switch,'game')
		#map
		drawmap(image,level)
		try:
			x,y,w,h = faces[0]
		except:
			continue
		# Create rectangle around the face
		cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

		# Recognize the face belongs to which ID
		#Id, www = recognizer.predict(gray[y:y+h,x:x+w])
		Id=1
		# map


		# Check the ID if exist 
		if(Id == 1):
		    Id = "Nicole"
		else:
		    Id = "Unknow"

		# Display the video frame with the bounded rectangle
		cv2.rectangle(im, (x-22,y-60), (x+w+22, y-22), (0,166,166), 2)
		cv2.putText(im, str(Id), (x,y-30), font, 1, (255,255,255), 2)

		if s==1:
			if sc>0:
				sc=sc-1
				try:
                			fx,fy,fw,fh = faces[0]
				except:
                			pass

			sx = 0
			sy = 200+level//2
	
			cv2.circle(image, (sx+(fx-x)*3, sy+(y-fy)*3), 25, (0, 255, 0), -1)
			if (700<sx+(fx-x+25//2)*3<800 )and (400<sy+(y-25//2-fy)*3<400+level):
				cv2.putText(image, str('Congradulation! Error : ')+str(c)+str(' times'), (x,y-60), font, 1, (255,255,255), 2)
				s=0
			elif (( sx+(fx-x+25//2)*3 < 300) and  (200 < sy+(y-25//2-fy)*3)and(sy+(y+25//2-fy)*3 < 200+level)):
				#cv2.putText(image, str('1'), (x,y-60), font, 1, (255,255,255), 2)
				pass
			elif (300-level<sx+(fx-x-25//2)*3)and (sx+(fx-x+25//2)*3<300) and (200<sy+(y-25//2-fy)*3)and (sy+(y+25//2-fy)*3<400+level):
				#cv2.putText(image, str('2'), (x,y-60), font, 1, (255,255,255), 2)
				pass
			elif (300-level<sx+(fx-x+25//2)*3<800) and (400<sy+(y-25//2-fy)*3)and (sy+(y+25//2-fy)*3<400+level):
				#cv2.putText(image, str('3'), (x,y-60), font, 1, (255,0,0), 2) 
				pass
			else:
				cv2.putText(image, str('Oops....'), (x,y-60), font, 1, (0,0,255), 2)
				c=c+1
		#image = cv2.resize(image, (600,600), interpolation=cv2.INTER_CUBIC)
		else:
			sc=1
			c=0
		# Put text describe who is in the picture
		cv2.imshow('game', image)
		cv2.imshow('face',im) 


		# If 'q' is pressed, close program
		if cv2.waitKey(10) & 0xFF == ord('q'):
			break

	# Stop the camera
	cam.release()

	# Close all windows	
	cv2.destroyAllWindows()
main()
