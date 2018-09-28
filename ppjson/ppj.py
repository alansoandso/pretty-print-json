#!/usr/bin/env python
import json
from pprint import pformat
import os
import sys


def set_clipboard(text):
    print(text)
    with os.popen('pbcopy', 'w') as f:
        f.write(text)
    return text


def get_clipboard():
    if sys.stdin.isatty():
        # from clipboard
        with os.popen('pbpaste', 'r') as f:
            text = f.read()
    else:
        # piped in
        text = sys.stdin.read()
    return text


def main():
    if len(sys.argv) == 2 and sys.argv[1].endswith(('--help', '-h')):
        print('Usage: {} [-h]\n' \
              'JSON Tool - Pretty print the JSON stored in the clipboard' \
              .format(os.path.basename(sys.argv[0])))
    else:
        # Retrieve contents of the clipboard
        show_json(get_clipboard())


def show_json(lines):
    lines = lines.replace('\\\\\\\"', '') \
        .replace("u'", '"') \
        .replace("'", '"') \
        .replace('\\n', '\n') \
        .replace('\\t', '\t') \
        .replace('\\', '') \
        .replace('True', 'true') \
        .replace('False', 'false')

    # Try to display some JSON
    try:
        output = pformat(json.loads(lines)).replace("u'", '"').replace("'", '"')
    except ValueError:
        # Instead split over multiple lines
        output = ''.join(['Not valid JSON\n', lines.replace(', ', ',\n').replace('","', '",\n"')])

    return set_clipboard(output)


if __name__ == '__main__':
    main()
