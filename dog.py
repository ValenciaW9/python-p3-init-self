#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

if __name__ == "__main__":
   # Creating a dog instance with name "Fido" and default breed "Mutt"
   fido = Dog("Fido")
