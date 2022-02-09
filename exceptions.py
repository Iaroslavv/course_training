import json

def format_message(message):
    return json.dumps(message, indent=4, ensure_ascii=False, sort_keys=True, separators=(',', ': ')) \
        if isinstance(message, (dict, list, tuple)) else str(message)

class HttpError(AssertionError):
    def __init__(self, message, response, *args):
        response_text = format_message(response)
        super().__init__(f'{message}\n{response_text}', *args)
