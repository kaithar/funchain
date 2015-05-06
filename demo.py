from __future__ import print_function
from funchain import Chain

demo1 = Chain() >> Chain.asArgs(range) >> Chain.emit("from range") >> sum >> print
demo1(0,4,1)

print("")

def inject(text):
    def inner(input):
        return input+text
    return inner

demo2 = Chain() >> inject(' World') >> [
        Chain() >> inject('.') >> [
            Chain() >> inject('') >> print,
            Chain() >> inject('..') >> print
        ],
        Chain() >> inject('!') >> print
    ]

ret = demo2('Hello')
print('Return is "{}"'.format(ret))
print("")

demo3 = Chain() >> inject('hai') >> [print, Chain() >> inject(' there') >> print]
demo3("")
