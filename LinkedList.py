
# Basic Use Case -> pull yourself through the linked list one link at a time
# Reversing a linked list
# Example: https://leetcode.com/problems/reverse-linked-list/

# solution that makes a new list
def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        # default
        if head == None:
            return None
        elif head.next == None:
            return head
        
        # initiallize the first node of the return, pointing to none
        newnode = ListNode(val=head.val, next=None)
        head = head.next
        
        # go through the list with each node pointing to the one before it
        while head != None:
            newnode = ListNode(val=head.val, next=newnode)
            head = head.next
            
        return newnode
      
# solution that changes pointers
def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None:
            return None
        elif head.next == None:
            return head
        
        prev = None
        
        while head != None:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            
        return prev







