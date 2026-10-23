def logo(thickness, c="H"):
    t = thickness
    top_cone = [(c * i).rjust(t - 1) + c + (c * i).ljust(t - 1) for i in range(t)]
    pillars = [(c * t).center(t * 2) + (c * t).center(t * 6) for _ in range(t + 1)]
    belt = [(c * t * 5).center(t * 6) for _ in range((t + 1) // 2)]
    bottom_cone = [
        ((c * (t - i - 1)).rjust(t) + c + (c * (t - i - 1)).ljust(t)).rjust(t * 6) for i in range(t)
    ]
    return top_cone + pillars + belt + pillars + bottom_cone
