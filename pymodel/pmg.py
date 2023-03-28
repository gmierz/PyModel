#!/usr/bin/env python
"""
PyModel Graphics - generate graphics from pymodel FSM
"""

from pymodel import GraphicsOptions
from pymodel.Dot import dotfile
from pymodel.ProductModelProgram import import_support_class

def main():
    (options, args) = GraphicsOptions.parse_args()
    if not args or len(args) > 2: # args must include one FSM module
        GraphicsOptions.print_help()
        exit()
    else:
        try:
            fsm = __import__(args[0])
        except ModuleNotFoundError:
            fsm = import_support_class(args[0])
        fbasename = options.output if options.output else args[0]
        fname = '%s.dot' % fbasename
        dotfile(fname, fsm, options.transitionLabels, options.noStateTooltip,
                options.noTransitionTooltip)

if __name__ == '__main__':
    main ()
