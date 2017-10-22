from math import *

class PointSet:
    def __init__(self,pt=[]):
        self.contents = pt
        for i in pt:
            self.x = i[0]
            self.y = i[1]
            
    def insertPt(self,newP):
        newPt =  PointSet(pt=[newP]+self.contents)
        return newPt
    
    def deletePt(self,delPt):
        if delPt in self.contents:
            self.contents.remove(delPt)
        else:
            print ("point not found")
 
    def sortX(Lx):
        Lx = PointSet(sorted(Lx.contents, key= lambda p: [p[0]]))
        return Lx
    
    def sortY(Ly):
        Ly = PointSet(sorted(Ly.contents, key= lambda p: [p[1]]))
        return Ly
    
    def manhattan_closest_dc(Lx,Ly,dListL,dListR,dmin):#divide and conqure 
        if len(Lx.contents) > 4 and len(Ly.contents) > 4:
            midX = len(Lx.contents)//2   
            midY = len(Ly.contents)//2
            leftX = PointSet(Lx.contents[:midX])  #divide the list sorted by x
            leftY = PointSet(Ly.contents[:midY])  #divide th list sorted by y
            rightX = PointSet(Lx.contents[midX:])
            rightY = PointSet(Ly.contents[midY:])
            
            if leftX.contents[0]!= leftY.contents[0]: 
                dxL = abs(leftX.contents[0][0]-leftY.contents[0][0])  
                dyL = abs(leftX.contents[0][1]-leftY.contents[0][1])
                dL = dxL + dyL
                dListL.append(dL)
                
                if len(leftX.contents)>1:
                    mid = len(leftX.contents) // 2 
                    midDxX1 = abs(leftX.contents[mid-1][0]- leftX.contents[mid][0])#pairs which one point on left                 
                    midDyX1 = abs(leftX.contents[mid-1][1]- leftX.contents[mid][1])#and one on right  side of the divide line
                    dmidX1 = midDxX1 + midDyX1
                    dListL.append(dmidX1)
                elif len(leftY.contents)>1:
                    mid = len(leftY.contents) // 2 
                    midDxY2 = abs(leftY.contents[mid][0]- leftY.contents[mid][0])
                    midDyY2 = abs(leftY.contents[midY][1]- leftY.contents[mid][1])
                    dmidY2 = midDxY2 + midDyY2
                    dListL.append(dmidY2)
                dminL = min(dListL)
                dmin.append(dminL)
                return leftX.manhattan_closest_dc(leftY,dListL,dListR,dmin)
            
            if leftX.contents[0] == leftY.contents[0]:
                dxL = abs(leftX.contents[0][0]-leftY.contents[1][0])
                dyL = abs(leftX.contents[0][1]-leftY.contents[1][1])
                dL = dxL + dyL
                dListL.append(dL)
                if len(leftX.contents)>1:
                    mid = len(leftX.contents) // 2 
                    midDxX1 = abs(leftX.contents[mid-1][0]- leftX.contents[mid][0])#pairs which one point on left                 
                    midDyX1 = abs(leftX.contents[mid-1][1]- leftX.contents[mid][1])#and one on right  side of the divide line
                    dmidX1 = midDxX1 + midDyX1
                    dListL.append(dmidX1) 
                elif len(leftY.contents)>1:
                    mid = len(leftY.contents) // 2 
                    midDxY2 = abs(leftY.contents[mid-1][0]- leftY.contents[mid][0])
                    midDyY2 = abs(leftY.contents[mid-1][1]- leftY.contents[mid][1])
                    dmidY2 = midDxY2 + midDyY2
                    dListL.append(dmidY2) 
                dminL = min(dListL)
                dmin.append(dminL)
                return leftX.manhattan_closest_dc(leftY,dListL,dListR,dmin)
                
            if rightX.contents[0]!=rightY.contents[0]:               
                dxR = abs(rightX.contents[0][0]-rightY.contents[0][0])
                dyR = abs(rightX.contents[0][1]-rightY.contents[0][1])
                dR = dxR + dyR
                dListR.append(dR)
                 
                if len(rightX.contents)>1:
                    mid = len(rightX.contents) // 2 
                    midDxX1 = abs(rightX.contents[mid-1][0] - rightX.contents[mid][0])
                    midDyX1 = abs(rightX.contents[mid-1][1] - rightX.contents[mid][1])
                    dmidX1 = midDxX1 + midDyX1
                    dListR.append(dmidX1)
                elif len(rightY.contents)>1:
                    mid = len(rightY.contents) // 2 
                    midDxY2 = abs(rightY.contents[mid-1][0] - rightY.contents[mid][0])
                    midDyY2 = abs(rightY.contents[mid-1][1] - rightY.contents[mid][1])
                    dmidY2 = midDxY2 + midDyY2                
                    dListR.append(dmidY2) 
                dminR = min(dListR)
                dmin.append(dminR)
                return rightX.manhattan_closest_dc(rightY,dListL,dListR,dmin)
                
            if rightX.contents[0]==rightY.contents[0]:
                dxR = abs(rightX.contents[0][0]-rightY.contents[1][0])
                dyR = abs(rightX.contents[0][1]-rightY.contents[1][1])
                dR = dxR + dyR
                dListR.append(dR)
                
                if len(rightX.contents)>1:
                    mid = len(rightX.contents) // 2 
                    midDxX1 = abs(rightX.contents[mid-1][0] - rightX.contents[mid][0])
                    midDyX1 = abs(rightX.contents[mid-1][1] - rightX.contents[mid][1])
                    dmidX1 = midDxX1 + midDyX1
                    dListR.append(dmidX1) 
                elif len(rightY.contents)>1:
                    mid = len(rightY.contents) // 2 
                    midDxY2 = abs(rightY.contents[mid-1][0] - rightY.contents[mid][0])
                    midDyY2 = abs(rightY.contents[mid-1][1] - rightY.contents[mid][1])
                    dmidY2 = midDxY2 + midDyY2                
                    dListR.append(dmidY2)
                dminR = min(dListR)
                dmin.append(dminR)
                return rightX.manhattan_closest_dc(rightY,dListL,dListR,dmin)  
        if len(Lx.contents) <= 4 or len(Ly.contents) <= 4 :
            point = []
            dx = 0
            dy = 0
            if len(Lx.contents) <= 1:
                return 0
            else:
                for p in Lx.contents:
                    for q in Ly.contents:
                        if p != q:
                            dx = abs(p[0]-q[0])
                            dy = abs(p[1]-q[1])
                            dmin.append(dx+dy)
                    
                for p in Lx.contents:
                    for q in Ly.contents:
                        dx = abs(p[0]-q[0])
                        dy = abs(p[1]-q[1])
                        if (dx+dy) == min(dmin) and p not in point:
                            point.append(p)
                            point.append(q)
                        
            if len(dmin)==0:
                return 0
            else:
                return point,min(dmin)
                
a = PointSet([(1,2),(3,4),(5,6),(4,3),(15,4),(27,29),(34,28),(45,64),(17,21),(38,53),(11,29),(41,23)])                
lx = a.sortX() #sort list by x 
ly = a.sortY()
lx.manhattan_closest_dc(ly,[],[],[]) 
                        
