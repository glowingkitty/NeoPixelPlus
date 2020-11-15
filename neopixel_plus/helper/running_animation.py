import os
import time

dirname = os.path.dirname(__file__)

# use these functions to make sure any previous animations are stopped before starting the new one.
# Made for "The Glowing Stripes Project"


class RunningAnimation:

    def create_animation_running():
        f = open(os.path.join(dirname, 'animation_running.txt'), 'w')
        f.write('')
        f.close()
        print('Created {}'.format(os.path.join(dirname, 'animation_running.txt')))

    def check_animation_running():
        if not os.path.exists(os.path.join(dirname, 'animation_running.txt')):
            f = open(os.path.join(dirname, 'animation_stopped.txt'), 'w')
            f.write('')
            f.close()
            print('Created {}'.format(os.path.join(
                dirname, 'animation_stopped.txt')))
            return False
        return True

    def stop_ongoing_animation():
        # check if "animation_running.txt" exists & delete it
        if os.path.exists(os.path.join(dirname, 'animation_running.txt')):
            os.remove(os.path.join(dirname, 'animation_running.txt'))
            print('Removed {}'.format(os.path.join(
                dirname, 'animation_running.txt')))

            # while "animation_stopped.txt" doesn't exists → wait
            tried_find_animation_stopped = 0
            while not os.path.exists(os.path.join(dirname, 'animation_stopped.txt')):
                if tried_find_animation_stopped > 10:
                    print(
                        'Seems no previous animation is running. Skipped removing animation_stopped.txt')
                    return
                tried_find_animation_stopped += 1
                time.sleep(0.1)

            # delete "animation_stopped.txt" and start new animation
            os.remove(os.path.join(dirname, 'animation_stopped.txt'))
            print('Removed {}'.format(os.path.join(
                dirname, 'animation_stopped.txt')))
