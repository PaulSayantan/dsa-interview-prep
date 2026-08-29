class MinStack {
    StackNode[] stack;
    static int MAX_SIZE = 30000;
    int size;
    public MinStack() {
        this.stack = new StackNode[MAX_SIZE];
        this.size = 0;
    }
    
    public void push(int value) {
        if (this.size > 0) {
            int currMin = this.getMin();
            int maxMin = currMin < value ? currMin: value;
            this.stack[this.size++] = new StackNode(value, maxMin);
        } else {
            this.stack[this.size++] = new StackNode(value, value);
        }
    }
    
    public void pop() {
        this.size--;
    }
    
    public int top() {
        return this.stack[this.size - 1].val;
    }
    
    public int getMin() {
        return this.stack[this.size - 1].minVal;
    }
}

class StackNode {
    int val;
    int minVal;
    public StackNode(int val, int minVal) {
        this.val = val;
        this.minVal = minVal;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(value);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */