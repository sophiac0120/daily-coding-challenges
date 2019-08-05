##Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
##
##Note: You may not slant the container and n is at least 2.
##Example:
##
##Input: [1,8,6,2,5,4,8,3,7]
##Output: 49
##The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


def maxArea(li):
    i = 0
    j = len(li) - 1
    if j < 0:
        return 0
    counter = 0
    max_area = get_maxArea(i, j, li)
    while i < j:
        area = get_maxArea(i, j, li)
        if area > max_area:
            max_area = area
        if counter == 0:
            i += 1
            counter += 1
        else:
            j -= 1
            counter -= 1
    return max_area

def get_maxArea(i, j, li):
    return (j - i) * min(li[i], li[j])
        