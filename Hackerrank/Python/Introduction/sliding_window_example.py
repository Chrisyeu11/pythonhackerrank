def sliding_window_example(s, k):
    window_start = 0
    for window_end in range(len(s)):
        # expand the window
        if window_end >= k:
            # shrink the window
            window_start += 1
