class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The restaurant\'s name is ' + self.restaurant_name)
        print('The cuisine type is ' + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + ' is opening')


restaurant = Restaurant('有家餐厅', '中式')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print('The restaurant name is ' + restaurant.restaurant_name.title())
print('The restaurant cuisine type is ' + restaurant.cuisine_type.title())
