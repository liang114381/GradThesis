from mpc.fields import Circular
from mpc.polynomial import Polynomial
from mpc.secretsharing import SecretSharer
from mpc.threadedsys.server import Server
from mpc.threadedsys.mpc import MpcControler
import random
import time
import logging

if __name__ == '__main__':

    # ss = SecretSharing(3, Circular)

    logging.basicConfig(level=logging.DEBUG)

    field = Circular(1001)

    # id = field.getIdentityElement()
    #
    # random.seed(time.time())
    #
    # print(field.generateRandomElement())

    # ids = [0,1,2,3,4]
    # xs = [0] * 5
    # vals = [3,3,3,3,3]
    #
    # for i in range(5):
    #     xs[i] = field.generateElement(ids[i])
    #     vals[i] = field.generateElement(vals[i])

    mpc = MpcControler(field, 2)

    for i in range(5):
        mpc.addServer(i)
    mpc.distributeKeys()

    mpc.addClient(0)

    time.sleep(1)

    # mpc.put('a', field.generateElement(340))
    # mpc.put('b', field.generateElement(7))
    # mpc.mul('a', 'b', 'c')
    # mpc.open('c')

    mpc.clients[0].commit('d', field.generateElement(11))
    mpc.open('d')