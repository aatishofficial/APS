# leetcode - https://leetcode.com/problems/range-sum-query-mutable/
class NumArray:
    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.data=nums
        self.n=len(nums)
        self.tree=[0]*(2*(2**math.ceil(math.log2(self.n))) - 1)
        self.build(0,self.n-1,0)
        
    def build(self,l,r,pos):
        if l==r:
            self.tree[pos]=self.data[l]
            return self.data[l]
        mid=l+(r-l)//2
        self.tree[pos]=self.build(l,mid,2*pos+1)+self.build(mid+1,r,2*pos+2)
        return self.tree[pos]

    def update(self, i: int, val: int) -> None:
        diff=val-self.data[i]
        self.data[i]=val
        self.updateutil(0,0,self.n-1,i,diff)
    
    def updateutil(self,pos,l,r,i,diff):
        if l<=i and i<=r:
            self.tree[pos]+=diff
            if l!=r:
                mid=l+(r-l)//2
                self.updateutil(2*pos+1,l,mid,i,diff)
                self.updateutil(2*pos+2,mid+1,r,i,diff)

    def sumRange(self, i: int, j: int) -> int:
        return self.sumutil(0,0,self.n-1,i,j)
    
    def sumutil(self,pos,l,r,i,j):
        if i<=l and j>=r:
            return self.tree[pos]
        if r<i or l > j:
            return 0
        mid=l+(r-l)//2
        return self.sumutil(2*pos+1,l,mid,i,j)+self.sumutil(2*pos+2,mid+1,r,i,j)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
