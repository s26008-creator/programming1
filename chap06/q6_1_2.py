class Person:
    def __init__(self,
                name = '',
                nationality = '',
                birth = '',
                address = ''):
        self.name = name
        self.nationality = nationality
        self.birth = birth
        self.address = address

    def show_attributes(self):
        print("名前:", self.name)
        print("国籍:", self.nationality)
        print("生まれた年:", self.birth)
        print("住んでいるところ:", self.address)
    
name = Person('大貴','日本','2006','沖縄県豊見城市')
name.show_attributes()
