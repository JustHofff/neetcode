class Node {
    int data;
    Node link;

    public Node(int data) {
        this(data, null);
    }

    public Node(int data, Node link) {
        this.data = data;
        this.link = link;
    }

    public void setLink(Node other) {
        this.link = other;
    }

    public Node getLink() {
        return link;
    }

    public void setData(int data) {
        this.data = data;
    }

    public int getData() {
        return data;
    }
}

class LinkedList {
    int size = 0;
    Node head;
    Node tail;

    public LinkedList() {
        this.head = null;
        this.tail = head;
    }

    public int get(int index) {
        Node current = head;
        int i = 0;
        while (current != null) {
            if (index == i) {
                return current.getData();
            }
            i++;
            current = current.getLink();
        }
        return -1;
    }

    public void insertHead(int val) {
        Node newNode = new Node(val);
        if (head == null) {
            this.head = newNode;
            this.tail = head;
        } else {
            newNode.setLink(head);
            this.head = newNode;
        }
        size++;
    }

    public void insertTail(int val) {
        Node newNode = new Node(val);
        if (tail == null) {
            this.tail = newNode;
            this.head = tail;
        } else {
            tail.setLink(newNode);
            this.tail = newNode;
        }
        size++;
    }

    public boolean remove(int index) {
        if (index >= size) {
            return false;
        } else if (index == 0) {
            head = head.getLink();
            return true;
        }
        Node current = head;
        Node previous = current;
        int i = 0;
        while (i < index) {
            previous = current;
            current = current.getLink();
            i++;
        }
        if (current == tail) {
            previous.setLink(null);
            tail = previous;
        } else {
            previous.setLink(current.getLink());
        }
        size--;
        return true;
    }

    public ArrayList<Integer> getValues() {
        Node current = head;
        ArrayList<Integer> arr = new ArrayList<Integer>();
        while (current != null) {
            arr.add(current.getData());
            current = current.getLink();
        }
        return arr;
    }
}
