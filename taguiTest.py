import rpa as t

t.init()
t.url('https://www.baidu.com')
t.type('q', 'decentralization[enter]')
t.snap('page', 'results.png')
t.close()