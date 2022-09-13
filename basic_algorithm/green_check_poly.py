# 使用 green formulation 来计算多变形的面积，顶点方向（逆时针、顺时针)
def check(vp):
	# xdy. if dy= 0 pass else  x= (x2-x1)/(y2-y1)(y-y1)+x1.inte = k/2*(y-y1)^2+x1*y|(y1,y2)
	#= 1/2(x2-x1)*(y2-y1)+x1*(y2-y1)
	s = 0
	for i in range(1,len(vp)):
		inte = 0
		dx = vp[i][0]-vp[i-1][0]
		dy = vp[i][1]-vp[i-1][1]
		
		inte = 1/2*dx*dy+vp[i-1][0]*dy
		s = s + inte
	# trail 
	if len(vp) >= 2:
		inte = 0
		dx = vp[0][0]-vp[-1][0]
		dy = vp[0][1]-vp[-1][1]
		inte = 1/2*dx*dy+vp[-1][0]*dy
		s = s + inte
	
	return s,s > 0

area, ans = check([[0,0],[1,0],[1,1]])
print("area={},isCounterClockWise={}".format(area, ans))
