from typing import Optional
import clr

clr.AddReference('System.Drawing')
clr.AddReference('Reversi')

import System as _CSharp
import System.Drawing as _Drawing
from Reversi import Reversi as _Reversi


Board = list[list[Optional[bool]]]


class Reversi:
    _internal: _Reversi

    def __init__(self) -> None:
        self._internal = _Reversi()

    @property
    def turn(self) -> bool:
        return self._internal.Turn

    @property
    def _board(self):
        return self._internal.Board

    @property
    def board(self) -> Board:
        internal = self._board
        result = []
        for i in range(internal.GetLength(0)):
            result.append([])
            for j in range(internal.GetLength(1)):
                result[i].append(internal[i, j])
        return result

    @property
    def _valid_moves(self):
        return self._internal.ValidMoves

    @property
    def valid_moves(self) -> list[tuple[int, int]]:
        internal = self._valid_moves
        result = []
        for move  in internal:
            result.append((move.Item1, move.Item2))
        return result

    @property
    def finished(self) -> bool:
        return self._internal.Finished

    @property
    def winner(self) -> Optional[bool]:
        return self._internal.Winner

    def _set_starting_board(self, board) -> None:
        self._internal.SetStartingBoard(board)

    def set_starting_board(self, board: Board) -> None:
        result = _CSharp.Array.CreateInstance(_CSharp.Nullable[bool], len(board), len(board[0]))
        for i in range(len(board)):
            for j in range(len(board[0])):
                result[i, j] = board[i][j]
        self._internal.SetStartingBoard(result)

    def reset(self) -> None:
        self._internal.Reset()
    
    def make_move(self, x: int, y: int) -> bool:
        return self._internal.MakeMove(x, y)

    def print_board(self) -> None:
        self._internal.PrintBoard()
    
    def create_image(self) -> _Drawing.Bitmap:
        return self._internal.CreateImage()
