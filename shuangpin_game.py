#!/usr/bin/env python3

map = {}
map['q'] = ['iu']
map['w'] = ['ei']
map['r'] = ['uan', 'van']
map['t'] = ['ve', 'ue']
map['y'] = ['vn', 'un']
map['u'] = ['sh']
map['i'] = ['ch']
map['o'] = ['uo']
map['p'] = ['ie']
map['s'] = ['ong', 'iong']
map['d'] = ['ai']
map['f'] = ['en']
map['g'] = ['eng']
map['h'] = ['ang']
map['j'] = ['an']
map['k'] = ['uai', 'ing']
map['l'] = ['iang', 'uang']
map['z'] = ['ou']
map['x'] = ['ia', 'ua']
map['c'] = ['ao']
map['v'] = ['zh', 'ui']
map['b'] = ['in']
map['n'] = ['iao']
map['m'] = ['ian']

array = [
    'iu', 'ei', 'uan', 'van', 've', 'ue', 'vn', 'un', 'sh', 'ch', 'uo', 'ie',
    'ong', 'iong', 'ai', 'en', 'eng', 'ang', 'an', 'uai', 'ing', 'iang',
    'uang', 'ou', 'ia', 'ua', 'ao', 'zh', 'ui', 'in', 'iao', 'ian'
]
index = 0
target = array[index]
str = input('INPUT THE KEY OF %s:' % (target))
while 'exit' != str:
    vals = map.get(str)
    if vals is not None and target in vals:
        index = index + 1
        if index >= 31:
            index = 0
    target = array[index]
    str = input('INPUT THE KEY OF %s:' % (target))
