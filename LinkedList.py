
# Basic Usecase -> pull yourself through the linked list one link at a time
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

# Removing nodes
# Example: https://leetcode.com/problems/remove-nth-node-from-end-of-list/



# Merging two linked lists
# Example: https://leetcode.com/problems/merge-two-sorted-lists/

def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # defaults
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        # intial setup
        if l1.val > l2.val:
            head = l2
            l2 = l2.next
        else:
            head = l1
            l1 = l1.next
        prevnode = head
        
        # go through lists
        while (l1 != None) and (l2 != None):
            
            # conditioned comparison
            if l1.val > l2.val:
                prevnode.next = l2
                prevnode = l2
                l2 = l2.next
            else:
                prevnode.next = l1
                prevnode = l1
                l1 = l1.next
        
        # clean up
        if l1 != None:
            prevnode.next = l1
        elif l2 != None:
            prevnode.next = l2  
            
        return head



