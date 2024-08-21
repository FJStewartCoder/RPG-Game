from time import sleep
from time import perf_counter

reading_speed = 180  # words per minute


def reading_test():
    global reading_speed

    sleep(1)

    test_text = 'Welcome to the reading test. Please do not skip any of this text otherwise you may have unexpected results. Once you finish reading this text press the enter key on your keyboard to end the test. You will then be provided with a score in words per minute that you can use next time. In order to maximise accuracy, the length of the text should be increased. This means that more words will be read and more time will have passed giving a more accurate result. You may be able to read very quickly for a short time but a longer time will give a more accurate result.'

    words = len(test_text.split(' '))

    start = perf_counter()
    input(test_text)
    end = perf_counter()

    time_to_read = end - start
    reading_speed = round(60 * words / time_to_read)

    print(f'Your score is {reading_speed}wpm.')
    sleep(1.5)

    return reading_speed


def dialogue(text: str, sleep_time: int = -1, bonus_sleep_time=0):
    if sleep_time == -1:
        words = len(text.split(' '))
        sleep_time = words / reading_speed
        sleep_time *= 60

    print(text)
    sleep(sleep_time + bonus_sleep_time)
    return


if __name__ == '__main__':
    reading_test()
    dialogue('Hello, User. This is the default test message for this function.')
