import argparse

from tabulate import tabulate

from src.classes.argument_generator import ArgumentGenerator
from src.classes.kfuzz_manager import KfuzzManager
from src.classes.word_list import WordList

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-target', required=True, help="Target binary.")
    ap.add_argument('-vectors', required=False, help="Path to text file with arguments to test with.")
    ap.add_argument('-fstring', dest='fstring', action='store_true',
                    help="Do you want to automatically generate format string arguments?")
    ap.add_argument('-oflow', dest='oflow', action='store_true',
                    help="Do you want to automatically generate overflow arguments?")
    ap.add_argument('-threads', required=False, type=int, help="Number of threads.")
    ap.set_defaults(threads=20, oflow=False, fstring=False)
    args = vars(ap.parse_args())

    target = args['target']
    threads = args['threads']
    if not args['vectors'] and not args['oflow'] and not args['fstring']:
        print("Please specify the <vectors>, <oflow>, or <fstring> argument.")
        exit(0)

    if args['vectors']:
        arguments = []
        vectors = args['vectors']
        arguments += WordList(vectors).word_list
        t = args['vectors'].split('/')[-1]
    elif args['fstring']:
        arguments = ArgumentGenerator('fstring')
        t = 'format string'
    elif args['oflow']:
        arguments = ArgumentGenerator('oflow')
        t = 'overflow'
    else:
        raise ValueError("Wrong argument.")

    manager = KfuzzManager(target, arguments, t, threads)

    manager.run()

    results = [r.to_list() for r in manager.results if not r.execution_successful]
    print(tabulate(results, headers=['binary', 'arg', 'signal', 'stdout/stderr', 'type']))
