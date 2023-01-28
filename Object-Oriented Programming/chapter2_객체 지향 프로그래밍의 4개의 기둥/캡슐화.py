class Citizen:
    """주민 클래스"""
    drinking_age = 19

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.set_age(age)
        self._resident_id = resident_id

    def authentinate(self, id_field):
        return self._resident_id == id_field

    def can_dring(self):
        return self._age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self._age) + "살입니다!"

    def get_age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        # 캡슐화된 속성을 클래스 안의 다른 메소드를 활용하여 접근하도록!
        # getter method
        return self._age

    def set_age(self, value):
        """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
        # setter method
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value

young = Citizen("kanghwan cha", 15, "12345678")
print(young.get_age())
young.set_age(30)
print(young.get_age())

# young = Citizen("kanghwan cha", 18, "12345678")
# print(young.get_age())
# young.set_age(25)
# print(young.get_age())