def read_input():
    line1 = map(int, input().split())
    line2 = map(int, input().split())
    return next(line1), next(line1), list(line2)

def print_output(res):
    print(res)

def solve(n, m, nums):
    res = cur = window = sum(nums[:m])
    for r in range(m, n):
        window += nums[r] - nums[r - m]
        cur = min(cur + nums[r], window)
        res = min(res, cur)
    return res

def main():
    n, m, nums = read_input()
    res = solve(n, m, nums)
    print_output(res)

if __name__ == "__main__":
    main()

