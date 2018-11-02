# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

import queue
from Agent import Agent

class MyAI ( Agent ):

    def __init__ ( self, alt = True ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        self._alt = alt
        self._moveQueue = queue.Queue()
        pass
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        if stench:
            return Agent.Action.SHOOT
        elif breeze:
            if self._alt:
                self._alt = False
                self._moveQueue.put(Agent.Action.FORWARD)
                self._moveQueue.put(Agent.Action.TURN_RIGHT)
                return Agent.Action.TURN_LEFT, Agent.Action.FORWARD
            else:
                self._alt = True
                self._moveQueue.put(Agent.Action.FORWARD)
                self._moveQueue.put(Agent.Action.TURN_LEFT)
                return Agent.Action.TURN_RIGHT, Agent.Action.FORWARD
        elif glitter:
            self._moveQueue.put(Agent.Action.TURN_LEFT)
            self._moveQueue.put(Agent.Action.TURN_LEFT)
            return Agent.Action.GRAB, self.returnToStart()
        elif bump:
            self._moveQueue.put(Agent.Action.TURN_RIGHT)
            return Agent.Action.TURN_LEFT
        elif scream:
            self._moveQueue.put(Agent.Action.FORWARD)
            return Agent.Action.FORWARD
        else:
            self._moveQueue.put(Agent.Action.FORWARD)
            return Agent.Action.FORWARD
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================

    def returnToStart(self):
        while self._moveQueue.qsize() > 0:
            return self._moveQueue.get()
        return self.Agent.Action.CLIMB
    
    # ======================================================================
    # YOUR CODE ENDS
    # ======================================================================