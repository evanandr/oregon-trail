from time import time


def shoot(timeout=7):
    start_time = time()
    # TODO: implement a timeout here? As is, any shoot event waits
    # indefinitely, slow and incorrect responses will still be penalized
    response = str(input('TYPE BANG ')).lower().strip()
    entry_time = time() - start_time
    print('')  # needed to move to next line
    if response.lower() != 'bang':
        entry_time = max(float(timeout), entry_time)
    return response, entry_time
