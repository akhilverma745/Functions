def even_numbers(nums):
    even_list = []
    for n in nums:
        if n % 2 == 0:
            even_list.append(n)
    return even_list

num_list = [1,2,4,45,24,22,11,78,5,9,14]
ans = even_numbers(num_list)
print("Even numbers are:", ans)
