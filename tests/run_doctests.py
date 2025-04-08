#!/usr/bin/env python3

"""
Script to run doctests on all Python scripts
"""

import doctest
import importlib
import os
import sys
import glob
import inspect

# Ensure the script directory is in the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
sys.path.insert(0, parent_dir)

def find_failed_functions(module, failures):
    """
    Find the names of functions that failed doctests in a module
    Returns a list of function names
    """
    failed_functions = []
    
    if failures == 0:
        return failed_functions
    
    # Get all functions in the module
    functions = inspect.getmembers(module, inspect.isfunction)
    
    # Run doctests individually on each function to identify which ones failed
    for name, func in functions:
        if func.__doc__ and '>>>' in func.__doc__:  # Only test functions with doctests
            finder = doctest.DocTestFinder()
            runner = doctest.DocTestRunner(verbose=False)
            
            for test in finder.find(func, name):
                results = runner.run(test)
                if results.failed > 0:
                    failed_functions.append(name)
                    break
    
    return failed_functions

def run_doctests_in_module(module_name):
    """
    Run doctests for a specific module
    Returns (failures, tests, failed_functions) tuple
    """
    print(f"Running doctests for {module_name}...")
    
    try:
        # Import the module
        module = importlib.import_module(module_name)
        
        # Run doctests for the module
        failures, tests = doctest.testmod(module, verbose=True)
        
        # Find which functions failed
        failed_functions = find_failed_functions(module, failures)
        
        # Print summary
        if failures == 0:
            print(f"✅ {module_name}: All {tests} tests passed!")
        else:
            print(f"❌ {module_name}: {failures} out of {tests} tests failed.")
            if failed_functions:
                print(f"   Failed functions: {', '.join(failed_functions)}")
        
        return failures, tests, failed_functions
    
    except ImportError as e:
        print(f"❌ Error importing {module_name}: {e}")
        return 1, 0, []
    except Exception as e:
        print(f"❌ Error running doctests on {module_name}: {e}")
        return 1, 0, []

def run_all_doctests():
    """
    Run doctests for all Python modules in the scripts directory
    """
    scripts_dir = os.path.join(parent_dir, "scripts")
    
    # Get list of Python files in scripts directory
    py_files = glob.glob(os.path.join(scripts_dir, "*.py"))
    
    # Convert file paths to module names
    module_names = [f"scripts.{os.path.basename(f)[:-3]}" for f in py_files]
    
    total_failures = 0
    total_tests = 0
    failed_modules = []  # Keep track of failed modules and functions
    
    # Run doctests for each module
    for module_name in module_names:
        failures, tests, failed_functions = run_doctests_in_module(module_name)
        total_failures += failures
        total_tests += tests
        
        if failures > 0:
            # Store the module name and failed functions
            module_shortname = module_name.split('.')[-1] + '.py'
            failed_modules.append((module_shortname, failed_functions))
    
    # Print overall summary
    print("\n" + "="*60)
    if total_failures == 0:
        print(f"✅ SUMMARY: All {total_tests} tests passed across {len(module_names)} modules!")
    else:
        print(f"❌ SUMMARY: {total_failures} out of {total_tests} tests failed across {len(module_names)} modules.")
        
        if failed_modules:
            print("\nFailed functions by file:")
            for module, functions in failed_modules:
                print(f"  {module} -> {', '.join(functions)}")
    
    return total_failures

if __name__ == "__main__":
    sys.exit(run_all_doctests()) 