class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        @cache
        def solve(start: int, end: int) -> list[int]:
            res = []
            for split in range(start, end):
                opr = expression[split]

                if opr not in "+-*":
                    continue

                left_exps = solve(start, split)
                right_exps = solve(split + 1, end)

                for left_exp in left_exps:
                    for right_exp in right_exps:
                        if opr == "+": res.append(int(left_exp + right_exp))
                        elif opr == "-": res.append(int(left_exp - right_exp))
                        else: res.append(int(left_exp * right_exp))

            if not res:
                return [int(expression[start:end])]
            return res

        return solve(0, len(expression))
        