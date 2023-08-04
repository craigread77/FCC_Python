class Rectangle:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)

    def __str__(self):
        return "{}(width={}, height={})".format(__class__.__name__, self.width, self.height)
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width + self.height) * 2

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):
        if any([self.width > 50, self.height > 50]):
            return "Too big for picture."

        out_str = ''
        for i in range(self.height):
            out_str += '*' * self.width + "\n"
        return out_str
    
    def get_amount_inside(self, shape):
        rem_area = self.get_area()
        shape_area = shape.get_area()


        return int(rem_area / shape_area)

        
            


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length
    
    def __str__(self):
        return "{}(side={})".format(__class__.__name__, self.width)
    
    def set_side(self, length):
        self.width = length
        self.height = length
    
    def set_width(self, length):
        self.width = length
        self.height = length

    def set_height(self, length):
        self.width = length
        self.height = length
    
