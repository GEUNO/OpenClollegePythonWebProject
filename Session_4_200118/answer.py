class Car:
    def __init__(self, company, model, color):
        self.etc= company
        self.model= model
        self.color= color
        self.oil= 1000

    def forward(self):
        self.oil -= 50
        print(self.etc, self.model, self.color, "차량이 전진합니다. 남은 기른양:", self.oil)


hyundai= Car("hyundai", "sonata", "silver")

hyundai.forward()


class Electric_Car(Car):
    def __init__(self, company, model, color):
        super().__init__(company, model, color)
        self.power= 100

    def forward(self):
        self.power -= 10
        print(self.etc, self.model, self.color, "차량이 전진합니다. 남은 충전잔량:", self.power)


tesla= Electric_Car("Tesla", "Model 3", "white")
tesla.forward()