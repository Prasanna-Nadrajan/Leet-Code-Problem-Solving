🟡 452. Minimum Number of Arrows to Burst Balloons (Medium)

There are some spherical balloons taped onto a flat wall that represents the XY-plane.
The balloons are represented as a 2D integer array points, where:

points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches from xstart to xend.

You do not know the exact y-coordinates of the balloons.

You can shoot arrows vertically upward from any x-coordinate on the x-axis.

Rules:

A balloon is burst if xstart ≤ x ≤ xend

An arrow travels infinitely upward and can burst multiple balloons

There is no limit on the number of arrows

Task:

Return the minimum number of arrows required to burst all balloons.

Examples:

Input: [[10,16],[2,8],[1,6],[7,12]]
Output: 2

Input: [[1,2],[3,4],[5,6],[7,8]]
Output: 4

Input: [[1,2],[2,3],[3,4],[4,5]]
Output: 2

Constraints:

1 ≤ points.length ≤ 10⁵

-2³¹ ≤ xstart < xend ≤ 2³¹ - 1
