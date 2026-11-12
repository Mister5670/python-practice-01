import tkinter as tk                                  # GUI-библиотека (окна, кнопки, поля)
from tkinter import filedialog, messagebox, scrolledtext   # диалоги файлов, сообщения, поле с прокруткой
import heapq, json, csv                               # куча (Хаффман), JSON, CSV-таблицы
src_path = None                                       # путь к исходному файлу; None — пока не выбран

def show(s):                                          # вывести строку в окно лога
    """Вывести строку в окно лога."""
    log_widget.insert(tk.END, str(s) + "\n")          # tk.END = "конец текста"; str() — на случай не-строки

def clear():                                          # очистить окно лога
    """Очистить окно лога."""
    log_widget.delete("1.0", tk.END)                  # удалить всё от «строка 1, символ 0» до конца

def short(s, n=400):                                  # обрезать длинную строку для экрана
    """Обрезать длинную строку для вывода на экран."""
    return s if len(s) <= n else s[:n] + "..."        # если коротко — как есть, иначе первые n + "..."

def get_src():                                        # прочитать исходный файл
    """Прочитать исходный файл. Вернуть None, если он не выбран."""
    if not src_path:                                  # None или "" — оба «ложны»
        messagebox.showerror("Ошибка", "Сначала выберите файл!")   # окно ошибки
        return None                                   # сигнал «не прочитали»
    with open(src_path, encoding="utf-8") as f:       # with гарантирует закрытие файла
        return f.read()                               # вернуть весь текст одной строкой

def choose_file():                                    # диалог выбора исходного файла
    global src_path                                   # хотим ИЗМЕНИТЬ глобальную переменную
    p = filedialog.askopenfilename(title="Выберите исходный текстовый файл")   # выбрать файл
    if p:                                             # "" (отмена) — ложь, попадём только при выборе
        src_path = p                                  # запомнить путь
        lbl.config(text=p, fg="black")                # показать путь в метке, цвет — чёрный

def ask(title, ext):                                  # универсальный диалог «выбрать файл»
    """Диалог выбора файла с расширением (например '*.lz78.json')."""
    return filedialog.askopenfilename(                # вернуть путь к файлу
        title=title, filetypes=[("Файлы", ext), ("Все файлы", "*.*")])   # фильтр: наш тип + все

def save_txt(path, text):                             # записать текст в файл
    """Сохранить текст в файл и сообщить об этом на экране."""
    with open(path, "w", encoding="utf-8") as f:      # "w" — перезапись, UTF-8
        f.write(text)                                 # записать строку
    show("Сохранено: " + path)                        # сообщить в логе

def check_src(decoded):                               # сверить декодированный текст с исходником
    """Сравнить результат декодирования с исходным файлом."""
    if not src_path:                                  # сравнивать не с чем
        return                                        # выйти
    with open(src_path, encoding="utf-8") as f:       # открыть исходник
        ok = f.read() == decoded                      # посимвольное равенство строк
    show("\nСовпадает с исходным: " + ("ДА" if ok else "НЕТ"))   # вывод результата

#  1. Алгоритм Хаффмана

def huff_table(text):                                 # построить {символ: битовый код}

    if text == "":                                    # пустой текст — кодировать нечего
        raise ValueError("Текст пустой")              # сообщить об ошибке

    frequency = {}                                    # словарь {символ: частота}
    for char in text:                                 # пройтись по каждому символу
        if char not in frequency:                     # если первый раз встретился
            frequency[char] = 0                       # инициализировать нулём
        frequency[char] += 1                          # увеличить счётчик

    heap = []                                         # минимальная куча
    counter = 0                                       # уникальный номер узла
    for char in frequency:                            # по всем уникальным символам
        heapq.heappush(heap, (frequency[char], counter, char))   # (частота, №, символ) — лист
        counter += 1                                  # следующий номер

    if len(heap) == 1:                                # текст из одного уникального символа
        return {heap[0][2]: "0"}                      # единственный код — "0"

    while len(heap) > 1:                              # пока не останется один корень
        freq1, _, left = heapq.heappop(heap)          # самый редкий узел — «левый»
        freq2, _, right = heapq.heappop(heap)         # следующий — «правый»
        node = (left, right)                          # новый узел-пара (лево, право)
        heapq.heappush(heap, (freq1 + freq2, counter, node))   # вес = сумма частот; обратно в кучу
        counter += 1                                  # новый уникальный номер

    codes = {}                                        # таблица {символ: код}

    def build_codes(node, code):                      # рекурсивный обход дерева
        if isinstance(node, str):                     # ЛИСТ — строка-символ
            codes[node] = code                        # записать накопленный код
        else:                                         # внутренний узел (пара)
            build_codes(node[0], code + "0")          # левое ребро — бит 0
            build_codes(node[1], code + "1")          # правое ребро — бит 1

    build_codes(heap[0][2], "")                       # запуск с корня, код пустой
    return codes                                      # готовая таблица

def huff_encode():                                    # ХАФФМАН: кнопка «Закодировать»
    text = get_src()                                  # прочитать исходный файл
    if text is None:                                  # файл не выбран — уже была ошибка
        return                                        # выходим

    try:                                              # ловим пустой текст
        table = huff_table(text)                      # построить таблицу кодов
    except ValueError as error:                       # пустой текст
        messagebox.showerror("Ошибка", str(error))    # показать ошибку
        return                                        # выйти

    bits = "".join(table[c] for c in text)            # склеить коды всех символов в одну строку

    clear()                                           # очистить лог
    show(" ХАФФМАН: КОДИРОВАНИЕ ")              # заголовок
    show(f"Символов: {len(text)}, бит: {len(bits)}")  # статистика
    show("\nТаблица «символ — битовая строка»:")      # подпись
    for ch, code in sorted(table.items(), key=lambda x: len(x[1])):   # сортировка по длине кода
        show(f"  {ch!r:6} -> {code}")                 # !r = repr (пробел/перевод строки видны)

    show("\nБиты: " + short(bits))                    # первые 400 битов на экран

    path = src_path + ".huff.json"                    # путь к файлу результата
    with open(path, "w", encoding="utf-8") as f:      # открыть на запись
        json.dump({"table": table, "bits": bits}, f, ensure_ascii=False)   # таблица + биты в JSON
    show("\nСохранено: " + path)                      # сообщить

def huff_decode():                                    # ХАФФМАН: кнопка «Декодировать»
    p = ask("Выберите файл Хаффмана", "*.huff.json")  # диалог выбора файла
    if not p:                                         # отменили
        return                                        # выйти

    with open(p, encoding="utf-8") as f:              # открыть файл
        data = json.load(f)                           # data = {"table": ..., "bits": ...}

    rev = {v: k for k, v in data["table"].items()}    # инверсия: {код: символ}
    out, buf = [], ""                                 # out — символы; buf — накопитель битов
    for b in data["bits"]:                            # пройтись по каждому биту
        buf += b                                      # добавить бит к буферу
        if buf in rev:                                # буфер совпал с кодом
            out.append(rev[buf])                      # выдать символ
            buf = ""                                  # обнулить буфер

    if buf != "":                                     # остались незакрытые биты — битый файл
        messagebox.showerror("Ошибка", "Ошибка в закодированной строке")   # сообщить
        return                                        # выйти

    text = "".join(out)                               # собрать символы в строку

    clear()                                           # очистить лог
    show(" ХАФФМАН: ДЕКОДИРОВАНИЕ ")           # заголовок
    show(f"Символов: {len(text)}")                    # длина
    show("\n" + short(text, 1000))                    # первые 1000 символов
    check_src(text)                                   # сверить с исходником
    save_txt(p + ".decoded.txt", text)                # сохранить рядом с JSON

#  2. Алгоритм LZ78
def lz78_encode():                                    # LZ78: кнопка «Закодировать»

    text = get_src()                                  # прочитать исходник
    if text is None:                                  # файл не выбран
        return                                        # выйти

    d = {"": 0}                                       # словарь; пустая строка = индекс 0
    w = ""                                            # накапливаемая текущая строка
    packets = []                                      # список пар (индекс, символ)

    for c in text:                                    # пройтись по каждому символу
        if w + c in d:                                # строка w+c уже есть в словаре
            w += c                                    # нарастить w и продолжить
        else:                                         # нет — фиксируем пакет
            packets.append((d[w], c))                 # пакет: (индекс w, новый символ c)
            d[w + c] = len(d)                         # добавить w+c в словарь с новым номером
            w = ""                                    # сбросить w

    if w:                                             # остаток после цикла
        packets.append((d[w], ""))                    # пакет: (индекс w, без нового символа)

    result = json.dumps(packets, ensure_ascii=False, indent=2)   # красивый JSON с отступами

    clear()                                           # очистить лог
    show(" LZ78: КОДИРОВАНИЕ ")                # заголовок
    show(f"Пакетов: {len(packets)}")                  # сколько пакетов
    show("\nПакет (JSON, как в LZ77):\n")             # подпись
    show(short(result, 3000))                         # первые 3000 символов JSON

    path = src_path + ".lz78.json"                    # путь к файлу
    with open(path, "w", encoding="utf-8") as f:      # открыть на запись
        json.dump(packets, f, ensure_ascii=False, indent=2)   # записать пакет в JSON
    show("\nСохранено: " + path)                      # сообщить

def lz78_decode():                                    # LZ78: кнопка «Декодировать»
    """LZ78: декодирование. Читаем JSON-файл с пакетом."""
    p = ask("Выберите файл LZ78", "*.lz78.json")      # диалог выбора файла
    if not p:                                         # отменили
        return                                        # выйти

    with open(p, encoding="utf-8") as f:              # открыть файл
        packets = json.load(f)                        # [[idx, ch], [idx, ch], ...]

    d = {0: ""}                                       # обратный словарь {номер: строка}
    parts = []                                        # накопитель восстановленных строк
    for idx, ch in packets:                           # по каждому пакету
        entry = d[idx] + ch                           # строка = «из словаря по idx» + символ
        parts.append(entry)                           # запомнить
        d[len(d)] = entry                             # добавить в словарь под новым номером
    text = "".join(parts)                             # склеить всё в исходный текст

    clear()                                           # очистить лог
    show(" LZ78: ДЕКОДИРОВАНИЕ ")              # заголовок
    show(f"Символов: {len(text)}")                    # длина
    show("\n" + short(text, 1000))                    # первые 1000 символов
    check_src(text)                                   # сверка
    save_txt(p + ".decoded.txt", text)                # сохранить рядом

#  3. Алгоритм LZW

def lzw_encode_data(text):
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")     # начальный алфавит A..Z
    for c in text:                                    # пройтись по тексту
        if c not in alphabet:                         # символ не из A..Z
            alphabet.append(c)                        # добавить в алфавит

    dictionary = {}                                   # словарь {строка: код}
    for i in range(len(alphabet)):                    # нумеруем алфавит
        dictionary[alphabet[i]] = i + 1               # коды с 1 (A=1, B=2, ...)

    next_code = len(alphabet) + 1                     # следующий свободный код
    codes = []                                        # коды результата
    encode_table = []                                 # журнал шагов для CSV

    for i in range(len(alphabet)):                    # журнал: начальный словарь
        encode_table.append([i + 1, alphabet[i], "Начальный символ"])   # (код, строка, примечание)

    w = ""                                            # накапливаемая строка
    for c in text:                                    # по каждому символу
        wc = w + c                                    # попытка w + c
        if wc in dictionary:                          # если есть в словаре
            w = wc                                    # нарастить w
        else:                                         # нет — фиксируем код
            codes.append(dictionary[w])               # код для w в результат
            dictionary[wc] = next_code                # добавить wc с новым кодом
            encode_table.append([next_code, wc, "Добавлена комбинация"])   # в журнал
            next_code += 1                            # следующий свободный
            w = c                                     # начать с c

    if w != "":                                       # остаток
        codes.append(dictionary[w])                   # выдать последний код

    if len(codes) > 0:                                # если есть коды
        max_code = max(codes)                         # самый большой код
        bit_width = max(1, max_code.bit_length())     # бит на код = длина в битах, минимум 1
    else:                                             # кодов нет
        bit_width = 1                                 # 1 бит

    bits = ""                                         # итоговая битовая строка
    for code in codes:                                # по всем кодам
        bits += format(code, "0" + str(bit_width) + "b")   # в двоичный с ведущими нулями

    return alphabet, codes, bits, bit_width, encode_table   # вернуть всё нужное

def lzw_decode_data(alphabet, codes):                 # «чистая» логика LZW-декодирования
    dictionary = {}                                   # обратный словарь {код: строка}
    for i in range(len(alphabet)):                    # по алфавиту
        dictionary[i + 1] = alphabet[i]               # код (с 1) → символ

    next_code = len(alphabet) + 1                     # следующий свободный код
    decode_table = []                                 # журнал шагов

    if len(codes) == 0:                               # пустой пакет
        return "", decode_table                       # пустой текст

    text = dictionary[codes[0]]                       # первый код всегда известен
    w = text                                          # предыдущая расшифрованная строка

    for code in codes[1:]:                            # остальные коды
        if code in dictionary:                        # код уже есть в словаре
            entry = dictionary[code]                  # берём оттуда
        elif code == next_code:                       # особый случай KWK
            entry = w + w[0]                          # строка = prev + первый символ prev
        else:                                         # код неизвестен — повреждение
            raise ValueError("Некорректный код LZW")  # ошибка

        text += entry                                 # дописать к результату
        new_entry = w + entry[0]                      # новая запись словаря
        dictionary[next_code] = new_entry             # добавить
        decode_table.append([next_code, new_entry, "Добавлена комбинация"])   # в журнал
        next_code += 1                                # следующий свободный
        w = entry                                     # сдвигаем «предыдущую»

    return text, decode_table                         # текст + журнал

def lzw_encode():                                     # LZW: кнопка «Закодировать»
    text = get_src()                                  # прочитать исходник
    if text is None:                                  # нет файла
        return                                        # выйти

    alphabet, codes, bits, bit_width, encode_table = lzw_encode_data(text)   # вычислить всё

    clear()                                           # очистить лог
    show(" LZW: КОДИРОВАНИЕ ")                 # заголовок
    show(f"Символов: {len(text)}, кодов: {len(codes)}, "      # статистика
         f"ширина кода: {bit_width} бит, всего бит: {len(bits)}")
    show("Коды: " + short(", ".join(map(str, codes)), 400))   # первые 400 символов списка кодов
    show("\nБиты: " + short(bits))                    # первые 400 битов

    path = src_path + ".lzw.json"                     # путь к файлу битов
    with open(path, "w", encoding="utf-8") as f:      # открыть
        json.dump({"bits": bits, "bits_per": bit_width, "alphabet": alphabet},
                  f, ensure_ascii=False)              # биты + параметры для декодера
    show("\nСохранено (биты):    " + path)            # сообщить

    tpath = src_path + ".lzw.tables.csv"              # путь к файлу таблиц
    with open(tpath, "w", encoding="utf-8", newline="") as f:   # newline="" — обязательно для CSV
        wr = csv.writer(f)                            # писатель CSV
        wr.writerow(["code", "string", "note"])       # заголовок
        for code_, s_, note in encode_table:          # по всем записям журнала
            wr.writerow([code_, s_ if s_.isprintable() else repr(s_), note])   # безопасный вывод строки
    show("Сохранено (таблицы): " + tpath)             # сообщить

def lzw_decode():                                     # LZW: кнопка «Декодировать»
    p = ask("Выберите файл LZW", "*.lzw.json")        # диалог выбора
    if not p:                                         # отменили
        return                                        # выйти

    with open(p, encoding="utf-8") as f:              # открыть
        data = json.load(f)                           # прочитать JSON
    bits, bp, alphabet = data["bits"], data["bits_per"], data["alphabet"]   # распаковка

    codes = [int(bits[i:i + bp], 2) for i in range(0, len(bits), bp)]   # нарезать биты на коды

    try:                                              # ловим ошибку декодирования
        text, _decode_table = lzw_decode_data(alphabet, codes)   # декодировать
    except ValueError as error:                       # битый пакет
        messagebox.showerror("Ошибка", str(error))    # показать
        return                                        # выйти

    clear()                                           # очистить лог
    show(" LZW: ДЕКОДИРОВАНИЕ ")               # заголовок
    show(f"Символов: {len(text)}")                    # длина
    show("\n" + short(text, 1000))                    # первые 1000 символов
    check_src(text)                                   # сверка
    save_txt(p + ".decoded.txt", text)                # сохранить

#  Интерфейс

root = tk.Tk()                                        # главное окно приложения
root.title("Лаб. 2 — Сжатие данных")                  # заголовок окна

top = tk.Frame(root)                                  # контейнер для верхней строки
top.pack(fill=tk.X, padx=5, pady=3)                   # растянуть по горизонтали, отступы
tk.Button(top, text="Выбрать исходный файл", command=choose_file).pack(side=tk.LEFT)   # кнопка выбора файла
lbl = tk.Label(top, text="(файл не выбран)", fg="gray")   # метка с путём
lbl.pack(side=tk.LEFT, padx=10)                       # разместить слева

btns = tk.Frame(root)                                 # контейнер для строк с кнопками
btns.pack(fill=tk.X, padx=5, pady=2)                   # растянуть

def add_row(label, enc, dec):                         # фабрика одной строки кнопок
    fr = tk.Frame(btns)                               # подконтейнер-строка
    fr.pack(fill=tk.X, pady=1)                        # разместить
    tk.Label(fr, text=label, width=10, anchor="w").pack(side=tk.LEFT)   # метка алгоритма
    tk.Button(fr, text="Закодировать", width=15, command=enc).pack(side=tk.LEFT, padx=2)   # кнопка «закодировать»
    tk.Button(fr, text="Декодировать", width=15, command=dec).pack(side=tk.LEFT, padx=2)  # кнопка «декодировать»

add_row("Хаффман", huff_encode, huff_decode)          # строка Хаффмана
add_row("LZ78",    lz78_encode, lz78_decode)          # строка LZ78
add_row("LZW",     lzw_encode,  lzw_decode)           # строка LZW

log_widget = scrolledtext.ScrolledText(root, width=100, height=30)   # окно лога (символов × строк)
log_widget.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)   # растягивать вместе с окном

root.mainloop()                                       # главный цикл: слушаем события