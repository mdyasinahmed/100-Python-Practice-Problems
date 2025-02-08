import math

# # def getAngle(H , M):
# #     # code here
# #     minuteAngle = M * 6
# #     hourAngle = (H*30) + (M*0.5)
    
# #     angle = abs(hourAngle - minuteAngle)

# #     return angle


# print(getAngle(9, 0))
H = 9
M = 0

angle = 360-((H+M/60)*30)

print(math.floor(angle))