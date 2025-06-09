# 50) Program for calculating how many no of cans paints require for painting the wall
import math
def paint_calculation(height,width,cover):
    area = height*width
    no_of_cans = math.ceil(area/cover)
    print(f"You will need {no_of_cans} cans of paints.")

h = float(input("Enter The height of wall in meters: \n"))
w = float(input("Enter The width of wall in meters: \n"))
coverage = 7
paint_calculation(width=w, height=h, cover=coverage)
