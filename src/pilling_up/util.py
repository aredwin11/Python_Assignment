def can_stack(blocks):
    left = 0
    right = len(blocks) - 1
    top = float('inf')

    while left <= right:
        if blocks[left] >= blocks[right]:
            if blocks[left] <= top:
                top = blocks[left]
                left += 1
            else:
                return "No"
        else:
            if blocks[right] <= top:
                top = blocks[right]
                right -= 1
            else:
                return "No"
    return "Yes"
