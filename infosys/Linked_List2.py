# Linked List

# Partition List
 """Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input
head
=
[1,4,3,2,5,2]

1
4
3
2
5
2
null
Input
x
=
3

3
Output
[1,2,2,4,3,5]

1
2
2
4
3
5
null
Example 2:
Input
head
=
[2,1]

2
1
null
Input
x
=
2

2
Output
[1,2]

1
2
null
"""
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        left, right = ListNode(0), ListNode(0)

        left_tail, right_tail = left, right

        while head:
            if head.val < x:
                left_tail.next = head
                left_tail = left_tail.next
            else:
                right_tail.next = head
                right_tail = right_tail.next

            head = head.next

        right_tail.next = None
        left_tail.next = right.next

        return left.next


       
 
