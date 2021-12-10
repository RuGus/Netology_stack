class Stack:
    """Class for work with stack"""

    def __init__(self) -> None:
        """Init method."""
        self.stack = []
        pass

    def isEmpty(self) -> bool:
        """Проверка стека на пустоту.

        Returns:
            bool: True, если стек пустой, иначе False.
        """
        return not bool(len(self.stack))

    def push(self, element: any) -> None:
        """Добавляет новый элемент на вершину стека.

        Args:
            element (any): новый элемент стека.
        """
        #
        self.stack.append(element)

    def pop(self) -> str:
        """Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека

        Returns:
            str: верхний элемент стека.
        """
        #
        return self.stack.pop()

    def peek(self) -> str:
        """Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.

        Returns:
            str: верхний элемент стека.
        """
        #
        return self.stack[-1]

    def size(self) -> int:
        """Возвращает количество элементов в стеке.

        Returns:
            int: количество элементов в стеке.
        """
        return len(self.stack)


def isBalansed(checking_string: str) -> None:
    """Print "Сбалансированно" if string is balansed, else print "Несбалансированно"

    Args:
        checking_string (str): string for cheking balanse
    """
    result = "Сбалансированно"
    open_brackets = ("(", "[", "{")
    close_brackets = (")", "]", "}")
    stack = Stack()
    for char in checking_string:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if stack.isEmpty() or close_brackets.index(char) != open_brackets.index(
                stack.pop()
            ):
                result = "Несбалансированно"
                break
    if not stack.isEmpty():
        result = "Несбалансированно"
    print(result)


if __name__ == "__main__":
    isBalansed(input("Введите строку для проверки: "))
    # isBalansed("(((([{}]))))")
    # isBalansed("[([])((([[[]]])))]{()}")
    # isBalansed("{{[()]}}")
    # isBalansed("}{}")
    # isBalansed("{{[(])]}}")
    # isBalansed("[[{())}]")
