// Runtime : 1588ms/5.03%
// Memory  : 14.98MB/56.54%
// type MinStack struct {
//     s       []int
// }


// func Constructor() MinStack {
//     return MinStack{
//         s: make([]int, 0),
//     }
// }


// func (this *MinStack) Push(value int)  {
//     this.s = append(this.s, value)
// }


// func (this *MinStack) Pop()  {
//     this.s = this.s[:len(this.s) - 1]
// }


// func (this *MinStack) Top() int {
//     return this.s[len(this.s) - 1]
// }


// func (this *MinStack) GetMin() int {
//     return slices.Min(this.s)
// }


// RUNTIME : 89ms/28.04%
// Memory : 14.82MB/59.44%

// type MinStack struct {
//     s       []int
//     mins    []int
// }


// func Constructor() MinStack {
//     return MinStack{
//         s: make([]int, 0),
//         mins: make([]int, 0),
//     }
// }


// func (this *MinStack) Push(value int)  {
//     this.s = append(this.s, value)
//     if len(this.mins) == 0 {
//         this.mins = append(this.mins, value)
//     } else {
//         if value < this.mins[len(this.mins) - 1] {
//             this.mins = append(this.mins, value)
//         } else {
//             this.mins = append(this.mins, this.mins[len(this.mins) - 1])
//         }
//     }
// }


// func (this *MinStack) Pop()  {
//     this.s = this.s[:len(this.s) - 1]
//     this.mins = this.mins[:len(this.mins) - 1]
// }


// func (this *MinStack) Top() int {
//     return this.s[len(this.s) - 1]
// }


// func (this *MinStack) GetMin() int {
//     return this.mins[len(this.mins) - 1]
// }


// Особо без изменений
type MinStack struct {
    s []Node
}

type Node struct{
    min int
    val int
}


func Constructor() MinStack {
    return MinStack{
        s: make([]Node, 0),
    }
}


func (this *MinStack) Push(value int)  {
    if len(this.s) == 0 {
        this.s = append(this.s, Node{val: value, min: value})
    } else {
        if this.s[len(this.s) - 1].min > value {
            this.s = append(this.s, Node{val: value, min: value})
        } else {
            this.s = append(this.s, Node{val: value, min: this.s[len(this.s) - 1].min})
        }
    }
}


func (this *MinStack) Pop()  {
    this.s = this.s[:len(this.s) - 1]
}


func (this *MinStack) Top() int {
    return this.s[len(this.s) - 1].val
}


func (this *MinStack) GetMin() int {
    return this.s[len(this.s) - 1].min
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(value);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */
