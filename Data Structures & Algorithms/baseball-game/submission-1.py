class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        cur_count = 0
        for index, value in enumerate(operations):
            if value == '+' and (cur_count + 1) > 1:
                new_val = records[cur_count-1] + records[cur_count-2]
                records.append(new_val)
                cur_count += 1
            elif value == 'C' and (cur_count + 1) > 0:
                records.pop()
                cur_count -= 1
            elif value == "D" and (cur_count + 1) > 0:
                new_val = records[-1] * 2
                records.append(new_val)
                cur_count += 1
            else:
                value = int(value)
                records.append(value)
                cur_count += 1
        return sum(records)
        