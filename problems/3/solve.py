def solve(values: list):
    ans = 0
    for i in range(32):
        edge_cost = 1 << i
        new_values = []
        values_or = 0
        for v in values:
            if v >> i & 1:
                values_or |= v
                ans += edge_cost
            else:
                new_values.append(v)
        ans -= edge_cost
        new_values.append(values_or)
        values = new_values
        if len(values) == 1:
            break

    return -1 if len(values) > 1 else ans