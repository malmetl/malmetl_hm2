from abc import ABC, abstractmethod


class Figure:
    @abstractmethod
    def get_area(self):
        raise ValueError("This method should be overridden by subclasses")

    @abstractmethod
    def get_perimeter(self):
        raise ValueError("This method should be overridden by subclasses")

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Argument is not a geometric figure")
        return self.get_area() + figure.get_area()
