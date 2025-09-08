import cv2
import matplotlib.pyplot as plt
import numpy as np

# Create a figure and axes for matplotlib
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()

# Reading video from web camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Convert the frame to the format expected by matplotlib
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Clear the axes and display the image
    ax.clear()
    ax.imshow(frame_rgb)
    
    # Display the frame
    plt.pause(0.001)
    
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
plt.close()
cv2.destroyAllWindows()
