import io
import json
from contextlib import redirect_stdout, redirect_stderr
import traceback

class CodeRunner:
    """Safe Python code execution for puzzle solutions"""
    
    RESTRICTED_IMPORTS = {
        'os', 'sys', 'subprocess', 'socket', 'urllib', 'requests', 
        'pickle', 'marshal', 'shelve', 'dbm', 'sqlite3', 'psycopg2',
        '__import__', 'eval', 'exec', 'compile', 'open', 'file',
        'input', 'raw_input'
    }
    
    @staticmethod
    def validate_code(code):
        """Check if code contains restricted operations"""
        for restriction in CodeRunner.RESTRICTED_IMPORTS:
            if restriction in code:
                return False, f"Restricted operation detected: {restriction}"
        return True, ""
    
    @staticmethod
    def execute_code(code, test_cases, timeout_seconds=5):
        """
        Execute user code against test cases
        Returns: dict with results
        """
        results = {
            'success': False,
            'passed_tests': 0,
            'total_tests': len(test_cases),
            'test_results': [],
            'error': None,
            'output': ''
        }
        
        if not test_cases:
            results['error'] = "No test cases available for this puzzle"
            return results
        
        # Validate code first
        valid, error_msg = CodeRunner.validate_code(code)
        if not valid:
            results['error'] = error_msg
            return results
        
        # Capture output
        output_buffer = io.StringIO()
        error_buffer = io.StringIO()
        
        try:
            # Create restricted globals
            restricted_globals = {
                '__builtins__': {
                    'len': len, 'str': str, 'int': int, 'float': float,
                    'list': list, 'dict': dict, 'tuple': tuple, 'set': set,
                    'bool': bool, 'range': range, 'enumerate': enumerate,
                    'zip': zip, 'map': map, 'filter': filter, 'sum': sum,
                    'max': max, 'min': min, 'abs': abs, 'round': round,
                    'sorted': sorted, 'reversed': reversed, 'all': all, 'any': any,
                    'print': print
                }
            }
            
            with redirect_stdout(output_buffer), redirect_stderr(error_buffer):
                # Execute the user's code
                exec(code, restricted_globals)
                
                # Check if solution function exists
                if 'solution' not in restricted_globals:
                    results['error'] = "No 'solution' function found. Please define a function named 'solution'."
                    return results
                
                solution_func = restricted_globals['solution']
                
                # Test each case
                for i, test_case in enumerate(test_cases):
                    try:
                        # Run the test case
                        if 'input' in test_case:
                            if isinstance(test_case['input'], list):
                                result = solution_func(*test_case['input'])
                            else:
                                result = solution_func(test_case['input'])
                        else:
                            result = solution_func()
                        
                        # Check expected output
                        expected = test_case['expected']
                        passed = result == expected
                        
                        results['test_results'].append({
                            'test_number': i + 1,
                            'input': test_case.get('input', 'No input'),
                            'expected': expected,
                            'actual': result,
                            'passed': passed,
                            'description': test_case.get('description', f'Test {i + 1}')
                        })
                        
                        if passed:
                            results['passed_tests'] += 1
                            
                    except Exception as e:
                        results['test_results'].append({
                            'test_number': i + 1,
                            'input': test_case.get('input', 'No input'),
                            'expected': test_case['expected'],
                            'actual': f"Error: {str(e)}",
                            'passed': False,
                            'description': test_case.get('description', f'Test {i + 1}')
                        })
        
        except Exception as e:
            error_output = error_buffer.getvalue()
            results['error'] = error_output if error_output else str(e)
        
        results['output'] = output_buffer.getvalue()
        results['success'] = results['passed_tests'] == results['total_tests'] and results['error'] is None
        
        return results