class Solution:
  def minTime(self, skill: list[int], mana: list[int]) -> int:
    """
    Calculates the minimum time required for all wizards to brew all potions in order.
    """
    n = len(skill)
    m = len(mana)

    skill_prefix_sum = [0] * n
    skill_prefix_sum[0] = skill[0]
    for i in range(1, n):
      skill_prefix_sum[i] = skill_prefix_sum[i-1] + skill[i]

    potion_start_time = 0
    for j in range(1, m):
      mana_prev = mana[j - 1]
      mana_curr = mana[j]
      
      max_delay_term = 0
      for i in range(n):
        sum_skill_i = skill_prefix_sum[i]

        sum_skill_i_minus_1 = skill_prefix_sum[i-1] if i > 0 else 0
        
        term = mana_prev * sum_skill_i - mana_curr * sum_skill_i_minus_1
        if term > max_delay_term:
          max_delay_term = term
      
      potion_start_time += max_delay_term


    total_time = potion_start_time + skill_prefix_sum[n-1] * mana[m-1]

    return total_time
