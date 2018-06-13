import argparse

from tabulate import tabulate

from src.classes.executor import Executor
from src.classes.word_list import WordList

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-target', required=True, help="Target binary.")
    ap.add_argument('-arg', required=False, help="Argument to test with")
    ap.add_argument('-vectors', required=False, help="Path to text file with arguments to test with.")
    args = vars(ap.parse_args())

    target = args['target']
    if not args['arg'] and not args['vectors']:
        print("Please specify either the <arg> or the <vectors> argument.")
        exit(0)

    arg_list = []
    if args['arg']:
        arg = args['arg']
        arg_list.append(arg)
    if args['vectors']:
        vectors = args['vectors']
        arg_list += WordList(vectors).word_list
    results = [r.to_list() for r in [Executor(target, arg) for arg in arg_list] if not r.execution_successful]
    print(tabulate(results, headers=['binary', 'arg', 'signal', 'stdout/stderr']))
