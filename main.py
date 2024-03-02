import PySimpleGUI as sg
import webbrowser
import urllib.parse

# Define the Google Dorking GUI layout
sg.theme('DarkBlack')
font = 'Poppins'

# Define Google Dork formats
dork_formats = [
    'intext', 'inurl', 'intitle', 'filetype:pdf', 'filetype:doc', 'filetype:xls', 'filetype:ppt',
    'filetype:txt', 'filetype:csv', 'filetype:log', 'site:".gov"', 'site:".edu"', 'site:".org"',
    'site:".com"', 'site:".net"', 'intext:"index of"', 'intext:"parent directory"', 'intext:".htpasswd"',
    'intext:".env"', 'intext:"database connection"'
]

# Define dropdown options
dropdown_options = [format.split(':')[0] for format in dork_formats]

# Define the Google Dorking GUI layout
layout = [
    [sg.Text('Google Dorking', font=(font, 30), justification='center')],
    [sg.Text('Search Term:', font=(font, 16)),
     sg.InputText(key='-SEARCH_TERM-', font=(font, 16), size=(35, 1), focus=True, enable_events=True)],
    [sg.Text('Select Dork Format to Search:', font=(font, 16))],
    [sg.DropDown(dropdown_options, font=(font, 14), key='-FORMAT-', size=(20, 1))],
    [sg.Button('Search', font=(font, 16), size=(10, 1)), sg.Button('Exit', font=(font, 16), size=(10, 1))]
]

# Create the window
window = sg.Window('Google Dorking', layout, font=(font, 16))

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Search' or (
            event == '-SEARCH_TERM-' and values['-SEARCH_TERM-'] and '\n' in values['-SEARCH_TERM-']):
        search_term = values['-SEARCH_TERM-']
        selected_format = values['-FORMAT-']

        query = f'{selected_format}:"{search_term}"'
        encoded_query = urllib.parse.quote_plus(query)
        search_url = f'https://www.google.com/search?q={encoded_query}'
        webbrowser.open_new_tab(search_url)

# Close the window
window.close()
