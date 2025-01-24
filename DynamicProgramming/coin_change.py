
# I initially naively thought that I could solve this problem by simply taking the maximum number each step
# And if it goes over the target amount, then take the other numbers.
# But this approach underestimate the possibility of already not taking the max
# number several steps before the final step.

from collections import deque
import math


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


# Bottom up DP
class DPSolution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                # The +1 here comes from the counting the coin that's used in this iteration of the loop
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


print(DPSolution().coinChange([4], 5))


class BFSolution:

    def coinChange(self, coins, amount: int) -> int:
        if amount == 0:
            return 0

        amount_queue = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True

        used_num_coin = 0

        while amount_queue:
            used_num_coin += 1

            for _ in range(len(amount_queue)):
                # [0], cur 0, nxt = 1, 2, 4, amount_queue = [1, 2, 5]
                # [1, 2, 5], cur = [1, 2, 5], nxt 1, 3, 5, 3, 4, 6, 6, 7, 9, amount_queue = [1, 3, 5, 4,7, 9]
                # basically this loop computes all results at each tree level, until any of the leaf at this level equals to the desired amount
                # it's sped up by skipping the amount that's already been composed of by other combination
                cur = amount_queue.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return used_num_coin
                    elif nxt >= amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    amount_queue.append(nxt)

        return -1


class DFSSolution:
    #  This solution likely cause the recursion depth out of limit
    # A way to improve it is to add a memroy array to not repeat the calculation
    # But it migth still exceeds the time limit.

    def coinChange(self, coins, amount: int):

        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]

            # res is the number of coin used. The initial value could be
            # an infinitely large number. Or any number that's larger than the amount
            res = math.inf

            for coin in coins:
                if amount - coin > 0:
                    res = min(res, 1+dfs(amount-coin))

            memo[amount] = res
            return res

        result = dfs(amount)
        return -1 if result >= math.inf else result


print(BFSolution().coinChange([4], 5))
print(DFSSolution().coinChange([4], 5))
