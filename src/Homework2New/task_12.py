def bouncingball(h, bounce, window):
    """Instructions

    How much times ball thrown from height h will be seen in window
    with height window.
    Float parameter "h" in meters must be greater than 0
    Float parameter "bounce" must be greater
    than 0 and less than 1
    Float parameter "window" must be less than h.
    - h = 3, bounce = 0.66, window = 1.5, result is 3
    - h = 3, bounce = 1, window = 1.5, result is -1
    (Condition 2) not fulfilled).
    """
    seen_number = -1
    if 0 < bounce < 1:
        while h > window and h > 0:
            seen_number += 2
            h *= bounce
    return seen_number


if __name__ == '__main__':
    print(bouncingball(30, 0.001, 1.5))
    print(bouncingball(30, 0.66, 1.5))
