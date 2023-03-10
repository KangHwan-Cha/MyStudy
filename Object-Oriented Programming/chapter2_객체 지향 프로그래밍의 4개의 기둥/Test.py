class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    # 모든 인스턴스 변수를 _를 통해서 외부 접근을 막는다
    def __init__(self, name, password, payment_limit):
        self.name = name
        self._password = password
        self._payment_limit = payment_limit

    @property
    def password(self):
        return "비밀 번호는 볼 수 없습니다"

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def payment_limit(self):
        return self._payment_limit

    @payment_limit.setter
    def payment_limit(self, new_payment_limit):
        if new_payment_limit >= 0 and new_payment_limit <= CreditCard.MAX_PAYMENT_LIMIT:
            self._payment_limit = new_payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")