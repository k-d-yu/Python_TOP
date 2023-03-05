from jinja2 import Environment, FileSystemLoader

cars = [{'model': 'Lada', 'price': 10000},
        {'model': 'Audi', 'price': 15000},
        {'model': 'Renault', 'price': 20000},
        {'model': 'BMW', 'price': 25000}
        ]

file_loader = FileSystemLoader("../HW_1_templates")
env = Environment(loader=file_loader)

tm = env.get_template("main.html")
msg = tm.render(car=cars, title="Домашнее задание", h1="Страница с домашним заданием", p="Домашнее задание выполнено!!!")
print(msg)
