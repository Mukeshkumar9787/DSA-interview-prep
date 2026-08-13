class Node {
    constructor(val, next=null){
        this.val = val;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        let i = 0;
        let curr = this.head;
        while(i < index && curr){
            i++;
            curr = curr.next;
        }
        if(curr){
            return curr.val;
        }
        return -1;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertHead(val) {
        this.head = new Node(val, this.head);
        if(!this.tail){
            this.tail = this.head;
        }
    }

    /**
     * @param {number} val
     * @return {void}
     */
    insertTail(val) {
        if(!this.head){
            this.insertHead(val);
            return;
        }
        let newNode = new Node(val);
        this.tail.next = newNode;
        this.tail = this.tail.next;
    }

    /**
     * @param {number} index
     * @return {boolean}
     */
    remove(index) {
        if(!this.head) return false;
        if(index === 0){
            this.head = this.head.next;
            if(!this.head){
                this.tail = null;
            }
            return true;
        }
        let i = 0;
        let curr = this.head;
        while((i < index - 1) && curr){
            i++;
            curr = curr.next;
        }
        if(!curr || !curr.next){
            return false;
        }
        let nodeToRemove = curr.next;
        curr.next = nodeToRemove.next;
        if(this.tail === nodeToRemove){
            this.tail = curr;
        }
        return true;
    }

    /**
     * @return {number[]}
     */
    getValues() {
        const result = [];
        let curr = this.head;
        while(curr){
            result.push(curr.val);
            curr = curr.next;
        }
        return result;
    }
}
