# hellkat_
# 31 Oct 2016
# A new TBAG using dicts and classes instead of lonely functions

from sys import exit
from random import randint

class Scene(object):

    # random statements to tell player they gave an incorrect command
    nope = [
        "That doesn't seem to work here...",
        "Try something else.",
        "Um, no. You can't do that.",
        "That's a terrible idea. Try again."
    ]

    def enter(self):
        print('Enter will be subclassed for each scene')

    # handles incorrect commands
    def sorry(self, scene_name):
        print('-' * 35)
        print(Scene.nope[randint(0, len(Scene.nope)-1)])
        print('-' * 35)
        return scene_name

    # just to congratulate myself for not breaking the game
    def test(self):
        print('#' * 30)
        print('Everything works up to this point!')
        print('#' * 30)

# runs game by calling enter() for each scene.
# therefore, each scene MUST have an enter() method.
# next scene must be specified in the if statements of current scene
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('final')
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class DefinePlayer(Scene):
    def enter(self):
        print("Welcome to Adventure or Die!\n")
        print("What is your name?")

        name = input("> ")

        print("Okay, %s. Press ANY KEY to begin." % name)

        ready = input("> ")
        if ready:
            return 'opener'
        else:
            return 'opener'

# currently, game exits when you die.
# this will soon change.
class Death(Scene):
    quips = [
        "The universe is indifferent to your non-existence.",
        "How about a nice game of chess?",
        "You died. This happens if you suck. You suck.",
        "You are better suited to dying than succeeding at this game."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class Opener(Scene):
    def enter(self):
        print("\nYou wake up from a long sleep. As you open your eyes, you ")
        print("realize your head hurts, a dull aching pain. You're in a small ")
        print("room, sitting on the floor. There is no furniture, only a door ")
        print("on the opposite wall.\n")
        print("What do you do?")

        while True:
            action = input("> ").lower()

            if 'stand' in action or 'door' in action:
                print("\nYou slowly rise, and walk over to the door. You try the ")
                print("knob, but it is locked.\n")
                return 'locked'
            else:
                return _scene.sorry('opener')

class Locked(Scene):
    def enter(self):
        print("You check out the door. It is old and wooden, with faded ")
        print("paint peeling off in spots. The hinges are rusty and made of ")
        print("brass. You have no idea where you are, and you decide you need ")
        print("to get this door open...")

        while True:
            action = input("> ").lower()

            if 'kick' in action and 'door' in action:
                print("\nYou back up a step, and kick the door with all your ")
                print("might. It creaks but doesn't open. It seems the hinges ")
                print("could be easier to break...")
            elif 'punch' in action or 'hit' in action:
                print("\nYou swing your fist at the door. Your blow lands ")
                print("ineffectually. Embarrassing!")
            elif 'kick' in action and 'hinges' in action:
                print("\nYou slam the heel of your boot into the middle hinge, ")
                print("and the old door breaks. It falls outward and lands ")
                print("on the ground. You step into the hallway.\n")
                return 'hallway'
            else:
                return _scene.sorry('locked')

class Hallway(Scene):
    def enter(self):
        _scene.test()
        exit(1)

class Map(object):
    scenes = {
        'define_player': DefinePlayer(),
        'death': Death(),
        'opener': Opener(),
        'locked': Locked(),
        'hallway': Hallway()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        run = Map.scenes.get(scene_name)
        return run

    def opening_scene(self):
        return self.next_scene(self.start_scene)

_scene = Scene()

boot_map = Map('define_player')
boot_game = Engine(boot_map)
boot_game.play()
