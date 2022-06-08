#!/usr/bin/env python
import os
import os.path as osp
import subprocess
import argparse

def run_cmd(cmd):
    cmd = ' '.join(cmd)
    print (cmd)
    subprocess.call(cmd, shell=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out', default='build_artifacts')
    parser.add_argument('--croot', default='conda-bld')
    parser.add_argument('--dirty', action='store_true')
    parser.add_argument('--include-recipe', action='store_true')
    parser.add_argument('--python', default='')
    parser.add_argument('--numpy', default='')
    parser.add_argument('--build-config', default='conda_build_config.yaml')
    parser.add_argument('--prefix-length', default=80)
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--builder', choices=['conda', 'mamba'], default='mamba')
    parser.add_argument('recipes', nargs='+')
    args = parser.parse_args()

    if args.builder == 'conda':
        build_str = 'build'
    else:
        build_str = 'mambabuild'

    cmd = ['conda', build_str, '--output-folder ' + args.out, '--croot=' + args.croot]

    if args.dirty:
        cmd.append('--dirty')
    if not args.include_recipe:
        cmd.append('--no-include-recipe')
    if args.python:
        cmd.append('--python ' + args.python)
    if args.numpy:
        cmd.append('--numpy ' + args.numpy)
    if args.build_config and osp.exists(args.build_config):
        cmd.append('-m ' + args.build_config)

    if args.debug:
        cmd.append('--debug')

    if args.prefix_length:
        cmd.append('--prefix-length ' + str(args.prefix_length))

    for recipe in args.recipes:
        recipe_cmd = cmd + [recipe]
        run_cmd(recipe_cmd)

if __name__ == "__main__":
    main()
