from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database import Разработчик, Менеджер, Проект, участие_в_проекте

def run_queries():
    engine = create_engine('sqlite:///project_management.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("\n1. Все проекты с менеджерами:")
    projects = session.query(Проект).all()
    for p in projects:
        print(f"{p.название} | Менеджер: {p.менеджер.имя} | Срок: {p.срок_сдачи}")

    print("\n2. Разработчики в нескольких проектах:")
    busy_devs = session.query(Разработчик).join(участие_в_проекте).group_by(Разработчик.id).having(func.count(участие_в_проекте.c.проект_id) > 1).all()
    for dev in busy_devs:
        print(f"{dev.имя} ({dev.должность}) - {len(dev.проекты)} проектов")

    print("\n3. Количество разработчиков по проектам:")
    project_stats = session.query(
        Проект.название,
        func.count(участие_в_проекте.c.разработчик_id).label('количество')
    ).join(участие_в_проекте).group_by(Проект.id).all()
    
    for p in project_stats:
        print(f"{p.название}: {p.количество} разработчиков")

    print("\n4. Проекты менеджера 'Иван Петров':")
    manager = session.query(Менеджер).filter_by(имя="Иван Петров").first()
    for p in manager.проекты:
        print(f"- {p.название} (до {p.срок_сдачи})")

if __name__ == "__main__":
    run_queries()
from tabulate import tabulate


print(tabulate(
    [["Мобильное приложение", "Иван Петров", "2023-12-31"]],
    headers=["Проект", "Менеджер", "Срок"],
    tablefmt="grid"
))