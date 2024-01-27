#!/usr/bin/env python3

from person import Person


class TestPerson:

    def test_is_class(self):
        guido = Person("Guido")
        assert isinstance(guido, Person)

    def test_saves_self_name(self):
        guido = Person("Guido")
        assert guido.name == "Guido"
