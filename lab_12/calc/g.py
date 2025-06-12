import tkinter as tk
from tkinter import messagebox
from .calc import calculate_energy_consumption, calculate_cost
from .rep import save_to_doc, save_to_xls

class ApplianceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Расчёт потребления электроэнергии")

        # Поля ввода
        tk.Label(root, text="Мощность прибора (Вт):").grid(row=0, column=0)
        self.power_entry = tk.Entry(root)
        self.power_entry.grid(row=0, column=1)

        tk.Label(root, text="Часы использования в день:").grid(row=1, column=0)
        self.hours_entry = tk.Entry(root)
        self.hours_entry.grid(row=1, column=1)

        tk.Label(root, text="Количество дней:").grid(row=2, column=0)
        self.days_entry = tk.Entry(root)
        self.days_entry.grid(row=2, column=1)

        tk.Label(root, text="Стоимость 1 кВт*ч:").grid(row=3, column=0)
        self.rate_entry = tk.Entry(root)
        self.rate_entry.grid(row=3, column=1)

        # Кнопки
        tk.Button(root, text="Рассчитать", command=self.calculate).grid(row=4, column=0)
        tk.Button(root, text="Сохранить в DOC", command=self.save_doc).grid(row=4, column=1)
        tk.Button(root, text="Сохранить в XLS", command=self.save_xls).grid(row=4, column=2)

        # Поле для вывода результата
        self.result_label = tk.Label(root, text="Результат:")
        self.result_label.grid(row=5, column=0, columnspan=3)

    def calculate(self):
        try:
            power = float(self.power_entry.get())
            hours = float(self.hours_entry.get())
            days = float(self.days_entry.get())
            rate = float(self.rate_entry.get())

            energy = calculate_energy_consumption(power, hours, days)
            cost = calculate_cost(energy, rate)

            self.result_label.config(text=f"Потребление: {energy:.2f} кВт*ч, Стоимость: {cost:.2f} руб.")
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа.")

    def save_doc(self):
        result = self.result_label.cget("text")
        if result != "Результат:":
            save_to_doc(result)
            messagebox.showinfo("Успех", "Результат сохранён в DOC файл.")
        else:
            messagebox.showerror("Ошибка", "Сначала выполните расчёт.")

    def save_xls(self):
        result = self.result_label.cget("text")
        if result != "Результат:":
            save_to_xls(result)
            messagebox.showinfo("Успех", "Результат сохранён в XLS файл.")
        else:
            messagebox.showerror("Ошибка", "Сначала выполните расчёт.")