ALL_SPACES = list('123456789')  # Klucze słownika planszy KIK.
X, O, BLANK = 'X', 'O', ' '  # Stałe reprezentujące wartości tekstowe.


def main():
    """Rozgrywka w kółko i krzyżyk."""
    print('Witaj w grze kółko i krzyżyk!')
    gameBoard = Board()  # Utwórz słownik planszy KIK.
    currentPlayer, nextPlayer = X, O  # X wykonuje ruch jako pierwszy, O jako następny.
    while True:
        print(gameBoard)  # Wyświetl planszę na ekranie.

        # Zadawaj graczowi pytanie, aż wprowadzi prawidłową liczbę od 1 do 9:
        move = None
        while not gameBoard.isValidSpace(move):
            print(f'Jaki jest ruch gracza {currentPlayer}? (1-9)')
            move = input()
        gameBoard.updateBoard(move, currentPlayer)  # Wykonanie ruchu.
        # Sprawdzenie, czy gra jest zakończona:
        if gameBoard.isWinner(currentPlayer):  # Sprawdzenie, kto wygrał.
            print(gameBoard)
            print(currentPlayer + ' wygrał grę!')
            break
        elif gameBoard.isBoardFull():  # Sprawdzenie remisu.
            print(gameBoard)
            print('Gra zakończyła się remisem!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # Zmiana gracza.
    print('Dziękuję za grę!')
    
class Board:
    def __init__(self) -> None:
        self.area = {}
        for space in ALL_SPACES:
            self.area[space] = BLANK  # Wszystkie pola na początku są puste.
            
            
    def __str__(self) -> str:
        return f'''
        {self.area['1']}|{self.area['2']}|{self.area['3']} 1 2 3 
            -+-+- 
        {self.area['4']}|{self.area['5']}|{self.area['6']} 4 5 6 
            -+-+- 
        {self.area['7']}|{self.area['8']}|{self.area['9']} 7 8 9'''
        
    def isValidSpace(self, space):
        if space is None:
            return False
        return space in ALL_SPACES or self.area[space] == BLANK
    
    def isWinner(self, player):
        b, p = self.area, player # Krótsze nazwy jako "składniowy cukier".
        return ((b['1'] == b['2'] == b['3'] == p) or # poziomo na górze
            (b['4'] == b['5'] == b['6'] == p) or # poziomo w środku
            (b['7'] == b['8'] == b['9'] == p) or # poziomo u dołu
            (b['1'] == b['4'] == b['7'] == p) or # pionowo z lewej
            (b['2'] == b['5'] == b['8'] == p) or # pionowo w środku
            (b['3'] == b['6'] == b['9'] == p) or # pionowo z prawej
            (b['3'] == b['5'] == b['7'] == p) or # przekątna 1
            (b['1'] == b['5'] == b['9'] == p)) # przekątna 2
        
        
    def isBoardFull(self):
        for space in ALL_SPACES:
         if self.area[space] == BLANK:
            return False # Jeśli nawet jedno pole jest puste, zwracaj False.
        return True # Nie ma wolnych pól, zatem zwróć True.

    def updateBoard(self, space, mark):
        """Ustawia pole na planszy na podany znak."""
        self.area[space] = mark
    






if __name__ == '__main__':
    main() # Wywołaj main(), jeśli ten moduł został uruchomiony, a nie zaimportowany.