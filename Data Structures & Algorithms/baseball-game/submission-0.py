class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total_sum = 0
        for op in operations:
            if op == '+':
                new_elem = record[-1] + record[-2]
                total_sum += new_elem
                record.append(new_elem)
            elif op == 'C':
                removed_elem = record.pop()
                total_sum -= removed_elem
            elif op == 'D':
                new_elem = record[-1] * 2
                total_sum += new_elem
                record.append(new_elem)
            else:
                record.append(int(op))
                total_sum += int(op)

        return total_sum           

        