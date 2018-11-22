class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, maximum):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.maximum = maximum

    def describe_restaurant(self):
        print('The restaurant\'s name is ' + self.restaurant_name)
        print('The cuisine type is ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + ' is opening')

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, maximum_people):
        self.maximum = maximum_people

restaurant = Restaurant('有家餐厅', '中式')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(20)
print('The restaurant name is ' + restaurant.restaurant_name.title())
print('The restaurant cuisine type is ' + restaurant.cuisine_type.title())
print('Totally ' + str(restaurant.number_served) + ' people eaten in this restaurant' )
print('The maximum people is ' + str(restaurant.increment_number_served))
# 1st way to change the value of number_served
# restaurant.number_served = 20

