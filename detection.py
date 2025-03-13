import aircv as ac


def locate_image(screenshot, reference, threshold):
    result = ac.find_template(screenshot, ac.imread(f"images/{reference}"), threshold)
    return result['result'][:2] if result else None