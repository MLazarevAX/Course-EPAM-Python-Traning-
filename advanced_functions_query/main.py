from typing import List, Dict, Any
import copy


def select_coloms(data, columns):
    copy_list = copy.deepcopy(data)
    finish_reverse = []
    for i in range(len(data)):
        for key in data[i].keys():
            try:
                if key in columns:
                    continue
                del copy_list[i][key]
            except KeyError:
                print(f"Doesn't exist key {key}")
        items = copy_list[i].items()
        finish_reverse.append({k: v for k, v in reversed(items)})
    return finish_reverse


def select(*field_names: str):
    '''
    select function selected field names in List
    :param field_names: param for select in List
    :return: select names
    '''
    return [i for i in field_names]


def field_filter(field_name: str, *values):
    '''
    field_filter function filtered list
    :param field_name: it's key in the dicts
    :param values: Filtering values
    :return: dicts{names:values}
    '''
    return {field_name: [i for i in values]}


def query(data: List[Dict[str, Any]], select: callable, *filters: callable) -> List[Dict[str, Any]]:
    '''
    query function provide with possibility to select necessary columns
    and make filtering by these columns
    :param data:
    :param selection:
    :param filters:
    :return: List[Dict[str, Any]]
    '''
    select_colom_name = select
    full_copy_data_with_select_columns = select_coloms(data, select_colom_name)
    filtered = {k: v for elem in filters for k, v in elem.items()}

    result = copy.deepcopy(full_copy_data_with_select_columns)
    for item in full_copy_data_with_select_columns:
        for key, values in filtered.items():
            if item[key] not in values and item in result:
                result.remove(item)
    return result





