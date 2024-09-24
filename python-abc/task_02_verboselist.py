#!/usr/bin/python3
class VerboseList(list):
    """
    A custom list class that provides notifications
    when items are added or removed.
    """

    def append(self, item):
        """
        Overrides the append method to add a notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Overrides the extend method to add a notification.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """
        Overrides the remove method to add
        a notification before removing the item.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        """
        Overrides the pop method to add a notification before popping the item.
        """
        if index is None:
            item = super().pop()
            print(f"Popped [{item}] from the list.")
        else:
            item = super().pop(index)
            print(f"Popped [{item}] from the list.")
        return item
