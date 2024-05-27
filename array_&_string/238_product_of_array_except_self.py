class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Required to solve without division and in O(n) time complexity
        #TODO: Follow up: Could you solve it with constant space complexity? (Excluding output array)
        """
        l = len(nums)
        zeros = 0
        prefix = []
        postfix = [0] * l
        output = []

        # Prefix
        product = 1
        for i in range(l):
            if nums[i] == 0:
                zeros += 1
                # If > 1 zero => return zero array
                if zeros > 1:
                    return [0] * l
                zero_idx = i
                prefix.append(product)
            else:
                product *= nums[i]
                prefix.append(product)
        
        # If one zero => return zero array & product in index of nums zero val 
        if zeros > 0:
            output = [0] * l
            output[zero_idx] = prefix[-1]
            return output
        
        # Postfix (Can assume no zeros)
        product = 1
        for i in range(l - 1, -1, -1):
            product *= nums[i]
            postfix[i] = product
        
        # Calculate product except self
        for i in range(l):
            if i == 0:
                output.append(postfix[i + 1])
            elif i == l - 1:
                output.append(prefix[i - 1])
            else:
                output.append(prefix[i - 1] * postfix[i + 1])

        return output

        