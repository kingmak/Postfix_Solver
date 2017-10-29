# my stack class using python lists

class Stack():
    def __init__(this):
        this.stack = []

    def peek(this):
        return this.stack[0]

    def push(this, item):
        this.stack.insert(0, item)

    def pop(this):
        item = this.peek()
        this.stack = this.stack[1:]
        return item

    def empty(this):
        return True if len(this.stack) == 0 else False