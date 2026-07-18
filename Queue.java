class Queue {
    int front = 0, rear = -1;
    int[] queue = new int[5];

    void insert(int x) {
        if (rear == 4)
            System.out.println("Queue Overflow");
        else
            queue[++rear] = x;
    }

    void delete() {
        if (front > rear)
            System.out.println("Queue Underflow");
        else
            System.out.println("Deleted: " + queue[front++]);
    }

    public static void main(String[] args) {
        Queue q = new Queue();
        q.insert(10);
        q.insert(20);
        q.delete();
    }
}
