#  https://leetcode.com/problems/climbing-stairs/description/

def climb_steps(n) -> int:
    hash_map = {}

    def recursive_calls(n, hash_map):
        if n in hash_map.keys():
            return hash_map[n]

        if n == 1:
            hash_map[n] = 1
            return 1
        if n == 2:
            hash_map[n] = 2
            return 2

        result = recursive_calls(n-1, hash_map) + \
            recursive_calls(n-2, hash_map)
        hash_map[n] = result
        return result

    return recursive_calls(n, hash_map)
