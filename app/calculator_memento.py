class HistoryMemento:
    def __init__(self, state: list):
        self._state = list(state)  # Create a copy of the state

    def get_state(self) -> list:
        return list(self._state)