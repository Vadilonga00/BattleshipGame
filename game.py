from __future__ import annotations
from abc import ABC, abstractmethod
import ship_types

class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"{type(state).__name__}'s turn")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def choose_and_shoot(self,ship_list):
        self._state.shoot(ship_list)


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def shoot(self,ship_list) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class Player1(State):
    def shoot(self,ship_list):
        row_guess = int(input("guess_row:\n"))
        col_guess = int(input("guess_column:\n"))
        for i in ship_list[1][:]:
            if [row_guess,col_guess] in i.coordinates:
                i.coordinates.remove([row_guess,col_guess])
                i.hits = i.hits + 1
                if ship_types.Ship.is_sunk(i):
                    print('Affondato, Spara di nuovo!')
                else:
                    print('Colpito, spara di nuovo!')
                Context(Player1()).choose_and_shoot(ship_list)
        print('Mancato')
        self.context.transition_to(Player2())


class Player2(State):
    def shoot(self,ship_list):
        row_guess = int(input("guess_row:\n"))
        col_guess = int(input("guess_column:\n"))
        for i in ship_list[0][:]:
            if [row_guess,col_guess] in i.coordinates:
                i.coordinates.remove([row_guess, col_guess])
                i.hits = i.hits+1
                if ship_types.Ship.is_sunk(i):
                    print('Affondato, Spara di nuovo!')
                else:
                    print('Colpito, spara di nuovo!')
                Context(Player2()).choose_and_shoot(ship_list)
        print('Mancato')
        self.context.transition_to(Player1())


