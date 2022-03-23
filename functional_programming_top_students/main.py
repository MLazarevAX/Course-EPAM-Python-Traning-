from typing import List

def get_top_student_by_sorted_list(result):
    res = {}
    for dictionary in result:
        if dictionary["course"] in res.keys():
            continue
        else:
            res[dictionary["course"]] = dictionary["name"]
    return res


def get_top(data: List[dict]) -> dict:
    """Returns top student name by course"""
    result = sorted(data, key=lambda item: (item["rate"]), reverse=True)
    return get_top_student_by_sorted_list(result)



