import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import FancyBboxPatch

# Node structure for the linked list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.movements = []  # Stores movements for animation

    def partition(self, head: ListNode, x: int):
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        idx_map = {}  # Track positions for each node
        idx = 0
        current = head
        while current:
            idx_map[current.val] = idx
            idx += 1
            current = current.next

        while fast.next:
            if fast.next.val >= x:
                fast = fast.next
            else:
                # Log movement: remove the node from fast and add after slow
                tmp = fast.next
                fast.next = fast.next.next

                # Log remove operation
                self.movements.append(('remove', tmp.val, idx_map[tmp.val]))

                # Insert node after slow
                tmp_next = slow.next
                slow.next = tmp
                tmp.next = tmp_next

                # Log insert operation
                self.movements.append(
                    ('insert', tmp.val, idx_map[slow.next.val]))

                # Move slow forward, skipping the dummy node in index mapping
                if slow != dummy:
                    idx_map[tmp.val] = idx_map[slow.val] + 1
                else:
                    idx_map[tmp.val] = 0

                # Move slow forward
                slow = slow.next
                fast = slow

        return dummy.next

# Visualization and animation


class LinkedListAnimator:
    def __init__(self, values, x):
        self.values = values
        self.x = x
        self.fig, self.ax = plt.subplots()
        self.rects = []
        self.solution = Solution()
        self.create_initial_plot()

    def create_initial_plot(self):
        self.ax.clear()
        self.rects = []
        for i, val in enumerate(self.values):
            rect = FancyBboxPatch(
                (i * 2, 0), 1.5, 1, boxstyle="round,pad=0.3", ec="black", fc="skyblue")
            self.ax.add_patch(rect)
            self.ax.text(i * 2 + 0.75, 0.5, str(val),
                         ha="center", va="center", fontsize=12)
            self.rects.append(rect)

        self.ax.set_xlim(-1, len(self.values) * 2)
        self.ax.set_ylim(-1, 3)
        self.ax.axis('off')

    def animate_partition(self):
        head = self.create_linked_list(self.values)
        self.solution.partition(head, self.x)
        self.ani = animation.FuncAnimation(self.fig, self.update_animation, frames=len(self.solution.movements),
                                           repeat=False, interval=1000, blit=False)
        plt.show()

    def update_animation(self, i):
        action, val, old_idx = self.solution.movements[i]
        idx = self.values.index(val)

        rect = self.rects[idx]
        if action == 'remove':
            rect.set_y(2)  # Move node upwards to remove
        elif action == 'insert':
            # Find the correct position after insertion
            new_position = old_idx + 1
            rect.set_x(new_position * 2)
            rect.set_y(0)  # Move it back down

    def create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head


# Example linked list values
values = [1, 4, 3, 2, 5, 2]
x = 3
animator = LinkedListAnimator(values, x)
animator.animate_partition()
