with open('tes2.html', 'r') as file:
    html_string = file.read()
    print(repr(html_string.replace(' ', '').replace('\n', '')))