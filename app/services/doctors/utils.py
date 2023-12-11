from datetime import time

from aiofiles.ospath import wrap

from app.config import settings


@wrap
def get_free_time(busy_time: list):
    busy_time_minutes = []
    for window in busy_time:
        start_time = window["start_time"].split(":")
        end_time = window["end_time"].split(":")
        start = int(start_time[0]) * 60 + int(start_time[1])
        end = int(end_time[0]) * 60 + int(end_time[1])
        busy_time_minutes.append((start, end))

    work_day_start = settings.WORK_DAY_START * 60
    work_day_end = settings.WORK_DAY_END * 60

    free_time = []
    current_time = work_day_start
    while current_time + settings.WORK_DAY_WINDOW <= work_day_end:
        is_free = True
        for window in busy_time_minutes:
            if (
                (
                    current_time <= window[0]
                    and (current_time + settings.WORK_DAY_WINDOW) > window[0]
                )
                or current_time >= window[0]
                and current_time < window[1]
            ):
                is_free = False
                break
        if is_free:
            free_time.append(
                {
                    "start": time(current_time // 60, current_time % 60),
                    "end": time(
                        (current_time + settings.WORK_DAY_WINDOW) // 60,
                        (current_time + settings.WORK_DAY_WINDOW) % 60,
                    ),
                }
            )
        current_time += settings.WORK_DAY_WINDOW
    return free_time
