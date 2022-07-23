seed = (1, 1, 1)

cache = set()

def solve(n, should_print=True):
    if n == 1:
        if should_print:
            print(*seed)
        cache.add(seed)
        return [seed]

    prev_ans_list = solve(n - 1, should_print)

    ans_list = []
    for prev_ans in prev_ans_list:
        # x z -> new_y
        new_y = 3 * prev_ans[0] * prev_ans[2] - prev_ans[1]
        # y z -> new_x
        new_x = 3 * prev_ans[1] * prev_ans[2] - prev_ans[0]

        ans1 = (prev_ans[0], prev_ans[2], new_y)
        ans2 = (prev_ans[1], prev_ans[2], new_x)

        if (ans1 not in cache):
            ans_list.append(ans1)
            cache.add(ans1)
        if (ans2 not in cache):
            ans_list.append(ans2)
            cache.add(ans2)

        if should_print:
            if ans1 == ans2:
                print(*ans1)
            else:
                print(*ans1)
                print(*ans2)
    return ans_list


N = int(input())
solve(N, should_print=True)
# display answers as sorted tuples
# print(sorted(cache))
