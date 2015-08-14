# -*- coding: utf-8 -*-
'''
Executors Directory
'''
from __builtin__ import isinstance
from salt.exceptions import SaltInvocationError


class ModuleExecutorBase():
    '''
    Base class for module executors.
    Each executor implementation have to override this class and have corresponding get function that creates the
    executor object.
    '''

    def __init__(self):
        '''
        Constructor shall perform all pre-exec steps needed by executor.
        All external data including  have to be passed to the constructor.
        '''
        pass
    
    def execute(self):
        '''
        Execute the function or another executor in a specific way or in 
        a specific environment. 
        '''
        pass