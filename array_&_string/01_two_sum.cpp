#include <map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::map<int, int> seenValues; //{value: nums index}
        int remainder;
        for (int i = 0; i < nums.size(); ++i)
        {
            remainder = target - nums[i];
            if (seenValues.find(remainder) != seenValues.end()) // Appears to be a whole millisecond faster than .contains(remainder)
            {
                return {seenValues[remainder], i};
            }
            seenValues[nums[i]] = i;
        }
        return {};
    }
};