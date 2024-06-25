import turtle as t

def hexagon(side):
  t.shape('turtle')
  for _ in range(6):
    t.forward(side)
    t.left(60)
  t.forward(side)  
  t.right(60)
    
for _ in range(6):
  hexagon(50)