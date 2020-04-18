def completed_trip(inv, track, cal):
    print("YOU FINALLY ARRIVED AT OREGON CITY")
    print("AFTER", track.total_trip_distance, "LONG MILES---HOORAY!!!!!")

    cal.rollback_date(int(track.last_turn_fraction * 14))
    cal.print_date()
    inv.print_inventory()

    print("PRESIDENT JAMES K. POLK SENDS YOU HIS")
    print("      HEARTIEST CONGRATULATIONS")
    print("")
    print("           AND WISHES YOU A PROSPEROUS LIFE AHEAD")
    print("")
    print("                      AT YOUR NEW HOME")
