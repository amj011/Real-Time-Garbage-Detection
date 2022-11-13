# import cv2
# import numpy as np
# import requests
# import json         
# import geocoder 
# import time1


# net = cv2.dnn.readNet('yolov3_training_last.weights', 'yolov3_testing.cfg')

# classes = ['Garbage']
# with open("classes.txt", "r") as f:
#     classes = f.read().splitlines()

# cap = cv2.VideoCapture(r'C:\Users\HP\Desktop\Garbage-Detection\videoplayback_Trim.mp4')
# font = cv2.FONT_HERSHEY_PLAIN
# colors = np.random.uniform(0, 255, size=(100, 3))

# while True:
#     _, img = cap.read()
#     height, width, _ = img.shape

#     blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
#     net.setInput(blob)
#     output_layers_names = net.getUnconnectedOutLayersNames()
#     layerOutputs = net.forward(output_layers_names)

#     boxes = []
#     confidences = []
#     class_ids = []

#     for output in layerOutputs:
#         for detection in output:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.2:
#                 center_x = int(detection[0]*width)
#                 center_y = int(detection[1]*height)
#                 w = int(detection[2]*width)
#                 h = int(detection[3]*height)

#                 x = int(center_x - w/2)
#                 y = int(center_y - h/2)

#                 boxes.append([x, y, w, h])
#                 confidences.append((float(confidence)))
#                 class_ids.append(class_id)

#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

#     if len(indexes)>0:
#         for i in indexes.flatten():
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             confidence = str(round(confidences[i],2))
#             color = colors[i]
#             cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
#             cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)

#     cv2.imshow('Image', img)
#     key = cv2.waitKey(1)
#     if key ==27:
#         break
   
#     while float(confidence) >= 0.5:
#         g = geocoder.ip('me')
#         a= str(g.latlng)
                
            
#         url = "https://www.fast2sms.com/dev/bulk"                         
#         my_data ={
#             'sender_id': 'wq2shq',
#             'message' : 'collection of Garbage detected. Kindly come and collect. The target location co-ordinates are: '+ a,
#             'language' : 'english',
#             'route' : 'p',
#             'numbers' : '7725912536'
#         }
#         headers = {
#             'authorization' : 'gjMZNYQXBWcLdlG9nxm0Ao7yJuO1t5aUreDsqkpSVP43TvECbRHxe6JvSyALU9MFk1QVWhIqoPTG8Opf',
#             'Content-Type' : "application/x-www-form-urlencoded",
#             'Cache-Control' : "no-cache"
#         }
#         response = requests.request("POST",url,data=my_data, headers= headers)
#         returned_msg = json.loads(response.text)
#         print(returned_msg['message'])
        
        
        
            


# cap.release()
# cv2.destroyAllWindows()




import cv2
import numpy as np
import requests
import json         
import geocoder
import time

net = cv2.dnn.readNet('yolov3_training_last.weights', 'yolov3_testing.cfg')

classes = ['Garbage']
with open("classes.txt", "r") as f:
    classes = f.read().splitlines()

cap = cv2.VideoCapture(r'C:\Users\HP\Desktop\Garbage-Detection\videoplayback_Trim.mp4')
font = cv2.FONT_HERSHEY_PLAIN
colors = np.random.uniform(0, 255, size=(100, 3))

while True:
    _, img = cap.read()
    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0,0,0), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.2:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.2, 0.4)

    if len(indexes)>0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i],2))
            color = colors[i]
            cv2.rectangle(img, (x,y), (x+w, y+h), color, 2)
            cv2.putText(img, label + " " + confidence, (x, y+20), font, 2, (255,255,255), 2)

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)
    if key==27:
        break

    if float(confidence) >= 0.5:
        g = geocoder.ip('me')
        a= str(g.latlng)
                
            
        url = "https://www.fast2sms.com/dev/bulk"                         
        my_data ={
            'sender_id': 'wq2shq',
            'message' : 'collection of Garbage detected. Kindly come and collect. The target location co-ordinates are: '+ a,
            'language' : 'english',
            'route' : 'p',
            'numbers' : '7725912536'
        }
        headers = {
            'authorization' : 'gjMZNYQXBWcLdlG9nxm0Ao7yJuO1t5aUreDsqkpSVP43TvECbRHxe6JvSyALU9MFk1QVWhIqoPTG8Opf',
            'Content-Type' : "application/x-www-form-urlencoded",
            'Cache-Control' : "no-cache"
        }
        response = requests.request("POST",url,data=my_data, headers= headers)
        returned_msg = json.loads(response.text)
        print(returned_msg['message'])

cap.release()
cv2.destroyAllWindows()











# Image 

# import cv2
# import numpy as np
# import glob
# import random


# # Load Yolo
# net = cv2.dnn.readNet(r"C:\Users\HP\Desktop\Garbage-Detection\yolov3_training_1000.weights", r"C:\Users\HP\Desktop\Garbage-Detection\yolov3_testing.cfg")

# # Name custom object
# classes = ["Garbage"]

# # Images path
# images_path = glob.glob(r"C:\Users\HP\Desktop\Garbage-Detection\Test Images\*.jpg")



# layer_names = net.getLayerNames()
# output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
# colors = np.random.uniform(0, 255, size=(len(classes), 3))

# # Insert here the path of your images
# random.shuffle(images_path)
# # loop through all the images
# for img_path in images_path:
#     # Loading image
#     img = cv2.imread(img_path)
#     img = cv2.resize(img, None, fx=0.4, fy=0.4)
#     height, width, channels = img.shape

#     # Detecting objects
#     blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

#     net.setInput(blob)
#     outs = net.forward(output_layers)

#     # Showing informations on the screen
#     class_ids = []
#     confidences = []
#     boxes = []
#     for out in outs:
#         for detection in out:
#             scores = detection[5:]
#             class_id = np.argmax(scores)
#             confidence = scores[class_id]
#             if confidence > 0.3:
#                 # Object detected
#                 print(class_id)
#                 center_x = int(detection[0] * width)
#                 center_y = int(detection[1] * height)
#                 w = int(detection[2] * width)
#                 h = int(detection[3] * height)

#                 # Rectangle coordinates
#                 x = int(center_x - w / 2)
#                 y = int(center_y - h / 2)

#                 boxes.append([x, y, w, h])
#                 confidences.append(float(confidence))
#                 class_ids.append(class_id)

#     indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
#     print(indexes)
#     font = cv2.FONT_HERSHEY_PLAIN
#     for i in range(len(boxes)):
#         if i in indexes:
#             x, y, w, h = boxes[i]
#             label = str(classes[class_ids[i]])
#             color = colors[class_ids[i]]
#             cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
#             cv2.putText(img, label, (x, y + 30), font, 3, color, 2)


#     cv2.imshow("Image", img)
#     key = cv2.waitKey(0)

# cv2.destroyAllWindows()