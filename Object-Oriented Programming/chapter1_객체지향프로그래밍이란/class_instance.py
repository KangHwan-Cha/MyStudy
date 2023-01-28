class User:
    count = 0
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        # 인사 메세지 출력 메소드
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def login(self, my_email, my_password):
        # 로그인 메소드
        if (self.email == my_email and self.password == my_password):
            print("로그인 성공, 환영합니다.")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 불린으로 리턴하는 메소드
        return self.name == name

    def __str__(self):
        return "사용자 : {}, 이메일 : {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        print("총 유저 수는: {}입니다.", format(cls.count))

# user1 = User("김대위", "captain@codeit.kr", "12345")
# user2 = User("강영훈", "younghoon@codeit.kr", "98765")
# user3 = User("Taeho", "taeho@codeit.kr", "123abc")
# user4 = User("Lisa", "lisa@codeit.kr", "abc123")


# user1.login("captain@codeit.kr", "12345")
# print(user1.check_name("김대위"))
# print(user1.check_name("강영훈"))
# print(user1)
# print(User.count)
User.number_of_users()
