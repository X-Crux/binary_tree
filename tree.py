class Tree:
    def __init__(self):
        self.catalog = {}
        self._temp = []

    def to_table(self, key: str, value: str):
        return f"{key}|{value}"

    def __str__(self):
        self._recursion_export(self.to_table, self.catalog["left"])
        self._temp.append(self.to_table(self.catalog["data"]["key"], self.catalog["data"]["value"]))
        self._recursion_export(self.to_table, self.catalog["right"])
        print(f"{'п/п'.ljust(4)}Наименование{'Цена'.rjust(40 - (len('Наименование') + 3))}")

        for i in range(len(self._temp)):
            elem = self._temp[i].split("|")
            num_line = f"{i + 1}."
            _value = str(elem[1]).rjust(40 - (len(elem[0]) + 3))
            print(f"{num_line.ljust(4)}{elem[0]}{_value}")

        self._temp.clear()

    def _recursion_find(self, node: dict, key: str):
        if not node:
            return f"Ключ '{key}' отсутствует"
        elif key == node["data"]["key"]:
            return node["data"]["value"]
        elif key > node["data"]["key"]:
            return self._recursion_find(node["right"], key)
        elif key < node["data"]["key"]:
            return self._recursion_find(node["left"], key)

    def find(self, key: str):
        if not self.catalog:
            return "Узел не найден"
        elif key == self.catalog["data"]["key"]:
            return self.catalog["data"]["value"]
        elif key > self.catalog["data"]["key"]:
            return self._recursion_find(self.catalog["right"], key)
        elif key < self.catalog["data"]["key"]:
            return self._recursion_find(self.catalog["left"], key)

    def _recursion_insert(self, parent: str, node: dict, key: str, value: str):
        if not node:
            return {
                "parent": parent,
                "left": {},
                "right": {},
                "data": {
                    "key": key,
                    "value": value
                }
            }
        elif key >= node["data"]["key"]:
            node["right"] = self._recursion_insert(node["data"]["key"], node["right"], key, value)
        elif key < node["data"]["key"]:
            node["left"] = self._recursion_insert(node["data"]["key"], node["left"], key, value)

        return node

    def insert(self, key: str, value: str):
        if not self.catalog:
            self.catalog = {
                "parent": "",
                "left": {},
                "right": {},
                "data": {
                    "key": key,
                    "value": value
                }
            }
        elif key >= self.catalog["data"]["key"]:
            self.catalog["right"] = self._recursion_insert(self.catalog["data"]["key"], self.catalog["right"], key, value)
        elif key < self.catalog["data"]["key"]:
            self.catalog["left"] = self._recursion_insert(self.catalog["data"]["key"], self.catalog["left"], key, value)

        print(f"Объект добавлен с ключом '{key}'")

    def _recursion_remove(self, node: dict, key: str):
        if key > node["data"]["key"]:
            node["right"] = self._recursion_remove(node["right"], key)
        elif key < node["data"]["key"]:
            node["left"] = self._recursion_remove(node["left"], key)
        elif key == node["data"]["key"]:
            if not node["left"] and not node["right"]:
                node = {}
            elif node["left"] and node["right"]:
                m_node = node["right"]["left"]
                m_node["left"] = node["left"]
                node["right"]["parent"] = node["parent"]
                node = node["right"]
                node["left"] = m_node
            elif node["left"] or node["right"]:
                if node["left"]:
                    node["left"]["parent"] = node["parent"]
                    node = node["left"]
                elif node["right"]:
                    node["right"]["parent"] = node["parent"]
                    node = node["right"]
        return node

    def remove(self, key):
        if not self.catalog:
            print("Каталог пустой")
        else:
            self.catalog = self._recursion_remove(self.catalog, key)
            print(f"Объект с ключом '{key}' удален")

    def _recursion_infix(self, func, node: dict):
        if not node:
            return 0
        self._recursion_infix(func, node["left"])
        print(func(node["data"]["key"], node["data"]["value"]))
        self._recursion_infix(func, node["right"])

    def traverse_infix(self, func):
        if not self.catalog:
            print("Каталог пустой")
        else:
            self._recursion_infix(func, self.catalog["left"])
            print(func(self.catalog["data"]["key"], self.catalog["data"]["value"]))
            self._recursion_infix(func, self.catalog["right"])

    def _recursion_prefix(self, func, node: dict):
        if not node:
            return 0
        print(func(node["data"]["key"], node["data"]["value"]))
        self._recursion_prefix(func, node["left"])
        self._recursion_prefix(func, node["right"])

    def traverse_prefix(self, func):
        if not self.catalog:
            print("Каталог пустой")
        else:
            print(func(self.catalog["data"]["key"], self.catalog["data"]["value"]))
            self._recursion_prefix(func, self.catalog["left"])
            self._recursion_prefix(func, self.catalog["right"])

    def _recursion_postfix(self, func, node: dict):
        if not node:
            return 0
        self._recursion_postfix(func, node["left"])
        self._recursion_postfix(func, node["right"])
        print(func(node["data"]["key"], node["data"]["value"]))

    def traverse_postfix(self, func):
        if not self.catalog:
            print("Каталог пустой")
        else:
            self._recursion_postfix(func, self.catalog["left"])
            self._recursion_postfix(func, self.catalog["right"])
            print(func(self.catalog["data"]["key"], self.catalog["data"]["value"]))

    def _recursion_export(self, func, node: dict):
        if not node:
            return 0
        self._recursion_export(func, node["left"])
        self._temp.append(func(node["data"]["key"], node["data"]["value"]))
        self._recursion_export(func, node["right"])

    def export(self, filename: str, func):
        if not self.catalog:
            print("Каталог пустой")
        else:
            self._recursion_export(func, self.catalog["left"])
            self._temp.append(func(self.catalog["data"]["key"], self.catalog["data"]["value"]))
            self._recursion_export(func, self.catalog["right"])
            filename = f"{filename}.txt"

            with open(filename, "w", encoding="utf-8") as f:
                for i in self._temp:
                    f.write(i)

            print(f"Записано элементов {len(self._temp)}, в файл '{filename}'")
            self._temp.clear()

    def import_file(self, filename: str):
        filename = f"{filename}.txt"

        try:
            with open(filename, "r", encoding="utf-8") as f:
                f = f.read()
                f = f.split("\n")

                for i in f[:-1]:
                    i = i.split("|")
                    self.insert(i[0], i[1])
            print("Данные импортированы")
        except Exception:
            print("Ошибка импорта")
