# generated by scripts/gen_api.py at 2018/10/19 14:28:34
apis = {   'channel': {   'archive': {'authentication': True, 'method': 'post'},
                   'create': {'authentication': True, 'method': 'post'},
                   'info': {'authentication': True, 'method': 'get'},
                   'invite': {'authentication': True, 'method': 'post'},
                   'join': {'authentication': True, 'method': 'post'},
                   'kick': {'authentication': True, 'method': 'post'},
                   'kickout': {'authentication': True, 'method': 'post'},
                   'leave': {'authentication': True, 'method': 'post'},
                   'list': {'authentication': True, 'method': 'get'},
                   'unarchive': {'authentication': True, 'method': 'post'}},
    'emoji': {'list': {'authentication': True, 'method': 'get'}},
    'message': {   'create': {'authentication': True, 'method': 'post'},
                   'delete': {'authentication': True, 'method': 'post'},
                   'forward': {'authentication': True, 'method': 'post'},
                   'info': {'authentication': True, 'method': 'get'},
                   'query': {'authentication': True, 'method': 'post'},
                   'update_text': {'authentication': True, 'method': 'patch'}},
    'message_pin': {   'create': {'authentication': True, 'method': 'post'},
                       'delete': {'authentication': True, 'method': 'post'},
                       'list': {'authentication': True, 'method': 'get'}},
    'meta': {'authentication': True, 'method': 'get'},
    'p2p': {   'create': {'authentication': True, 'method': 'post'},
               'info': {'authentication': True, 'method': 'get'},
               'list': {'authentication': True, 'method': 'get'}},
    'rtm': {'start': {'authentication': True, 'method': 'post'}},
    'session_channel': {   'archive': {   'authentication': True,
                                          'method': 'post'},
                           'convert_to_channel': {   'authentication': True,
                                                     'method': 'post'},
                           'create': {'authentication': True, 'method': 'post'},
                           'info': {'authentication': True, 'method': 'get'},
                           'invite': {'authentication': True, 'method': 'post'},
                           'kick': {'authentication': True, 'method': 'post'},
                           'kickout': {   'authentication': True,
                                          'method': 'post'},
                           'leave': {'authentication': True, 'method': 'post'},
                           'list': {'authentication': True, 'method': 'get'}},
    'sticker': {'list': {'authentication': True, 'method': 'get'}},
    'team': {'info': {'authentication': True, 'method': 'get'}},
    'user': {   'info': {'authentication': True, 'method': 'get'},
                'list': {'authentication': True, 'method': 'get'},
                'me': {'authentication': True, 'method': 'get'},
                'update_me': {'authentication': True, 'method': 'patch'}},
    'vchannel': {'info': {'authentication': True, 'method': 'get'}}}
