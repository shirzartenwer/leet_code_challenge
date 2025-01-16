
# I initially naively thought that I could solve this problem by simply taking the maximum number each step
# And if it goes over the target amount, then take the other numbers.
# But this approach underestimate the possibility of already not taking the max
# number several steps before the final step.
class WrongSolution:
    def coinChange(self, coins, amount) -> int:
        current_sum = 0
        num_coins = 0
        candidate = coins

        while current_sum < amount and len(candidate) > 0:
            current_ele = max(candidate)
            if current_sum + current_ele <= amount:
                current_sum += current_ele
                num_coins += 1
                candidate = coins
            else:
                candidate = [ele for ele in candidate if ele != current_ele]

        if current_sum == amount:
            return num_coins
        else:
            return -1


# Here I thought then: okay, if it goves over the target amount,
# then I retrace back one step and reuse other smaller coins.
# But this stil didn't work.


class LessWrongSolution:
    def coinChange(self, coins, amount) -> int:
        current_sum = 0
        num_coins = 0
        candidate = coins
        used_coins = []
        memory = []

        def search(current_sum, num_coins, candidate, used_coins, memory):
            while current_sum < amount and len(candidate) > 0:
                current_ele = max(candidate)
                if current_sum + current_ele <= amount:
                    current_sum += current_ele
                    num_coins += 1
                    candidate = coins
                    used_coins.append(current_ele)
                else:
                    candidate = [
                        ele for ele in candidate if ele != current_ele]

            if current_sum == amount:
                return num_coins
            else:
                if len(used_coins) > 0:
                    memory.append(used_coins[-1])
                    if len(memory) < len(coins):
                        current_sum -= used_coins[-1]
                        candidate = [
                            ele for ele in candidate if ele != used_coins[-1]]
                        search(current_sum, num_coins-1,
                               candidate, used_coins[:-1], memory)
                    else:
                        return -1
                else:
                    return -1
        return search(current_sum, num_coins, candidate, used_coins, memory)


class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                # The +1 here comes from the counting the coin that's used in this iteration of the loop
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


print(Solution().coinChange([2], 3))
