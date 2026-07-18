class Stack {
    int top = -1;
    int[] stack = new int[5];

    void push(int x) {
        if (top == 4)
            System.out.println("Stack Overflow");
        else
            stack[++top] = x;
    }

    void pop() {
        if (top == -1)
            System.out.println("Stack Underflow");
        else
            System.out.println("Popped: " + stack[top--]);
    }

    public static void main(String[] args) {
        Stack s = new Stack();
        s.push(10);
        s.push(20);
        s.pop();
    }
}
