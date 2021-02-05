import re


def layout_handle(layout):
    result = []
    content = re.match('^(\d)室(\d)厅(\d)厨(\d)卫', layout)
    if content:
        for i in range(1, 5):
            result.append(content.group(i))
    return result


def floor_handle(floor):
    result = []
    content = re.match('^(.)楼层\(共(\d*)层\)', floor)
    if content:
        for i in range(1, 3):
            result.append(content.group(i))
    return result


layout = '3室2厅1厨2卫'
a = layout_handle(layout)
print(a)

floor = '中楼层(共32层)'
b = floor_handle(floor)
print(b)
