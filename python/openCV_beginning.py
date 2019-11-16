import cv2
import numpy as np
import matplotlib

image = cv2.imread('./../images/input.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
img = cv2.imread('./../images/input.jpg',0)


cv2.imshow('Hello World', image)
cv2.waitKey()
cv2.destroyAllWindows()

print(image.shape)

# BGR Values for the first 0,0 pixel
B, G, R = image[0, 0] 
print(B, G, R)
print(image.shape)

i = img[0,0]

cv2.imwrite('./images/first_output.png', image)

# Create a black image
image_b = np.zeros((512,512,3), np.uint8)

# Can we make this in black and white?
image_bw = np.zeros((512,512), np.uint8)

cv2.imshow("Black Rectangle (Color)", image_b)
cv2.imshow("Black Rectangle (B&W)", image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.line(image_b, (0,0), (511,511), (255,127,0), 5)
cv2.rectangle(image_b, (100,100), (300,250), (127,50,127), -1)
cv2.circle(image_b, (350, 350), 100, (15,75,50), -1) 
cv2.polylines(image_b, [pts], True, (0,0,255), 3)
cv2.putText(image_b, 'Hello World!', (75,290), cv2.FONT_HERSHEY_COMPLEX, 2, (100,170,0), 3)

