class Piece:
    def __init__(self, count: int = 0):
        self.count = count
    
    def add_piece(self) -> bool:
        if self.count == 3:
            return False
        self.count += 1
        return True

    def get_count (self) -> int:
        return self.count