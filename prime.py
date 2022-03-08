import cv2 as cv
import numpy as np
import os


os.chdir(os.path.dirname(os.path.abspath(__file__)))
# cv.IMREAD_UNCHANGED
# IMREAD_REDUCED_COLOR_2
class Prime:
    find_img = None
    resorce_width = 0
    resorce_height = 0
    method_find = 0

    def __init__(self,find_resource_path, method = cv.TM_CCOEFF_NORMED):
            self.find_img = cv.imread(find_resource_path, cv.IMREAD_REDUCED_COLOR_2)

            self.resorce_width = self.find_img.shape[1]
            self.resorce_height = self.find_img.shape[0]

            self.method_find = method

    def findClickPositions( self, cryofall_img, match_threshold = 0.6, debug_mode=None):

        result = cv.matchTemplate(cryofall_img, self.find_img, self.method_find)

        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        y_loc, x_loc = np.where(result >= match_threshold)

        rectangles = []
        for (x,y) in zip(x_loc, y_loc):
            rectangles.append([int(x), int(y), int(self.resorce_width), int(self.resorce_height)])
            rectangles.append([int(x), int(y), int(self.resorce_width), int(self.resorce_height)])

        rectangles, weights = cv.groupRectangles(rectangles, 1, 0.2)

        points = []
        if len(rectangles):
            print('Found Resource')
            for (x, y, resorce_width, resorce_height) in rectangles:
                center_x_loc = x + int(resorce_width/2)
                center_y_loc = y + int(resorce_height/2)
                points.append((center_x_loc, center_y_loc))
                if debug_mode == 'rectangles':               
                    cv.rectangle(cryofall_img, (x,y), (x + resorce_width, y + resorce_height), (0,255,0), 1)
                elif debug_mode == 'points':
                    cv.drawMarker(cryofall_img, (center_x_loc, center_y_loc), (0,255,255), 2)
        if debug_mode:
            cv.imshow("Resource Match", cryofall_img)
            # cv.waitKey()
            # cv.destroyAllWindows()

        return points

# points = findClickPositions('./rock_stack.jpeg', './find_tree.jpeg', debug_mode='rectangles', match_threshold= 0.6)


# finding a tree threshold === .30
# The threshold to collect stons === 0.6
# The threshold to collect wood === 0.7

















# locations = list(zip(*locations[::-1]))
# print(locations)

# if locations:
#     print('Found Rocks')

#     rock_width = find_img.shape[1]
#     rock_height = find_img.shape[0]
#     line_color = (0, 255, 0)
#     line_type = cv.LINE_4

#     for loc in locations:
#         top_left = loc
#         bottom_right = (top_left[0] + rock_width, top_left[1] + rock_height)
#         cv.rectangle(crystall_img, top_left, bottom_right, line_color, line_type)

#         cv.imshow('Matches', crystall_img)
#         cv.waitKey()

#     else:
#         print("Rock not Found")


# cv.imshow('Result', result_img)
# cv.waitKey()
