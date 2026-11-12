# -*- coding: utf-8 -*-
"""
Лаб. №2 «Сжатие данных». Вариант (чётный) — LZ78.
Алгоритмы: Хаффман, LZ78, LZW. Интерфейс: tkinter.

Требования (напоминание):
  1) Хаффман: вывести таблицу «символ ↔ код», сохранить биты в файл,
     при декодировании читать таблицу и биты из файла.
  2) LZ78 (чётный): вывести пакеты (индекс, следующий символ), сохранить в файл.
  3) LZW: результат в битовом виде + ВСЕ промежуточные таблицы — в файлы.
  Интерфейс: отдельная кнопка на каждое действие + отдельный выбор файла.
"""
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import heapq, json, csv

src_path = None   # путь к исходному текстовому файлу


# ============================================================
#  Общие вспомогательные функции
# ============================================================
def show(s):
    """Вывести строку в окно лога."""
    log_widget.insert(tk.END, str(s) + "\n")


def clear():
    """Очистить окно лога."""
    log_widget.delete("1.0", tk.END)


def short(s, n=400):
    """Обрезать длинную строку для вывода на экран."""
    return s if len(s) <= n else s[:n] + "..."


def get_src():
    """Прочитать исходный файл. Вернуть None, если он не выбран."""
    if not src_path:
        messagebox.showerror("Ошибка", "Сначала выберите файл!")
        return None
    with open(src_path, encoding="utf-8") as f:
        return f.read()


def choose_file():
    global src_path
    p = filedialog.askopenfilename(title="Выберите исходный текстовый файл")
    if p:
        src_path = p
        lbl.config(text=p, fg="black")


def ask(title, ext):
    """Диалог выбора файла с расширением ext (например '*.lz78.json')."""
    return filedialog.askopenfilename(
        title=title, filetypes=[("Файлы", ext), ("Все файлы", "*.*")])


def save_txt(path, text):
    """Сохранить текст в файл и сообщить об этом на экране."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    show("Сохранено: " + path)


def check_src(decoded):
    """Сравнить результат декодирования с исходным файлом."""
    if not src_path:
        return
    with open(src_path, encoding="utf-8") as f:
        ok = f.read() == decoded
    show("\nСовпадает с исходным: " + ("ДА" if ok else "НЕТ"))


# ============================================================
#  1. АЛГОРИТМ ХАФФМАНА   (не трогаем)
# ============================================================
def huff_table(text):
    """
    Строит дерево Хаффмана и возвращает {символ: код}.
    """
    if text == "":
        raise ValueError("Текст пустой")

    frequency = {}
    for char in text:
        if char not in frequency:
            frequency[char] = 0
        frequency[char] += 1

    heap = []
    counter = 0
    for char in frequency:
        heapq.heappush(heap, (frequency[char], counter, char))
        counter += 1

    if len(heap) == 1:
        return {heap[0][2]: "0"}

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)
        node = (left, right)
        heapq.heappush(heap, (freq1 + freq2, counter, node))
        counter += 1

    codes = {}

    def build_codes(node, code):
        if isinstance(node, str):
            codes[node] = code
        else:
            build_codes(node[0], code + "0")
            build_codes(node[1], code + "1")

    build_codes(heap[0][2], "")
    return codes


def huff_encode():
    text = get_src()
    if text is None:
        return

    try:
        table = huff_table(text)
    except ValueError as error:
        messagebox.showerror("Ошибка", str(error))
        return

    bits = "".join(table[c] for c in text)

    clear()
    show("=== ХАФФМАН: КОДИРОВАНИЕ ===")
    show(f"Символов: {len(text)}, бит: {len(bits)}")
    show("\nТаблица «символ — битовая строка»:")
    for ch, code in sorted(table.items(), key=lambda x: len(x[1])):
        show(f"  {ch!r:6} -> {code}")
    show("\nБиты: " + short(bits))

    path = src_path + ".huff.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"table": table, "bits": bits}, f, ensure_ascii=False)
    show("\nСохранено: " + path)


def huff_decode():
    p = ask("Выберите файл Хаффмана", "*.huff.json")
    if not p:
        return

    with open(p, encoding="utf-8") as f:
        data = json.load(f)

    rev = {v: k for k, v in data["table"].items()}
    out, buf = [], ""
    for b in data["bits"]:
        buf += b
        if buf in rev:
            out.append(rev[buf])
            buf = ""

    if buf != "":
        messagebox.showerror("Ошибка", "Ошибка в закодированной строке")
        return

    text = "".join(out)

    clear()
    show("=== ХАФФМАН: ДЕКОДИРОВАНИЕ ===")
    show(f"Символов: {len(text)}")
    show("\n" + short(text, 1000))
    check_src(text)
    save_txt(p + ".decoded.txt", text)


# ============================================================
#  2. АЛГОРИТМ LZ78   (ИЗМЕНЕНО: вывод как в LZ77 — JSON)
# ============================================================
def lz78_encode():
    """
    LZ78: пакет — список пар (индекс_в_словаре, следующий_символ).
    Вывод и сохранение — как в LZ77-примере: JSON-строка (список кортежей).
    """
    text = get_src()
    if text is None:
        return

    d = {"": 0}          # словарь; пустая строка — нулевой индекс
    w = ""               # текущая накапливаемая строка
    packets = []         # сюда пишем (индекс, следующий_символ)

    for c in text:
        if w + c in d:   # такая строка уже есть — наращиваем
            w += c
        else:            # нет — выдаём пакет и добавляем новую строку
            packets.append((d[w], c))
            d[w + c] = len(d)
            w = ""

    if w:                # остаток текста
        packets.append((d[w], ""))

    # ---- ВЫВОД КАК В LZ77: пакет показываем JSON-строкой ----
    result = json.dumps(packets, ensure_ascii=False, indent=2)

    clear()
    show("=== LZ78: КОДИРОВАНИЕ ===")
    show(f"Пакетов: {len(packets)}")
    show("\nПакет (JSON, как в LZ77):\n")
    show(short(result, 3000))

    # ---- СОХРАНЕНИЕ: пишем JSON-файл (вместо CSV) ----
    path = src_path + ".lz78.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(packets, f, ensure_ascii=False, indent=2)
    show("\nСохранено: " + path)


def lz78_decode():
    """LZ78: декодирование. Читаем JSON-файл с пакетом (как в LZ77)."""
    p = ask("Выберите файл LZ78", "*.lz78.json")
    if not p:
        return

    with open(p, encoding="utf-8") as f:
        packets = json.load(f)   # [[idx, ch], [idx, ch], ...]

    # Восстанавливаем строки по индексам, последовательно пополняя словарь.
    d = {0: ""}
    parts = []
    for idx, ch in packets:
        entry = d[idx] + ch
        parts.append(entry)
        d[len(d)] = entry
    text = "".join(parts)

    clear()
    show("=== LZ78: ДЕКОДИРОВАНИЕ ===")
    show(f"Символов: {len(text)}")
    show("\n" + short(text, 1000))
    check_src(text)
    save_txt(p + ".decoded.txt", text)


# ============================================================
#  3. АЛГОРИТМ LZW   (не трогаем — как в прошлой версии)
# ============================================================
def lzw_encode_data(text):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for c in text:
        if c not in alphabet:
            alphabet.append(c)

    dictionary = {}
    for i in range(len(alphabet)):
        dictionary[alphabet[i]] = i + 1

    next_code = len(alphabet) + 1
    codes = []
    encode_table = []

    for i in range(len(alphabet)):
        encode_table.append([i + 1, alphabet[i], "Начальный символ"])

    w = ""
    for c in text:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            codes.append(dictionary[w])
            dictionary[wc] = next_code
            encode_table.append([next_code, wc, "Добавлена комбинация"])
            next_code += 1
            w = c

    if w != "":
        codes.append(dictionary[w])

    if len(codes) > 0:
        max_code = max(codes)
        bit_width = max(1, max_code.bit_length())
    else:
        bit_width = 1

    bits = ""
    for code in codes:
        bits += format(code, "0" + str(bit_width) + "b")

    return alphabet, codes, bits, bit_width, encode_table


def lzw_decode_data(alphabet, codes):
    dictionary = {}
    for i in range(len(alphabet)):
        dictionary[i + 1] = alphabet[i]

    next_code = len(alphabet) + 1
    decode_table = []

    if len(codes) == 0:
        return "", decode_table

    text = dictionary[codes[0]]
    w = text

    for code in codes[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = w + w[0]
        else:
            raise ValueError("Некорректный код LZW")

        text += entry
        new_entry = w + entry[0]
        dictionary[next_code] = new_entry
        decode_table.append([next_code, new_entry, "Добавлена комбинация"])
        next_code += 1
        w = entry

    return text, decode_table


def lzw_encode():
    text = get_src()
    if text is None:
        return

    alphabet, codes, bits, bit_width, encode_table = lzw_encode_data(text)

    clear()
    show("=== LZW: КОДИРОВАНИЕ ===")
    show(f"Символов: {len(text)}, кодов: {len(codes)}, "
         f"ширина кода: {bit_width} бит, всего бит: {len(bits)}")
    show("Коды: " + short(", ".join(map(str, codes)), 400))
    show("\nБиты: " + short(bits))

    path = src_path + ".lzw.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"bits": bits, "bits_per": bit_width, "alphabet": alphabet},
                  f, ensure_ascii=False)
    show("\nСохранено (биты):    " + path)

    tpath = src_path + ".lzw.tables.csv"
    with open(tpath, "w", encoding="utf-8", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["code", "string", "note"])
        for code_, s_, note in encode_table:
            wr.writerow([code_, s_ if s_.isprintable() else repr(s_), note])
    show("Сохранено (таблицы): " + tpath)


def lzw_decode():
    p = ask("Выберите файл LZW", "*.lzw.json")
    if not p:
        return

    with open(p, encoding="utf-8") as f:
        data = json.load(f)
    bits, bp, alphabet = data["bits"], data["bits_per"], data["alphabet"]

    codes = [int(bits[i:i + bp], 2) for i in range(0, len(bits), bp)]

    try:
        text, _decode_table = lzw_decode_data(alphabet, codes)
    except ValueError as error:
        messagebox.showerror("Ошибка", str(error))
        return

    clear()
    show("=== LZW: ДЕКОДИРОВАНИЕ ===")
    show(f"Символов: {len(text)}")
    show("\n" + short(text, 1000))
    check_src(text)
    save_txt(p + ".decoded.txt", text)


# ============================================================
#  Интерфейс — БЕЗ ИЗМЕНЕНИЙ
# ============================================================
root = tk.Tk()
root.title("Лаб. 2 — Сжатие данных")

top = tk.Frame(root)
top.pack(fill=tk.X, padx=5, pady=3)
tk.Button(top, text="Выбрать исходный файл", command=choose_file).pack(side=tk.LEFT)
lbl = tk.Label(top, text="(файл не выбран)", fg="gray")
lbl.pack(side=tk.LEFT, padx=10)

btns = tk.Frame(root)
btns.pack(fill=tk.X, padx=5, pady=2)

def add_row(label, enc, dec):
    fr = tk.Frame(btns)
    fr.pack(fill=tk.X, pady=1)
    tk.Label(fr, text=label, width=10, anchor="w").pack(side=tk.LEFT)
    tk.Button(fr, text="Закодировать", width=15, command=enc).pack(side=tk.LEFT, padx=2)
    tk.Button(fr, text="Декодировать", width=15, command=dec).pack(side=tk.LEFT, padx=2)

add_row("Хаффман", huff_encode, huff_decode)
add_row("LZ78",    lz78_encode, lz78_decode)
add_row("LZW",     lzw_encode,  lzw_decode)

log_widget = scrolledtext.ScrolledText(root, width=100, height=30)
log_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

root.mainloop()