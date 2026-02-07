import cv2 as cv
import numpy as np


def draw_shapes(width=512, height=512):
   
    """
    Draws basic geometric shapes and text using OpenCV.

    Returns:
        img (numpy.ndarray): Image with drawings
  

  OpenCV Coordinate System (512 x 512 image)

        (top-left)               (511, 0)
        (0, 0)  -------------------------> X (width)
                |                          |
                |                          |
                |                          |
                |                          |
                |                          |
                |                          |
    Y (height)  v                          v
        (0, 511)---------------------------> (511, 511)
        
            

    - Origin (0, 0) is at the top-left corner of the image
    - X-axis increases from left to right (width)
    - Y-axis increases from top to bottom (height)
   
    """


    

    # Create a black image
    img = np.zeros((height, width, 3), np.uint8)

    # -----------------------
    # Draw Line
    # -----------------------
    cv.line(
        img,
        (0, 0),
        (width - 1, height - 1),
        (255, 0, 0),  # Blue
        thickness=5
    )

    # -----------------------
    # Draw Rectangle
    # -----------------------
    cv.rectangle(
        img,
        (350, 20),# Top-left corner of the rectangle
        (500, 150),# Bottom-right corner of the rectangle
        (0, 255, 0),  # Green
        thickness=3
    )

    # -----------------------
    # Draw Circle
    # -----------------------
    cv.circle(
        img, 
        (425, 85), # Center of the circle
        60, # Radius of the circle
        (0, 0, 255),  # Red
        thickness=-1  # Filled circle
    )

    # -----------------------
    # Draw Ellipse
    # -----------------------
    cv.ellipse(
        img,
        (256, 256),        # Center
        (120, 60),         # Axes length
        0,                 # Rotation angle
        0, 180,            # Start and end angle
        (255, 255, 0),     # Cyan
        thickness=3
    )

    # -----------------------
    # Draw Polygon
    # -----------------------
    pts = np.array(
        [[50, 300], [150, 250], [250, 300], [200, 400], [100, 400]],
        np.int32
    )
    pts = pts.reshape((-1, 1, 2))

    cv.polylines(
        img,
        [pts],
        isClosed=True,
        color=(0, 255, 255),  # Yellow
        thickness=3
    )

    # -----------------------
    # Add Text
    # -----------------------
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(
        img,
        "OpenCV Drawing Demo",
        (20, height - 20),
        font,
        0.8, # font scale
        (255, 255, 255),
        2, #thickness
        cv.LINE_AA
    )

    return img


img = draw_shapes()

cv.imshow("Output", img)
cv.waitKey(0)
cv.destroyAllWindows()


   
