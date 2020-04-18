#!/usr/bin/env python3
from oregon.utilities.user_prompts import ask_yes_no, ask_numeric
from oregon.tracking.calendar import Calendar
from oregon.state.turnstate import TurnState
from oregon.tracking.triptracker import TripTracker
# Events
from oregon.events.dying import dying
from oregon.events.next_fort import next_fort
from oregon.events.hunt import hunt
from oregon.events.eating import eating
from oregon.events.riders import do_riders_attack, riders_attack
from oregon.events.mountains import mountains
from oregon.events.turn import turn_event_selection
from oregon.events.instructions import print_instructions
from oregon.events.purchases import initial_purchases
from oregon.events.completed_trip import completed_trip

if __name__ == "__main__":

    if ask_yes_no("DO YOU NEED INSTRUCTIONS  (YES/NO)"):
        print_instructions()

    # initial purchases generate an inventory
    inventory = initial_purchases()

    calendar = Calendar()
    tracker = TripTracker()
    turn = TurnState()

    while not calendar.is_final_turn() and not tracker.reached_oregon():
        calendar.print_date()
        inventory.zeroize_negative_values()

        # Resolve health issues from the previous turn
        if turn.illness or turn.injured:
            inventory.spend(20)
            if inventory.money < 0:
                print("YOU CAN'T AFFORD A DOCTOR")
                if turn.illness:
                    print("YOU DIED OF PNEUMONIA")
                elif turn.injured:
                    print("YOU DIED OF INJURIES")
                dying()
            else:
                print("DOCTOR'S BILL IS $20")
                turn.illness = False
                turn.injured = False

        # Show inventory status and mileage
        inventory.print_warnings()
        tracker.print_mileage()

        # Ask for turn options
        inventory.print_inventory()
        turn_response = ask_numeric("DO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT, \nOR (3) CONTINUE", 1, 3)
        if turn_response == 1:
            next_fort(inventory, tracker)
        elif turn_response == 2:
            hunt(inventory, tracker)

        # Eating
        if inventory.food.value < 13:
            print("YOU RAN OUT OF FOOD AND STARVED TO DEATH")
            dying()
        eating(inventory, turn)

        # Advance mileage now, events may subtract from overall
        # progress for each turn
        tracker.random_advance(inventory.oxen)

        # Rider attack
        if do_riders_attack(tracker):
            riders_attack(inventory, tracker, turn)

        # Random per turn events
        turn_event_selection(inventory, tracker, turn)

        # Mountain events
        mountains(inventory, tracker, turn)

        # Move to next turn
        calendar.advance_date()

    # Turns have been exhausted or Oregon has been reached
    if tracker.reached_oregon:
        completed_trip(inventory, tracker, calendar)
    else:
        print("TIME HAS RUN OUT.  WINTER HAS SET IN AND YOU DID NOT REACH OREGON.")
        print("DISTANCE REMAINING: ", tracker.total_trip_distance - tracker.mileage)
