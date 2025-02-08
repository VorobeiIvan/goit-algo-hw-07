class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Функція для знаходження найбільшого значення в дереві
def find_max(root):
    while root.right:  # Рухаємося праворуч, поки є наступний вузол
        root = root.right
    return root.value

# Функція для знаходження найменшого значення в дереві
def find_min(root):
    while root.left:  # Рухаємося ліворуч, поки є наступний вузол
        root = root.left
    return root.value

# Функція для знаходження суми всіх значень у дереві
def sum_values(root):
    if root is None:  # Якщо дерево порожнє, повертаємо 0
        return 0
    # Рекурсивно додаємо значення всіх вузлів дерева
    return root.value + sum_values(root.left) + sum_values(root.right)


class Comment:
    def __init__(self, text, author):
        self.text = text  # Текст коментаря
        self.author = author  # Автор коментаря
        self.replies = []  # Список відповідей
        self.is_deleted = False  # Прапорець для видалення

    def add_reply(self, reply):
        """Додає відповідь до коментаря"""
        self.replies.append(reply)
        print(f"Відповідь додано: {reply.author}: {reply.text}")

    def remove_reply(self):
        """Видаляє відповідь, змінюючи текст і встановлюючи прапорець is_deleted в True"""
        self.is_deleted = True
        self.text = "Цей коментар було видалено."
        print(f"Відповідь видалено: {self.text}")

    def display(self, indent=0):
        """Рекурсивно відображає коментар та відповіді"""
        print("    " * indent + f"{self.author}: {self.text}")
        if self.is_deleted:
            print("    " * (indent + 1) + "Цей коментар було видалено.")
        for reply in self.replies:
            reply.display(indent + 1)

# Тестування функцій для дерев та коментарів

def test_tree_functions():
    print("Тестування функцій дерева:")
    
    # Створення дерева
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(20)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(25)
    
    # Перевірка на найбільше значення в дереві
    max_value = find_max(root)
    assert max_value == 25, f"Помилка! Очікувалося 25, отримано {max_value}"
    print(f"Найбільше значення в дереві: {max_value}")
    
    # Перевірка на найменше значення в дереві
    min_value = find_min(root)
    assert min_value == 3, f"Помилка! Очікувалося 3, отримано {min_value}"
    print(f"Найменше значення в дереві: {min_value}")
    
    # Перевірка на суму всіх значень в дереві
    total_sum = sum_values(root)
    assert total_sum == 85, f"Помилка! Очікувалося 85, отримано {total_sum}"
    print(f"Сума всіх значень в дереві: {total_sum}")

def test_comment_functions():
    print("\nТестування функцій коментарів:")
    
    # Створення кореневого коментаря
    root_comment = Comment("Яка чудова книга!", "Бодя")
    
    # Створення відповідей
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")
    
    # Додавання відповідей
    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)
    
    # Перевірка, чи відповіді додано
    assert len(root_comment.replies) == 2, f"Помилка! Очікувалося 2 відповіді, отримано {len(root_comment.replies)}"
    print(f"Відповіді додано: {len(root_comment.replies)}")
    
    # Додавання відповіді до першої відповіді
    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)
    
    # Перевірка, чи додано ще одну відповідь
    assert len(reply1.replies) == 1, f"Помилка! Очікувалося 1 відповідь, отримано {len(reply1.replies)}"
    print(f"Відповідь додано до відповіді: {len(reply1.replies)}")
    
    # Видалення першої відповіді
    reply1.remove_reply()
    assert reply1.is_deleted == True, "Помилка! Відповідь не була видалена"
    print("Перша відповідь видалена.")

    # Виведення всіх коментарів та відповідей
    print("\nВиведення коментарів та відповідей:")
    root_comment.display()

# Виконання тестів
test_tree_functions()
test_comment_functions()
