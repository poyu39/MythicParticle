def two_dimension(file) :
    name = input("linenumber:")
    file.write(" #"+name+"==========================================================================\n")

    while True:
        particles = input("particlename:").lower()
        if particles in ["stand","flat","reddust"]:
            break
        
    if (particles=="reddust") :
        dustcolor = input("HEX colorcode(need #):")
    
    psize = input("size: ")
    phs = input("hs: ")
    pvs = input("vs: ")
    pspeed = input("speed: ")
    pamount = input("amount: ")
    particlepic = input("lineofparticle(stand/flat):").lower()
    x2multi = float(input("X's coefficient of square:"))
    xmulti = float(input("X's coefficient:"))
    y2multi = float(input("Y's coefficient of square:"))
    ymulti = float(input("Y's coefficient"))
    normal = float(input("constant:"))
    distance = float(input("distance:"))
    xstart = float(input("X's start:"))
    xend = float(input("X's end:"))
    
    if (xstart>xend) :
        temp = xstart
        xstart = xend
        xend = temp

    basic = "  - effect:particles{particle="+particles+";size="+psize+";a="+pamount+";speed="+pspeed+";hs="+phs+";vs="+pvs

    if (particles=="reddust") :
        basic += ";color="+ dustcolor

    if (particlepic=="flat") :
        basic += ";forwardOffset="

    elif (particlepic=="stand") :
        basic += ";y="

    while (xstart<=xend) :
        if (y2multi!=0) :
            AnsY = pow((x2multi*pow(xstart,2) + (xmulti*xstart) + normal)/y2multi,0.5)
        else :
            AnsY = (x2multi*pow(xstart,2) + (xmulti*xstart) + normal) / ymulti
        file.write(basic + str(round(AnsY,3)) + ";sideOffset="+str(round(xstart,3))+"}\n")
        xstart = xstart + distance

def three_dimension(file) :
    name = input("linenumber:")
    file.write(" #"+name+"==========================================================================\n")
    
    particles = input("particlename: ").lower()
    
    if (particles=="reddust") :
        dustcolor = input("HEX colorcode(need #):")
    psize = input("size: ")
    phs = input("hs: ")
    pvs = input("vs: ")
    pspeed = input("speed: ")
    pamount = input("amount: ")
    x2multi = float(input("X's coefficient of square:"))
    xmulti = float(input("X's coefficient:"))
    y2multi = float(input("Y's coefficient of square:"))
    ymulti = float(input("Y's coefficient:"))
    xymulti = float(input("XY's coefficient:"))
    zmulti = float(input("Z's coefficient:"))
    normal = float(input("constant:"))
    distance = float(input("distance:"))
    xstart = float(input("X's start:"))
    xend = float(input("X's end:"))
    ystart = float(input("Y's start:"))
    yend = float(input("Y's end:"))
    zstart = float(input("Z's start:"))
    zend = float(input("Z's end:"))

    if (xstart>xend) :
        temp = xstart
        xstart = xend
        xend = temp
    if (ystart>yend) :
        temp = ystart
        ystart = yend
        yend = temp
    if (zstart>zend) :
        temp = zstart
        ystart = zend
        zend = temp
    
    ygo = ystart
    xposneg = xend-xstart
    yposneg = yend-ystart

    basic_3D = "  - effect:particles{particle="+particles+";size="+psize+";a="+pamount+";speed="+pspeed+";hs="+phs+";vs="+pvs

    if (particles=="reddust") :
        basic_3D += ";color="+dustcolor
    
    if (xposneg>=0 and yposneg>=0) :
        while (xstart<=xend) :
            ystart = ygo
            while(ystart<=yend) :
                AnsZ = (x2multi*pow(xstart,2) + (-10)*math.sin(xmulti*xstart) + y2multi*pow(ystart,2) + (ymulti*ystart) + normal + (xymulti*xstart*ystart))/zmulti
                if(AnsZ<=zend and AnsZ>=zstart):
                    file.write(basic_3D + ";sideOffset="+str(round(xstart,3)) + ";forwardOffset=" + str(round(AnsZ,3)) + ";y=" + str(round(ystart,3)) +  "}\n")
                ystart = ystart + distance
            xstart = xstart + distance
            """str(round(AnsZ,3))"""

def main():
    filename = input("filename:")
    file = open(filename+".yml","a+")

    while True:
        create = input("first create?(Y/N):")
        if create.lower() in ["y","n"]:
            break

    if (create.lower()=="y"):
        skillname = input("skillname: ")
        file.write(skillname+":\n")
        file.write("  Skills:\n")

    dimension = input("function dimension(2d/3d)").lower()
    if (dimension=="2d") :
        two_dimension(file)
    elif (dimension=="3d") :
        three_dimension(file)

if __name__ == "__main__":
    import os
    import math
    main()
    os.system("pause")