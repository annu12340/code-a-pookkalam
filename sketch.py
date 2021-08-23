
def s(color, side):
    return rectangle(w=side, h=side, fill=color, stroke='#fff')
darkred = rectangle(w=230, h=230,fill='#c92a2a',stroke='none') | repeat(9, rotate(10))
lightred =rectangle(w=210, h=210,fill='#e03131',stroke='none') | repeat(9, rotate(10))
darkorange=rectangle(w=200, h=200,fill='#f76707',stroke='#fff') | repeat(9, rotate(10))
lightorange=rectangle(w=190, h=190,fill='#f08c00',stroke='#fff') | repeat(9, rotate(10))

lyellowp= rectangle(w=175, h=175,fill='#ff922b',stroke='#fff')|  rotate(10) | repeat(30,  rotate(50))
lyellowp1= s(side=150, color='#ffd43b') | rotate(80) | repeat(100,  rotate(160))
whitep = s(side=145, color='#212529')  | repeat(10,  rotate(10))

show(darkred,lightred,darkorange,lightorange,lyellowp,lyellowp1,whitep)



shape = circle(x=90, y=0, r=2,stroke="#fff") | repeat(50, rotate(30))
show(shape)

shapeEllipse = ellipse(w=175,h=60, fill="#2b8a3e" , stroke="#fff") | repeat(50,rotate(50))
show(shapeEllipse)

# e1=ellipse(h=167,w=60,fill="#2b8a3e",stroke="none")|repeat(20,rotate(20))
e2=ellipse(h=150,w=35,fill="#e03131",stroke="none")|rotate(10)|repeat(100,rotate(20))
e4=ellipse(h=150,w=30,fill="#ff922b",stroke="none")|rotate(15)|repeat(150,rotate(20))
e5=ellipse(h=150,w=30,fill="#c92a2a",stroke="none")|rotate(10)|repeat(100,rotate(20))

e10=circle(r=55,fill="#fff",stroke="none")
show(e2,e4,e5,e10)

shapeEllipse = ellipse(w=105,h=30, fill="#fff" , stroke="#fff") | repeat(50,rotate(50))
show(shapeEllipse)


c4=circle(r=30,fill="#fff",stroke="none")
show(c4)


sun=circle(r=7,x=15,y=10,fill="#FF7C00",stroke="none",stroke_width=1.5)
boatbase=ellipse(y=-20,w=80,h=5,fill="#495057")
el3=ellipse(x=-20,y=-3,h=35,w=12,fill="black")
h1=circle(x=-10, y=12, r=3,fill="black")
boat=boatbase+el3|scale(0.5)
show(sun,boat,h1)

z2 = line(-20, 1, 10, -20)
show(z2)




st = "hello onam"
print(' '.join(format(ord(x), 'b') for x in st))




