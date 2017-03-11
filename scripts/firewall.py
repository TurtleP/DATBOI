import nfqueue
from dpkt import ip

qu = None

def cb(dummy, payload):
#make sure that you want to allow the packet. In this case drop everything
    payload.set_verdict(nfqueue.NF_DROP)

qu = nfqueue.queue
qu.open()
qu.bind()
qu.set_callback(cb)
qu.create_queue(1)

qu.try_run()
