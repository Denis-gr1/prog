from sqlalchemy.orm import sessionmaker
from database import init_db, Разработчик, Менеджер, Проект
from datetime import date

def fill_database():
    engine = init_db()
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Разработчик).delete()
    session.query(Менеджер).delete()
    session.query(Проект).delete()
    session.commit()

 
    менеджер1 = Менеджер(имя="Иван Петров", email="i.petrov@company.com")
    менеджер2 = Менеджер(имя="Светлана Иванова", email="s.ivanova@company.com")

    dev1 = Разработчик(имя="Алексей Смирнов", должность="Бэкенд", email="a.smirnov@company.com")
    dev2 = Разработчик(имя="Мария Кузнецова", должность="Фронтенд", email="m.kuznetsova@company.com")
    dev3 = Разработчик(имя="Дмитрий Васильев", должность="Fullstack", email="d.vasiliev@company.com")

    проект1 = Проект(
        название="Мобильное приложение",
        описание="Разработка для iOS и Android",
        срок_сдачи=date(2023, 12, 31),
        менеджер=менеджер1
    )
    
    проект2 = Проект(
        название="Обновление сайта",
        описание="Создание сайта",
        срок_сдачи=date(2023, 11, 15),
        менеджер=менеджер2
    )
    проект1.разработчики.extend([dev1, dev2])
    проект2.разработчики.extend([dev2, dev3])

    session.add_all([менеджер1, менеджер2, dev1, dev2, dev3, проект1, проект2])
    session.commit()
    print("База данных успешно заполнена тестовыми данными!")

if __name__ == "__main__":
    fill_database()