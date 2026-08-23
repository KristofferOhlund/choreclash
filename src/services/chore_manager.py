

class ChoreManager:
    """Class to handle all chores for users"""
    def __init__(self):
        self.chores = None

    def add_chore(self, chore):
        """Add chore to list of chores"""
        if not self.chores:
            self.chores = []
        self.chores.append(chore)