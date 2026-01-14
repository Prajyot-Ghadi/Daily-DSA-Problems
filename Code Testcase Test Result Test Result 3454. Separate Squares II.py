class Solution:
    def separateSquares(self, squares):
        # Step 1: create events
        events = []
        for x, y, l in squares:
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))

        events.sort()

        # Helper: union length of x-intervals
        def union_length(intervals):
            if not intervals:
                return 0
            intervals.sort()
            total = 0
            cur_l, cur_r = intervals[0]
            for l, r in intervals[1:]:
                if l > cur_r:
                    total += cur_r - cur_l
                    cur_l, cur_r = l, r
                else:
                    cur_r = max(cur_r, r)
            total += cur_r - cur_l
            return total

        # Step 2: compute total area
        active = []
        prev_y = events[0][0]
        total_area = 0

        for y, typ, l, r in events:
            height = y - prev_y
            if height > 0:
                total_area += union_length(active) * height

            if typ == 1:
                active.append((l, r))
            else:
                active.remove((l, r))

            prev_y = y

        half = total_area / 2

        # Step 3: find split y
        active.clear()
        prev_y = events[0][0]
        cur_area = 0

        for y, typ, l, r in events:
            height = y - prev_y
            if height > 0:
                width = union_length(active)
                strip_area = width * height

                if cur_area + strip_area >= half:
                    # exact y inside this strip
                    return prev_y + (half - cur_area) / width

                cur_area += strip_area

            if typ == 1:
                active.append((l, r))
            else:
                active.remove((l, r))

            prev_y = y

        return prev_y
