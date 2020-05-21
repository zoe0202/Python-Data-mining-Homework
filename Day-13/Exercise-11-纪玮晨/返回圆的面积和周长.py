import math

class Circle(object):
	def __init__(self,radius):
		self._radius = radius
	def area(self):
		return math.pi * self._radius ** 2
	def perimeter(self):
		return 2 * math.pi * self._radius

def main():
	r = int(input("请输入圆的半径："))
	circle = Circle(r)
	print("圆的面积为：",circle.area())
	print("圆的周长为：",circle.perimeter())

if __name__ == "__main__":
	main()