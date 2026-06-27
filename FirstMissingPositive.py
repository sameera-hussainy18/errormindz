nums = [1, 2, 4]

n = len(nums)

i = 0
while i < n:
    if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    else:
        i += 1

ans = n + 1

for i in range(n):
    if nums[i] != i + 1:
        ans = i + 1
        break

print(ans)
