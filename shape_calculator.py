class Rectangle:
   def __init__(self, width, height):
     self.width = width
     self.height = height
   
   def __str__(self):
     string = 'Rectangle(width='+ str(self.width) +', height=' + str(self.height)+')'

     return string

   def set_width(self,  width):
     self.width = width
     return self.width

   def set_height(self, height):
     self.height = height
     return self.height

   def get_area(self):
      return self.height * self.width



   def get_perimeter(self):
     return 2 * self.width + 2 * self.height

   def get_picture(self):
      
      if self.height > 50 or self.width > 50:
        return "Too big for picture."      
      
      string = ('*' * self.width) + '\n'
      string *= self.height

      return string

   def get_diagonal(self):

    return (self.width ** 2 + self.height ** 2) ** .5
    
   def get_amount_inside(self, rect):
     count = 0
     temp_height = rect.height
     temp_width = rect.width

     
     
     while(self.width >= temp_width):
        temp_width += rect.width 
        count += 1
       
       
     while(self.height >= temp_height and  self.width >= temp_height or  self.width >= temp_height):
       temp_height +=  rect.height 
       count += 1
       
     temp_height = rect.height
     temp_width = rect.width



    #  print("final count: " + str(count))
     return count

class Square(Rectangle):
  #  def __init__(self,side):
  #     self.side = side
   def __init__(self,  side):
    super(Square, self).__init__(side, side)
    self.side = side


   def __str__(self):
     string = 'Square(side='+ str(self.width) +')'
     #The issue is that I had to call self.width instead of self.side
    
     return string

   
   def set_side(self, side):
       self.side = side
       self.width = self.set_width(side) #fixed shape problem
       self.height = self.set_height(side) # fixed shape problem

       return self.side


  