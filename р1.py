import tkinter as tk
from tkinter import filedialog, messagebox
import heapq
import json

def huffman_encode(text):
    if text == "":
        raise ValueError("Текст пустой")

    frequency = {} #словарь для частот

    for char in text:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1

    heap = []
    counter = 0

    for char in frequency:
        heapq.heappush(
            heap, (frequency[char], counter, char)
        )
        counter += 1

    # Если в тексте только один уникальный символ
    if len(heap) == 1:
        codes = {heap[0][2]: "0"}

    else:
        while len(heap) > 1:
            freq1, _, left = heapq.heappop(heap)
            freq2, _, right = heapq.heappop(heap)

            node = (left, right)

            heapq.heappush(
                heap, (freq1 + freq2, counter, node)
            )
            counter += 1

        codes = {} #для таблицы кодов

        def build_codes(node, code):
            if isinstance(node, str):
                codes[node] = code
            else:
                build_codes(node[0], code + "0")
                build_codes(node[1], code + "1")

        build_codes(heap[0][2], "")

    encoded = "" #закодированный текст

    for char in text:
        encoded += codes[char]

    return encoded, codes


def huffman_decode(encoded, codes):
    reverse_codes = {} #ключи битовые строки, значения символы

    for char in codes:
        reverse_codes[codes[char]] = char

    result = ""
    current = "" #для накопления битов пока не станут кодом символа

    for bit in encoded:
        current += bit

        if current in reverse_codes:
            result += reverse_codes[current]
            current = ""

    if current != "":
        raise ValueError("Ошибка в закодированной строке")

    return result


# Графический интерфейс

class HuffmanApp:
    def __init__(self, root): #root - главное окно переданное при создании обьекта
        self.root = root #сохраняем ссылку на главное окно в обьекте
        self.root.title("Лабораторная работа №2 — Хаффман")
        self.root.geometry("850x650")

        self.source_text = ""   #для хранения исходного текста

        tk.Button(
            root,
            text="Выбрать текстовый файл",
            command=self.open_file
        ).pack(pady=5)

        tk.Label(root, text="Исходный текст").pack() #надпись

        self.input_box = tk.Text(root, height=8)   #текстовое поле
        self.input_box.pack(fill="x", padx=10, pady=5)

        buttons = tk.Frame(root)  #создание области для создания кнопок
        buttons.pack(pady=5)

        tk.Button(
            buttons,
            text="Закодировать",
            command=self.encode
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            buttons,
            text="Сохранить код",
            command=self.save_code
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            buttons,
            text="Декодировать из файла",
            command=self.decode
        ).grid(row=0, column=2, padx=5)

        tk.Label(
            root,
            text="Таблица кодов и результат"
        ).pack()

        self.output_box = tk.Text(root, height=18)
        self.output_box.pack(
            fill="both", expand=True, padx=10, pady=5
        )

        self.encoded = ""
        self.codes = {}

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[("Текстовые файлы", "*.txt"),
                       ("Все файлы", "*.*")]
        )

        if path:
            try:
                with open(path, "r", encoding="utf-8") as file:
                    self.source_text = file.read()

                self.input_box.delete("1.0", tk.END)
                self.input_box.insert("1.0", self.source_text)

            except Exception as error:
                messagebox.showerror("Ошибка", str(error))

    def encode(self):
        text = self.input_box.get("1.0", "end-1c")

        try:
            self.encoded, self.codes = huffman_encode(text)

            result = "ТАБЛИЦА КОДОВ:\n\n"

            for char in self.codes:
                if char == " ":
                    symbol = "[пробел]"
                elif char == "\n":
                    symbol = "[перенос строки]"
                elif char == "\t":
                    symbol = "[табуляция]"
                else:
                    symbol = char

                result += symbol + " : " + self.codes[char] + "\n"

            result += "\nЗАКОДИРОВАННАЯ ПОСЛЕДОВАТЕЛЬНОСТЬ:\n\n"
            result += self.encoded

            self.show_result(result)

        except Exception as error:
            messagebox.showerror("Ошибка", str(error))

    def save_code(self):
        if not self.encoded:
            messagebox.showwarning(
                "Внимание", "Сначала закодируйте текст"
            )
            return

        path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("Файлы JSON", "*.json")]
        )

        if path:
            data = {
                "encoded": self.encoded,
                "codes": self.codes
            }

            try:
                with open(path, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=2)

                messagebox.showinfo(
                    "Готово", "Закодированные данные сохранены"
                )

            except Exception as error:
                messagebox.showerror("Ошибка", str(error))

    def decode(self):
        path = filedialog.askopenfilename(
            title="Выберите файл с кодом Хаффмана",
            filetypes=[("Файлы JSON", "*.json")]
        )

        if path:
            try:
                with open(path, "r", encoding="utf-8") as file:
                    data = json.load(file)

                decoded = huffman_decode(
                    data["encoded"], data["codes"]
                )

                self.show_result(
                    "ВОССТАНОВЛЕННЫЙ ТЕКСТ:\n\n" + decoded
                )

                save_path = filedialog.asksaveasfilename(
                    title="Сохранить восстановленный текст",
                    defaultextension=".txt",
                    filetypes=[("Текстовые файлы", "*.txt")]
                )

                if save_path:
                    with open(
                        save_path, "w", encoding="utf-8"
                    ) as file:
                        file.write(decoded)

                    messagebox.showinfo(
                        "Готово", "Текст сохранён"
                    )

            except Exception as error:
                messagebox.showerror("Ошибка", str(error))

    def show_result(self, text):
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert("1.0", text)


root = tk.Tk()
app = HuffmanApp(root)
root.mainloop()
