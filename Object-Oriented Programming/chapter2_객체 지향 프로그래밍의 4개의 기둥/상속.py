class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name # 이름
        self.wage = wage # 시급

    def raise_pay(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        self.wage *= self.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + "직원: " + self.name

class Cashier(Employee): # 클래스 정의 한뒤에 괄호로 묶어 상속받을 부모 클래스를 적어준다.
    """계산대 직원 클래스"""
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
            return Cashier.company_name + " 계산대 직원: " + self.name


class DeliveryMan(Employee):
    """배달원 클래스"""

    def __init__(self, name, wage, on_standby):
        super().__init__(name, wage)
        self.on_standby = on_standby

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원 복귀를 처리한다"""
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + " 배달원: " + self.name

# 다중 상속하기
## 다중 상속의 단점은 __str__(던더에스티알)의 활용이 어렵다.
class CashierDeliveryMan(DeliveryMan, Cashier):
    def __init__(self, name, wage, on_standby, number_sold=0):
        Employee.__init__(self, name, wage)
        self.on_standby = on_standby
        self.number_sold = number_sold


##****테스트 주석
# taeho = DeliveryMan("성태호", 7000, True)
#
# taeho.raise_pay()
# print(taeho.wage)
#
# taeho.deliver("서울시 코드잇로 51 최고 건물 401호")
# taeho.deliver("서울시 코드잇로 51 최고 건물 402호")
#
# taeho.back()
# taeho.deliver("서울시 코드잇로 51 최고 건물 402호")
#
# print(taeho)
#
# print(DeliveryMan.mro())