// RUNTIME : 60ms/24.44%
// MEMORY : 11.15MD/14.17%
// BAD
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    m := make(map[*ListNode]struct{}, 0)

    for headA != nil {
        m[headA] = struct{}{}
        headA = headA.Next
    }

    for headB != nil {
        if _, ok := m[headB]; ok {
            return headB
        }
        headB = headB.Next
    }

    return nil
}
