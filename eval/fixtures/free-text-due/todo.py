"""A small command-line todo tool."""
import json
import sys
from pathlib import Path

STORE = Path(__file__).with_name("todos.json")


def load():
    return json.loads(STORE.read_text(encoding="utf-8"))


def save(todos):
    STORE.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")


def add(title, due):
    todos = load()
    todos.append({"title": title, "due": due})
    save(todos)


def show():
    for todo in load():
        print(f"{todo['title']} ({todo['due']})")


if __name__ == "__main__":
    if sys.argv[1] == "add":
        add(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "list":
        show()
